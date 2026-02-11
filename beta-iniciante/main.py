valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Em quantos anos você vai pagar: "))

meses = anos * 12
prestacao = valorCasa / meses

if prestacao <= salario * 0.3:
    print("Empréstimo aceito")
else:
    print("Empréstimo negado")
