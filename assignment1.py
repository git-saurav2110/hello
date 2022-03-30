input= [[1,2],[3,3],[2,1],[1,1],[4,1],[3,1]]
#expected output: [[4, 1], [3, 1], [3, 3], [2, 1], [1, 1], [1, 2]]
res=sorted(input,key=lambda x:(-x[0],x[1]))
print(res)