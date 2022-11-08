import numpy as np
import collections
from datetime import datetime

def num_acidentes(meses):
  acidentes = []
  
  counter = collections.Counter(meses)

  for i in counter.keys():
    acidentes.append(counter[f'{i}'])

  return acidentes

def acidentes_dia_mes(df):
  dia_mes = []

  for i in df['DATA_BOLETIM']:
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
  
def get_horario(horas):

  horario = {'MADRUGADA': 0, 'MANHA': 0, 'TARDE': 0, 'NOITE': 0}

  madru_ini = datetime.strptime('00:00', '%H:%M').time()
  madru_fim = datetime.strptime('05:59', '%H:%M').time()
  manha_ini = datetime.strptime('06:00', '%H:%M').time()
  manha_fim = datetime.strptime('11:59', '%H:%M').time()
  tarde_ini = datetime.strptime('12:00', '%H:%M').time()
  tarde_fim = datetime.strptime('17:59', '%H:%M').time()
  noite_ini = datetime.strptime('18:00', '%H:%M').time()
  noite_fim = datetime.strptime('23:59', '%H:%M').time()

  for i in horas:
    time_object = datetime.strptime(i, '%H:%M').time()
    
    if time_object > madru_ini and time_object < madru_fim :
      horario['MADRUGADA'] += 1

    if time_object > manha_ini and time_object < manha_fim :
      horario['MANHA'] += 1

    if time_object > tarde_ini and time_object < tarde_fim :
      horario['TARDE'] += 1

    if time_object > noite_ini and time_object < noite_fim :
      horario['NOITE'] += 1


  return horario  