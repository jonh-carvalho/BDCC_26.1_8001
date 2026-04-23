# Plano de Aula - Big Data (Modelo Colunar e Modelo Orientado a Documentos)

## 1. Contexto da Aula

- **Disciplina**: Big Data / Bancos NoSQL
- **Tema central**: Comparacao entre armazenamento colunar e orientado a documentos
- **Base pratica**:
  - [bigdata/colunar/colunar.ipynb](bigdata/colunar/colunar.ipynb)
  - [bigdata/orientadodocumento/odoc.ipynb](bigdata/orientadodocumento/odoc.ipynb)
  - [bigdata/colunar/dados_logs.csv](bigdata/colunar/dados_logs.csv)
  - [bigdata/colunar/dados_logs.parquet](bigdata/colunar/dados_logs.parquet)
  - [bigdata/orientadodocumento/dados_usuarios.json](bigdata/orientadodocumento/dados_usuarios.json)
  - [bigdata/orientadodocumento/usuarios_tinydb.json](bigdata/orientadodocumento/usuarios_tinydb.json)

## 2. Objetivos de Aprendizagem

Ao final da aula, o estudante devera ser capaz de:

1. Diferenciar modelo colunar e modelo orientado a documentos.
2. Explicar porque Parquet tende a ser mais eficiente que CSV em analitica.
3. Executar consultas analiticas com DuckDB sobre arquivos colunares.
4. Inserir, consultar, atualizar e remover documentos com TinyDB/MongoDB.
5. Identificar criterios de escolha entre banco relacional, colunar e documento.

## 3. Pre-requisitos

- Python 3.x funcional.
- Bibliotecas:
  - `pandas`, `numpy`, `pyarrow`, `duckdb`, `matplotlib`
  - `tinydb` (e opcionalmente `pymongo` + MongoDB local)
- No minimo um notebook executando no VS Code/Jupyter.

## 4. Duracao Sugerida

- **Total**: 2h40 (pode ser adaptado para 2h ou 4h).

## 5. Roteiro de Aula (Passo a Passo)

## Bloco A - Abertura e alinhamento (15 min)

1. Apresentar o problema: diferentes cargas de trabalho exigem diferentes modelos de armazenamento.
2. Definir rapidamente:
	- OLTP vs OLAP
	- Dados estruturados, semi-estruturados e aninhados
3. Mostrar o mapa da pasta [bigdata](bigdata).

## Bloco B - Pratica 1: Modelo Colunar (55 min)

1. Executar os passos de [bigdata/colunar/colunar.ipynb](bigdata/colunar/colunar.ipynb):
	- Geracao ou leitura de dados de log.
	- Conversao CSV -> Parquet.
	- Consulta SQL com DuckDB.
2. Coletar evidencias objetivas:
	- Tamanho dos arquivos.
	- Tempo de leitura/consulta.
3. Discussao guiada:
	- Por que leitura de colunas reduz I/O?
	- Em quais cenarios o ganho cresce?
4. Entrega rapida do bloco:
	- Tabela com `metrica`, `csv`, `parquet`, `diferenca_percentual`.

## Bloco C - Pratica 2: Modelo Orientado a Documentos (55 min)

1. Executar os passos de [bigdata/orientadodocumento/odoc.ipynb](bigdata/orientadodocumento/odoc.ipynb):
	- Geracao de JSON de usuarios com estrutura aninhada.
	- Insercao em TinyDB (e opcionalmente MongoDB).
	- Consultas por atributo aninhado.
	- Atualizacao e exclusao de documentos.
2. Discussao guiada:
	- Flexibilidade de esquema e evolucao de modelo.
	- Trade-off entre flexibilidade e governanca de dados.
3. Entrega rapida do bloco:
	- Uma consulta por cidade.
	- Uma consulta por usuario.
	- Uma atualizacao correta de campo aninhado.

## Bloco D - Comparacao consolidada (20 min)

1. Construir quadro comparativo em sala com 5 eixos:
	- Estrutura de dados
	- Performance de leitura analitica
	- Facilidade de evolucao de schema
	- Complexidade de consulta
	- Casos de uso tipicos
2. Relacionar com servicos AWS:
	- Colunar/analitico: S3 + Athena, Redshift
	- Documento: DynamoDB (document-like key-value), DocumentDB/MongoDB

