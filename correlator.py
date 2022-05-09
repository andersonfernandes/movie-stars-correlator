from stars_data import dict_add_relationship

stars_relations = dict_add_relationship()

path = 'stars.txt'
stars = open(path)
fullLines = stars.readlines()

print(fullLines)
print(stars_relations)

mapping = {}

for line in fullLines:
  parent, description = line.strip().split(',')
  node = {
      'description': description,
      'parent': parent,
      'cost': 1
  }
  if parent in mapping:
    mapping[parent].append(node)
  else:
    mapping[parent] = [node]


def getChilds(city):
  return mapping[city]

# Realizando a busca
initialState = {
  'description': 'Tom Hanks',
  'parent': None,
  'cost': 0
}

finalState = {
  'description': 'John Belushi'
}

neighbors = []
visited = []

# Fronteira trabalhando como FIFO
def getNeighbor():
  node = neighbors[0]
  return node, neighbors[1:]

def hasBeenVisited(city):
  node = filter(lambda currentChild: currentChild['description'] == city, visited)
  if list(node):
    return True
  return False

def getNode(city):
  for node in reversed(visited):
    if (node['description'] == city):
      return node
  return None

neighbors.append(initialState)

while (len(neighbors) > 0):
  node, neighbors = getNeighbor()
  if (node['description'] == finalState['description']):
    route = []
    route.append(node)
    currentParent = getNode(node['parent'])
    while (not currentParent == None):
      route.insert(0, currentParent)
      currentParent = getNode(currentParent['parent'])

    cost = 0
    for node in route:
      print(node['description'])
      cost += node['cost']
    print('Custo: ' + str(cost))
    break
  else:
    if (not hasBeenVisited(node['description'])):
      visited.append(node)
      neighbors.extend(getChilds(node['description']))

stars.close()
