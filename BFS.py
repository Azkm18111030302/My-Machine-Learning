from route import Graph, Vertex
from util import Queue
##Breadth first Search employs Queue() class imported from util.py
def BFS(start, stop, Q, path, distance ):
	if start.get_id()==stop.get_id():
		return 0;	
	vetc=[]
	currentnode=Vertex('copy object')

	for v in start.get_connections():
		if(v.visited!='yes'):
			vetc.append(v)
			v.visited='yes'
		else:
		 	continue
	if vetc==None:
		return 0

	for x in range(0,len(vetc)):
		for y in range(0,x):
			if start.get_weight(vetc[y])>start.get_weight(vetc[x]):
				vetc[y], vetc[x]=vetc[x], vetc[y] 
		
	for x in range(0, len(vetc)):
		Q.push(vetc[x])
		

	currentnode=Q.pop()
	path.append(currentnode.get_id())
	if currentnode in start.adjacent.keys():	
		distance+=start.get_weight(currentnode)
	if currentnode.get_id()==stop.get_id():
		print'The path for Breadth-First Search for the graph is %s and the distance taken is %d' %(path, distance)	
		return 0
	BFS(currentnode,stop, Q, path, distance)
	return 0

if __name__ == '__main__':
	g = Graph()
	distance=0
	Q=Queue()
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

	path.append('houston')
	g.get_vertex('houston').visited='yes'
	BFS(g.get_vertex('houston'), g.get_vertex('lafayette'), Q, path, distance)
