class produto:
    def __init__(self, nome, preco, quantidade):

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


   

    def mostrar_info(self):
        print(f"nome: {self.nome}")  # Saída: nome do produto
        print(f"preço: R$ {self.preco}")  # Saída: 1.99 preço do produto
        print(f"quantidade: {self.quantidade}")  # Saída: será a quantidade do produto

        def mostrar_valor_total_estoque(self):
         valor_total = self.preco * self.quantidade
         print(f"O valor total de estoque deste produto é"{round(valor_total, 2)})    


                

  
 # Exemplo de uso da classe Produto(seu comportamento)
       
p1 = produto("Água", 1.99, 20)#estes ites que mostra a saida do prduto nao pode esta nomesmo nivel da class
p1.mostrar_info()

p2 = produto("Refrigerante", 2.50, 10)
p2.mostrar_info()


   

