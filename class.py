class House:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
    
    def mostrar_cor(self):
        print(f'A cor da cada é {self.cor}')

    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quartos')

    def mostrar_banheiros(self):
        print(f'Esta casa tem {self.banheiros} banheiros')
    
    def adicionar_quarto(self):
        self.quartos += 1
        print(f'Esta casa tem agora tem {self.quartos} quartos')

    def trocar_cor(self, nova_cor):
        print(f'pintando a casa {self.cor} para {nova_cor}')

print('Casa1:')
casa1 = House('Azul', 4, 5)
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()

print('Casa2:')
casa2 = House('Amarelo', 3, 4)
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.trocar_cor('Verde')