## Bloco E - Fechamento e avaliacao (15 min)

1. Quiz rapido (5 perguntas objetivas).
2. Debrief: quando **nao** usar cada modelo.
3. Definicao de atividade pos-aula.

## 6. Avaliacao

## Formativa (durante a aula)

- Participacao nas discussoes.
- Execucao correta dos notebooks.
- Interpretacao dos resultados de performance.

## Somativa (pos-aula)

- Mini-relatorio (1 pagina) contendo:
  1. Comparacao tecnica entre os dois modelos.
  2. Evidencias coletadas (tempo e tamanho).
  3. Recomendacao para um cenario real escolhido pelo aluno.

## Rubrica (0 a 10)

1. Correta execucao tecnica: 3,0
2. Analise critica dos resultados: 3,0
3. Justificativa da escolha de tecnologia: 3,0
4. Clareza e organizacao: 1,0

## 7. Abordagens Significantes Faltantes (e recomendadas)

Com base nos materiais atuais da pasta [bigdata](bigdata), estas abordagens merecem ser adicionadas:

1. **Qualidade de dados e validacao de schema**
	- Falta checagem de nulos, duplicatas, tipos invalidos e regras de negocio.
	- Recomendar uma celula de validacao antes das consultas.

2. **Benchmark metodologicamente justo**
	- Hoje a comparacao CSV vs Parquet e simples.
	- Incluir repeticoes, aquecimento de cache e media/desvio padrao para evitar conclusoes enviesadas.

3. **Particionamento e compressao em Parquet**
	- Assunto central em Big Data e nao aparece no roteiro atual.
	- Demonstrar particionamento por data/categoria e impacto em scan.

4. **Evolucao de schema em documentos**
	- Mostrar documentos com campos faltantes/adicionados e como tratar no codigo.
	- Essencial para cenarios reais de crescimento de produto.

5. **Indexacao e custo de consulta**
	- Em MongoDB/TinyDB, faltou discutir indices e impacto em latencia.
	- Em colunar, faltou discutir pushdown, pruning e custo de varredura.

6. **Consistencia e integridade em atualizacao aninhada**
	- O arquivo [bigdata/orientadodocumento/usuarios_tinydb.json](bigdata/orientadodocumento/usuarios_tinydb.json) mostra um caso de inconsistência de atualizacao de campo aninhado.
	- Incluir atividade de "detectar e corrigir inconsistencias" como objetivo explicito.

7. **Conexao com arquitetura em nuvem (AWS)**
	- Falta um fechamento arquitetural: quando usar S3 + Athena + Glue, quando usar DynamoDB, e limites de cada escolha.

## 8. Extensao Recomendada (opcional, 40 min extra)

1. Implementar uma pipeline curta:
	- JSON de eventos -> validacao -> armazenamento em Parquet particionado.
2. Criar 2 consultas:
	- Uma agregacao analitica (colunar).
	- Uma busca por perfil/entidade (documento).
3. Defender arquitetura escolhida em 3 minutos por grupo.

## 9. Materiais de Apoio

- Notebook colunar: [bigdata/colunar/colunar.ipynb](bigdata/colunar/colunar.ipynb)
- Notebook documentos: [bigdata/orientadodocumento/odoc.ipynb](bigdata/orientadodocumento/odoc.ipynb)
- Datasets da pratica:
  - [bigdata/colunar/dados_logs.csv](bigdata/colunar/dados_logs.csv)
  - [bigdata/colunar/dados_logs.parquet](bigdata/colunar/dados_logs.parquet)
  - [bigdata/orientadodocumento/dados_usuarios.json](bigdata/orientadodocumento/dados_usuarios.json)
  - [bigdata/orientadodocumento/usuarios_tinydb.json](bigdata/orientadodocumento/usuarios_tinydb.json)

## 10. Checklist do Professor

1. Conferir bibliotecas instaladas antes da aula.
2. Garantir que os notebooks abrem sem erro de kernel.
3. Preparar resultado esperado das consultas para comparacao rapida.
4. Reservar 15 min finais para reflexao de arquitetura.
5. Coletar mini-relatorio com prazo e criterios claros.
