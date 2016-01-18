from route import Graph, Vertex
from util import Stack
#Depth first search employs Stack() class imported from util.py
def DFS( start, stop, stk, path, distance):
	if start.get_id()==stop.get_id():
		return 0;	
	vetc=[]
	currentnode=Vertex('copy object')

	for v in start.get_connections():
		if(v.visited!='yes'):
			vetc.append(v)
		else:
		 	continue
	if vetc==None:
		return 0

	for x in range(0,len(vetc)):
		for y in range(0,x):
			if start.get_weight(vetc[y])>start.get_weight(vetc[x]):
				vetc[y], vetc[x]=vetc[x], vetc[y] 
	
	for x in range(0, len(vetc)):
		if vetc[x].visited!='yes':
			stk.push(vetc[x])
			vetc[x].visited='yes'
			path.append(vetc[x].get_id())
			distance+=start.get_weight(vetc[x])
			if vetc[x].get_id()==stop.get_id():
				print'The path for Depth-First Search for the graph is %s and the distance taken is %d' %(path, distance)	
				return 0		
			DFS(vetc[x], stop, stk, path, distance)
		if stk.isEmpty()!=True:
			stk.pop()
	return 0

if __name__ == '__main__':
	g = Graph()
	distance=0
	stack= Stack()
	path=[]
	f=open('input.txt', 'r')
	f.readline()
	k=f.readline()
	p=k.split(', ')
	for name in p:
		g.add_vertex(name)
		print name
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
	stack.push(g.get_vertex('houston'))
	g.get_vertex('houston').visited='yes'
	path.append('houston')
	DFS(g.get_vertex('houston'), g.get_vertex('lafayette'), stack, path, distance)
	

