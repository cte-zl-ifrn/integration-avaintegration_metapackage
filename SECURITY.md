# Política de Segurança

## Versões Suportadas

Apenas a versão mais recente do `avaintegration_metapackage` recebe atualizações de segurança.

| Versão | Suportada          |
| ------ | ------------------ |
| 1.0.x  | :white_check_mark: |
| < 1.0  | :x:                |

## Dependências e Atualizações

Este metapackage agrega dependências de terceiros. Monitoramos ativamente as vulnerabilidades das seguintes dependências críticas:

### Atualizações Prioritárias
- **Django** - Framework core, atualizado conforme releases de segurança
- **psycopg** - Driver PostgreSQL, monitorado para CVEs
- **requests** - Vulnerabilidades HTTP/SSL
- **sentry-sdk** - Exposição de dados sensíveis
- **gunicorn/uvicorn** - Vulnerabilidades em servidores WSGI/ASGI

### Processo de Atualização
1. Dependências são revisadas mensalmente
2. Vulnerabilidades críticas (CVSS ≥ 7.0) são corrigidas em 48h
3. Vulnerabilidades médias (CVSS 4.0-6.9) são corrigidas em 7 dias
4. Novas versões são publicadas automaticamente via tag

## Reportando Vulnerabilidades

### 🔒 Para Vulnerabilidades de Segurança

**NÃO abra issues públicas para vulnerabilidades de segurança.**

Por favor, reporte vulnerabilidades de segurança de forma privada:

1. **Email**: Envie para [ead@ifrn.edu.br](mailto:dead.zl@ifrn.edu.br)
2. **Assunto**: `[SECURITY] avaintegration_metapackage - [descrição breve]`
3. **Conteúdo mínimo**:
   - Descrição detalhada da vulnerabilidade
   - Passos para reproduzir
   - Versão afetada
   - Impacto potencial
   - Sugestão de correção (se houver)

### Resposta Esperada

| Prazo | Ação |
|-------|------|
| 24h | Confirmação de recebimento |
| 48h | Avaliação inicial e classificação de severidade |
| 7 dias | Plano de ação e cronograma de correção |

### Processo após Correção

1. Fix desenvolvido em branch privada
2. Testes de validação
3. Release de versão com patch de segurança
4. Publicação de advisory (após usuários terem tempo de atualizar)
5. Crédito ao pesquisador (se desejado)

## Práticas de Segurança

### Desenvolvimento

- ✅ Dependências fixadas com versões específicas
- ✅ Monitoramento automatizado com Dependabot/Renovate
- ✅ Build reproduzível via Docker
- ✅ Token de API com escopo mínimo necessário
- ✅ Secrets nunca commitados no repositório

### Publicação

- ✅ CI/CD com GitHub Actions (ambiente confiável)
- ✅ Autenticação via API tokens, não credenciais
- ✅ Assinatura de releases (quando possível)
- ✅ Imagens Docker com hash digest

### Consumo

**Recomendações para usuários**:

```bash
# ✅ Use versões específicas, não 'latest'
pip install avaintegration_metapackage==1.0.0

# ✅ Verifique integridade com hash (quando disponível)
pip install avaintegration_metapackage==1.0.0 \
  --hash=sha256:...

# ✅ Use ambientes isolados
python -m venv .venv
source .venv/bin/activate
```

## Responsabilidades

### Mantenedores do Projeto

- Monitorar CVEs de dependências
- Avaliar e corrigir vulnerabilidades reportadas
- Publicar advisories de segurança
- Manter documentação atualizada

### Usuários

- Manter o metapackage atualizado
- Reportar comportamentos suspeitos
- Seguir práticas seguras de deployment
- Não usar credenciais em código

## Escopo de Segurança

### O que ESTÁ no escopo

✅ Vulnerabilidades nas dependências listadas  
✅ Problemas no processo de build/publicação  
✅ Exposição acidental de credenciais  
✅ Injeção maliciosa de código  

### O que NÃO está no escopo

❌ Problemas em aplicações que usam este metapackage  
❌ Configurações inseguras do usuário  
❌ Vulnerabilidades em repositórios privados dos usuários  
❌ Ataques de engenharia social  

## Auditoria e Compliance

### Logs de Segurança

Mantemos logs de:
- Publicações no PyPI (via GitHub Actions logs)
- Alterações de dependências (via git history)
- Issues de segurança resolvidas

### Ferramentas Utilizadas

- **Dependabot**: Alertas automáticos de vulnerabilidades
- **pip-audit**: Verificação de dependências Python
- **Sentry**: Monitoramento de erros em produção
- **GitHub Security Advisories**: Rastreamento de CVEs

## Recursos Adicionais

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)
- [PyPI Security Policy](https://pypi.org/security/)

## Histórico de Segurança

Nenhum incidente de segurança reportado até o momento.

---

**Última atualização**: Fevereiro 2026  
**Mantido por**: IFRN - Diretoria de Educação a Distância (DEAD)
