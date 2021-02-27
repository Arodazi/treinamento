import mysql.connector

def gerenciar_cafes(pessoas, cafes):

    # Conectar ao banco de dados
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="treinamento"   
    )

    numero_pessoas = len(pessoas)
    numero_espacos = len(cafes)

    ocupacao_espacos = [None] * numero_espacos

    pessoas_por_espaco = int(numero_pessoas / numero_espacos)
    pessoas_sobrando = numero_pessoas % numero_espacos


    # Determinar quantas pessoas ocuparão cada espaco
    for i in range (numero_espacos):
        #Checar a lotação do espaco para ver se pode comportar o numero de pessoas
        if int(cafes[i][2]) < pessoas_por_espaco:
            print (f"O espaco {cafes[i][1]} foi preenchido ate sua capacidade total de {cafes[i][2]} e o restante de pessoas sera distribuido no outro espaco de cafe")
            ocupacao_espacos[i] = int(cafes[i][2])
            pessoas_por_espaco = int((numero_pessoas - int(ocupacao_espacos[i]) ) / (numero_espacos - 1))
            pessoas_sobrando = int((numero_pessoas - int(ocupacao_espacos[i]) ) % (numero_espacos - 1))

    
    # Determina a quantidade de pessoas levando em consideração o quociente da divisão
    for i in range (numero_espacos):
        if (ocupacao_espacos[i]) == (cafes[i][2]):
            continue
        else:
            ocupacao_espacos[i] = pessoas_por_espaco

    
    # Determina a quantidade de pessoas levando em consideração o resto da divisão
    i = 0
    while (pessoas_sobrando != 0):
        if int(ocupacao_espacos[i]) == int(cafes[i][2]):
            i += 1

        else:
            ocupacao_espacos[i] += 1
            pessoas_sobrando -= 1
            i += 1


    # Distribuir alunos na etapa 01    
    n = 0
    while n < numero_pessoas:
        for i in range(numero_espacos):
            lotacao = ocupacao_espacos[i]
            for j in range(lotacao):
                 
                cursor = banco.cursor()
                comando_SQL = f"UPDATE alunos_etapa01 SET id_espacos = {cafes[i][0]} WHERE id_aluno = {pessoas[n][0]}"
                cursor.execute(comando_SQL)
                banco.commit()
                n += 1
                

    # Distribuir alunos na etapa 02
    numero_pessoas = len(pessoas)
    pessoas_por_espaco = int(numero_pessoas / numero_espacos)
    pessoas_sobrando = numero_pessoas % numero_espacos

    pessoas_troca = int((pessoas_por_espaco+ pessoas_sobrando) / 2)
    
    n = pessoas_troca
    for i in range(n):        
        cursor = banco.cursor()
        comando_SQL = f"UPDATE alunos_etapa02 SET id_espacos = {cafes[numero_espacos - 1][0]} WHERE id_aluno = {pessoas[i][0]}"
        cursor.execute(comando_SQL)
        banco.commit()
        
    while n < numero_pessoas:
        for i in range(numero_espacos):
            lotacao = ocupacao_espacos[i]
            for j in range(lotacao):
                if n < numero_pessoas:  
                    cursor = banco.cursor()
                    comando_SQL = f"UPDATE alunos_etapa02 SET id_espacos = {cafes[i][0]} WHERE id_aluno = {pessoas[n][0]}"
                    cursor.execute(comando_SQL)
                    banco.commit()
                    n += 1 
