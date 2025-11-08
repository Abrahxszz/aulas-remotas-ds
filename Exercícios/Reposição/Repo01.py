nome = input("Insira seu nome: ") # Cria uma variável que pede o nome -> string
idade_text = input("Insira sua idade: ") # Cria uma variável que pede a idade -> sting
idade_int = int(idade_text) # Converte a variável Idade_Text (que estava em string) para Int (num.)

if idade_int >=18: # Se {idade inserida} for maior ou igual a 18
    print(f"Olá, {nome}, você é maior de idade!")
else: # Se não...
    print(f"Olá, {nome}, você é menor de idade!")