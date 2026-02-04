# Release Notes - v1.0.0

**Data de lançamento**: 04 de fevereiro de 2026

## 🎉 Primeiro Release Oficial

Esta é a primeira versão estável do **avaintegration_metapackage**, um meta-pacote Python que consolida todas as dependências necessárias para projetos Django do ecossistema de Integração AVA.

## ✨ Recursos Principais

### 📦 Gerenciamento Unificado de Dependências
- **65+ pacotes** Python curados e testados
- Versionamento fixo para garantir reprodutibilidade
- Compatibilidade testada entre todas as dependências

### 🐳 Imagem Docker Base
- Imagem `avaintegrationbase:1.0.0` disponível no Docker Hub
- Python 3.14.2 slim-trixie
- Todas as dependências pré-instaladas
- Tamanho otimizado para produção

### 🔄 CI/CD Automatizado
- GitHub Actions para publicação automática
- Deploy no PyPI ao criar tags
- Build e publicação de imagem Docker sincronizada
- Aguarda propagação do PyPI antes do build Docker

## 📚 Dependências Incluídas

### Core Framework
- **Django 5.2.11** - Framework web principal
- **django-extensions 4.1** - Utilitários para desenvolvimento
- **sc4py 0.1.4** - Sistema de configuração

### Pacotes Internos DEAD
- **django-rule-engine 1.0.1** - Motor de regras de negócio
- **django-dsgovbr 5.2.3** - Tema Design System GovBR

### Banco de Dados
- **psycopg 3.3.2** [binary,pool] - Driver PostgreSQL otimizado

### Cache & Session
- **django-valkey 0.4.0** - Integração Valkey/Redis
- **valkey 6.1.1** - Cliente Valkey

### Interface Administrativa
- **whitenoise 6.11.0** - Servir arquivos estáticos
- **django-import-export 4.4.0** - Importação/exportação de dados
- **django-json-widget 2.1.1** - Editor JSON
- **django-admin-autocomplete-filter 0.7.1** - Filtros com autocomplete
- **django-richtextfield 1.6.2** - Editor de texto rico

### Assets & Compilação
- **libsass 0.23.0** - Compilador SASS
- **django-compressor 4.6.0** - Compressão de assets
- **django-sass-processor 1.4.2** - Processamento SASS

### APIs & HTTP
- **requests 2.32.5** - Cliente HTTP
- **httpie 3.2.4** - Cliente HTTP CLI

### Validação & Regras
- **django-better-choices 1.18** - Choices tipadas
- **jsonschema 4.26.0** - Validação JSON Schema
- **rule-engine 4.5.3** - Motor de regras genérico

### Auditoria
- **django-simple-history 3.11.0** - Histórico de alterações

### Produção & Monitoramento
- **gunicorn 23.0.0** - Servidor WSGI
- **uvicorn 0.40.0** - Servidor ASGI
- **sentry-sdk 2.49.0** [django,rq] - Monitoramento de erros

## 🚀 Como Usar

### Instalação via PyPI

```bash
pip install avaintegration_metapackage==1.0.0
```

### Uso com Docker

```dockerfile
FROM avaintegrationbase:1.0.0

COPY . /app
WORKDIR /app

# Suas dependências adicionais
RUN pip install -r requirements-extra.txt

CMD ["gunicorn", "myproject.wsgi:application"]
```

### Atualização de Projeto Existente

```bash
# Remova dependências individuais do requirements.txt
# e substitua por:
avaintegration_metapackage==1.0.0

# Instale
pip install -r requirements.txt

# Verifique se tudo funciona
python manage.py check
```

## 🔧 Configuração Necessária

### Secrets do GitHub (para CI/CD)

Se for fazer fork ou contribuir:

```yaml
PYPI_API_TOKEN: Token de API do PyPI
DOCKERHUB_USERNAME: Usuário do Docker Hub
DOCKERHUB_TOKEN: Token do Docker Hub
```

## 📋 Requisitos

- **Python**: 3.12+ (recomendado 3.14)
- **PostgreSQL**: 12+ (para psycopg 3.x)
- **Valkey/Redis**: 6+ (opcional, para cache)

## 🐛 Problemas Conhecidos

Nenhum problema conhecido nesta versão.

## ⚠️ Breaking Changes

Não aplicável (primeira versão).

## 🔐 Segurança

- Todas as dependências auditadas para vulnerabilidades conhecidas
- Versionamento fixo previne atualizações automáticas não testadas
- Processo de reporte de vulnerabilidades documentado em [SECURITY.md](SECURITY.md)

## 📖 Documentação

- **README.md**: Guia completo de uso
- **SECURITY.md**: Política de segurança
- **GitHub Workflow**: `.github/workflows/publish-pypi-and-docker.yml`

## 🙏 Agradecimentos

Agradecemos a todos os mantenedores dos pacotes open source incluídos neste metapackage.

## 🔗 Links

- **PyPI**: https://pypi.org/project/avaintegration_metapackage/1.0.0/
- **Docker Hub**: https://hub.docker.com/r/<username>/avaintegrationbase
- **Código Fonte**: https://github.com/IFRN/ava-metapackage
- **Issues**: https://github.com/IFRN/ava-metapackage/issues

## 📝 Próximos Passos

Para a versão 1.1.0, planejamos:
- Adicionar suporte para PostgreSQL async (psycopg3 async)
- Incluir ferramentas de testes (pytest, coverage)
- Adicionar suporte para Celery/RQ workers
- Melhorias na imagem Docker (multi-stage build otimizado)

---

**Mantido por**: IFRN - Diretoria de Educação a Distância (DEAD)  
**Licença**: Ver arquivo LICENSE
