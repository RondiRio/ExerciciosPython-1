codigo = input("Entre com o código do funcionário")
codigo = int(codigo)
salario = 1500.00
nome = 'jose'
situacao = True

tipo = type(salario)

if codigo < 10 or codigo > 10:
    print("Funcionário não encontrado")
elif codigo == 10:
    print("código\n", codigo, "\nSalário\n", salario, "\nNome\n", nome, "\nSituação\n", situacao)