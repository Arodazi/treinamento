from PyQt5 import uic, QtWidgets
import mysql.connector


from gerenciar_salas import gerenciar_salas
from gerenciar_cafes import gerenciar_cafes

# Conectar ao banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="treinamento"   
)

# Definir funcoes de cadastro

# Funcao de cadastro de pessoa
def chama_cad_pessoa():
    cad_pessoa.show()    

    def f_cad_pessoa():
        nome_pessoa = cad_pessoa.lineEdit.text()
        sobrenome_pessoa = cad_pessoa.lineEdit_2.text()
        
        #Comando banco de dados
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO pessoas (nome, sobrenome) VALUES (%s, %s)"
        dados = (str(nome_pessoa), str(sobrenome_pessoa))
        cursor.execute(comando_SQL,dados)
        banco.commit()

    cad_pessoa.pushButton.clicked.connect(f_cad_pessoa)
   

# Funcao de cadastro de sala
def chama_cad_sala():
    cad_sala.show()    

    def f_cad_sala():
        nome_sala = cad_sala.lineEdit.text()
        lotacao_sala = cad_sala.lineEdit_2.text()
        
        #Comando banco de dados
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO salas (nome, lotacao) VALUES (%s, %s)"
        dados = (str(nome_sala), str(lotacao_sala))
        cursor.execute(comando_SQL,dados)
        banco.commit()

    cad_sala.pushButton.clicked.connect(f_cad_sala)


# Funcao de cadastro de espaco para cafe
def chama_cad_cafe():
    cad_cafe.show()    

    def f_cad_cafe():
        nome_cafe = cad_cafe.lineEdit.text()
        lotacao_cafe = cad_cafe.lineEdit_2.text()
        
        #Comando banco de dados
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO espacos (nome, lotacao) VALUES (%s,%s)"
        dados = (str(nome_cafe), str(lotacao_cafe))
        cursor.execute(comando_SQL,dados)
        banco.commit()

    cad_cafe.pushButton.clicked.connect(f_cad_cafe)

# Definir funcao de distribuicao de pessoas em salas ou espacos
def distribuir():
    # Salvar informacoes no banco de dados
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pessoas"
    cursor.execute(comando_SQL)
    pessoas = cursor.fetchall()
    
    comando_SQL = "SELECT * FROM salas"
    cursor.execute(comando_SQL)
    salas = cursor.fetchall()
    
    comando_SQL = "SELECT * FROM espacos"
    cursor.execute(comando_SQL)
    cafes = cursor.fetchall()
        
    gerenciar_salas(pessoas, salas)
    gerenciar_cafes(pessoas, cafes)
    

# Definir funcoes de consulta

# Apresentar tela de consulas
def chama_cons():
    consultas.show() 

    consultas.pushButton_2.clicked.connect(chama_cons_pessoa)
    consultas.pushButton_5.clicked.connect(chama_cons_sala)
    consultas.pushButton_6.clicked.connect(chama_cons_cafe)


