def calculadora(num1,num2,op): # Cria uma função que "chama" as variáveis num1, num2 e op
    if op == "+": # Se a variável op for +
       return  num1 + num2 # Retornará como resultado da função
    elif op == "-": 
        return num1 - num2 
    elif op == "*": 
        return num1 * num2 
    elif op == "/": 
        return num1/num2 
    else: # Caso nenhuma das condições anteriores forem satisfeitas, retornará como erro.
        return "Erro!" 

num1 = int(input("num1: ")) # Pode colocar input depois da função
# Boa prática definir função antes e depois "chamar" os inputs 
num2 = int(input("num2: "))
op = input("Operações (+, -, *, /): ")

print(calculadora(num1,num2,op)) # Não esquecer de colocar os argumentos da função, se não, ela não receberá nenhum valor