# Roteiro Introdutório de Testes no Django REST

Este roteiro apresenta os fundamentos de testes automatizados no Django usando o que ja esta implementado no app de produtos.

## Parte 1 - Objetivo da aula

Ao final deste roteiro, voce deve conseguir:

1. Entender a estrutura basica de um teste no Django.
2. Executar os testes do app produtos.
3. Explicar o que cada teste valida na API.
4. Escrever um novo teste simples seguindo o mesmo padrao.

## Parte 2 - Pre-requisitos

1. Ambiente virtual ativado.
2. Dependencias instaladas.
3. Estar na raiz do projeto (onde fica o arquivo manage.py).

## Parte 3 - Onde estao os testes atuais

Os testes base usados neste roteiro estao em:

- [produtos/tests.py](produtos/tests.py)

As rotas testadas sao definidas em:

- [catalogo/urls.py](catalogo/urls.py)
- [produtos/urls.py](produtos/urls.py)

## Parte 4 - Estrutura minima de um teste

No Django, os testes normalmente:

1. Herdam de TestCase.
2. Criam um cliente HTTP de teste (APIClient no caso de DRF).
3. Executam uma requisicao.
4. Comparam o resultado obtido com o resultado esperado usando asserts.

## Parte 5 - Teste 1 (Healthcheck)

### O que ele faz

O teste Healthcheck chama a rota raiz / e valida:

1. Status HTTP 200.
2. Corpo JSON igual a {"status": "ok"}.

### Por que ele e importante

Serve como teste rapido de disponibilidade da API. Se ele falha, ha forte indicio de problema de roteamento ou de inicializacao da aplicacao.

## Parte 6 - Teste 2 (Lista de produtos)

### O que ele faz

O teste de listagem:

1. Cria um Produto no banco de dados de teste.
2. Faz GET em /api/produtos/.
3. Valida status 200.
4. Valida que retornou 1 item.
5. Valida o nome do item retornado.

### Conceito-chave

Durante a execucao dos testes, o Django cria um banco de dados temporario. Isso isola os testes e evita afetar dados reais.

## Parte 7 - Executando os testes

Comando para rodar apenas os testes do app produtos:

```bash
python manage.py test produtos
```

Opcional: rodar apenas uma classe especifica:

```bash
python manage.py test produtos.tests.ProdutoApiTests
```

## Parte 8 - Interpretando resultados

1. OK: teste passou.
2. FAIL: a regra de negocio nao bateu com o esperado.
3. ERROR: ocorreu excecao durante execucao (ex.: rota invalida, import quebrado).

## Parte 9 - Exercicio guiado (novo teste)

Implemente um teste para garantir que a lista de produtos inicia vazia quando nenhum produto foi criado.

Sugestao de nome do metodo:

- test_lista_produtos_vazia_retorna_array_vazio

Regras esperadas:

1. Fazer GET em /api/produtos/ sem criar dados antes.
2. Esperar status 200.
3. Esperar lista vazia ([]).

## Parte 10 - Checklist final

1. Conseguiu executar python manage.py test produtos.
2. Entendeu o objetivo de cada assert do healthcheck.
3. Entendeu o objetivo de cada assert da listagem de produtos.
4. Criou e executou pelo menos um teste novo.
5. Confirmou que os testes nao alteram o banco de producao.

## Resumo rapido

Os testes atuais cobrem dois pontos essenciais:

1. API respondendo na rota de healthcheck.
2. API listando produtos corretamente via endpoint REST.

Com essa base, o proximo passo natural e aumentar cobertura para criacao, edicao e exclusao de produtos.
