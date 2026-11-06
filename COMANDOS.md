# Comandos para rodar repositórios pelo terminal

Guia de referência rápida. A sequência é sempre a mesma:
**clonar → entrar na pasta → instalar dependências → configurar variáveis → rodar.**

Se quiser pular a decoreba, use o script deste repositório:

```bash
./scripts/rodar-repo.sh https://github.com/usuario/projeto.git
```

Ele clona, detecta o tipo de projeto, instala as dependências e roda. Veja [Script auxiliar](#script-auxiliar).

---

## 1. Clonar e entrar no repositório

```bash
git clone https://github.com/usuario/projeto.git
```

```bash
cd projeto
```

Clone raso (bem mais rápido em repositórios grandes — baixa só o último commit):

```bash
git clone --depth 1 https://github.com/usuario/projeto.git
```

Clonar um branch específico:

```bash
git clone --branch nome-do-branch --single-branch https://github.com/usuario/projeto.git
```

Com o GitHub CLI (`gh`), que resolve a autenticação sozinho:

```bash
gh repo clone usuario/projeto
```

## 2. Descobrir o que o projeto é

Antes de instalar qualquer coisa, olhe os arquivos da raiz. O "arquivo-marcador" diz a tecnologia:

```bash
ls -la
```

```bash
cat README.md
```

| Arquivo na raiz | Tecnologia | Como instalar | Como rodar |
|---|---|---|---|
| `package.json` | Node.js / JS / TS | `npm ci` | `npm run dev` |
| `requirements.txt` | Python | `pip install -r requirements.txt` | `python main.py` |
| `pyproject.toml` | Python (moderno) | `uv sync` ou `pip install -e .` | `uv run python main.py` |
| `manage.py` | Django | `pip install -r requirements.txt` | `python manage.py runserver` |
| `docker-compose.yml` | Docker | — | `docker compose up --build` |
| `Dockerfile` | Docker | `docker build -t app .` | `docker run -p 3000:3000 app` |
| `go.mod` | Go | `go mod download` | `go run .` |
| `Cargo.toml` | Rust | — | `cargo run` |
| `Gemfile` | Ruby | `bundle install` | `bundle exec rails server` |
| `composer.json` | PHP | `composer install` | `php artisan serve` |
| `pom.xml` | Java (Maven) | `mvn install` | `mvn spring-boot:run` |
| `build.gradle` | Java (Gradle) | `./gradlew build` | `./gradlew bootRun` |
| `Makefile` | qualquer | — | `make` ou `make run` |
| `index.html` só | site estático | — | `python3 -m http.server 8000` |

Para ver os alvos disponíveis num `Makefile`:

```bash
grep -E '^[a-zA-Z0-9_-]+:' Makefile
```

## 3. Variáveis de ambiente

Muito projeto só sobe depois que o `.env` existe. Se houver um `.env.example`:

```bash
cp .env.example .env
```

Depois abra o `.env` e preencha as chaves. **Nunca** faça commit do `.env` com segredos reais — confirme que ele está no `.gitignore`:

```bash
grep -n '.env' .gitignore
```

## 4. Receitas por tecnologia

### Node.js / JavaScript / TypeScript

```bash
npm ci
```

`npm ci` instala exatamente o que está no `package-lock.json` (reprodutível, mais rápido); use `npm install` só quando não existir lock ou quando você quer atualizar dependências.

```bash
npm run dev
```

Para ver quais scripts existem antes de adivinhar:

```bash
npm run
```

Se o projeto usa outro gerenciador, o lockfile denuncia qual: `pnpm-lock.yaml` → `pnpm install` / `pnpm dev`; `yarn.lock` → `yarn install` / `yarn dev`; `bun.lockb` → `bun install` / `bun dev`.

Trocar a versão do Node para a exigida pelo projeto (arquivo `.nvmrc`):

```bash
nvm install && nvm use
```

### Python

Sempre em ambiente virtual, para não sujar o Python do sistema:

```bash
python3 -m venv .venv && source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

Para sair do ambiente virtual:

```bash
deactivate
```

Com `uv` (muito mais rápido, lê o `pyproject.toml` e cria o venv sozinho):

```bash
uv sync && uv run python main.py
```

Django:

```bash
python manage.py migrate && python manage.py runserver
```

### Docker

A opção mais segura quando o projeto tem banco, fila ou vários serviços — não instala nada na sua máquina:

```bash
docker compose up --build
```

Rodar em segundo plano e acompanhar os logs:

```bash
docker compose up -d --build
```

```bash
docker compose logs -f
```

Derrubar tudo (o `-v` apaga também os volumes/dados):

```bash
docker compose down -v
```

Sem compose, só com `Dockerfile`:

```bash
docker build -t meu-app . && docker run --rm -p 3000:3000 --env-file .env meu-app
```

### Go

```bash
go mod download && go run .
```

### Rust

```bash
cargo run
```

Versão otimizada:

```bash
cargo run --release
```

### Ruby on Rails

```bash
bundle install && bundle exec rails db:setup && bundle exec rails server
```

### PHP / Laravel

```bash
composer install && cp .env.example .env && php artisan key:generate && php artisan serve
```

### Java

```bash
./gradlew bootRun
```

```bash
mvn spring-boot:run
```

## 5. Rodar os testes

Vale rodar antes de mexer em qualquer coisa: se os testes já falham no clone limpo, o problema não é seu.

```bash
npm test
```

```bash
pytest
```

```bash
go test ./...
```

```bash
cargo test
```

```bash
bundle exec rspec
```

```bash
mvn test
```

## 6. Quando dá erro

| Erro | O que costuma ser | Comando |
|---|---|---|
| `command not found` | a ferramenta não está instalada | `command -v node` para confirmar |
| `EADDRINUSE` / porta ocupada | outro processo na mesma porta | `lsof -i :3000` e depois `kill -9 <PID>` |
| `permission denied` ao rodar script | falta bit de execução | `chmod +x script.sh` |
| `MODULE_NOT_FOUND` / `ModuleNotFoundError` | dependências não instaladas | refaça o passo de instalação |
| versão errada da linguagem | projeto exige outra versão | `nvm use`, `pyenv local`, etc. |
| `.env` ausente | variáveis não configuradas | `cp .env.example .env` |

Descobrir qual processo está numa porta:

```bash
lsof -i :3000
```

Matar o processo pelo PID que o comando acima mostrou:

```bash
kill -9 <PID>
```

Começar do zero quando a instalação corrompeu (Node):

```bash
rm -rf node_modules package-lock.json && npm install
```

## 7. Git no dia a dia

```bash
git status
```

```bash
git switch -c minha-branch
```

```bash
git add -A && git commit -m "descrição do que mudou"
```

```bash
git push -u origin minha-branch
```

Atualizar sua cópia com o que mudou no remoto:

```bash
git pull origin main
```

Ver as últimas mudanças de forma compacta:

```bash
git log --oneline --graph --decorate -15
```

Desfazer alterações não commitadas de um arquivo:

```bash
git restore caminho/do/arquivo
```

---

## Script auxiliar

`scripts/rodar-repo.sh` automatiza os passos 1 a 4: aceita uma URL ou uma pasta, identifica a tecnologia pelo arquivo-marcador, instala as dependências e executa o projeto.

```bash
./scripts/rodar-repo.sh
```

```bash
./scripts/rodar-repo.sh https://github.com/usuario/projeto.git
```

```bash
./scripts/rodar-repo.sh --dry-run ../outro-projeto
```

```bash
./scripts/rodar-repo.sh --install-only .
```

```bash
./scripts/rodar-repo.sh --cmd "npm run storybook" .
```

| Opção | O que faz |
|---|---|
| (nenhuma) | instala e roda o projeto da pasta atual |
| `--dry-run` | só imprime os comandos, sem executar — ótimo para conferir antes |
| `--install-only` | instala as dependências e para |
| `--cmd "..."` | ignora a detecção e roda o comando que você passar |
| `-h`, `--help` | ajuda |

Para chamar de qualquer pasta, crie um atalho no seu shell:

```bash
echo "alias rodar='$HOME/jujubecker/scripts/rodar-repo.sh'" >> ~/.bashrc && source ~/.bashrc
```

Ajuste o caminho se você clonou este repositório em outro lugar. Em Mac com zsh, troque `~/.bashrc` por `~/.zshrc`.

---

## Referências

Documentação oficial e material acadêmico/aprofundado para ir além deste resumo:

- **Chacon, S. & Straub, B. — _Pro Git_ (2ª ed., Apress, 2014).** Livro de referência sobre Git, gratuito e completo: <https://git-scm.com/book/pt-br/v2>
- **Git — documentação de referência dos comandos:** <https://git-scm.com/docs>
- **The Missing Semester of Your CS Education (MIT, 2020).** Curso aberto do MIT sobre shell, ferramentas de linha de comando, controle de versão e depuração — a melhor ponte entre "sei programar" e "sei usar o terminal": <https://missing.csail.mit.edu/>
- **GNU Bash Reference Manual.** A especificação do shell, útil para entender `set -e`, expansões e redirecionamentos: <https://www.gnu.org/software/bash/manual/bash.html>
- **Boettiger, C. (2015). "An introduction to Docker for reproducible research." _ACM SIGOPS Operating Systems Review_, 49(1), 71–79.** Artigo clássico sobre por que containers resolvem o problema de reprodutibilidade — o fundamento do `docker compose up`: <https://doi.org/10.1145/2723872.2723882>
- **Docker Compose — referência da CLI:** <https://docs.docker.com/compose/reference/>
- **npm CLI — documentação (diferença entre `npm ci` e `npm install`):** <https://docs.npmjs.com/cli/v10/commands/npm-ci>
- **Python Packaging User Guide — ambientes virtuais e dependências:** <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>
- **The Twelve-Factor App — fator III, "Config".** Explica por que configuração vai em variáveis de ambiente (`.env`) e não no código: <https://12factor.net/pt_br/config>
- **ShellCheck.** Analisador estático para scripts shell; rode nele qualquer script que você escrever: <https://www.shellcheck.net/>
