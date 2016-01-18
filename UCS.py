from route import Graph, Vertex
from util import PriorityQueue
from copy import deepcopy
# Uniform Cost search employs PriorityQueue() imported from util.py 
def UCS(g, stop, PQ, route, rslt):
	while PQ.isEmpty()!=True:
		start=PQ.pop()
		p=start.split('->')
		if stop.get_id() in p:
			rslt.append(start)
			return 0
		a=0
		for v in g.get_vertex(p[len(p)-1]).get_connections():
			if(v.get_id() in p ):	
				continue
			else:
				a=1
				route[start+'->'+v.get_id()]=route[start]+g.get_vertex(p[len(p)-1]).get_weight(v)
				PQ.push(start+'->'+v.get_id(),route[start+'->'+v.get_id()])
		if a==1:	
			UCS(g, stop, PQ, route, rslt)
	return 0

if __name__ == '__main__':
	g = Graph()
	PQ=PriorityQueue()
	results=[]
	route={}
	f=open('input.txt', 'r')
	f.readline()
	k=f.readline()
	p=k.split(', ')
	for name in p:
		g.add_vertex(name)

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

	PQ.push('houston', 0)
	g.get_vertex('houston').visited='yes'
	route['houston']=0
	UCS(g, g.get_vertex('lafayette'), PQ, route, results)
	if PQ.isEmpty():
		mn=route[results[0]]
		for ki in results:
			if mn>route[ki]:
				mn=route[ki]
		for kil in route.keys():
			if mn==route[kil] and g.get_vertex('lafayette').get_id() in kil.split('->'):
				break
		print "The path used by Uniform cost search is %s and the distance covered is %d" %(kil, mn)


