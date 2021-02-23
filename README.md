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
   * [Execução](#testes)
   * [Referências](#tecnologias)
<!--te-->

#Mapa
<p align="left"> Os mapas utilizados são bidimensionais e representados por matrizes, e pode ser visto como um tilemap. Um jogo baseado em tilemap é àquele que consiste de pequenos blocos que formam o mapa. Cada um desses blocos, pode ter propriedades diferentes. Para a aplicação, existem apenas dois tipos: O tile de terreno, em que o agente pode andar, e o de parede, que é intransponível. </p>
