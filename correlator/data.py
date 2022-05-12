import csv
import pandas as pd
from functools import reduce
from ast import literal_eval

_movies_relations = None

def movies_mapper(mapping, movie_data):
  star = movie_data['actor']
  relations = literal_eval(movie_data['relations'])

  create_node = lambda relation: {
    'description': relation['name'],
    'movie': relation['movie'],
    'parent': star
  }

  mapping[star] = map(create_node, relations)

  return mapping

def load_movies_relations_graph():
  print('Loading movies graph ...')
  graph_df = pd.read_csv('./movies_data.csv')

  global _movies_relations
  _movies_relations = reduce(movies_mapper, graph_df.T.to_dict().values(), {})
  print('Movies graph loaded!')

def movies_relations():
  global _movies_relations
  return _movies_relations
