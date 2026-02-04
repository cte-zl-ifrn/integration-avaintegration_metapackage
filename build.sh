#!/bin/bash
# Script para construir e testar o meta pacote localmente

set -e  # Sair em caso de erro

echo "🔨 Construindo o meta pacote django-integration-metapackage..."
echo ""

# Limpar builds anteriores
echo "🧹 Limpando builds anteriores..."
rm -rf dist/ build/ *.egg-info django_integration_metapackage.egg-info
echo "✓ Builds anteriores removidos"
echo ""

# Construir o pacote
echo "📦 Construindo pacote..."
python -m build
echo "✓ Pacote construído com sucesso!"
echo ""

# Mostrar arquivos gerados
echo "📋 Arquivos gerados:"
ls -lh dist/
echo ""

# Perguntar se deseja instalar em ambiente de teste
read -p "❓ Deseja instalar em um ambiente virtual de teste? (s/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Ss]$ ]]; then
    TEST_ENV="/tmp/test_django_metapackage"
    
    echo "🔧 Criando ambiente virtual de teste em $TEST_ENV..."
    rm -rf "$TEST_ENV"
    python -m venv "$TEST_ENV"
    
    echo "📥 Instalando o pacote no ambiente de teste..."
    "$TEST_ENV/bin/pip" install --upgrade pip > /dev/null
    "$TEST_ENV/bin/pip" install dist/*.whl
    
    echo ""
    echo "✅ Pacote instalado com sucesso!"
    echo ""
    
    echo "📊 Informações do pacote instalado:"
    "$TEST_ENV/bin/pip" show django-integration-metapackage
    
    echo ""
    echo "🧪 Testando imports..."
    "$TEST_ENV/bin/python" -c "
import django_integration_metapackage
import django
from django_better_choices import Choices
import requests
print(f'✓ Meta package version: {django_integration_metapackage.__version__}')
print(f'✓ Django version: {django.get_version()}')
print(f'✓ Requests version: {requests.__version__}')
print('✓ Todos os imports funcionaram!')
"
    
    echo ""
    echo "📦 Dependências instaladas:"
    "$TEST_ENV/bin/pip" list | grep -E "(django|jsonschema|rule-engine|requests|psycopg|whitenoise)"
    
    echo ""
    echo "✅ Teste concluído com sucesso!"
    echo "🗑️  Para remover o ambiente de teste, execute: rm -rf $TEST_ENV"
else
    echo "⏭️  Instalação em ambiente de teste ignorada."
fi

echo ""
echo "🎉 Build concluído com sucesso!"
echo ""
echo "📝 Próximos passos:"
echo "   1. Revisar os arquivos em dist/"
echo "   2. Testar a instalação: pip install dist/*.whl"
echo "   3. Para publicar no PyPI, consulte PUBLISH_GUIDE.md"