# Definir funcao de consulta de pessoa
def chama_cons_pessoa():
    cons_pessoa.show() 
    cons_pessoa.comboBox.clear()

    # Mostrar lista de nomes
    cursor1 = banco.cursor()
    comando_SQL = "SELECT * FROM pessoas ORDER BY nome;"
    cursor1.execute(comando_SQL)
    dados_lidos = cursor1.fetchall()
    numero_pessoas = len(dados_lidos)
    
    for i in range(numero_pessoas):
        cons_pessoa.comboBox.addItem(str(dados_lidos[i][0]) + " - " + dados_lidos[i][1] + " " + dados_lidos[i][2])

    def f_cons_pessoa():

        # Selecionar pessoa da lista disponivel
        pessoa_selecionada = cons_pessoa.comboBox.currentText().split()
        id_selecionado = pessoa_selecionada[0]
      
        #Comando banco de dados
        cursor = banco.cursor()
        comando_SQL = f"SELECT pessoas.nome, pessoas.sobrenome, salas.nome, espacos.nome FROM alunos_etapa01 JOIN pessoas ON pessoas.id = alunos_etapa01.id_aluno JOIN salas ON salas.id = alunos_etapa01.id_salas JOIN espacos on espacos.id = alunos_etapa01.id_espacos WHERE id_aluno = {id_selecionado} ;"                  
        
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
                
        cons_pessoa.tableWidget.setRowCount(len(dados_lidos))
        cons_pessoa.tableWidget.setColumnCount(len(dados_lidos[0]))
        cons_pessoa.tableWidget.setHorizontalHeaderLabels(['Nome','Sobrenome','Sala','Café'])

        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_pessoa.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        
        # Comando banco de dados
        cursor = banco.cursor()
        comando_SQL = f"SELECT pessoas.nome, pessoas.sobrenome, salas.nome, espacos.nome FROM alunos_etapa02 JOIN pessoas ON pessoas.id = alunos_etapa02.id_aluno JOIN salas ON salas.id = alunos_etapa02.id_salas JOIN espacos on espacos.id = alunos_etapa02.id_espacos WHERE id_aluno = {id_selecionado} ;"
        
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
                
        cons_pessoa.tableWidget_2.setRowCount(len(dados_lidos))
        cons_pessoa.tableWidget_2.setColumnCount(len(dados_lidos[0]))
        cons_pessoa.tableWidget_2.setHorizontalHeaderLabels(['Nome','Sobrenome','Sala','Café'])

        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_pessoa.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    cons_pessoa.pushButton.clicked.connect(f_cons_pessoa)   

    def cons_todaspessoas():       

        cursor = banco.cursor()
        comando_SQL = f"SELECT pessoas.nome, pessoas.sobrenome, salas.nome, espacos.nome FROM pessoas JOIN alunos_etapa01 ON alunos_etapa01.id_aluno = pessoas.id JOIN salas ON salas.id = alunos_etapa01.id_salas JOIN espacos ON espacos.id = alunos_etapa01.id_espacos ORDER BY pessoas.nome;"

        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        cons_pessoa.tableWidget_3.setRowCount(len(dados_lidos))
        cons_pessoa.tableWidget_3.setColumnCount(len(dados_lidos[0]))
        cons_pessoa.tableWidget_3.setHorizontalHeaderLabels(['Nome','Sobrenome','Sala','Café'])


        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_pessoa.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

        
        cursor = banco.cursor()
        comando_SQL = f"SELECT pessoas.nome, pessoas.sobrenome, salas.nome, espacos.nome FROM pessoas JOIN alunos_etapa02 ON alunos_etapa02.id_aluno = pessoas.id JOIN salas ON salas.id = alunos_etapa02.id_salas JOIN espacos ON espacos.id = alunos_etapa02.id_espacos ORDER BY pessoas.nome;"

        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        cons_pessoa.tableWidget_4.setRowCount(len(dados_lidos))
        cons_pessoa.tableWidget_4.setColumnCount(len(dados_lidos[0]))
        cons_pessoa.tableWidget_4.setHorizontalHeaderLabels(['Nome','Sobrenome','Sala','Café'])


        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_pessoa.tableWidget_4.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    cons_pessoa.pushButton_2.clicked.connect(cons_todaspessoas) 
    
  
# Definir funcao de consulta de sala   
def chama_cons_sala():
    cons_sala.show() 
    cons_sala.comboBox.clear()  
    
    # Mostrar lista de salas
    cursor1 = banco.cursor()
    comando_SQL = "SELECT * FROM salas ORDER BY nome;"
    cursor1.execute(comando_SQL)
    dados_lidos = cursor1.fetchall()
    numero_salas = len(dados_lidos)
    
    for i in range(numero_salas):
        cons_sala.comboBox.addItem(str(dados_lidos[i][0]) + " - " + dados_lidos[i][1])

    def f_cons_sala():

        # Selecionar sala da lista disponivel
        sala_selecionada = cons_sala.comboBox.currentText().split()
        id_selecionado = sala_selecionada[0]
       
        # Comando banco de dados
        cursor = banco.cursor()
        comando_SQL = f'SELECT pessoas.nome, pessoas.sobrenome FROM salas JOIN alunos_etapa01 ON alunos_etapa01.id_salas = salas.id JOIN pessoas ON pessoas.id = alunos_etapa01.id_aluno WHERE salas.id = {id_selecionado} ;'
        
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()      
        
        cons_sala.tableWidget.setRowCount(len(dados_lidos))
        cons_sala.tableWidget.setColumnCount(len(dados_lidos[0]))
        cons_sala.tableWidget.setHorizontalHeaderLabels(['Nome','Sobrenome'])      
        
        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_sala.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        
        cursor = banco.cursor()
        comando_SQL = f'SELECT pessoas.nome, pessoas.sobrenome FROM salas JOIN alunos_etapa02 ON alunos_etapa02.id_salas = salas.id JOIN pessoas ON pessoas.id = alunos_etapa02.id_aluno WHERE salas.id = {id_selecionado} ;'
                  
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        cons_sala.tableWidget_2.setRowCount(len(dados_lidos))
        cons_sala.tableWidget_2.setColumnCount(len(dados_lidos[0]))
        cons_sala.tableWidget_2.setHorizontalHeaderLabels(['Nome','Sobrenome'])        
        
        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_sala.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
      
    cons_sala.pushButton.clicked.connect(f_cons_sala)   
    
   
