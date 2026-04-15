# AP1

## Objetivo 

Adicionar uma nova classe ao aplicativo Django Rest existente, que já possui uma classe `Produto`, e realizar o deploy do projeto na AWS utilizando o Elastic Beanstalk com o arquivo `app.zip` segundo roteiro de aula.

### Entrega - 15/04/2026

- **Não é necessário a presença do Grupo no Lab 308** se até o início da aula o projeto já estiver  atualizado e o deploy realizado. 
- Repositório Github - Código-fonte do projeto atualizado, incluindo a nova classe e as APIs relacionadas.
- Instruções claras sobre como configurar e executar o projeto localmente, bem como detalhes sobre as alterações realizadas.
- Documentação das etapas realizadas para a implementação e deploy.
- Link para o projeto deployado na AWS Elastic Beanstalk.
- Publique no Github e me adicione no repositório,  e coloque no readme o link da API da aws "no ar" .


### Cenário

Você possui um projeto Django Rest com uma classe `Produto`. Seu objetivo é criar uma nova classe (por exemplo, `Categoria`), relacioná-la adequadamente com `Produto` e garantir que as APIs estejam funcionando corretamente. Após as alterações, faça o deploy do projeto na AWS Elastic Beanstalk utilizando um arquivo `app.zip`. Você deve alterar os arquivos de configuração necessários para garantir que o deploy seja bem-sucedido, seguindo o roteiro de aula fornecido acrescentando as instruções específicas para a configuração do ambiente para a criação do usuário admin(root), para que seja possivel logar no django-admin com administrador.

### Referências

- [Documentação Django Rest Framework](https://www.django-rest-framework.org/)
- [Deploy de aplicações Python no AWS Elastic Beanstalk](https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
- [Roteiro de aula para deploy na AWS Elastic Beanstalk](https://jonh-carvalho.github.io/BDCC_CDIA_26.1_8001/Disciplina/roteiros/07%20-%20eb/)

## Critérios de Correção

- Implementação correta da nova classe e relacionamento com `Produto`
- APIs funcionando conforme esperado
- Deploy realizado com sucesso na AWS Elastic Beanstalk usando `app.zip`
- Documentação clara das etapas realizadas
