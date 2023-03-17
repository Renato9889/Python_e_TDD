import pytest

from codigo.bytebank import Funcionario
from pytest import mark
class TestClass:
    def test_quando_idade_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000" # Given-Contexto
        esperado = 23

        funvionario_teste = Funcionario("Teste",entrada,3111)
        resultado = funvionario_teste.idade() #When-ação

        assert resultado==esperado #Then-desfecho
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho' #Given
        esperado = "Carvalho"

        lucas = Funcionario(entrada,"11/11/2000",2111)
        resultado = lucas.sobrenome() #When

        assert resultado == esperado #Then

    def test_quando_decresscimo_salario_recebe_100000_retorna_90000(self):
        entrada_salario = 100000  # Given
        entrada_nome = "Paulo Mourão"
        esperado = 90000

        funvionario_teste = Funcionario(entrada_nome,11/12/1997,entrada_salario)
        funvionario_teste.decrescimo_salario() #When
        resultado = funvionario_teste.salario

        assert resultado==esperado #Then
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100_deve_retorna_100(self):
        entrada = 1000  # Given
        esperado = 100

        funcionario_teste = Funcionario("Teste", "11/11/2000", entrada)
        resultado = funcionario_teste.calcular_bonus() # When

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000  # Given

            funcionario_teste = Funcionario("Teste", "11/11/2000", entrada)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado  # Then
    #def test_retorn0_str(self):
      #  nome, data_nascimento, salario = "Teste", "12/03/1999",2000  # Given
      #  esperado = 'Funcionario(Teste, 12/03/1999, 2000)'

      #  funcionario_teste = Funcionario(nome, data_nascimento, salario)
      #  resultado = funcionario_teste.__str__()  # When

      #  assert resultado == esperado  # Then