import os
import random
from datetime import datetime, timedelta
from faker import Faker

#contador pra saber se realmente passamos X dados
contadorDeIteracao = 0
numeroTotalDeDados = 49653

#Gerar dados falsos apartir da biblioteca Faker
gerarDadoFalso = Faker()

# Lista de codigos de Paises da america do sul
ProductID = [
                'FE01', 'FE02', 'FE03', 'FE04', 'FE05', 'FE06', 'FE07', 'FE08', 'FE09', 'FE10', 
                'BE01', 'BE02', 'BE03', 'BE04', 'BE05', 'BE06', 'BE07', 'BE08', 'BE09', 'BE10',
                'SER1', 'SER2', 'SER3', 'SER4', 'SER5'
            ]

# Cria um arquivo chamado "data_sample"
with open("2022_market.txt", "w") as file:

    # Escreve um header
    file.write("TransactionID, ClientID, ProductID, BoughtDate\n")
    
    #Gravar 15 mil dados (possivel escolher quantidade)
    for i in range(numeroTotalDeDados):
        
        contadorDeIteracao += 1
        clientID = random.randint(55001,75001)
        
        produtosComprados = random.randint(1,4)
        random.shuffle(ProductID)
        productBought = random.sample(ProductID, k = produtosComprados)
        
        boughtDate = (datetime(2022,1,1) + timedelta(days=random.randint(0,364))).strftime("%Y-%m-%d")

        file.write('{}, {}, {}, {}\n'.format(contadorDeIteracao, clientID, '#'.join(productBought), boughtDate))

# Ve se o arquivo foi criado corretamente
if os.path.exists("2022_market.txt") and (contadorDeIteracao == numeroTotalDeDados):
    print('Arquivo criado com sucesso')

else:
    print("A criação do arquivo falhou")