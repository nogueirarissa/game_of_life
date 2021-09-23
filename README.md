<h1 align="center">Game of Life</h1>
<p align="center">Repositório com código para executar o jogo da vida (baseado no jogo criado por John Horton Conway)</p>

### Pré-requisitos:
Você precisará ter as bibliotecas matplotlib (pacotes pyplot e animation), seaborn, e random instaladas.

- Para instalar as bibliotecas, rode no terminal o comando: 
```
pip install matplotlib seaborn
```
### Instruções para executar:
- Com as bibliotecas devidamente instaladas, basta executar o código.

### Regras do jogo:
1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
2. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
4. Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.

### Como usar:
**1. Definição do tabuleiro:** ao rodar o código, irá ser pedido que o usuário entre com o valor do número de linhas (x) e colunas (y).

**2. Preenchimento do tabuleiro:** o usuário tem duas opções: a primeira é inserir manualmente os valores a partir das coordenadas de linhas e colunas, a segunda opção é o preenchimento aleatório.
- Observação¹: se optar pelo preechimento manual, o usuário deverá colocar o número de células vivas que deseja colocar no tabuleiro (este número não pode ser maior que o número     de casas que o tabuleiro possui, anteriormente definido). 
- Observação²: após definir quantas células vivas entraram no jogo, será pedido as coordenadas de linha (x) e coluna (y) que não podem exceder as dimensões do tabuleiro.
2.1. Caso opte pelo preenchimento aleatório, o tabuleiro se preencherá automaticamente com valores aleatórios.

**3. Escolha da visualização do resultado do jogo:** o usuário primeiramente deve definir quantas rodadas (quantas gerações) o jogo terá por meio do número de interações. Posteriormente, escolherá se irá querer ver o resultado por meio de um plot (utilizando o pyplot), e depois irá escolher se irá salvar os resultados por meio de um arquivo .gif, e se optar por salvar, deverá entrar com um nome de arquivo (não esqueça de colocar o ".gif" após o nome para salvar no formato).
