file = open('grid.txt', 'r')
i = 0
j = 0
k = 0
grid = []
rows = 0
cols = 0
startrow = 0
startcol = 0
endrow = 0
endcol = 0
visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


class Position:
    def __init__(self, x, y, depth, cost, value, parent):
        self.x = x
        self.depth = depth
        self.y = y
        self.cost = cost
        self.value = value
        self.parent = parent


def dfs(visited, queue, node):
    res = 0
    if node.x == endrow and node.y == endcol:
        res = 1
        print("Path found")
        temp = node
        while(temp.parent != None):
            grid[temp.x][temp.y] = '*'
            temp= temp.parent
        grid[temp.x][temp.y]='*'
        print("Cost : ", node.cost)
        print(" ")
        for i in range (rows):
            print(grid[i])
        return res
    else:
            s = node
            visited.append(s)
            if s.x - 1 >= 0:
                if (s.x-1 == endrow and s.y == endcol) and grid[s.x - 1][s.y] == '1':
                    print("The final state can't be reached there is a hurdle there")
                else:
                    if grid[s.x - 1][s.y] != '1' and res == 0:
                        one = Position(s.x - 1, s.y, s.cost + 2, grid[s.x - 1][s.y], s)
                        if one not in visited:
                         queue.insert(0,one)
            if s.y + 1 < cols :
                if (s.x  == endrow and s.y + 1 == endcol) and grid[s.x][s.y + 1] == '1':
                    print("The final state can't be reached there is a hurdle there")
                else:
                    if grid[s.x][s.y + 1] != '1' and res == 0:
                        two = Position(s.x, s.y + 1, s.cost + 2, grid[s.x][s.y + 1], s)
                        if two not in visited:
                         queue.insert(0,two)
            if (s.x - 1 >= 0 and s.y + 1 < cols):
                if (s.x - 1  == endrow and s.y + 1 == endcol) and grid[s.x - 1][s.y + 1] == '1':
                    print("The final state can't be reached there is a hurdle there")
                else:
                    if grid[s.x - 1][s.y + 1] != '1' and res == 0:
                        three = Position(s.x - 1, s.y + 1, s.cost + 3, grid[s.x - 1][s.y + 1], s)
                        if three not in visited:
                         queue.insert(0,three)
                if queue:
                    new = queue.pop(0)
                    dfs(visited, queue, new)
            else:
                queue.pop()
for each in file:
    if i == 0:
        splitted = each.split()
        rows = int(splitted[0])
        cols = int(splitted[1])
        i = i + 1
    else:
        splitted = each.split()
        if i == 1:
            startrow = int(splitted[0])
            startrow = rows - 1 - startrow
            startcol = int(splitted[1])
        if i == 2:
            endrow = int(splitted[0])
            endrow = rows - 1 - endrow
            endcol = int(splitted[1])
        if i >= 3:
            grid.append(each.split())
        i = i + 1
grid.pop()
if startrow < endrow:
    print("No path found")
else:
    if '1' != grid[startrow][startcol]:
            node = Position(startrow, startcol,0 , 0, grid[startrow][startcol], None)
            queue.append(node)
            dfs(visited, queue, node)
    else:
        print("Starting position is a hurdle I am sorry")



