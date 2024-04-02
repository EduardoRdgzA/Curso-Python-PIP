import csv
import matplotlib.pyplot as plt


###########################  LECTOR  ###########################
#Transformación de datos. Lista de diccionarios.
# NOTA: 
# Los iteradores están diseñados para ser recorridos secuencialmente, elemento por elemento, y una vez que un elemento ha sido consumido (leído), no puede ser accedido nuevamente sin reiniciar el iterador desde el principio
#Elemento de la lista (  print(data[131])):
#{'Rank': '10', 'CCA3': 'MEX', 'Country/Territory': 'Mexico', 'Capital': 'Mexico City', 'Continent': 'North America', '2022 Population': '127504125', '2020 Population': '125998302', '2015 Population': '120149897', '2010 Population': '112532401', '2000 Population': '97873442', '1990 Population': '81720428', '1980 Population': '67705186', '1970 Population': '50289306', 'Area (km²)': '1964375', 'Density (per km²)': '64.9082', 'Growth Rate': '1.0063', 'World Population Percentage': '1.6'}
def data_lector(ruta):
  with open(ruta,'r') as datafile:
    objeto_lector = csv.reader(datafile, delimiter = ',') #ITERADOR. Cada línea es devuelta como lista de strings ['','',...]. 
    l1_encabezado = next(objeto_lector) #LISTA. Se devuelve la primera fila. ['Rank','CCA3',...]
    data = [] # Lista vacía.  
    for fila in objeto_lector: # Para cada fila en el objeto lector(ITERADOR). 
      l1_zip = zip(l1_encabezado,fila) #Devuelve una lista de tuplas. [(enabezado,fila),(),...].
      l1_diccionario = {clave:valor for clave,valor in l1_zip} # Convierte la lista de tuplas a un diccionario.
      data.append(l1_diccionario) # Se añade cada diccionario a la lista. 
  return data


# La siguinete función tiene como objetivo selecionar solo un país con "todos" sus datos.
# Estructura: [{ : , : , ...}], lista de un solo diccionario.
# Filtro por país de la data.
def country(country,data):
  a = filter(lambda x: x['Country/Territory'] == country, data) # Filtro para seleccionar la 'country'
  return list(a) 


#Crea un diccionario con los "datos de la población" del pais seleccionado.
def population(data_country): # diccionario del país.
  country = data_country[0]
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

###########################  GRÁFICAS ###########################

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
  plt.savefig(f'./images/{country}.png')
  plt.close()

###########################  EJECUCION ###########################
#Está función solicita el país cuya gráfica se obtendrá. 
def country_plot(path):
  data = data_lector(path)
  pais = input('Escribe el País:')
  data_country = country(pais,data)
  data_population = population(data_country)
  chart(data_population,pais)
  


if __name__ == '__main__':
  country() 


