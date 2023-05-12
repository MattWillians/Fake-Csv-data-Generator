# gerador de lista de clientes - pode ser modificado para usos variados!

#A biblioteca OS pode ser usada para criar, remover, analisar, verificar existencias de N arquivos em sua maquina de forma a apresentar informações relevantes de sua escolha
#RANDOM Consegue pegar N coisas aleatórias em varios lugares, até de listas e dicionarios
#Datetime é usada para tratamento de dados, pode ser usada de formas variadas
#gerador de dados falsos (FAKER)

import os
import random
from datetime import datetime, timedelta
from faker import Faker

#contador pra saber se realmente passamos X dados
contadorDeIteracao = 0
numeroTotalDeDados = 20000

#Gerar dados falsos apartir da biblioteca Faker
gerarDadoFalso = Faker()

# Lista de codigos de Paises da america do sul
listaDePaises = [
                    "AR", "BO", "BR", "CL", "CO", "EC", "GF", "GY", "PE", "PY", "SR", "UY", "VE", #America do Sul
                    "CA", "US", "MX", #America do norte
                    "AL", "AD", "AT", "BY", "BE", "BA", "BG", "HR", "CY", "CZ", "DK", "EE", "FO", "FI", "FR", "DE", "GI", "GR", "HU", "IS", "IE", "IT", "LV", "LI", "LT", "LU", "MK", "MT", "MD", "MC", "ME", "NL", "NO", "PL", "PT", "RO", "RU", "SM", "RS", "SK", "SI", "ES", "SE", "CH", "UA", "GB", "VA" #Europa, (não são todos)
                ]

# Cria um arquivo chamado "data_sample"
with open("client_data_sample.txt", "w") as file:

    # Escreve um header
    file.write("USE itSolutions;\n")
    
    #Gravar 15 mil dados (possivel escolher quantidade)
    for i in range(numeroTotalDeDados):

        # Escolhe um dos codigos de cidade
        codigoDePais = random.choice(listaDePaises)
        
        # gera um nome de empresa aleatorio
        listaDeEmpresasFalsas = set()
        while True:
            nomeDaEmpresa = gerarDadoFalso.company()
            if nomeDaEmpresa not in listaDeEmpresasFalsas:
                listaDeEmpresasFalsas.add(nomeDaEmpresa)
                break
        
        # Gera renda mensal
        rendaMensal = round(random.uniform(20000000, 999999999))

        # gera um nivel de satisfação aleatorio
        nivelDeSatisfacao = random.randint(1,10)

        # escolhe uma data de 01/01/2019 ate 31/12/2019 
        primeiroContato = (datetime(2019,1,1) + timedelta(days=random.randint(0,364))).strftime("%Y-%m-%d")

        # escreve no arquivo
        file.write('INSERT INTO ourclients (CountryCode, CompanyName, MensalIncome, PartnershipStart, SatisfactionLevel) VALUES ("{}","{}",{},"{}",{});\n'.format(codigoDePais, nomeDaEmpresa, rendaMensal, primeiroContato, nivelDeSatisfacao))
        
        contadorDeIteracao += 1

# Ve se o arquivo foi criado corretamente
if os.path.exists("client_data_sample.txt") and (contadorDeIteracao == numeroTotalDeDados):
    print('Arquivo criado com sucesso')

else:
    print("A criação do arquivo falhou")