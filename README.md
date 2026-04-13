
[![PyPI version](https://badge.fury.io/py/avaintegration-metapackage.svg)](https://badge.fury.io/py/avaintegration-metapackage)
[![Python Version](https://img.shields.io/pypi/pyversions/avaintegration-metapackage.svg)](https://pypi.org/project/avaintegration-metapackage/)
[![Docker Image](https://img.shields.io/docker/v/ctezlifrn/avaintegrationbase?label=docker)](https://hub.docker.com/r/ctezlifrn/avaintegrationbase)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/cte-zl-ifrn/integration-avaintegration_metapackage/publish-pypi-and-docker.yml?branch=main)](https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/actions)
[![GitHub License](https://img.shields.io/github/license/cte-zl-ifrn/integration-avaintegration_metapackage)](hhttps://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/cte-zl-ifrn/integration-avaintegration_metapackage?style=social)](https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/cte-zl-ifrn/integration-avaintegration_metapackage)](https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/issues)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cte-zl-ifrn/integration-avaintegration_metapackage)](https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/commits/main)

# AVA Integration Metapackage
Meta-pacote Python que agrega todas as dependências necessárias para projetos Django do ecossistema de Integração AVA (Integrador, Painel e Gestor).



## 📦 O que é um metapackage?

Um metapackage é um pacote Python que não contém código próprio, mas declara um conjunto de dependências. Ao instalar o metapackage, todas as suas dependências são instaladas automaticamente, garantindo:

- ✅ **Versionamento unificado** de dependências entre projetos
- ✅ **Consistência** entre ambientes de desenvolvimento, teste e produção
- ✅ **Simplificação** do gerenciamento de dependências
- ✅ **Sincronização automática** via imagem Docker base


## Tecnologias

![Django](https://img.shields.io/badge/Django-6.0.4-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14.4-3776AB?style=flat&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Valkey-6.1.1-DC382D?style=flat&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-enabled-2496ED?style=flat&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-25.3.0-499848?style=flat&logo=gunicorn&logoColor=white)
![Sentry](https://img.shields.io/badge/Sentry-2.57.0-362D59?style=flat&logo=sentry&logoColor=white)

Olhe o arquivo [setup.py](https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/blob/e7ec1a52f216d008539f4a56161fe9461d360c4e/setup.py#L33), atributo `install_requires`, para conhecer as demais bibliotecas.

## 🚀 Instalação

### Via PyPI

```bash
pip install avaintegration_metapackage
```

### Via Docker

A imagem Docker base já inclui o metapackage instalado:

```dockerfile
FROM ctezlifrn/avaintegrationbase:6.0.4.8
```

## 🔄 Workflow de CI/CD


```bash
# 1. Atualize a versão no setup.py (será sobrescrita pela tag)
# 2. Crie e envie a tag
git tag 6.0.4.8
git push origin 6.0.4.8

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
  --build-arg PACKAGE_VERSION=6.0.4.8 .
```

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
