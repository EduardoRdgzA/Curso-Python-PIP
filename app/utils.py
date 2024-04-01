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



if __name__ == '__main__':
  
  data = data_dict('ACTUALIZACION DE UBICACIÓN') # Lista de diccionarios.
  # data_country = country('Mexico',data) # Lista del diccionario.
  # data_population = population(data_country) # Diccionario
  # data_wp_percent_2 = world_population_percent_2(data)
  # print(data_wp_percent_2)
  # chart_pie_2(data_wp_percent_2)
  chart_pie_continent(data)



