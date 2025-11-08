num = input("Digite o número que você quer multiplicar: ") # cria uma variável que pergunta o número que será multiplicado
num_int = int(num) # String -> Int

print(f"--- Tabuada do {num} ---")

for i in range(1,11): # Loop de i que começa em 1 e vai até 10, pois para antes do 11.
    print(f"{num_int} * {i} = {num_int*i}")