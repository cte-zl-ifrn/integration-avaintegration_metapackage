# Guia de Publicação no PyPI

Este documento explica como publicar o meta pacote `django-integration-metapackage` no PyPI (Python Package Index).

## Pré-requisitos

1. Conta no PyPI: https://pypi.org/account/register/
2. Conta no TestPyPI (opcional, para testes): https://test.pypi.org/account/register/
3. Instalar ferramentas necessárias:
   ```bash
   pip install --upgrade pip build twine
   ```

## Passos para Publicação

### 1. Preparar o Ambiente

```bash
# Garantir que você está na raiz do projeto
cd /caminho/para/python-integration_metapackage

# Limpar builds anteriores
rm -rf dist/ build/ *.egg-info
```

### 2. Construir o Pacote

```bash
python -m build
```

Este comando criará dois arquivos na pasta `dist/`:
- `django_integration_metapackage-1.0.0-py3-none-any.whl` (wheel)
- `django_integration_metapackage-1.0.0.tar.gz` (source distribution)

### 3. (Opcional) Testar no TestPyPI

Antes de publicar no PyPI oficial, você pode testar no TestPyPI:

```bash
# Upload para TestPyPI
python -m twine upload --repository testpypi dist/*

# Testar instalação do TestPyPI
pip install --index-url https://test.pypi.org/simple/ django-integration-metapackage
```

### 4. Publicar no PyPI

```bash
# Upload para PyPI
python -m twine upload dist/*
```

Você será solicitado a fornecer suas credenciais do PyPI.

### 5. Verificar Publicação

Após a publicação, o pacote estará disponível em:
- https://pypi.org/project/django-integration-metapackage/

E pode ser instalado com:
```bash
pip install django-integration-metapackage
```

## Usando Tokens de API (Recomendado)

Para maior segurança, use tokens de API em vez de senha:

1. Vá para https://pypi.org/manage/account/token/
2. Crie um novo token com escopo apropriado
3. Use o token ao fazer upload:
   ```bash
   python -m twine upload --username __token__ --password <seu-token-aqui> dist/*
   ```

## Configuração do .pypirc (Opcional)

Você pode criar um arquivo `~/.pypirc` para armazenar credenciais:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = <seu-token-pypi>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = <seu-token-testpypi>
```

**ATENÇÃO**: Nunca comite o arquivo `.pypirc` no git!

## Atualizando o Pacote

Para publicar uma nova versão:

1. Atualize a versão em `pyproject.toml` e `django_integration_metapackage/__init__.py`
2. Faça as alterações necessárias
3. Reconstrua e publique:
   ```bash
   rm -rf dist/ build/ *.egg-info
   python -m build
   python -m twine upload dist/*
   ```

## Versionamento Semântico

Siga o [Semantic Versioning](https://semver.org/):
- **MAJOR** (1.x.x): Mudanças incompatíveis com versões anteriores
- **MINOR** (x.1.x): Nova funcionalidade compatível com versões anteriores
- **PATCH** (x.x.1): Correções de bugs compatíveis

Exemplos:
- `1.0.0` → `1.0.1`: Atualização de versões de dependências (patch)
- `1.0.0` → `1.1.0`: Adição de novas dependências (minor)
- `1.0.0` → `2.0.0`: Remoção ou mudança drástica de dependências (major)

## Recursos Adicionais

- Documentação do PyPI: https://packaging.python.org/
- Guia de Publicação: https://packaging.python.org/tutorials/packaging-projects/
- Twine: https://twine.readthedocs.io/
