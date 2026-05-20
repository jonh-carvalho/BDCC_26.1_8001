from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Produto

# Como executar os testes:
# 1. Certifique-se de que o ambiente virtual esteja ativado e que as dependências estejam instaladas.
# 2. Navegue até o diretório do projeto onde está localizado o arquivo manage.py.
# 3. Execute o comando: python manage.py test produtos
# 4. O Django irá procurar por classes de teste que herdam de TestCase dentro do aplicativo "produtos" e executará os métodos de teste definidos nessas classes.
# 5. Os resultados dos testes serão exibidos no terminal, indicando quais testes passaram, falharam ou foram ignorados, juntamente com detalhes sobre quaisquer falhas.
# Certifique-se de que o banco de dados de teste esteja configurado corretamente, pois o Django criará um banco de dados temporário para executar os testes e o destruirá após a conclusão dos testes.


# Crie seus testes aqui.
class HealthcheckTests(TestCase):
	def setUp(self):
		self.client = APIClient()

	# Teste para verificar se a rota de healthcheck retorna um status code 200 e o JSON esperado
	def test_healthcheck_root_retornar_200(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), {'status': 'ok'})

# Explique o teste abaixo, o que ele faz e qual é o resultado esperado

# O teste abaixo é uma classe de teste chamada ProdutoApiTests, que herda de TestCase. Ele tem um método setUp que é executado antes de cada teste, onde ele cria uma instância do APIClient para fazer requisições à API.
# O método test_lista_produtos_retorna_200 é um teste que verifica se a lista de produtos retorna um status code 200 (OK) e se os dados retornados estão corretos. Ele cria um produto no banco de dados com nome "Teclado Mecanico", descrição "Teclado sem fio" e preço 299.90. Em seguida, ele faz uma requisição GET para a URL '/api/produtos/' e verifica se o status code da resposta é 200, se o número de produtos retornados é 1 e se o nome do produto retornado é "Teclado Mecanico". O resultado esperado é que o teste passe, indicando que a API está funcionando corretamente para listar os produtos.
# O teste verifica se a API de produtos está funcionando corretamente, retornando um status code 200 e os dados corretos para um produto criado. Se o teste passar, significa que a API está funcionando como esperado.
# O teste é importante para garantir que a funcionalidade de listar produtos na API esteja funcionando corretamente e que os dados retornados sejam precisos. Ele ajuda a identificar possíveis problemas na implementação da API e garante que as mudanças futuras não quebrem essa funcionalidade.
# Em resumo, o teste verifica se a API de produtos retorna um status code 200 e os dados corretos para um produto criado, garantindo que a funcionalidade de listar produtos esteja funcionando corretamente.

class ProdutoApiTests(TestCase):
	# Configuração inicial para os testes
	def setUp(self):
		# Cria um cliente de teste para fazer requisições à API
		self.client = APIClient()

	# Teste para verificar se a lista de produtos retorna um status code 200 e os dados corretos
	def test_lista_produtos_retorna_200(self):
		# Cria um produto no banco de dados para testar a listagem
		Produto.objects.create(
			nome='Teclado Mecanico',
			descricao='Teclado sem fio',
			preco=Decimal('299.90'),
		)

		# Faz uma requisição GET para a URL de listagem de produtos
		response = self.client.get('/api/produtos/')

		# Verifica se o status code da resposta é 200 (OK)
		self.assertEqual(response.status_code, 200)
		# Verifica se o número de produtos retornados é 1
		self.assertEqual(len(response.json()), 1)
		# Verifica se o nome do produto retornado é "Teclado Mecanico"
		self.assertEqual(response.json()[0]['nome'], 'Teclado Mecanico')
