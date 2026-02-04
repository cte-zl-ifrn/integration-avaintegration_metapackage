from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="avaintegration_metapackage",
    version="1.0.1",
    description="Meta-pacote para projetos Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="IFRN - DEAD",
    author_email="dead.zl@ifrn.edu.br",
    url="https://github.com/IFRN/ava-metapackage",
    project_urls={
        "Bug Reports": "https://github.com/IFRN/ava-metapackage/issues",
        "Source": "https://github.com/IFRN/ava-metapackage",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[
        # Core
        "Django==5.2.11",
        "sc4py==0.1.4",
        "django-extensions==4.1",

        # Da DEAD
        "django-rule-engine==1.0.1",
        "django-dsgovbr==5.2.3",

        # Models
        "django-better-choices==1.18",

        # Rule engine
        "jsonschema==4.26.0",
        "rule-engine==4.5.3",

        # REST
        "httpie==3.2.4",
        "requests==2.32.5",

        # Cache and Session
        "django-valkey==0.4.0",
        "valkey==6.1.1",

        # # Security
        # "cryptography==46.0.3",
        # "pyjwt==2.10.1",

        # Audit
        "django-simple-history==3.11.0",

        # UI
        "whitenoise==6.11.0",
        "django-import-export==4.4.0",
        "django-json-widget==2.1.1",
        "django-admin-autocomplete-filter==0.7.1",
        "django-richtextfield==1.6.2",
        "libsass==0.23.0",
        "django-compressor==4.6.0",
        "django-sass-processor==1.4.2",        

        # Database
        "psycopg[binary,pool]==3.3.2",

        # # Image
        # "pillow==11.3.0",

        # Production
        "sentry-sdk[django,rq]==2.49.0",
        "gunicorn==23.0.0",
        "uvicorn==0.40.0",
    ],
    packages=["avaintegration_metapackage"],
)
