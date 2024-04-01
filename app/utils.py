import csv
import matplotlib.pyplot as plt

#Transformación de datos. Lista de diccionarios.
def data_dict(ruta):
  with open(ruta,'r') as datafile:
    objeto_lector = csv.reader(datafile, delimiter = ',') #ITERADOR. Cada línea es devuelta como lista de strings ['','',...]. 
    l1_encabezado = next(objeto_lector) #LISTA. Se devuelve la primera fila. ['Rank','CCA3',...]
    datos = [] # Lista vacía.  
    for fila in objeto_lector: # Para cada fila en el objeto lector(ITERADOR). 
      l1_zip = zip(l1_encabezado,fila) #Devuelve una lista de tuplas. [(enabezado,fila),(),...].
      l1_diccionario = {clave:valor for clave,valor in l1_zip} # Convierte la lista de tuplas a un diccionario.
      datos.append(l1_diccionario) # Se añade cada diccionario a la lista. 
  return datos
# NOTA: 
# Los iteradores están diseñados para ser recorridos secuencialmente, elemento por elemento, y una vez que un elemento ha sido consumido (leído), no puede ser accedido nuevamente sin reiniciar el iterador desde el principio

#Elemento de la lista (  print(data[131])):
#{'Rank': '10', 'CCA3': 'MEX', 'Country/Territory': 'Mexico', 'Capital': 'Mexico City', 'Continent': 'North America', '2022 Population': '127504125', '2020 Population': '125998302', '2015 Population': '120149897', '2010 Population': '112532401', '2000 Population': '97873442', '1990 Population': '81720428', '1980 Population': '67705186', '1970 Population': '50289306', 'Area (km²)': '1964375', 'Density (per km²)': '64.9082', 'Growth Rate': '1.0063', 'World Population Percentage': '1.6'}



#Filtro de la columna World Population Percentage obtenidos de data_dict
def world_population_percent_1(data):
  data_population = []
  for linea in data:
    a = linea['World Population Percentage']
    data_population.append(float(a))
  return data_population

def world_population_percent_2(data):
  data_population = []
  for diccionario in data:
    x = diccionario['Country/Territory']
    y = diccionario['World Population Percentage']
    data_population.append({x:y})
  return data_population



# Filtro por país de la data.
def country(country,data):
  a = filter(lambda x: x['Country/Territory'] == country, data) # Filtro para seleccionar la 'country'
  return list(a) 


#Crea un diccionario con los datos de la población del pais seleccionado
def population(data_country): # diccionario del país.
  country= data_country[0]
  a = {
    int('2022') : int(country['2022 Population']),
    int('2020') : int(country['2020 Population']),
    int('2015') : int(country['2015 Population']),
    int('2010') : int(country['2010 Population']),
    int('2000') : int(country['2000 Population']),
    int('1990') : int(country['1990 Population']),
    int('1980') : int(country['1980 Population']),
    int('1970') : int(country['1970 Population'])
      }
  return a



#Gráfica de barras de la población
def chart(data_population,country):
  #initialize: import matplotlib.pyplot as plt
  #preparate:
  
  X =data_population.keys()
  Y = data_population.values()
  #Render:
  fig, ax = plt.subplots()
  ax.bar(X,Y)
  ax.set_title(f'{country}')
  ax.set_xlabel('Año')
  ax.set_ylabel('Población [1e8 = 100 000 000]')
  ax.grid()
  #ax.set_yscale('log')
  plt.show()

#Gráfica de pastel 
def chart_pie_1(data_wp_percent_2):
  #initialize: import matplotlib.pyplot as plt
  #preparate: 
  X = data_wp_percent
  #Render:
  fig, ax = plt.subplots()
  ax.pie(X)
  plt.show()
  
#World Population Percentage
def chart_pie_2(data_wp_percent_2):
  #initialize: 'World Population Percentage'
  #preparate:
  X = []
  labels = []
  for diccionario in data_wp_percent_2:
    dict_values = diccionario.values() # devuelve un objeto vista.
    values = list(dict_values) # converitir el objeto vista a lista.
    X.append(float(values[0]))  # b[0] extrae el elemento de la lista.
    
    dict_keys = diccionario.keys()
    keys = list(dict_keys)
    labels.append(keys[0])
  #Render
  fig, ax= plt.subplots()
  ax.pie(X, labels=labels)
  plt.show()
  # return print(labels)

def chart_pie_continent(path):
  conti = set()
  for element in path:
    conti.add(element['Continent'])
  print('Elige un continente para gráficar:')
  for i in conti:
    print(i)
  continente = input('=>: ')
  
  dict_continent = filter(lambda x:x['Continent'] == continente,path)
  #preparate
  X = []
  labels = []
  for element in dict_continent:
    X.append(float(element['World Population Percentage']))
    labels.append(element['Country/Territory'])
  # Render
  fig, ax = plt.subplots()
  ax.pie(X,labels = labels)
  plt.show()
  


def country_plot(path):
  data = data_dict(path)
  pais = input('Escribe el Paìs:')
  data_country = country(pais,data)
  data_population = population(data_country)
  chart(data_population,pais)
  


if __name__ == '__main__':
  
  data = data_dict('./project/data.csv') # Lista de diccionarios.
  # data_country = country('Mexico',data) # Lista del diccionario.
  # data_population = population(data_country) # Diccionario
  # data_wp_percent_2 = world_population_percent_2(data)
  # print(data_wp_percent_2)
  # chart_pie_2(data_wp_percent_2)
  chart_pie_continent(data)



