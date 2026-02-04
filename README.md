# Django Integration Metapackage

Meta pacote Python para o ecossistema de Integração AVA (Integrador, Painel e Gestor)

## Descrição

Este é um meta pacote que agrega todas as dependências necessárias para projetos Django do ecossistema de Integração AVA. Em vez de gerenciar um arquivo `requirements.txt` com múltiplas dependências, você pode simplesmente instalar este pacote e todas as dependências necessárias serão instaladas automaticamente.

## Dependências Incluídas

Este meta pacote inclui as seguintes dependências:

- Django 5.2.10
- django-rule-engine 1.0.1
- django-dsgovbr 5.2.3
- django-better-choices 1.18
- jsonschema 4.26.0
- rule-engine 4.5.3
- requests 2.32.5
- django-valkey 0.4.0
- django-simple-history 3.11.0
- whitenoise 6.11.0
- django-import-export 4.4.0
- django-json-widget 2.1.1
- django-admin-autocomplete-filter 0.7.1
- django-richtextfield 1.6.2
- psycopg[binary,pool] 3.3.2

## Instalação

### Via pip

```bash
pip install django-integration-metapackage
```

### Instalação a partir do código-fonte

```bash
git clone https://github.com/cte-zl-ifrn/python-integration_metapackage.git
cd python-integration_metapackage
pip install .
```

### Instalação em modo de desenvolvimento

```bash
pip install -e .
```

## Uso

Após a instalação, todas as dependências estarão disponíveis em seu ambiente Python. Você pode começar a usar Django e os outros pacotes imediatamente:

```python
import django
from django_better_choices import Choices
# ... outros imports
```

## Como funciona um Meta Pacote

Um meta pacote é um pacote Python que não contém código próprio, mas serve para agrupar um conjunto de dependências relacionadas. Isso facilita:

- **Gerenciamento de dependências**: Instale múltiplos pacotes com um único comando
- **Versionamento consistente**: Garanta que todos os projetos usem as mesmas versões das dependências
- **Simplicidade**: Substitui arquivos `requirements.txt` longos por uma única dependência

## Desenvolvimento

### Estrutura do Projeto

```
python-integration_metapackage/
├── django_integration_metapackage/
│   └── __init__.py
├── pyproject.toml
├── README.md
└── LICENSE
```

### Atualizando Dependências

Para atualizar as dependências incluídas neste meta pacote:

1. Edite o arquivo `pyproject.toml`
2. Atualize a versão no array `dependencies`
3. Incremente a versão do pacote
4. Faça commit e publique uma nova versão

## Licença

MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contribuindo

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request no repositório do projeto.
