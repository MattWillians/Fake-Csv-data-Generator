# Fake-Csv-data-Generator

# Pode ser modificado para usos variados!!

Uma automatização simples feita para gerar query de SQL ou CSV's com dados falsos, facilitando o testes de alguns sistemas feitos por mim

Ele usa a biblioteca Faker para gerar dados falsos, como nomes de empresas, renda mensal, nível de satisfação e datas de contato. O objetivo é criar um arquivo de texto chamado "client_data_sample.txt" que contenha os dados gerados.

Aqui está uma explicação passo a passo do código:
As bibliotecas necessárias são importadas:

os é usada para interagir com o sistema operacional e manipular arquivos.
random é usada para gerar números aleatórios.
datetime é usada para manipular datas e horários.
Faker é uma biblioteca que gera dados falsos realistas.
O contador contadorDeIteracao é iniciado para rastrear o número de iterações e verificar se o número total de dados foi gerado. numeroTotalDeDados define o número desejado de clientes fictícios.

Uma lista chamada listaDePaises é criada com códigos de países da América do Sul, América do Norte e alguns países da Europa. Esses códigos são usados para representar o país de cada cliente.

O código abre um arquivo chamado "client_data_sample.txt" em modo de escrita.

O cabeçalho é escrito no arquivo para indicar que o banco de dados que será usado é "itSolutions". Isso pode ser modificado conforme necessário.

O loop for é executado numeroTotalDeDados vezes para gerar os clientes fictícios.

Dentro do loop, um código de país é escolhido aleatoriamente a partir da lista listaDePaises.

Em seguida, é gerado um nome de empresa fictício usando a função company() da biblioteca Faker. É usado um conjunto (listaDeEmpresasFalsas) para garantir que não haja empresas duplicadas na lista.

A renda mensal é gerada usando a função uniform() da biblioteca random. Ela gera um número aleatório entre 20.000.000 e 999.999.999, e o resultado é arredondado.

O nível de satisfação é gerado aleatoriamente entre 1 e 10.

Uma data de primeiro contato é gerada escolhendo aleatoriamente um dia entre 01/01/2019 e 31/12/2019. A biblioteca datetime é usada para manipular datas, e a função strftime() é usada para formatar a data no formato "YYYY-MM-DD" esperado pelo banco de dados.

Os dados gerados são escritos no arquivo no formato de uma instrução SQL INSERT. A instrução INSERT INTO é usada para inserir os valores nas colunas CountryCode, CompanyName, MensalIncome, PartnershipStart e SatisfactionLevel da tabela ourclients.

O contador de iterações é incrementado.

Após o término do loop, o arquivo é fechado.

É verificado se o arquivo foi criado corretamente e se o número de iterações é igual ao número total de dados solicitado. Em caso afirmativo, é exibida a mensagem "Arquivo criado com sucesso". Caso contrário, é exibida a mensagem "A criação falhou"
