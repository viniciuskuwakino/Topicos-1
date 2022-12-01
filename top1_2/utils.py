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
  
def get_periodo(horas):
  array = []

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
    
    if time_object >= madru_ini and time_object <= madru_fim :
      array.append('MADRUGADA')

    if time_object >= manha_ini and time_object <= manha_fim :
      array.append('MANHA')

    if time_object >= tarde_ini and time_object <= tarde_fim :
      array.append('TARDE')

    if time_object >= noite_ini and time_object <= noite_fim :
      array.append('NOITE')

  return array

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
    
    if time_object >= madru_ini and time_object <= madru_fim :
      horario['MADRUGADA'] += 1

    if time_object >= manha_ini and time_object <= manha_fim :
      horario['MANHA'] += 1

    if time_object >= tarde_ini and time_object <= tarde_fim :
      horario['TARDE'] += 1

    if time_object >= noite_ini and time_object <= noite_fim :
      horario['NOITE'] += 1


  return horario


def get_localizacao(dado):

  localizacao = {}

  for i in dado:
    if len(localizacao) == 0:
      if len(i) == 1:
        localizacao.update({f"{i[0]}": 1})

      elif len(i) == 2:
        localizacao.update({f"{i[0]}{i[1]}": 1})
            
    else:
      if len(i) == 1:
        if f"{i[0]}" in localizacao:
          localizacao[f"{i[0]}"] += 1
        else:
          localizacao.update({ f"{i[0]}": 1 })

      if len(i) == 2:
        if f"{i[0]}{i[1]}" in localizacao:
          localizacao[f"{i[0]}{i[1]}"] += 1
        else:
          localizacao.update({ f"{i[0]}{i[1]}": 1 })
    

  return localizacao


def set_days(dias):

  days = {'DOMINGO': 0, 'SEGUNDA': 0, 'TERCA': 0, 'QUARTA': 0, 'QUINTA': 0, 'SEXTA': 0, 'SABADO': 0}

  for i in dias:
    a = i.split('/')
    a = a[::-1]
    
    match datetime(int(a[0]), int(a[1]), int(a[2])).weekday():
      case 0:
        days['SEGUNDA'] += 1

      case 1:
        days['TERCA'] += 1

      case 2:
        days['QUARTA'] += 1

      case 3:
        days['QUINTA'] += 1

      case 4:
        days['SEXTA'] += 1

      case 5:
        days['SABADO'] += 1

      case 6:
        days['DOMINGO'] += 1
        
      case _:
        pass

  array = [days['DOMINGO'], days['SEGUNDA'], days['TERCA'], days['QUARTA'], days['QUINTA'], days['SEXTA'], days['SABADO']]

  return array
  
