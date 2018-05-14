for a in 84 104 252 65
do
    for b in 166 201 35 4 
    do
        #time ./ids.sh map1.map 0 0 $a $b > ids.out
        echo "ucs"
        ./ucs.sh map1.map 0 0 $a $b 0 > ucs.out
        echo "bfs"
        ./bfs.sh map1.map 0 0 $a $b 0 > bfs.out
        echo "astar 0"
        ./astar.sh map1.map 0 0 $a $b 0 > astar0.out
        echo "astar 1"
        ./astar.sh map1.map 0 0 $a $b 1 > astar1.out
        #echo "ids and ucs"
        #diff ids.out ucs.out
        #echo "ids and bfs"
        #diff ids.out bfs.out
        #echo "ids and astar 0"
        #diff ids.out astar0.out
        #echo "ids and astar 1"
        #diff ids.out astar1.out
        echo "ucs and bfs"
        diff ucs.out bfs.out
        echo "ucs and astar 0"
        diff ucs.out astar0.out
        echo "ucs and astar 1"
        diff ucs.out astar1.out
        echo "bfs and astar 0"
        diff bfs.out astar0.out
        echo "bfs and astar 1"
        diff bfs.out astar1.out
        echo "astar 0 and astar 1"
        diff astar0.out astar1.out
    done
done

rm *.pyc
#rm *.out

