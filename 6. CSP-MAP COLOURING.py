class Graph():
def  init (self, vertices): self.V = vertices
self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

def isSafe(self, v, colour, c): for i in range(self.V):
if self.graph[v][i] == 1 and colour[i] == c: return False
return True

def graphColourUtil(self, m, colour, v): if v == self.V:
return True

for c in range(1, m+1):
if self.isSafe(v, colour, c): colour[v] = c
if self.graphColourUtil(m, colour, v+1): return True
colour[v] = 0 return False
def graphColouring(self, m): colour = [0] * self.V
if not self.graphColourUtil(m, colour, 0): return False
print("Solution exists and the following are the assigned colours:") for c in colour:
print(c, end=' ') return True

if  name	== ' main ': g = Graph(4)
 
g.graph = [ [0, 1, 1, 1],
[1, 0, 1, 0],
[1, 1, 0, 1],
[1, 0, 1, 0]
]
m = 3 g.graphColouring(m)