# Definir funcao de consulta de espaco para cafe
def chama_cons_cafe():
    cons_cafe.show()
    cons_cafe.comboBox.clear()
    
    # Mostrar lista de cafes
    cursor1 = banco.cursor()
    comando_SQL = "SELECT * FROM espacos ORDER BY nome;"
    cursor1.execute(comando_SQL)
    dados_lidos = cursor1.fetchall()
    numero_cafes = len(dados_lidos)
       

    for i in range(numero_cafes):
        cons_cafe.comboBox.addItem(str(dados_lidos[i][0]) + " - " + dados_lidos[i][1])

    def f_cons_cafe():

        # Selecionar espaco da lista disponivel        
        espaco_selecionado = cons_cafe.comboBox.currentText().split()
        id_selecionado = espaco_selecionado[0]
       
        #Comando banco de dados
        cursor = banco.cursor()
        comando_SQL = f'SELECT pessoas.nome, pessoas.sobrenome FROM espacos JOIN alunos_etapa01 ON alunos_etapa01.id_espacos = espacos.id JOIN pessoas ON pessoas.id = alunos_etapa01.id_aluno WHERE espacos.id = {id_selecionado} ;'
    
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()       
        
        cons_cafe.tableWidget.setRowCount(len(dados_lidos))
        cons_cafe.tableWidget.setColumnCount(len(dados_lidos[0]))
        cons_cafe.tableWidget.setHorizontalHeaderLabels(['Nome','Sobrenome'])       
        
        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_cafe.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        
        cursor = banco.cursor()
        comando_SQL = f'SELECT pessoas.nome, pessoas.sobrenome FROM espacos JOIN alunos_etapa02 ON alunos_etapa02.id_espacos = espacos.id JOIN pessoas ON pessoas.id = alunos_etapa02.id_aluno WHERE espacos.id = {id_selecionado} ;'
    
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        cons_cafe.tableWidget_2.setRowCount(len(dados_lidos))
        cons_cafe.tableWidget_2.setColumnCount(len(dados_lidos[0])) 
        cons_cafe.tableWidget_2.setHorizontalHeaderLabels(['Nome','Sobrenome'])      
        
        for i in range(0,len(dados_lidos)):
            for j in range(0,len(dados_lidos[0])):
                cons_cafe.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
      
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

    cons_cafe.pushButton.clicked.connect(f_cons_cafe)     

app = QtWidgets.QApplication([])

# Carregar janelas
inicio = uic.loadUi("views/cadastro_consulta.ui")
cad_pessoa = uic.loadUi("views/cadastro_pessoa.ui")
cad_sala = uic.loadUi("views/cadastro_sala.ui")
cad_cafe = uic.loadUi("views/cadastro_café.ui")
consultas = uic.loadUi("views/consultas.ui")
cons_pessoa = uic.loadUi("views/consulta_pessoa.ui")
cons_sala = uic.loadUi("views/consulta_sala.ui")
cons_cafe = uic.loadUi("views/consulta_café.ui") 

# Botoes de cadastro
inicio.pushButton.clicked.connect(chama_cad_pessoa)
inicio.pushButton_3.clicked.connect(chama_cad_sala)
inicio.pushButton_4.clicked.connect(chama_cad_cafe)

# Botao Distribuir
inicio.pushButton_5.clicked.connect(distribuir)

# Botao de consulta
inicio.pushButton_2.clicked.connect(chama_cons)

inicio.show()
app.exec()
