## Implementing a graph structure that takes input from a text file in the following input 
##Vertices: 
## a,b,....
##Edges:
##a, b, distance
## the edges are considered to have the same weight in both directions of traversal
from util import Queue, Stack, PriorityQueue

class Vertex:
	def __init__(self, node, X, Y):
		self.id = node
		self.x=X
		self.y=Y
		self.adjacent = {}
		self.visited = 'No'
	def __str__(self):
		return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

	def add_neighbor(self, neighbor, weight = 0):
		self.adjacent[neighbor] = weight

	def get_connections(self):
		return self.adjacent.keys()
	
	def get_id(self):
		return self.id
	
	def get_weight(self, neighbor):
		return self.adjacent[neighbor]

	def ifvisited(self):
		visited='yes'
	
	def distance(self, node):
		return abs(int(node.x)-int(self.x))+abs(int(node.y)-int(self.y))

	def distance1(self, node):
		return max(abs(int(node.x)-int(self.x)), abs(int(node.y)-int(self.y)))

class Graph:
	def __init__(self):
		self.vert_dict = {}
		self.num_vertices = 0
	def __iter__(self):return iter(self.vert_dict.values())

	def add_vertex(self, node, X, Y):
		self.num_vertices = self.num_vertices + 1
		new_vertex = Vertex(node, X, Y)
		self.vert_dict[node] = new_vertex
		return new_vertex
	
	def get_vertex(self, n):
		if n in self.vert_dict:
			return self.vert_dict[n]
		else:
			return None
	def add_edge(self, frm, to, cost = 0):
		if frm not in self.vert_dict:
			self.add_vertex(frm)
		if to not in self.vert_dict:
			self.add_vertex(to)
		self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
		self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
	
	def get_vertices(self):
		return self.vert_dict.keys()

	
if __name__ == '__main__':
	g = Graph()
	f=open('input.txt', 'r')
	f.readline()
	k=f.readline()
	while (k!= 'Edges:\n'):
		p=k.split(', ')
		g.add_vertex(p[0], p[1], p[2])
		k=f.readline()
	while(k !=None):
		if(k==''):
			break
		elif(k!= 'Edges:\n'):
			p=k.split(', ')
			g.add_edge(p[0], p[1], int(p[2]))
			k=f.readline()
		else:
			k=f.readline()
			continue
	for v in g:
		for w in v.get_connections():
			vid = v.get_id()
			wid = w.get_id()
			print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

	for v in g:
		print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])
	
