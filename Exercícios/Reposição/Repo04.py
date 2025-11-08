class Veiculo:
    def __init__(self, marca, modelo): # define suas caracs. | Self -> pois precisa se auto caracterizar.
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo): # (...) -> Para herdar de qual classe ele é.
    def __init__(self, marca, modelo, numero_portas): # Define as caracs. da classe "filho"
        super().__init__(marca, modelo) # O que ele herda
        self.numero_portas = numero_portas # Atributo novo


teste = Carro("Nissan", "Silvia s15", "2") # Fiz só por desencargo de consciência

print(teste.marca)         # Nissan
print(teste.modelo)        # Silvia s15
print(teste.numero_portas) # 2