Home
====

Meta-pacote Python 3.14 que agrega todas as dependências necessárias para projetos Django 6.0 
do ecossistema AVA do IFRN(Integrador AVA, Painel AVA, Gestor AVA e Leitor EaD).

.. image:: https://img.shields.io/badge/GitHub-Repository-blue?logo=github
   :target: https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage
   :alt: GitHub Repository

.. image:: https://img.shields.io/badge/License-MIT-lemon.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License

.. image:: https://img.shields.io/pypi/pyversions/avaintegration_metapackage.svg
   :target: https://pypi.org/project/avaintegration_metapackage/
   :alt: Python

.. image:: https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/actions/workflows/publish-pypi.yml/badge.svg
   :target: https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/actions/workflows/publish-pypi.yml
   :alt: Publish

.. image:: https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/actions/workflows/publish-docker-hub.yml/badge.svg
   :target: https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/actions/workflows/publish-docker-hub.yml
   :alt: Publish

.. image:: https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/actions/workflows/docs.yml/badge.svg
   :target: https://kelsoncm.github.io/python-avaintegration_metapackage/
   :alt: Docs

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit


📦 O que é um metapackage?
--------------------------

Um metapackage é um pacote Python que não contém código próprio, mas declara um conjunto de dependências. Ao instalar o metapackage, todas as suas dependências são instaladas automaticamente, garantindo:

- ✅ **Versionamento unificado** de dependências entre projetos
- ✅ **Consistência** entre ambientes de desenvolvimento, teste e produção
- ✅ **Simplificação** do gerenciamento de dependências
- ✅ **Sincronização automática** via imagem Docker base


Tecnologias
-----------


.. image:: https://img.shields.io/badge/Django-6.0.5-092E20?style=flat&logo=django&logoColor=white
   :alt: Django

.. image:: https://img.shields.io/badge/Python-3.14.4-3776AB?style=flat&logo=python&logoColor=white
   :alt: Python

.. image:: https://img.shields.io/badge/PostgreSQL-16-336791?style=flat&logo=postgresql&logoColor=white
   :alt: PostgreSQL

.. image:: https://img.shields.io/badge/Valkey-6.1.1-DC382D?style=flat&logo=redis&logoColor=white
   :alt: Valkey

.. image:: https://img.shields.io/badge/Docker-enabled-2496ED?style=flat&logo=docker&logoColor=white
   :alt: Docker

.. image:: https://img.shields.io/badge/Gunicorn-25.3.0-499848?style=flat&logo=gunicorn&logoColor=white
   :alt: Gunicorn

.. image:: https://img.shields.io/badge/Sentry-2.57.0-362D59?style=flat&logo=sentry&logoColor=white
   :alt: Sentry

Olhe o arquivo 
`pyproject.toml <https://github.com/cte-zl-ifrn/integration-avaintegration_metapackage/blob/main/pyproject.toml>`_,
atributo `dependencies`, para conhecer as demais bibliotecas.

🚀 Instalação
-------------

Via pip
^^^^^^^
.. code-block:: bash
   pip install avaintegration_metapackage

Via Docker
^^^^^^^^^^

A imagem Docker base já inclui o metapackage instalado:

.. code-block:: dockerfile
   FROM ctezlifrn/avaintegrationbase:6.0.4.18

🔄 Workflow de CI/CD
--------------------


.. code-block:: bash
   # 1. Atualize a versão no setup.py (será sobrescrita pela tag)
   # 2. Crie e envie a tag
   git tag 6.0.4.13
   git push origin 6.0.4.13

   # 3. O GitHub Action irá:
   #    - Atualizar setup.py com a versão da tag
   #    - Publicar no PyPI
   #    - Aguardar 60s para propagação
   #    - Construir imagem Docker instalando o pacote do PyPI
   #    - Publicar imagem no Docker Hub

Secrets necessários no GitHub
-----------------------------

Configure os seguintes secrets no repositório:

- `PYPI_API_TOKEN` - Token de API do PyPI
- `DOCKERHUB_USERNAME` - Usuário do Docker Hub
- `DOCKERHUB_TOKEN` - Token de acesso do Docker Hub

🛠️ Desenvolvimento
------------------

Estrutura do projeto
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none
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

Atualizando dependências
^^^^^^^^^^^^^^^^^^^^^^^^

1. Edite `setup.py` e ajuste as versões em `install_requires`
2. Teste localmente:
   .. code-block::bash
      pip install -e .
3. Faça commit e crie uma nova tag

Testando localmente
^^^^^^^^^^^^^^^^^^^^

.. code-block::bash
   # Build do pacote
   python -m build

   # Instalação local
   pip install dist/avaintegration_metapackage-*.whl

   # Teste da imagem Docker
   docker build -t avaintegrationbase:test -f .github/docker/Dockerfile --build-arg PACKAGE_VERSION=6.0.4.13 .

🤝 Contribuindo
---------------

Contribuições são bem-vindas! Por favor:

1. Crie um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-dependencia`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova dependência X'`)
4. Push para a branch (`git push origin feature/nova-dependencia`)
5. Abra um Pull Request

📞 Suporte
----------

Para questões ou problemas, abra uma issue no repositório do projeto.

**Mantido por**: IFRN - Diretoria de Educação a Distância (DEAD)

Next steps
----------

.. toctree::
   :maxdepth: 1

   avaintegration_metapackage