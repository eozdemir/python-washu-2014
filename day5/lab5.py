"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 

# Horizontal edges
ring = {}
n = 16
rows = range(1,n**2,n)
for x in rows:
  for i in range(x, x+(n-1)):
    ring = makeLink(ring, i, i+1)

# Vertical edges
for i in range(1, n**2-(n-1)):
  ring = makeLink(ring, i, i+n)
    
print ring


# TODO: define a function countEdges

def countEdges(ring):
  return sum([len(ring[node]) for node in ring.keys()])/2 

print countEdges(ring)

# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

print movies

# How many nodes in movies?
# How many edges in movies?

print len(movies.keys())
print countEdges(movies)

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [] 
tour(movies, movie_tour)

Eulerian_tour = [kb, ms, rd, dh, kb, jr, dh, ss, jr, ah, ms]
print tour(movies, Eulerian_tour)

def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

# print findPath(movies, jr, ms)

# TODO: implement findAllPaths() to find all paths between two nodes

def findAllPaths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for child in graph[start]:
        	if child not in path:
        		newpaths = findAllPaths(graph, child, end, path)
        		for new_path in newpaths:
        			paths.append(new_path)
        return paths
 
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path

print findAllPaths(movies, ms, ss)
  
# TODO: implement findShortestPath()

def findShortestPath(graph, start, end):
		all_paths = findAllPaths(graph, start, end)
		num = len(all_paths)
		tmp = []
		for i in range(num):
			tmp.append(len(all_paths[i]))
		for i in range(num):
			if len(all_paths[i]) == min(tmp):
				print all_paths[i]
		
print findShortestPath(movies, ms, ss)