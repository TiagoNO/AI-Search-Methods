<h1 align="center">Métodos de Busca</h1>
<p align="left">	Esse projeto teve como objetivo implementar quatro metodos de busca em espaço de estados. Dado um mapa, o agente deve encontrar o menor caminho entre o ponto inicial e um objetivo.  </p>

Tabela de conteúdos
=================
<!--ts-->
   * [Mapa](#mapa)
   * [Problema de busca](#problemas-de-busca)
      * [Definições](#definicoes)
      * [Propriedades](#propriedades)
      * [Tipos](#tipos)
   * [Métodos](#metodos)
      * [Iterative Deepening Search](#ids)
      * [Breadth-first Search](#bfs)
      * [Uniform-Cost Search](#ucs)
      * [A*](#astar)
   * [Execução](#execucao)
   * [Referências](#referencias)
<!--te-->

<h1 align="" id="mapa"> Mapa </h1>
  <p align="left">
    Os mapas utilizados são bidimensionais e representados por matrizes, e pode ser visto como um tilemap. Um jogo baseado em tilemap é aquele que consiste de pequenos blocos que formam o mapa. Cada bloco pode ter propriedades diferentes. Para a aplicação, existem apenas dois tipos: O tile de terreno, em que o agente pode andar, e o de parede, que é intransponível. Os valores na matriz são "." para representar o terreno, e "@" para as paredes. 
  </p>
  
  <p align="left"> 
    O agente pode movimentar nas oito direções (cima, baixo, direita, esquerda e diagonais). Os movimentos realizados possuem um custo associado, podendo ser visto como distância àquele tile. No caso do projeto, andar reto possui um custo de 1, e para andar nas diagonais o custo é de 1,5. 
  </p>

<h1 align="" id="problemas-de-busca"> Problema de busca </h1>
  <h3 align="" id="definicoes"> Definições </h3>
    <p align="left"> 
      Um problema de busca contêm alguns principais componentes: 
    </p>
    <ol>
      <li><b>Estado inicial:</b> O estado em que o agente irá começar a busca;</li>
      <li><b>Ações:</b> Conjunto de possíveis ações que o agente pode executar naquele estado. No nosso caso, são os oito movimentos para blocos de terreno;</li>
      <li><b>Função de Transição:</b> Função que retorna pares de ações e estado. Ela faz a transição para o próximo estado dado a ação do agente. Ela também é chamada de função sucessora;</li>
      <li><b>Espaço de busca:</b> Definida pelo estado inicial e função sucessora. Conjunto de todos os possíveis estados de um problema. Estado pode ser visto como as possíveis soluções para um determinado problema. Para o nosso caso, são todos as possíveis posições no mapa alcançaveis apartir do estado inicial;</li>
      <li><b>Teste do objetivo:</b>  Função que verifica se o estado atual é o objetivo;</li>
      <li><b>Custo da solução:</b> Cada ação possui um custo para ser executada. A solução ótima é aquela que tem o menor custo somado;</li>
    </ol>
  <h3 align="" id="propriedades"> Propriedades </h3>
    <p align="left"> 
      Um problema de busca contêm alguns principais componentes: 
    </p>
    <ol>
      <li><b>Completude:</b> Um algorítmo de busca é dito ser completo se é garantido que ele retornará uma solução, se existe uma, para qualquer entrada;</li>
      <li><b>Otimalidade:</b> É dito ser ótimo se a solução retornada é garantida ser a melhor (com menor custo) entre todas as outras solução;</li>
      <li><b>Complexidade de tempo:</b>  É uma medida de tempo para um algorítmo completar a busca.</li>
      <li><b>Complexidade de espaço:</b> É uma medida de espaço de armazenamento usado durante a pesquisa.</li>
    </ol>
  <h3 align="" id="tipos"> Tipos </h3>
    <p align="left"> 
      Os métodos de busca podem ser classificados entre dois tipos: Blind Search ( ou Uninformed Search) e Heuristic Search (Informed Search).
    </p>    
    <p align="left"> 
      Blind Search são métodos que não possuem informações sobre o problema. Eles trabalham apenas com o estado inicial e o objetivo. A busca realizada é por força bruta, examinando todos os nós até chegar ao objetivo. Alguns exemplos são: Breadth-first search, Uniform-cost search e Iterative deepening depth-first search.
    </p>
    <p align="left"> 
      Heuristic Search são métodos que se utilizam de alguma informação sobre o problema. Eles usam essa informação para guiar a busca, e encontrar a solução de forma mais eficiente que os métodos blind search. Uma heurística é um meio que nem sempre garante a otimalidade da solução, mas garante encontrar a solução em melhor tempo. Alguns exemplos são: Greedy Search e A* Search.
    </p>

<h1 align="" id="metodos"> Métodos </h1>
  <p align="left"> 
    Muitos dos métodos de busca se diferem em como eles lidam com a borda (lista aberta) e quais nós serão expandidos. Dessa forma, na implementação foi criado uma classe base, que modela a estrutura principal. As classes derivadas apenas fazem as sobreposições das funções necessárias.
  </p>
  <h3 align="" id="ids"> Iterative Deepening Search </h3>
    <p align="left"> 
      Iterative-Deepening Search (IDS) faz uma busca por profundidade em sequencia na árvore. O algorítmo sempre expande o nó mais profundo até um certo limite. Caso não ache o objetivo, o limite aumenta e a busca continua. A lista aberta é uma pilha. O método é completo e ótimo (caso o custo seja crescente).
    </p>
  <h3 align="" id="bfs"> Breadth-first Search </h3>
    <p align="left"> 
      O Breadth-first Search (BDS) é um método contrário ao IDS. Ele irá sempre expandir os nós de uma certa profundidade antes de procurar os mais profundos. A lista aberta é uma fila. O método é completo, e ótimo (caso a função de custo não seja decrescente em relação a profundidade).
    </p>
  <h3 align="" id="ucs"> Uniform-Cost Search </h3>
    <p align="left"> 
      Uniform-Cost Search (UCS) sempre expande o nó com menor custo. Ele se assemelha ao BFS. Sua lista aberta é um heap (fila de prioridades). O método é completo (se cada passo tem um custo maior) e ótimo.
    </p>
  <h3 align="" id="astar"> A* </h3>
    <p align="left"> 
      Esse método expande os nós considerando uma heurística e o custo real. A heurística é uma função que faz uma estimativa do custo do atual nó até o objetivo. Dessa forma, a avaliação é feita com a soma do valor da heurística e custo. Assim, o método calcula a estimativa da possível melhor solução apartir do nó atual. A lista aberta é uma fila de prioridades que se baseia no valor calculado. O algorítmo é ótimo (se a heurística usada é admissível) e completo. 
    </p>
    <p align="left"> 
      No nosso caso, foram usadas duas heurísticas para calcular a distância do estado atual e o objetivo. Essas são a distancia de Manhatam e Octile baseadas na posição (x,y) do tile.    
    </p>

<h1 align="" id="execucao"> Execução </h1>
    <p align="left"> 
  	O programa foi implementado inteiramente em python. Além disso, para a visualização gráfica dos métodos é necessário a biblioteca pygame. Para instala-lá numa máquina linux, basta utilizar o comando:
    </p>
        
        sudo apt-get install python3-pygame
      
  <p align="left"> 
    Para executar o programa, basta utilizar o comando:
    </p>

        python3 Main.py --map [directory_to_map] --method [method_name] --gui [True/False]
        
    --method pode ser entre [UCS, BFS, Astar, IDS], e determina qual método irá executar. 
    --gui determina se terá uma apresentação gráfica do processo. 
    --map, argumento necessário, que é o diretório e arquivo do mapa a ser usado.
  <p align="left"> 
    Esse projeto apresenta 4 mapas, e estão localizados na pasta maps/. Você pode criar seus próprios mapas e rodar, desde que eles sigam o template a seguir:
    </p>
    
    type [tipo]
    height [altura]
    width [comprimento]
    [nome_mapa]
    [matriz do mapa]
<h1 align="" id="referencias"> Referências </h1>
