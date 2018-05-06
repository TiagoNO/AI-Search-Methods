

echo "Testing IDS:"
time ./ids.sh map1.map 190 249 175 249
time ./ids.sh map1.map 201 207 84 166
#time ./ids.sh map1.map 235 12 0 154

#echo "Testing UCS:"
#time ./ucs.sh map1.map 190 249 175 249
#time ./ucs.sh map1.map 201 207 84 166
#time ./ucs.sh map1.map 235 12 0 154

#echo "Testing BFS:"
#time ./bfs.sh map1.map 190 249 175 249
#time ./bfs.sh map1.map 201 207 84 166
#time ./bfs.sh map1.map 235 12 0 154

#echo "Testing A*:"
#time ./astar.sh map1.map 190 249 175 249 0 
#time ./astar.sh map1.map 201 207 84 166 0 
#time ./astar.sh map1.map 235 12 0 154 0 
#time ./astar.sh map1.map 190 249 175 249 1 
#time ./astar.sh map1.map 201 207 84 166 1 
#time ./astar.sh map1.map 235 12 0 154 1
