#im sorry its in portuguese because im portuguese


unidade = input("A Temperatura esta em Graus Celsius ou em Fahrenheit (C/F): ")
temp = float(input("Entra a temperatura: "))

if unidade == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"A temperatura em Fahrenheit é: {temp}ºF")
elif unidade == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"A temperatura em Celsius é: {temp}ºC")
else:print(f"{unidade} não é uma unidade de temperatura")
