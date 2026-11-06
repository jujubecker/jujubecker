#!/usr/bin/env bash
# rodar-repo.sh - clona (opcional) e roda um repositorio detectando o tipo de projeto.
#
# Uso:
#   ./scripts/rodar-repo.sh                       # roda o projeto da pasta atual
#   ./scripts/rodar-repo.sh ../outro-projeto      # roda o projeto dessa pasta
#   ./scripts/rodar-repo.sh https://github.com/user/repo.git
#   ./scripts/rodar-repo.sh --install-only .      # so instala as dependencias
#   ./scripts/rodar-repo.sh --dry-run .           # mostra os comandos sem executar
#
# Opcoes:
#   --install-only   instala dependencias e para
#   --dry-run        imprime o que faria, sem rodar
#   --cmd "..."      ignora a deteccao e roda esse comando
#   -h, --help       esta ajuda

set -euo pipefail

INSTALL_ONLY=0
DRY_RUN=0
CUSTOM_CMD=""
TARGET=""

info()  { printf '\033[1;34m==>\033[0m %s\n' "$*"; }
warn()  { printf '\033[1;33m[!]\033[0m %s\n' "$*" >&2; }
erro()  { printf '\033[1;31m[x]\033[0m %s\n' "$*" >&2; exit 1; }

uso() { awk 'NR>1 && /^#/ {sub(/^# ?/, ""); print; next} NR>1 {exit}' "$0"; }

# roda um comando respeitando --dry-run
executar() {
  printf '\033[1;32m$\033[0m %s\n' "$*"
  if [ "$DRY_RUN" -eq 0 ]; then
    eval "$@"
  fi
}

tem() { command -v "$1" >/dev/null 2>&1; }

while [ $# -gt 0 ]; do
  case "$1" in
    --install-only) INSTALL_ONLY=1; shift ;;
    --dry-run)      DRY_RUN=1; shift ;;
    --cmd)          CUSTOM_CMD="${2:-}"; [ -n "$CUSTOM_CMD" ] || erro "--cmd precisa de um comando"; shift 2 ;;
    -h|--help)      uso; exit 0 ;;
    -*)             erro "opcao desconhecida: $1 (use --help)" ;;
    *)              TARGET="$1"; shift ;;
  esac
done

TARGET="${TARGET:-.}"

# 1. Se o alvo for uma URL, clona primeiro
case "$TARGET" in
  http://*|https://*|git@*|ssh://*)
    nome="$(basename "$TARGET" .git)"
    if [ -d "$nome" ]; then
      info "pasta '$nome' ja existe, usando ela"
    else
      info "clonando $TARGET"
      executar "git clone --depth 1 '$TARGET' '$nome'"
    fi
    TARGET="$nome"
    ;;
esac

[ -d "$TARGET" ] || erro "pasta nao encontrada: $TARGET"
cd "$TARGET"
RAIZ="$(pwd)"
info "projeto: $RAIZ"

# 2. Comando explicito ganha de tudo
if [ -n "$CUSTOM_CMD" ]; then
  executar "$CUSTOM_CMD"
  exit 0
fi

# 3. Avisa sobre variaveis de ambiente esperadas
for exemplo in .env.example .env.sample env.example; do
  if [ -f "$exemplo" ] && [ ! -f .env ]; then
    warn "existe $exemplo e nao existe .env — copie e preencha: cp $exemplo .env"
    break
  fi
done

# 4. Deteccao por arquivo-marcador, do mais especifico para o mais generico
# Node / JavaScript / TypeScript
if [ -f package.json ]; then
  if   [ -f pnpm-lock.yaml ] && tem pnpm; then PM=pnpm
  elif [ -f yarn.lock ]      && tem yarn; then PM=yarn
  elif [ -f bun.lockb ]      && tem bun;  then PM=bun
  else PM=npm
  fi
  info "Node detectado (gerenciador: $PM)"

  if [ ! -d node_modules ]; then
    case "$PM" in
      npm)  [ -f package-lock.json ] && executar "npm ci" || executar "npm install" ;;
      yarn) executar "yarn install --frozen-lockfile || yarn install" ;;
      pnpm) executar "pnpm install" ;;
      bun)  executar "bun install" ;;
    esac
  else
    info "node_modules ja existe, pulando instalacao"
  fi

  [ "$INSTALL_ONLY" -eq 1 ] && exit 0

  # escolhe o script: dev > start > serve
  for s in dev start serve; do
    if node -e "process.exit(require('./package.json').scripts?.['$s']?0:1)" 2>/dev/null; then
      info "rodando script '$s'"
      [ "$PM" = npm ] && executar "npm run $s" || executar "$PM run $s"
      exit 0
    fi
  done
  warn "nenhum script dev/start/serve no package.json; scripts disponiveis:"
  node -e "console.log(Object.keys(require('./package.json').scripts||{}).join(', ')||'(nenhum)')"
  exit 1
