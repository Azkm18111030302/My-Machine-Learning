from route import Graph, Vertex
from util import PriorityQueue
from copy import deepcopy
# Greedy Best-First search employs PriorityQueue() imported from util.py 
def GBFS(g, stop, PQ, route, rslt):
	while PQ.isEmpty()!=True:
		start=PQ.pop()
		p=start.split('->')
		if stop.get_id() in p:
			rslt.append(start)
			return 0
		a=0
		for v in g.get_vertex(p[len(p)-1]).get_connections():
			if(v.visited=='yes'):
				continue
			elif(v.get_id() in p ):	
				continue
			else:
				v.visited='yes'
				a=1
				route[start+'->'+v.get_id()]=route[start]+g.get_vertex(p[len(p)-1]).get_weight(v)
				PQ.push(start+'->'+v.get_id(), g.get_vertex('lafayette').distance(v))
		if a==1:	
			GBFS(g, stop, PQ, route, rslt)
	return 0
def GBFS1(g, stop, PQ1, route, rslt):
	while PQ1.isEmpty()!=True:
		start=PQ1.pop()
		p=start.split('->')
		if stop.get_id() in p:
			rslt.append(start)
			return 0
		a=0
		for v in g.get_vertex(p[len(p)-1]).get_connections():
			if(v.visited=='yes'):
				continue
			elif(v.get_id() in p ):	
				continue
			else:
				v.visited='yes'
				a=1
				route[start+'->'+v.get_id()]=route[start]+g.get_vertex(p[len(p)-1]).get_weight(v)
				PQ1.push(start+'->'+v.get_id(), g.get_vertex('lafayette').distance1(v))
		if a==1:	
			GBFS1(g, stop, PQ1, route, rslt)
	return 0

if __name__ == '__main__':
	g = Graph()
	PQ=PriorityQueue()
	results=[]
	route={}
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

	PQ.push('houston', 0)
	g.get_vertex('houston').visited='yes'
	route['houston']=0
	GBFS(g, g.get_vertex('lafayette'), PQ, route, results)
	if PQ.isEmpty():
		mn=route[results[0]]
		for ki in results:
			if mn>route[ki]:
				mn=route[ki]
		for kil in route.keys():
			if mn==route[kil] and g.get_vertex('lafayette').get_id() in kil.split('->'):
				break
		print "The path used by Greedy Best-First Search(manhattan distance) is %s and the distance covered is %d" %(kil, mn)
	PQ1=PriorityQueue()
	results1=[]
	route1={}
	for v in g:
		v.visited='no'
	PQ1.push('houston', 0)
	g.get_vertex('houston').visited='yes'
	route1['houston']=0
	GBFS1(g, g.get_vertex('lafayette'), PQ1, route1, results1)
	if PQ1.isEmpty():
		mn=route1[results1[0]]
		for ki in results:
			if mn>route1[ki]:
				mn=route1[ki]
		for kil in route1.keys():
			if mn==route1[kil] and g.get_vertex('lafayette').get_id() in kil.split('->'):
				break
		print "The path used by Greedy Best-First Search(manhattan distance) is %s and the distance covered is %d" %(kil, mn)
	
