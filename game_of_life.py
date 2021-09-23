### Game of Life  ###
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import random

#Vivo == True
#Morto == False

 ########### EXEMPLO DA MATRIZ ############
## canto(0,0) | bordas(0,x) | canto(0,m)  ##
## bordas(x,0)| meios(x,x)  | bordas(x,m) ##
## canto(m,0) | bordas(m,x) | canto(m,m)  ##
 ########################################## 

 ##################################
### Classe definindo o tabuleiro ###
 ##################################

class Board:
    def __init__(self,board):
        self.board = board
        self.tamanho = [len(board),len(board[0])]
        self.aux_board = [[False for x in range(self.tamanho[0])] for y in range(self.tamanho[1])]

    def ler_vizinhos(self,vec_lei,row_index,colum_index):
        mortos = 0
        vivos = 0
        for i in vec_lei: #verifica os vizinhos
            if(self.board[i[0]][i[1]]):
                vivos += 1  #conta os vizinhos vivos
            else:
                mortos += 1 #conta os vizinhos mortos

         ##########################
        ### Aplicacao das Regras ###
         ##########################

        if(self.board[row_index][colum_index] and vivos < 2):
            self.aux_board[row_index][colum_index] = False #morreu regra 1 
        elif(self.board[row_index][colum_index] and vivos > 3):
            self.aux_board[row_index][colum_index] = False #morreu regra 2
        elif(self.board[row_index][colum_index] == False and vivos == 3):
            self.aux_board[row_index][colum_index] = True #ressucitou regra 3
        elif(self.board[row_index][colum_index] and (2 <= vivos < 4)):
            self.aux_board[row_index][colum_index] = True #sobreviveu regra 4
        else:
            self.aux_board[row_index][colum_index] = False #morreu
        
         ##############################################
        ### Verificar qual posicao o individuo estah ###
         ##############################################

    def descobrir_estado(self,r_id,c_id):
        if(r_id > 0 and r_id < (self.tamanho[0] - 1) and c_id > 0 and c_id < (self.tamanho[1] - 1)):
            #individuo no meio
            vetor_de_leitura = [[r_id-1,c_id-1],[r_id-1,c_id],[r_id-1,c_id+1],[r_id,c_id-1],[r_id,c_id+1],[r_id+1,c_id-1],[r_id+1,c_id],[r_id+1,c_id+1]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(r_id + c_id == 0):
            #canto (0,0)
            vetor_de_leitura = [[r_id,c_id+1],[r_id+1,c_id],[r_id+1,c_id+1]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(r_id + c_id == self.tamanho[1] - 1 and (r_id == 0)):
            #canto (0,max)
            vetor_de_leitura = [[r_id,c_id-1],[r_id+1,c_id-1],[r_id+1,c_id]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(r_id + c_id == self.tamanho[0] - 1 and (c_id == 0)):
            #canto (max,0)
            vetor_de_leitura = [[r_id-1,c_id],[r_id-1,c_id+1],[r_id,c_id+1]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(r_id + c_id == self.tamanho[0] + self.tamanho[1] -2):
            #canto (max,max)
            vetor_de_leitura = [[r_id,c_id-1],[r_id-1,c_id-1],[r_id-1,c_id]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(r_id == 0):
            #borda (0,x)
            vetor_de_leitura = [[r_id,c_id-1],[r_id+1,c_id-1],[r_id+1,c_id],[r_id+1,c_id+1],[r_id,c_id+1]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(r_id == self.tamanho[0] - 1):
            #borda (max,x) 
            vetor_de_leitura = [[r_id,c_id-1],[r_id-1,c_id-1],[r_id-1,c_id],[r_id-1,c_id+1],[r_id,c_id+1]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(c_id == 0):
            #borda (x,0)
            vetor_de_leitura = [[r_id-1,c_id],[r_id-1,c_id+1],[r_id,c_id+1],[r_id+1,c_id+1],[r_id+1,c_id]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        elif(c_id == self.tamanho[1] - 1):
            #borda (x,max)
            vetor_de_leitura = [[r_id-1,c_id],[r_id-1,c_id-1],[r_id,c_id-1],[r_id+1,c_id-1],[r_id+1,c_id]]
            self.ler_vizinhos(vetor_de_leitura,r_id,c_id)
        else:
            print('error')

    def ver_posicao(self):

         ##############################
        ### Atualizacao de tabuleiro ###
         ##############################

        for row_index in range(self.tamanho[0]):
            for colum_index in range(self.tamanho[1]):
                #executa as funcoes de celula em celula
                self.descobrir_estado(row_index,colum_index)
        self.board = self.aux_board #atualiza a board
        self.aux_board = [[False for x in range(self.tamanho[0])] for y in range(self.tamanho[1])] #zera a board auxiliar
        return self.board

 ######################## 
### Execucao do Codigo ###
 ######################## 

if(True):

     ################################ 
    ### Inicializacao do tabuleiro ###
     ################################
    
    print(' ################################## \n#### Inicializacao do tabuleiro ####\n ################################## ')
    print('tamanho do tabuleiro (x,y)')
    tamanho = [0,0]
    texto = ['x: ','y: ']
    #entrada do tamanho do tabuleiro e controle da entrada do usuario
    for i in range(2):
        while(True):
            tamanho[i] = int(input(texto[i]))
            if(isinstance(tamanho[i],int) == False or tamanho[i] < 1):
                print('\nErro: Apenas numeros inteiros e positivos!\n')
            else:
                break
    board = [[False for x in range(tamanho[0])] for y in range(tamanho[1])]
     
     ################################
    ### Preenchimento do tabuleiro ###
     ################################

    print(' ################################## \n#### Preenchimento do tabuleiro ####\n ################################## ')
    #entrada do tipo de preenchimento e controle da entrada do usuario
    while(True):
        print('a) Inserir manualmente\nb) Preenchimento aleatorio')
        resposta = input('resposta:')
        if(resposta != 'a' and resposta != 'b'):
            print('\nErro: Escolha uma alternativa valida!\n')
        else:
            break
    if(resposta == 'a'):
        #preencher tabuleiro manualmente
        while(True):
            print('Quantas entradas? (max',tamanho[0]*tamanho[1], 'entradas)')
            entradas = int(input('numero de entradas: '))
            if(entradas > tamanho[0]*tamanho[1]):
                print('\nErro: Numero de entradas maior que o possivel!\n')
            elif(isinstance(entradas,int) == False or entradas < 1):
                print('\nErro: Apenas numeros inteiros e positivos!\n')
            else:
                break
        for i in range(entradas):
            coord = [0,0]
            print('coordenada da ',i+1,'\ba entrada')
            for i in range(2):
                while(True):
                    coord[i] = int(input(texto[i]))
                    if(isinstance(tamanho[i],int) == False or tamanho[i] < 1 or (i == 0 and coord[i] > tamanho[i]) or (i == 1 and coord[i] > tamanho[i])):
                        print('\nErro: Apenas numeros inteiros e positivos!\n')
                    else:
                        break
            board[coord[0]][coord[1]] = True
    else:
        #preenchimento do tabuleiro aleatoriamente
        for i in range(tamanho[0]):
            for j in range(tamanho[1]):
                if(random.random() > 0.5):
                    board[i][j] = True

     ##################
    ### Visualizacao ###
     ##################

    print(' #################### \n#### Visualizacao ####\n #################### ')
    interation_n = int(input('numero de interacoes: '))
    #visualizar em plot
    while(True):
        show = input('visualizar resuldado? (s,n): ')
        if(show == 's'):
            show = True
            break
        elif(show == 'n'):
            show = False
            break
        else:
            print('\nErro: Escolha uma alternativa valida!\n')
    while(True):
        #salvar o resultado em um gif
        save = input('salvar .gif? (s,n): ')
        if(save == 's'):
            save = True
            nome_arquivo = input('nome do arquivo: ')
            break
        elif(save == 'n'):
            save = False
            break
        else:
            print('\nErro: Escolha uma alternativa valida!\n')
    
    board_use = Board(board) #instancia a board
    mesa = [] #mesa vai receber todas as boards

    #criando a figura
    fig = plt.figure()
    fig.set_size_inches(5, 5, forward=True)
   
    sns.heatmap(board, cbar=False) #representando a board em um grafico de "heatmap"
    for i in range(interation_n):
        mesa.append(board_use.ver_posicao())

    #funcoes para criacao da animacao
    def init():
        sns.heatmap([[False for x in range(board_use.tamanho[0])] for y in range(board_use.tamanho[1])], vmax=.8, cbar=False)

    def animate(i):
        data = mesa[i]
        sns.heatmap(data, cbar=False)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=interation_n, interval=100, repeat=False)

    if(save):
        anim.save(nome_arquivo,writer='imagemagick') #salva resultado em .gif
    if(show):
        plt.show() #mostra o resultado em plot
