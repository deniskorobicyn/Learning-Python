from vertex import Vertex
v = Vertex(5, 8)
k = Vertex(5, 8)
print(v == k)
v = Vertex(10, 6)
k = Vertex(10, 8)
print(v == k)
v = Vertex(10, 8)
k = Vertex(5, 8)
print(v == k)
v = Vertex(4, 2)
k = Vertex(5, 8)
print(v == k)
v = Vertex(5, 5)
k = Vertex(5, 5)
print(v == k)
c = Vertex(4, 8)
labirinth = {c:[0,2,3,4]}
print(labirinth)