# Checklist Final de Validacao - Django no AWS Elastic Beanstalk

Data de referencia: 2026-05-18

## Como usar esta checklist

- Marque cada item com [x] somente apos evidenciar no terminal, console AWS ou teste HTTP.
- Reprovacao em qualquer item critico bloqueia o deploy para producao.
- Esta checklist foi pensada para aula/lab (pre e pos deploy).

## Criterios de aprovacao

- Aprovado para aula/demo: 100% dos itens criticos + 80% dos itens importantes.
- Aprovado para producao: 100% dos itens criticos + 100% dos itens importantes.

---

## 1) Pre-deploy (local)

### 1.1 Codigo e dependencias

- [] `requirements.txt` atualizado e sem dependencias de desenvolvimento desnecessarias.
- [] `gunicorn` presente em `requirements.txt`.
- [] `Procfile` presente na raiz do projeto.
- [] `Procfile` sem bind em `127.0.0.1` (usar `0.0.0.0` ou sem bind fixo).
- [] Projeto sobe localmente sem erro com `python manage.py runserver`.

### 1.2 Configuracoes Django (seguranca)

- [] `DEBUG` desabilitado para producao (`DJANGO_DEBUG=False`).
- [] `SECRET_KEY` vem de variavel de ambiente (sem valor hardcoded inseguro).
	
    - Exemplo em `settings.py`: `SECRET_KEY = os.getenv('SECRET_KEY')`.
	- Validar fallback inseguro: nao usar `SECRET_KEY = 'django-insecure-...'` fixo em producao.
	- Configurar `SECRET_KEY` no Elastic Beanstalk em **Configuration > Software > Environment properties**.
	- Em ambiente local, definir no terminal antes de subir a app (PowerShell): `$env:SECRET_KEY='sua-chave-forte'`.
	- [] `ALLOWED_HOSTS` usa variavel de ambiente e inclui dominio do EB.
    #   - Exemplo em `settings.py`: `ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')`.
    - Configurar `DJANGO_ALLOWED_HOSTS` no EB com o dominio da aplicacao (ex: `myapp.elasticbeanstalk.com`).
    #  - Em ambiente local, definir no terminal: `$env:DJANGO_ALLOWED_HOSTS='localhost,

# redireciona todas as requisições HTTP para HTTPS.
- [] `SECURE_SSL_REDIRECT=True` em producao.
# garante que o cookie de sessao so seja enviado via HTTPS.
- [] `SESSION_COOKIE_SECURE=True` em producao.

# garante que o cookie de CSRF so seja enviado via HTTPS.
- [] `CSRF_COOKIE_SECURE=True` em producao.

# ativa HSTS por um tempo definido (em segundos), forçando navegadores a usar HTTPS.
- [] `SECURE_HSTS_SECONDS` configurado em producao.

### 1.3 Banco e segredos

- [] Sem senha de banco hardcoded no codigo.
- [] Variaveis de banco via ambiente (`RDS_*` ou equivalentes).
- [ ] Migrations existentes e consistentes.
- [ ] Comando `python manage.py migrate --plan` executa sem erro.

### 1.4 Elastic Beanstalk (arquivos)

- [] `.ebextensions/django.config` contem `migrate` e `collectstatic`.
- [] Nao existe comando de criacao de superusuario com senha fixa.
- [] Nao existem comandos de permissao ampla (`chmod 777`, `chmod 666`) no projeto.
- [] Mapeamento de staticfiles no proxy esta correto.

### 1.5 Validacao automatica local

- [ ] `python manage.py check --deploy` sem erros criticos.
- [ ] Alertas de seguranca tratados ou justificados para o escopo do lab.

Comando sugerido (PowerShell):

```powershell
$env:DJANGO_DEBUG='False'
python manage.py check --deploy
```

---

## 2) Deploy no Elastic Beanstalk

### 2.1 Ambiente AWS

- [ ] Plataforma Python selecionada corretamente no ambiente EB.
- [ ] Variaveis de ambiente configuradas no EB (`DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, `SECRET_KEY`, banco).
- [ ] Security Group da aplicacao permite trafego HTTP/HTTPS conforme esperado.
- [ ] Banco (RDS) acessivel a partir das instancias do EB.

### 2.2 Publicacao

- [ ] Aplicacao publicada sem rollback automatico.
- [ ] `Health` do ambiente EB em `Green`.
- [ ] Eventos do EB sem erro em `migrate`/`collectstatic`.
- [ ] Processo web iniciado com sucesso (Gunicorn).

---

## 3) Pos-deploy (validacao funcional)

### 3.1 Endpoints e resposta

- [ ] URL raiz responde `200`.
- [ ] Endpoint de healthcheck responde `200` com payload esperado.
- [ ] Endpoint da API principal responde `200` (ou status esperado com autenticacao).
- [ ] Admin Django acessivel quando exigido pelo roteiro.

### 3.2 Arquivos estaticos e midia

- [ ] Arquivos estaticos carregam sem erro 404.
- [ ] Upload de midia funciona no fluxo esperado do lab.
- [ ] URLs de midia retornam arquivo com permissao correta.

### 3.3 Banco e dados

- [ ] CRUD principal grava e le dados no banco do ambiente.
- [ ] Nao ha erro de conexao intermitente com banco nos logs.
- [ ] Charset/collation e timezone estao coerentes com a aplicacao.

### 3.4 Logs e observabilidade

- [ ] Logs do EB sem stack trace recorrente.
- [ ] Erros 5xx monitorados no periodo de validacao.
- [ ] Alarmes basicos (CPU/memoria/erro HTTP) configurados para demonstracao.

---

## 4) Evidencias minimas para entrega (aula/lab)

- [ ] Print da tela de `Health: Green` no Elastic Beanstalk.
- [ ] Print dos eventos mostrando deploy concluido.
- [ ] Print/saida do `check --deploy`.
- [ ] Teste HTTP (curl/Postman/browser) da raiz, healthcheck e API.
- [ ] Pequeno relato de incidentes e correcoes aplicadas.

---

## 5) Bloqueadores comuns (nao prosseguir sem corrigir)

- [ ] `DEBUG=True` em ambiente publicado.
- [ ] `SECRET_KEY` insegura ou hardcoded.
- [ ] Senha de banco no codigo.
- [ ] Superusuario criado automaticamente com senha fixa.
- [ ] Permissoes amplas no filesystem (`777`/`666`).
- [ ] App sem responder no dominio EB por bind incorreto do Gunicorn.

---

## 6) Registro rapido da validacao

- Responsavel:
- Turma/Lab:
- Ambiente EB:
- URL da aplicacao:
- Data/hora da validacao:
- Resultado final: ( ) Aprovado aula/demo  ( ) Aprovado producao  ( ) Reprovado
- Observacoes finais:

