from route import Graph, Vertex
from util import PriorityQueue
from copy import deepcopy
# A* search employs PriorityQueue() imported from util.py 
def AS(g, stop, PQ, route, rslt, b):
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
				route[start+'->'+v.get_id()]=route[start] + g.get_vertex(p[len(p)-1]).get_weight(v)
				if b==1:
					PQ.push(start+'->'+v.get_id(), g.get_vertex('houston').distance(v)+g.get_vertex('lafayette').distance(v))
				else:
					PQ.push(start+'->'+v.get_id(), g.get_vertex('houston').distance1(v)+g.get_vertex('lafayette').distance1(v))
		if a==1:	 
			AS(g, stop, PQ, route, rslt, b)
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
	vi=g.get_vertex('houston')
	g.get_vertex('houston').visited='yes'
	route['houston']=0
	for i in range(1,3):
		if i==1:
			st='manhattan'
			PQ.push('houston', g.get_vertex('houston').distance(vi)+g.get_vertex('lafayette').distance(vi))
		else:
			st='biolab'
			PQ.push('houston', g.get_vertex('houston').distance1(vi)+g.get_vertex('lafayette').distance1(vi))
		AS(g, g.get_vertex('lafayette'), PQ, route, results, i)
		if PQ.isEmpty():
			mn=route[results[0]]
			for ki in results:
				if mn>route[ki]:
					mn=route[ki]
			for kil in route.keys():
				if mn==route[kil] and g.get_vertex('lafayette').get_id() in kil.split('->'):
					break
			print "The path used by A* search is %s and the distance covered is %d" %(kil, mn)
			print "The distance measure used is %s" %st

