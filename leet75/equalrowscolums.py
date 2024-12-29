grid = [[3,1,2,2],
        [1,4,4,4],
        [2,4,2,2],
        [2,5,2,2]]

n = len(grid)
count = 0
rows = {}

for row in range(n):
    ele=tuple(grid[row])
    rows[ele]=rows.get(ele,0)+1

for i in range(n):
    col=tuple( grid[j][i] for j in range(n))
    
    count +=rows.get(col,0)
print(count)

    