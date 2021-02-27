# SISTEMA DE GERENCIAMENTO DE EVENTOS

## DESCRIÇÃO

Será realizado um treinamento para uma empresa de TI. O treinamento será realizado em 2 etapas e as pessoas serão divididas em salas com lotação variável. 
Serão realizados também dois intervalos de café em 2 espaços distintos. O presente sistema gerenciará este evento.

## PRINCIPAIS FUNCIONALIDADES

* O cadastro de pessoas, com nome e sobrenome;
* O cadastro das salas do evento, com nome e lotação;
* O cadastro dos espaços de café pelo nome e lotação;
* A consulta de cada pessoa;
* A consulta de cada sala e espaço de café

## REQUISITOS

Para execução do sistema é necessário possuir as bibliotecas PyQt5 e mysql.connector

O PyQt5 é uma ferramenta utilizada para desenvolvimento de interfaces voltada para Python, desenvolvida em código aberto. Sua licença é GPLV3.

O mysql.connector é um driver para persistência de dados. Sob licença GPL.



## BANCO DE DADOS

Foi realizado um backup do banco de dados com o auxílio da ferramenta phpMyAdmin, gerando o arquivo "treinamento.sql", contendo toda a estrutura da database "treinamento", já preenchida com alguns dados modelo. Para uso da aplicação, o backup deve
ser importado para o banco de dados mySQL com o uso de uma ferramenta de preferência do usuário.
O banco de dados por padrão está configurado com user = "root" e senha vazia passwd = "". Caso o banco de dados do usuário use configurações diferentes, os arquivos "controle.py", "gerenciar_cafes.py" e "gerenciar_salas.py" devem ter seus dados referentes à persistência de dados alterados para conexão com o banco de dados.

## EXECUÇÃO DO CÓDIGO

Para execução do código, serão necessários:
* Python 3.9
* MySQL
* PyQT5
* MySQL Connector

## Como rodar a aplicação

* Instalar o Python pelo site oficial, e adicionar nas variáveis de ambiente:https://www.python.org/

* Clonar ou fazer o download do projeto:
```
    git clone https://github.com/Arodazi/treinamento/tree/master
```

* Importar o arquivo 'treinamento.sql' para o MySQL por meio de uma ferramenta gerenciadora de banco de dados;

* Instalar as bibliotecas pela linha de comando:
    * PYQT5
    
    ```
        pip install PyQt5
    ```

    * MySQL Connector
    ```
        pip install mysql-connector-python
    ```

* Abrir a pasta do projeto com a IDE de sua escolha, e executar o arquivo 'controle.py'

## TESTES

O código foi compilado com a IDE Visual Studio Code, pelo comando "Run Code", no arquivo "controle.py".

## USO DA INTERFACE

O sistema apresenta na tela inicial as opções de cadastro disponíveis, um botão de distribuição de alunos e um botão de consulta.

### CADASTRO DE PESSOA

O botão "CADASTRO DE PESSOA" abre uma nova janela, que permite ao usuário preencher "NOME" e "SOBRENOME". Ao preencher, levar em consideração
apenas a primeira palavra do nome completo como "NOME". Ex.: NOME: Ana SOBRENOME: Paula da Silva. 
Ao clicar no botão "ENVIAR", os dados de NOME e SOBRENOME serão adicionados ao banco de dados, na tabela "pessoas" juntamente com uma id única.
Após finalizar o cadastro das pessoas, clicar no botão de fechar janela para retornar à janela inicial.

### CADASTRO DE SALA

O botão "CADASTRO DE SALA" abre uma nova janela, que permite ao usuário preencher "NOME" e "LOTAÇÃO" da sala. 
Ao clicar no botão "ENVIAR", os dados de NOME e LOTAÇÃO serão adicionados ao banco de dados, na tabela "salas" juntamente com uma id única.
Após finalizar o cadastro das salas, clicar no botão de fechar janela para retornar à janela inicial.

### CADASTRO DE ESPAÇO PARA CAFÉ

O botão "CADASTRO DE ESPAÇO PARA CAFÉ" abre uma nova janela, que permite ao usuário preencher "NOME" e "LOTAÇÃO" do espaço para café. 
Ao clicar no botão "ENVIAR", os dados de NOME e LOTAÇÃO serão adicionados ao banco de dados, na tabela "espacos" juntamente com uma id única.
Após finalizar o cadastro dos espaços para café, clicar no botão de fechar janela para retornar à janela inicial.

## DISTRIBUIÇÃO DE ALUNOS

Após finalizar todos os cadastros, caso seja a primeira execução ou tenha ocorrido novo cadastro, é necessário clicar em "DISTRIBUIR ALUNOS".
A distribuição de alunos é feita de maneira a preencher de maneira semelhante todas as salas e espaços de café, com diferença máxima de um aluno 
entre salas/espaços de café.
Os dados de aluno, sala e espaço para café serão armazenados no banco de dados em tabelas específicas para cada etapa.
Para a primeira etapa, o id de cada aluno juntamente com seus respectivos id de sala e id de espaço serão armazenados no banco de dados na tabela "alunos_etapa01".
A distribuição para a segunda etapa fará a divisão de metade dos alunos presentes nas salas e acomodá-los em salas diferentes. Para garantir maior
diversificação, o mesmo será feito para os espaços de café. 
Para a segunda etapa, o id de cada aluno juntamente com seus respectivos id de sala e id de espaço serão armazenados no banco de dados na tabela "alunos_etapa02".

O botão "CONSULTAR" abre uma nova janela que permite a consulta de "PESSOA", "SALA" ou "ESPAÇO PARA CAFÉ".
Obs.: Certificar que o botão "DISTRIBUIR ALUNOS" tenha sido clicado antes de clicar em "CONSULTAR".

## CONSULTAS

### CONSULTA DE PESSOA

A janela de CONSULTA DE PESSOA permite selecionar um aluno da lista de alunos disponíveis. Ao clicar no botão BUSCAR, serão mostradas as informações: NOME, SOBRENOME, NOME DA SALA, NOME DO ESPAÇO PARA CAFÉ
referentes aquele aluno, para cada uma das duas etapas.
Há também o botão LISTAR TODOS, que permite a exibição de uma lista com todos os alunos, com as informações NOME, SOBRENOME, NOME DA SALA, NOME DO ESPAÇO PARA CAFÉ
referentes a cada aluno, para cada uma das duas etapas. Obs.: Ao realizar novo cadastro, se certificar de clicar novamente em LISTAR TODOS.

### CONSULTA DE SALA

A janela de CONSULTA DE SALA permite selecionar uma sala da lista de salas disponíveis. Ao clicar no botão BUSCAR, serão listados os alunos (NOME e SOBRENOME) que ocuparão aquela sala em cada uma das etapas.

### CONSULTA DE ESPAÇO PARA CAFÉ

A janela de CONSULTA DE ESPAÇO PARA CAFÉ permite selecionar um espaço para café da lista de espaços disponíveis. Ao clicar no botão BUSCAR, serão listados os alunos (NOME e SOBRENOME) 
que ocuparão aquele espaço para café em cada uma das etapas.
