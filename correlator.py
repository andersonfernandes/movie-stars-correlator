from stars_data import dict_add_relationship

def search(source, destination):
  source_node = {
    'description': source,
    'parent': None,
    'movie': None,
    'cost': 0
  }

  destination_node = {
    'description': destination
  }

  mapping = build_mapping()
  neighbors = []
  visited = []

  neighbors.append(source_node)

  while (len(neighbors) > 0):
    node, neighbors = pop(neighbors)
    if (node['description'] == destination_node['description']):
      route = []
      route.append(node)
      currentParent = get_node(node['parent'], visited)
      while (not currentParent == None):
        route.insert(0, currentParent)
        currentParent = get_node(currentParent['parent'], visited)

      cost = 0
      print(f'Connecting {source} with {destination}:')
      for node in route:
        if node['movie'] != None: print(f"{node['parent']} acted with {node['description']} at the movie {node['movie']}")

        cost += node['cost']
      print('Custo: ' + str(cost))
      break
    else:
      if (not was_visited(visited, node['description'])):
        visited.append(node)
        neighbors.extend(get_childs_from(mapping, node['description']))

def build_mapping():
  stars_relations = dict_add_relationship()

  mapping = {}
  for star, relations in stars_relations.items():
    for relation in relations:
      node = {
        'description': relation['name'],
        'movie': relation['movie'],
        'parent': star,
        'cost': 1
      }
      if star in mapping:
        mapping[star].append(node)
      else:
        mapping[star] = [node]

  return mapping

def get_childs_from(mapping, star):
  return mapping[star]

def pop(neighbors):
  node = neighbors[0]
  return node, neighbors[1:]

def was_visited(visited, star):
  node = filter(lambda currentChild: currentChild['description'] == star, visited)

  if list(node): return True

  return False

def get_node(star, visited):
  for node in reversed(visited):
    if (node['description'] == star):
      return node
  return None
