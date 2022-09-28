import numpy as np
import collections

def num_acidentes(meses):
  acidentes = []
  
  counter = collections.Counter(meses)

  for i in counter.keys():
    acidentes.append(counter[f'{i}'])

  return acidentes

def acidentes_dia_mes(df):
  dia_mes = []

  for i in df['data_boletim']:
    a = i.split('/')
    dia_mes.append(a[0] + '/' + a[1])

  counter = collections.Counter(dia_mes)
  c = collections.OrderedDict(sorted(counter.items()))

  meses = dict()

  for i in range(1,13):
    a = str(i)
    if len(a) == 1:
      a = '0' + a
    meses.update({f"{a}": dict()})
      
  for i in c.keys():
    dm = i.split('/')
    meses[f"{dm[1]}"].update({f"{i}": c[i]})

  return meses

def get_x_y(meses):

  x = []
  y = []

  for i in range(1,13):
    a = str(i)

    if len(a) == 1:
      a = '0' + a

    dia = []
    count = []

    for i in meses[a].keys():
      b = i.split('/')
      dia.append(b[0])
      count.append(meses[a][i])
    
    x.append(dia)
    y.append(count)
  
  return x, y
  