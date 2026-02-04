# AVA Integration Metapackage

[![PyPI version](https://badge.fury.io/py/avaintegration-metapackage.svg)](https://badge.fury.io/py/avaintegration-metapackage)
[![Python Version](https://img.shields.io/pypi/pyversions/avaintegration-metapackage.svg)](https://pypi.org/project/avaintegration-metapackage/)
[![Docker Image](https://img.shields.io/docker/v/_/avaintegrationbase?label=docker)](https://hub.docker.com/r/avaintegrationbase)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/IFRN/ava-metapackage/publish-pypi-and-docker.yml?branch=main)](https://github.com/IFRN/ava-metapackage/actions)
[![GitHub License](https://img.shields.io/github/license/IFRN/ava-metapackage)](https://github.com/IFRN/ava-metapackage/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/IFRN/ava-metapackage?style=social)](https://github.com/IFRN/ava-metapackage/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/IFRN/ava-metapackage)](https://github.com/IFRN/ava-metapackage/issues)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/IFRN/ava-metapackage)](https://github.com/IFRN/ava-metapackage/commits/main)

### Tecnologias

![Django](https://img.shields.io/badge/Django-5.2.11-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-3.3.2-336791?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Valkey-6.1.1-DC382D?style=flat&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-enabled-2496ED?style=flat&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-23.0.0-499848?style=flat&logo=gunicorn&logoColor=white)
![Sentry](https://img.shields.io/badge/Sentry-2.49.0-362D59?style=flat&logo=sentry&logoColor=white)

Meta-pacote Python que agrega todas as dependências necessárias para projetos Django do ecossistema de Integração AVA (Integrador, Painel e Gestor).

## 📦 O que é um metapackage?

Um metapackage é um pacote Python que não contém código próprio, mas declara um conjunto de dependências. Ao instalar o metapackage, todas as suas dependências são instaladas automaticamente, garantindo:

- ✅ **Versionamento unificado** de dependências entre projetos
- ✅ **Consistência** entre ambientes de desenvolvimento, teste e produção
- ✅ **Simplificação** do gerenciamento de dependências
- ✅ **Sincronização automática** via imagem Docker base

## 🎯 Dependências Incluídas

### Core Django
- Django 5.2.11
- django-extensions 4.1
- sc4py 0.1.4

### Pacotes Internos DEAD
- django-rule-engine 1.0.1
- django-dsgovbr 5.2.3

### Banco de Dados
- psycopg[binary,pool] 3.3.2

### Models & Validação
- django-better-choices 1.18
- jsonschema 4.26.0
- rule-engine 4.5.3

### REST & HTTP
- httpie 3.2.4
- requests 2.32.5

### Cache & Session
- django-valkey 0.4.0
- valkey 6.1.1

### Auditoria
- django-simple-history 3.11.0

### Interface & UI
- whitenoise 6.11.0
- django-import-export 4.4.0
- django-json-widget 2.1.1
- django-admin-autocomplete-filter 0.7.1
- django-richtextfield 1.6.2
- libsass 0.23.0
- django-compressor 4.6.0
- django-sass-processor 1.4.2

### Produção & Monitoramento
- sentry-sdk[django,rq] 2.49.0
- gunicorn 23.0.0
- uvicorn 0.40.0

## 🚀 Instalação

### Via PyPI

```bash
pip install avaintegration_metapackage
```

### Via Docker

A imagem Docker base já inclui o metapackage instalado:

```dockerfile
FROM avaintegrationbase:latest
```

Ou versão específica:

```dockerfile
FROM avaintegrationbase:1.0.0
```

## 📋 Uso

### Em projetos Django

Adicione ao seu `requirements.txt` ou `pyproject.toml`:

```txt
avaintegration_metapackage==1.0.0
```

### Com Poetry

```bash
poetry add avaintegration_metapackage
```

### Com pip-tools

```txt
# requirements.in
avaintegration_metapackage==1.0.0
```

```bash
pip-compile requirements.in
pip-sync requirements.txt
```

## 🔄 Workflow de CI/CD

Este projeto utiliza GitHub Actions para automatizar:

1. **Publicação no PyPI** ao criar uma tag Git
2. **Build da imagem Docker** usando o pacote publicado
3. **Push para Docker Hub** com tags `latest` e versionada

### Como fazer um release

```bash
# 1. Atualize a versão no setup.py (será sobrescrita pela tag)
# 2. Crie e envie a tag
git tag 1.0.1
git push origin 1.0.1

# 3. O GitHub Action irá:
#    - Atualizar setup.py com a versão da tag
#    - Publicar no PyPI
#    - Aguardar 60s para propagação
#    - Construir imagem Docker instalando o pacote do PyPI
#    - Publicar imagem no Docker Hub
```

### Secrets necessários no GitHub

Configure os seguintes secrets no repositório:

- `PYPI_API_TOKEN` - Token de API do PyPI
- `DOCKERHUB_USERNAME` - Usuário do Docker Hub
- `DOCKERHUB_TOKEN` - Token de acesso do Docker Hub

## 🛠️ Desenvolvimento

### Estrutura do projeto

```
metapackage/
├── .github/
│   ├── docker/
│   │   └── Dockerfile          # Dockerfile para imagem base
│   └── workflows/
│       └── publish-pypi-and-docker.yml
├── avaintegration_metapackage/
│   └── __init__.py             # Versão do pacote
├── setup.py                    # Configuração e dependências
├── Dockerfile                  # Dockerfile de desenvolvimento
└── README.md
```

### Atualizando dependências

1. Edite `setup.py` e ajuste as versões em `install_requires`
2. Teste localmente:
   ```bash
   pip install -e .
   ```
3. Faça commit e crie uma nova tag

### Testando localmente

```bash
# Build do pacote
python -m build

# Instalação local
pip install dist/avaintegration_metapackage-*.whl

# Teste da imagem Docker
docker build -t avaintegrationbase:test -f .github/docker/Dockerfile \
  --build-arg PACKAGE_VERSION=1.0.0 .
```

## 📝 Licença

Este projeto está licenciado sob a [Licença especificada no arquivo LICENSE].

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Crie um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-dependencia`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova dependência X'`)
4. Push para a branch (`git push origin feature/nova-dependencia`)
5. Abra um Pull Request

## 📞 Suporte

Para questões ou problemas, abra uma issue no repositório do projeto.

---

**Mantido por**: IFRN - Diretoria de Educação a Distância (DEAD)
