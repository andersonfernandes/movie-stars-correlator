from stars_data import dict_add_relationship
from functools import reduce

class Correlator:
  def __init__(self, source, destination):
    self.source = source
    self.destination = destination
    self.neighbors = [self.__source_node(source)]
    self.visited = []
    self.mapping = self.__build_mapping()

  def search(self):
    while (len(self.neighbors) > 0):
      node = self.__pop_node()

      if (node['description'] == self.destination):
        return self.__get_route_to_root(node)

      if (not self.__was_visited(node['description'])):
        self.visited.append(node)
        self.neighbors.extend(self.mapping[node['description']])

  def __get_route_to_root(self, node):
    route = [node]
    currentParent = self.__get_node(node['parent'])
    while (not currentParent is None):
      route.insert(0, currentParent)
      currentParent = self.__get_node(currentParent['parent'])

    cost = 0
    print(f'Connecting {self.source} with {self.destination}:')
    for node in route:
      if node['movie'] != None: print(f"{node['parent']} acted with {node['description']} at the movie {node['movie']}")

      cost += node['cost']
    print('cost: ' + str(cost))

    return route

  def __pop_node(self):
    node = self.neighbors[0]
    self.neighbors = self.neighbors[1:]
    return node

  def __get_node(self, description):
    for node in reversed(self.visited):
      if (node['description'] == description):
        return node

    return None

  def __was_visited(self, description):
    return any(filter(lambda currentChild: currentChild['description'] == description, self.visited))

  def __source_node(self, source):
    return {
      'description': self.source,
      'parent': None,
      'movie': None,
      'cost': 0
    }

  def __build_mapping(self):
    stars_relations = dict_add_relationship()

    return reduce(self.__build_node, stars_relations.items(), {})

  def __build_node(self, mapping, data):
    star, relations = data

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
