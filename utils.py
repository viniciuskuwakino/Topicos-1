import numpy as np
import collections

def num_acidentes(meses):
  acidentes = []
  
  counter = collections.Counter(meses)

  for i in counter.keys():
    acidentes.append(counter[f'{i}'])

  return acidentes
