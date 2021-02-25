<h1 align="center">Métodos de Busca</h1>
<p align="left">	Esse projeto teve como objetivo implementar quatro metodos de busca em espaço de estados. Dado um mapa, o agente deve encontrar o menor caminho entre o ponto inicial e um objetivo.  </p>

Tabela de conteúdos
=================
<!--ts-->
   * [Descrição](#descricao)
   * [Tabela de Conteudo](#tabela-de-conteudo)
   * [Mapa](#mapa)
   * [Métodos](#metodos)
      * [Iterative Deepening Search](#ids)
      * [Breadth-first Search](#bfs)
      * [Uniform-Cost Search](#ucs)
      * [A*](#astar)
   * [Execução](#execucao)
   * [Referências](#tecnologias)
<!--te-->

<h1 align="" id="mapa"> Mapa </h1>
  <p align="left">
    Os mapas utilizados são bidimensionais e representados por matrizes, e pode ser visto como um tilemap. Um jogo baseado em tilemap é àquele que consiste de pequenos blocos que formam o mapa. Cada bloco pode ter propriedades diferentes. Para a aplicação, existem apenas dois tipos: O tile de terreno, em que o agente pode andar, e o de parede, que é intransponível. Os valores na matriz são "." para representar o terreno, e "@" para as paredes.
  </p>
  
  <p align="left"> 
    O agente pode movimentar nas oito direções (cima, baixo, direita, esquerda e diagonais). Os movimentos realizados possuem um custo associado, podendo ser visto como distância àquele tile. No caso do projeto, andar reto possui um custo de 1, e para andar nas diagonais o custo é de 1,5.
  </p>
  

    

<h1 align="" id="metodos"> Métodos </h1>
  <p align="left"> 
    Um problema de busca contêm alguns principais componentes: 
  </p>
  <ol>
    <li><b>Estado inicial:</b> O estado em que o agente irá começar a busca;</li>
    <li><b>Ações:</b> Conjunto de possíveis ações que o agente pode executar naquele estado. No nosso caso, são os oito movimentos para blocos de terreno;</li>
    <li><b>Função de Transição:</b> Função que retorna pares de ações e estado. Ela faz a transição para o próximo estado dado a ação do agente. Ela também é chamada de função sucessora;</li>
    <li><b>Espaço de busca:</b> Definida pelo estado inicial e função sucessora. Conjunto de todos os possíveis estados de um problema. Estado pode ser visto como as possíveis soluções para um determinado problema. Para o nosso caso, são todos as possíveis posições no mapa;</li>
    <li><b>Teste do objetivo:</b>  Função que verifica se o estado atual é o objetivo;</li>
    <li><b>Custo da solução:</b> Cada ação possui um custo para ser executada. A solução ótima é aquela que tem o menor custo somado;</li>
  </ol>


  <h2 align="" id="ids"> Iterative Deepening Search </h1>
  <h2 align="" id="bfs"> Breadth-first Search </h1>
  <h2 align="" id="ucs"> Uniform-Cost Search </h1>
  <h2 align="" id="astar"> A* </h1>

<h1 align="" id="execucao"> Execução </h1>
<h1 align="" id="tecnologias"> Referências </h1>
