from stars_data import dict_add_relationship
from queue import Queue
from functools import reduce

class Correlator:
  def __init__(self, source, destination):
    self.source = source
    self.destination = destination
    self.neighbors = Queue()
    self.visited = []
    self.mapping = self.__build_mapping()

  def search(self):
    self.neighbors.put(self.__source_node())

    while (not self.neighbors.empty()):
      node = self.neighbors.get()

      if (node['description'] == self.destination):
        return self.__get_route_to_root(node)

      if (not self.__was_visited(node['description'])):
        self.visited.append(node)
        list(map(self.neighbors.put, self.mapping[node['description']]))

  def __get_route_to_root(self, node):
    route = [node]
    currentParent = self.__get_node(node['parent'])
    while (not currentParent is None):
      route.insert(0, currentParent)
      currentParent = self.__get_node(currentParent['parent'])

    cost = 0
    print(f'Connecting {self.source} with {self.destination}:')
    for node in route:
      if node['movie'] is None: continue

      print(f"{node['parent']} acted with {node['description']} at the movie {node['movie']}")

      cost += 1
    print('cost: ' + str(cost))

    return route

  def __get_node(self, description):
    for node in reversed(self.visited):
      if (node['description'] == description):
        return node

    return None

  def __was_visited(self, description):
    return any(filter(lambda currentChild: currentChild['description'] == description, self.visited))

  def __source_node(self):
    return {
      'description': self.source,
      'parent': None,
      'movie': None
    }

  def __build_mapping(self):
    stars_relations = dict_add_relationship()
    return reduce(self.__build_relations, stars_relations.items(), {})

  def __build_relations(self, mapping, data):
    star, relations = data
    create_node = lambda relation: {
      'description': relation['name'],
      'movie': relation['movie'],
      'parent': star
    }

    for relation in relations:
      node = create_node(relation)

      if star in mapping:
        mapping[star].append(node)
      else:
        mapping[star] = [node]

    return mapping