fi

# Python
if [ -f pyproject.toml ] || [ -f requirements.txt ] || [ -f Pipfile ]; then
  info "Python detectado"
  if [ -f pyproject.toml ] && tem uv; then
    executar "uv sync"
    [ "$INSTALL_ONLY" -eq 1 ] && exit 0
    if [ -f manage.py ]; then executar "uv run python manage.py runserver"; exit 0; fi
    for entry in main.py app.py src/main.py; do
      [ -f "$entry" ] && { executar "uv run python $entry"; exit 0; }
    done
    warn "instalado, mas nao achei ponto de entrada (main.py / app.py / manage.py)"
    exit 1
  fi

  [ -d .venv ] || executar "python3 -m venv .venv"
  # shellcheck disable=SC1091
  if [ "$DRY_RUN" -eq 0 ]; then . .venv/bin/activate; else echo '$ source .venv/bin/activate'; fi
  [ -f requirements.txt ] && executar "pip install -r requirements.txt"
  [ -f pyproject.toml ] && [ ! -f requirements.txt ] && executar "pip install -e ."
  [ "$INSTALL_ONLY" -eq 1 ] && exit 0

  if [ -f manage.py ]; then executar "python manage.py runserver"; exit 0; fi
  for entry in main.py app.py src/main.py; do
    [ -f "$entry" ] && { executar "python $entry"; exit 0; }
  done
  warn "instalado, mas nao achei ponto de entrada (main.py / app.py / manage.py)"
  exit 1
fi

# Docker Compose
if [ -f docker-compose.yml ] || [ -f docker-compose.yaml ] || [ -f compose.yml ] || [ -f compose.yaml ]; then
  info "Docker Compose detectado"
  [ "$INSTALL_ONLY" -eq 1 ] && { executar "docker compose build"; exit 0; }
  executar "docker compose up --build"
  exit 0
fi

# Go
if [ -f go.mod ]; then
  info "Go detectado"
  executar "go mod download"
  [ "$INSTALL_ONLY" -eq 1 ] && exit 0
  executar "go run ./..."
  exit 0
fi

# Rust
if [ -f Cargo.toml ]; then
  info "Rust detectado"
  [ "$INSTALL_ONLY" -eq 1 ] && { executar "cargo fetch"; exit 0; }
  executar "cargo run"
  exit 0
fi

# Ruby
if [ -f Gemfile ]; then
  info "Ruby detectado"
  executar "bundle install"
  [ "$INSTALL_ONLY" -eq 1 ] && exit 0
  if [ -f config.ru ]; then executar "bundle exec rackup"; else executar "bundle exec rake"; fi
  exit 0
fi

# PHP / Composer
if [ -f composer.json ]; then
  info "PHP detectado"
  executar "composer install"
  [ "$INSTALL_ONLY" -eq 1 ] && exit 0
  if [ -f artisan ]; then executar "php artisan serve"; else executar "php -S localhost:8000"; fi
  exit 0
fi

# Java / Maven / Gradle
if [ -f pom.xml ]; then
  info "Maven detectado"
  [ "$INSTALL_ONLY" -eq 1 ] && { executar "mvn -q dependency:resolve"; exit 0; }
  executar "mvn spring-boot:run || mvn -q compile exec:java"
  exit 0
fi
if [ -f build.gradle ] || [ -f build.gradle.kts ]; then
  info "Gradle detectado"
  GRADLE="./gradlew"; [ -x "$GRADLE" ] || GRADLE=gradle
  [ "$INSTALL_ONLY" -eq 1 ] && { executar "$GRADLE dependencies"; exit 0; }
  executar "$GRADLE bootRun || $GRADLE run"
  exit 0
fi

# Makefile como ultimo recurso
if [ -f Makefile ]; then
  info "Makefile detectado"
  if grep -qE '^(run|dev|start):' Makefile; then
    alvo="$(grep -oE '^(run|dev|start):' Makefile | head -1 | tr -d ':')"
    executar "make $alvo"
  else
    executar "make"
  fi
  exit 0
fi

# Site estatico
if [ -f index.html ]; then
  info "site estatico detectado"
  executar "python3 -m http.server 8000"
  exit 0
fi

erro "nao reconheci o tipo de projeto em $RAIZ — rode com --cmd \"seu comando\""
