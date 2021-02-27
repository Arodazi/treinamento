import mysql.connector

def gerenciar_salas(pessoas, salas):

    # Conectar ao banco de dados
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="treinamento"   
    )

    numero_pessoas = len(pessoas)
    numero_salas = len(salas)

    ocupacao_salas = [None] * numero_salas
    
    pessoas_por_sala = int(numero_pessoas / numero_salas)
    pessoas_sobrando = numero_pessoas % numero_salas

    # Cadastrar id_aluno na etapa01
    for i in range(numero_pessoas):
        id_aluno = pessoas[i][0]
        cursor = banco.cursor()
        comando_SQL = f"SELECT * FROM alunos_etapa01 WHERE id_aluno = {id_aluno};"
        
        cursor.execute(comando_SQL)        
        dados_lidos = (cursor.fetchall())
        
        rows = cursor.rowcount
                
        if rows == 0:
            comando_SQL = f"INSERT INTO alunos_etapa01 (id_aluno) VALUES({id_aluno});"
            cursor.execute(comando_SQL)
            banco.commit()
        else: 
            continue

    # Cadastrar id_aluno na etapa02
    for i in range(numero_pessoas):
        id_aluno = pessoas[i][0]
        cursor = banco.cursor()
        comando_SQL = f"SELECT * FROM alunos_etapa02 WHERE id_aluno = {id_aluno};"
        
        cursor.execute(comando_SQL)        
        dados_lidos = (cursor.fetchall())        
        rows = cursor.rowcount
                
        if rows == 0:
            comando_SQL = f"INSERT INTO alunos_etapa02 (id_aluno) VALUES({id_aluno});"
            cursor.execute(comando_SQL)
            banco.commit()
        else: 
            continue      
     

    # Determinar quantas pessoas ocuparão cada sala
    for i in range (numero_salas):
        #Checar a lotação da sala para ver se pode comportar o numero de pessoas
        if int(salas[i][2]) < pessoas_por_sala:
            print (f"A sala {salas[i][1]} foi preenchida ate sua capacidade total de {salas[i][1]} e o restante de pessoas sera distribuido nas demais salas")
            #salas[i][3] = int(salas[i][2])
            ocupacao_salas[i] = int(salas[i][2])
            pessoas_por_sala = int((numero_pessoas - int(ocupacao_salas[i]) ) / (numero_salas - 1))
            pessoas_sobrando = int((numero_pessoas - int(ocupacao_salas[i]) ) % (numero_salas - 1))

    # Determina a quantidade de pessoas levando em consideração o quociente da divisão
    for i in range (numero_salas):
        if ocupacao_salas[i] == int(salas[i][2]):
            continue
        else:
            ocupacao_salas[i] = pessoas_por_sala

    # Determina a quantidade de pessoas levando em consideração o resto da divisão
    i = 0
    while (pessoas_sobrando != 0):
        if int(ocupacao_salas[i]) == int(salas[i][2]):
            i += 1

        else:
            ocupacao_salas[i] += 1
            pessoas_sobrando -= 1
            i += 1

    # Distribuir alunos na etapa 01
    n = 0
    while n < numero_pessoas:
        for i in range(numero_salas):
            lotacao = ocupacao_salas[i]
            for j in range(lotacao):
               
                cursor = banco.cursor()
                comando_SQL = f"UPDATE alunos_etapa01 SET id_salas = {salas[i][0]} WHERE id_aluno = {pessoas[n][0]}"
                cursor.execute(comando_SQL)
                banco.commit()
                n += 1

             
    # Distribuir alunos na etapa 02
    numero_pessoas = len(pessoas)
    pessoas_por_sala = int(numero_pessoas / numero_salas)
    pessoas_sobrando = numero_pessoas % numero_salas

    pessoas_troca = int((pessoas_por_sala + pessoas_sobrando) / 2)
    
    n = pessoas_troca
    for i in range(n):        
        cursor = banco.cursor()
        comando_SQL = f"UPDATE alunos_etapa02 SET id_salas = {salas[numero_salas - 1][0]} WHERE id_aluno = {pessoas[i][0]}"
        cursor.execute(comando_SQL)
        banco.commit()

    while n < numero_pessoas:
        for i in range(numero_salas):
            lotacao = ocupacao_salas[i]
            for j in range(lotacao):
                if n < numero_pessoas:                    
                    cursor = banco.cursor()
                    comando_SQL = f"UPDATE alunos_etapa02 SET id_salas = {salas[i][0]} WHERE id_aluno = {pessoas[n][0]}"
                    cursor.execute(comando_SQL)
                    banco.commit()
                    n += 1 