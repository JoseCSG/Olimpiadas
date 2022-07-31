#importando librerías esenciales
import pandas as pd
import matplotlib.pyplot as plt

#Variables que leen los archivos de excel con pandas
medallas=pd.read_excel('Medals.xlsx')
generos=pd.read_excel('EntriesGender.xlsx')
Atletas = pd.read_excel('Athletes.xlsx')
Entrenadores = pd.read_excel('Coaches.xlsx')

#Lista con Paises
ListaPaises = ["Algeria", "American samoa", "Andorra", "Angola", "Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh", "Barbados", "Belarus", "Belgium", 
"Belize","Benin","Bermuda","Bhutan","Bolivia", "Bosnia Darussalam","Bulgaria", "Burkina Faso","Burundi", "Cambodia","Cameroon","Canada","Cape Verde", "Cayman Islands", "Central African Republic", 
"Chad","Chile","Chinese Taipei","Colombia","Comoros", "Congo", "Cook Islands", "Costa Rica", "Côte d'lvoire", "Croatia", "Cuba", "Cyprus", "Czech Republic","Democratic Republic of the Congo", 
"Democratic Republic of Timor-Leste","Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", 
"Ethiopia","Federated States of Micronesia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Great Britain", "Greece", "Grenada", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", 
"Guyana","Haiti", "Honduras", "Hong Kong, China", "Hungary", "Iceland", "India", "Indonesia", "Iraq", "Ireland", "Islamic Republic of Iran", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazkshtan", 
"Kenya","Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya","Liechtenstein", "Lithuania", "Luxemburg", "Madagascar", 
"Malawi","Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar","Namibia", "Nauru", "Nepal", 
"Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "People's Republic of China", 
"Peru, Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Refugee Olympic Team", "Republic of Korea", "Republic of Moldova", "ROC", "Romania", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Samoa", "San Marino", 
"Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Sloveno", "Solomon Islands", "Somalia", 
"South Africa", "South Sudan", "Spain", "Sri Lanka", "St Vincent and the Grenadines", "Sudan", "Suriname", "Sweden", "Switzerland","Syrian Arab Republic", "Tajikistan", 
"Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Republic of Tanzania", 
"United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands, British", "Virgin Islands, US", "Yemen", "Zambia", "Zimbabwe"]

def medallero(medallasRegion):

  #capturando la respuesta del usuario
  medallasPaises=medallasRegion['Team/NOC']
  print("--------------------------------")
  print("Seleccione el tipo de medalla: ")
  print("1.Oro")
  print("2.Plata")
  print("3.Bronce")
  print("4.Todas")
  print("--------------------------------")
  tipo=int(input())
  try: 
    if tipo==1:
      #ploteando la grafica de medallas de oro
      medallasOro=medallasRegion['Gold']
      plt.bar(medallasPaises,medallasOro, label='Medallas', color='gold')
      plt.xticks(rotation=90)
      plt.xlabel('Países')
      plt.ylabel('Medallas')
      plt.title('Total Medallas de oro Tokio 2020')
      plt.legend()
      plt.show()

    elif tipo==2:
      #ploteando la grafica de medallas de plata
      medallasPlata=medallasRegion['Silver']
      plt.bar(medallasPaises,medallasPlata, label='Medallas',color='silver')
      plt.xticks(rotation=90)
      plt.xlabel('Países')
      plt.ylabel('Medallas')
      plt.title('Total Medallas de plata Tokio 2020')
      plt.legend()
      plt.show()

    elif tipo==3:
      #ploteando la grafica de medallas de bronce
      medallasBronce=medallasRegion['Bronze']
      plt.bar(medallasPaises,medallasBronce, label='Medallas',color='darkgoldenrod')
      plt.xticks(rotation=90)
      plt.xlabel('Países')
      plt.ylabel('Medallas')
      plt.title('Total Medallas de bronce Tokio 2020')
      plt.legend()
      plt.show()

    elif tipo==4:
      #ploteando la grafica de todas las medallas
      medallasTotal=medallasRegion['Total']
      plt.bar(medallasPaises,medallasTotal, label='Medallas')
      plt.xticks(rotation=90)
      plt.xlabel('Países')
      plt.ylabel('Medallas')
      plt.title('Total Medallas Tokio 2020')
      plt.legend()
      plt.show()

  #exception en caso de poner un valor no válido
  except ValueError:
    print("===========================")
    print("INGRESE UN NÚMERO DEL NEMÚ")  
    print("===========================")

def medalleroRegion(op):
  #agrupando los valores de la columna "region" por continentes
  if op==1:
    medallasRegion=medallas.groupby('Region').get_group('America')
  elif op==2:
    medallasRegion=medallas.groupby('Region').get_group('Europe')
  elif op==3:
    medallasRegion=medallas.groupby('Region').get_group('Asia')
  elif op==4:
    medallasRegion=medallas.groupby('Region').get_group('Africa')
  elif op==5:
    medallasRegion=medallas.groupby('Region').get_group('Oceania')

  return medallasRegion

def label(con):
  #poniendo el nombre del continente al label del plot de la funcion comparar
  if con==1:
    label="America"
  elif con==2:
    label="Europa"
  elif con==3:
    label="Asia"
  elif con==4:
    label="Africa"
  elif con==5:
    label="Oceania"
  return label

def comparar(con1,con2):
  #creando las variables necesarias para el plot
  temp1=con1
  temp2=con2
  con1=medalleroRegion(con1)
  con2=medalleroRegion(con2)
  medallasPaisesCon1=con1['Team/NOC']
  medallasPaisesCon2=con2['Team/NOC']
  temp1=label(temp1)
  temp2=label(temp2)

  try:
    #pidiendo que tipo de medalla quiere comparar
    print("--------------------------------")
    print("Seleccione el tipo de medalla: ")
    print("1.Oro")
    print("2.Plata")
    print("3.Bronce")
    print("4.Todas")
    print("--------------------------------")
    op=int(input("Ingrese una opción: "))

    if op==1:
      #obteniendo los valores de las medallas de oro de los dos continentes
      medallasCon1=con1['Gold']
      medallasCon2=con2["Gold"]
      color="gold"

    elif op==2:
      #obteniendo los valores de las medallas de plata de los dos continentes
      medallasCon1=con1['Silver']
      medallasCon2=con2["Silver"]
      color="silver"

    elif op==3: 
      #obteniendo los valores de las medallas de bronce de los dos continentes
      medallasCon1=con1['Bronze']
      medallasCon2=con2["Bronze"]
      color="darkgoldenrod"

    elif op==4:
      #obteniendo los valores de todas las medallas de los dos continentes
      medallasCon1=con1['Total']
      medallasCon2=con2["Total"]
      color="blue"

    #creando una gráfica de dos columnas y una fila, y ploteando en la primera columna
    plt.subplot(1,2,1)
    plt.bar(medallasPaisesCon1,medallasCon1,label=temp1,color=color)
    plt.xticks(rotation=90)
    plt.legend()

    #creando una gráfica de dos columnas y una fila, y ploteando en la segunda columna
    plt.subplot(1,2,2)
    plt.bar(medallasPaisesCon2,medallasCon2,label=temp2,color=color)
    plt.xticks(rotation=90)
    
    #mostrando el plot
    plt.legend()
    plt.show()

  except ValueError:
    #en caso de ingresar un caracter no valido
    print("===========================")
    print("INGRESE UN NÚMERO DEL NEMÚ")  
    print("===========================")

def categorias(cat):
  #mostrando las disciplinas por subcategoria que el usuario escogió
  temp=list(cat['Discipline'])
  for deportes in temp:
    print(deportes,end= ", ")
  print("")

def hombres_mujeres(sexo,subCat):
  #condicion que da el color de la gráfica de hombres o mujeres
  if sexo=="Female":
    color="pink"
  else:
    color="blue"

  #plot de cantidad de hombres o mujeres por disciplinas
  plt.bar(subCat['Discipline'],subCat[sexo],color=color,label=sexo)
  plt.xticks(rotation=90)
  plt.xlabel("Disciplinas")
  plt.ylabel("Número de atletas")
  plt.legend()
  plt.show()

def hombresMujeresPie(subCat):
  #plot de pastel donde se compara el total de hombres y mujeres en las disciplinas
  labels=['Hombres','Mujeres']
  numeroHombres=list(subCat['Male'])
  numeroMujeres=list(subCat['Female'])
  disciplina=list(subCat['Discipline'])

  for i in range(len(subCat['Discipline'])):
    sizes=[numeroHombres[i],numeroMujeres[i]]
    explode=(0,0)

    fig1,ax1=plt.subplots()
    ax1.pie(sizes,explode=explode,labels=labels,startangle=90,autopct='%1.1f%%')
    ax1.axis('equal')
    plt.title(disciplina[i])
    plt.show()

def DatosAtletas():
  #muestra los paises disponibles
  print("Algeria - American samoa - Andorra - Angola - Antigua and Barbuda - Argentina - Armenia - Aruba - Australia - Austria - Azerbaijan - Bahamas - Bahrain - Bangladesh - Barbados - Belarus - Belgium \n") 
  print("Belize - Benin - Bermuda - Bhutan - Bolivia - Bosnia Darussalam - Bulgaria - Burkina Faso - Burundi - Cambodia - Cameroon - Canada - Cape Verde - Cayman Islands - Central African Republic  \n")
  print("Chad - Chile - Chinese Taipei - Colombia - Comoros - Congo - Cook Islands - Costa Rica - Côte d'lvoire - Croatia - Cuba - Cyprus - Czech Republic - Democratic Republic of the Congo \n")
  print("Democratic Republic of Timor-Leste - Denmark - Djibouti - Dominica - Dominican Republic - Ecuador - Egypt - El Salvador - Equatorial Guinea - Eritrea - Estonia - Eswatini\n")
  print("Ethiopia - Federated States of Micronesia - Fiji - Finland - France - Gabon - Gambia - Georgia - Germany - Ghana - Great Britain - Greece - Grenada - Guam - Guatemala, Guinea - Guinea-Bissau\n" )
  print("Guyana - Haiti, Honduras - Hong Kong - China - Hungary, Iceland, India, Indonesia - Iraq - Ireland - Islamic Republic of Iran - Israel - Italy - Jamaica - Japan - Jordan - Kazkshtan,\n") 
  print("Kenya - Kiribati - Kosovo - Kuwait - Kyrgyzstan - Lao People's Democratic Republic - Latvia - Lebanon - Lesotho - Liberia - Libya - Liechtenstein - Lithuania - Luxemburg - Madagascar \n")
  print("Malawi - Malaysia - Maldives - Mali - Malta - Marshall Islands - Mauritania - Mauritius - Mexico - Monaco - Mongolia - Montenegro - Morocco - Mozambique - Myanmar - Namibia - Nauru - Nepal  \n")
  print("Netherlands - New Zealand - Nicaragua - Niger - Nigeria - North Macedonia - Norway - Oman - Pakistan - Palau - Palestine - Panama - Papua New Guinea - Paraguay - People's Republic of China  \n")
  print("Peru - Philippines - Poland - Portugal - Puerto Rico - Qatar - Refugee Olympic Team - Republic of Korea - Republic of Moldova - ROC - Romania - Rwanda - Saint Kitts and Nevis - Saint Lucia - Samoa - San Marino\n")
  print("Sao Tome and Principe - Saudi Arabia - Senegal - Serbia - Seychelles-- Sierra Leone - Singapore - Slovakia - Sloveno, Solomon Islands - Somalia, \n")
  print("South Africa - South Sudan, Spain, Sri Lanka - St Vincent and the Grenadines - Sudan - Suriname -  Sweden - Switzerland - Syrian Arab Republic - Tajikistan \n")
  print("Thailand - Togo - Tonga - Trinidad and Tobago - Tunisia - Turkey - Turkmenistan - Tuvalu - Uganda - Ukraine - United Arab Emirates - United Republic of Tanzania\n") 
  print("United States of America - Uruguay - Uzbekistan - Vanuatu - Venezuela - Vietnam - Virgin Islands - British - Virgin Islands, US - Yemen - Zambia - Zimbabwe \n")
  busqueda = input("Digite el país que desea buscar (Escribalo exactamente igual): \n") 
  iterador = 0 #contador para avanzar atraves de la lista de paises
  while True:
      #valida en la lista de paises si el país digitado coincide
      if ListaPaises[iterador] == busqueda:
        #busca en el archivo de excel el país digitado y filtra los demás
        display = Atletas['Name'].where(Atletas['NOC'] == busqueda)
        print(display.dropna())
        break
      else:
        if ListaPaises[iterador] != "Zimbabwe":
          iterador += 1 
        else:
          print("No seleccionó un país valido")
          break
def DatosEntrenadores():
  #muestra los paises disponibles
  print("Algeria - American samoa - Andorra - Angola - Antigua and Barbuda - Argentina - Armenia - Aruba - Australia - Austria - Azerbaijan - Bahamas - Bahrain - Bangladesh - Barbados - Belarus - Belgium \n") 
  print("Belize - Benin - Bermuda - Bhutan - Bolivia - Bosnia Darussalam - Bulgaria - Burkina Faso - Burundi - Cambodia - Cameroon - Canada - Cape Verde - Cayman Islands - Central African Republic  \n")
  print("Chad - Chile - Chinese Taipei - Colombia - Comoros - Congo - Cook Islands - Costa Rica - Côte d'lvoire - Croatia - Cuba - Cyprus - Czech Republic - Democratic Republic of the Congo \n")
  print("Democratic Republic of Timor-Leste - Denmark - Djibouti - Dominica - Dominican Republic - Ecuador - Egypt - El Salvador - Equatorial Guinea - Eritrea - Estonia - Eswatini\n")
  print("Ethiopia - Federated States of Micronesia - Fiji - Finland - France - Gabon - Gambia - Georgia - Germany - Ghana - Great Britain - Greece - Grenada - Guam - Guatemala, Guinea - Guinea-Bissau\n" )
  print("Guyana - Haiti, Honduras - Hong Kong - China - Hungary, Iceland, India, Indonesia - Iraq - Ireland - Islamic Republic of Iran - Israel - Italy - Jamaica - Japan - Jordan - Kazkshtan,\n") 
  print("Kenya - Kiribati - Kosovo - Kuwait - Kyrgyzstan - Lao People's Democratic Republic - Latvia - Lebanon - Lesotho - Liberia - Libya - Liechtenstein - Lithuania - Luxemburg - Madagascar \n")
  print("Malawi - Malaysia - Maldives - Mali - Malta - Marshall Islands - Mauritania - Mauritius - Mexico - Monaco - Mongolia - Montenegro - Morocco - Mozambique - Myanmar - Namibia - Nauru - Nepal  \n")
  print("Netherlands - New Zealand - Nicaragua - Niger - Nigeria - North Macedonia - Norway - Oman - Pakistan - Palau - Palestine - Panama - Papua New Guinea - Paraguay - People's Republic of China  \n")
  print("Peru - Philippines - Poland - Portugal - Puerto Rico - Qatar - Refugee Olympic Team - Republic of Korea - Republic of Moldova - ROC - Romania - Rwanda - Saint Kitts and Nevis - Saint Lucia - Samoa - San Marino\n")
  print("Sao Tome and Principe - Saudi Arabia - Senegal - Serbia - Seychelles-- Sierra Leone - Singapore - Slovakia - Sloveno, Solomon Islands - Somalia, \n")
  print("South Africa - South Sudan, Spain, Sri Lanka - St Vincent and the Grenadines - Sudan - Suriname -  Sweden - Switzerland - Syrian Arab Republic - Tajikistan \n")
  print("Thailand - Togo - Tonga - Trinidad and Tobago - Tunisia - Turkey - Turkmenistan - Tuvalu - Uganda - Ukraine - United Arab Emirates - United Republic of Tanzania\n") 
  print("United States of America - Uruguay - Uzbekistan - Vanuatu - Venezuela - Vietnam - Virgin Islands - British - Virgin Islands, US - Yemen - Zambia - Zimbabwe \n")
  busqueda = input("Digite el país que desea buscar (Escribalo exactamente igual): \n") 
  iterador = 0 #contador para avanzar atraves de la lista de paises
  while True:
      #valida en la lista de paises si el país digitado coincide
      if ListaPaises[iterador] == busqueda:
        #busca en el archivo de excel el país digitado y filtra los demás 
        display = Entrenadores['Name'].where(Entrenadores['NOC'] == busqueda)
        print(display.dropna())
        break
      else:
        if ListaPaises[iterador] != "Zimbabwe":
          iterador += 1 
        else:
          print("No seleccionó un país valido")
          break

def menu():
  #Display del menú principal
  print("---------------------")
  print("¿Qué desea revisar?")
  print("1.Medallas")
  print("2.Atletas")
  print("3.Categorias")
  print("4.Datos generales")
  print("5.Salir")
  print("---------------------")
  
def main():
  print("Bienvenido al resumen de las olimpiadas Tokio 2020")
  while True:
    #llamando al menú
    menu() 
    try:
      #tomando input del usuario
      resp = int(input("Digite una opción: ")) 
      if resp == 1:
        while True:
          #submenu de la primera opción - Medallas
          print("---------------------------------------")
          print("Seleccione el continente a mostrar: ")
          print("1. America")
          print("2. Europa")
          print("3. Asia")
          print("4. Africa")
          print("5. Oceania")
          print("6.Todos los paises")
          print("7.Comparar entre dos continentes")
          print("8.Volver al menu principal")
          print("---------------------------------------")

          try:
            #capturando el input del usuario y llamando a funciones acorde a la respuesta
            resp = int(input("Digite una opción: "))
            if resp == 1:
              #se obtiene las medallas por region y se manda a la funcion medallero
              medallasRegion=medalleroRegion(resp)
              medallero(medallasRegion)

            elif resp == 2:
              #se obtiene las medallas por region y se manda a la funcion medallero
              medallasRegion=medalleroRegion(resp) 
              medallero(medallasRegion)

            elif resp == 3:
              #se obtiene las medallas por region y se manda a la funcion medallero
              medallasRegion=medalleroRegion(resp) 
              medallero(medallasRegion)

            elif resp == 4:
              #se obtiene las medallas por region y se manda a la funcion medallero
              medallasRegion=medalleroRegion(resp) 
              medallero(medallasRegion)

            elif resp == 5:
              #se obtiene las medallas por region y se manda a la funcion medallero
              medallasRegion=medalleroRegion(resp) 
              medallero(medallasRegion)

            elif resp==6:
              #plot de todas las medallas de todos los paises
              medallasPaises=medallas['Team/NOC']
              medallasTotales=medallas['Total']
              plt.bar(medallasPaises,medallasTotales, label="Medallas")
              plt.xticks(rotation=90)
              plt.xlabel('Países')
              plt.ylabel('Medallas')
              plt.title('Total Medallas Tokio 2020')
              plt.legend()
              plt.show()

            elif resp==7:
              #se escojen dos continentes a comparar y se envian a la funcion comparar
              print("---------------------------")
              print("1. America")
              print("2. Europa")
              print("3. Asia")
              print("4. Africa")
              print("5. Oceania")
              print("---------------------------")

              continente1=int(input("Escoge un continente: "))
              continente2=int(input("Escoge otro continente: "))
              comparar(continente1,continente2)

            elif resp==8:
              #termina el ciclo y regresa al menú superior
              break
            #excepción en caso de introducir un caracter erróneo
            else:
              print("===========================")
              print("INGRESE UN NÚMERO DEL NEMÚ")
              print("===========================")
          #excepción en caso de introducir un caracter erróneo
          except ValueError:
            print("===========================")
            print("INGRESE UN NÚMERO DEL NEMÚ")
            print("===========================")

    #submenú de la segunda opción  
      elif resp == 2:
        while True:
          print("------------------------------------------------------")
          print("1.Hombres")
          print("2.Mujeres")
          print("3.Comparación de hombres y mujeres en subcategorias")
          print("4.volver al menu principal")
          print("------------------------------------------------------")
          resp=int(input(""))
        
          if resp==1:
            print("---------------------------")
            print("Hay tres subcategorias")
            print("1.Cerrado")
            print("2.Abierto")
            print("3.Aguas")
            print("---------------------------")
            resp=int(input("Escoja alguna: "))

            if resp==1:
              #se obtienen las disciplinas en la subcategoria cerrado y se envian a la funcion hombres_muejeres
              subCat=generos.groupby('Tipo').get_group('Cerrado')
              genero='Male'
              hombres_mujeres(genero,subCat)

            elif resp==2:
              #se obtienen las disciplinas en la subcategoria abierto y se envian a la funcion hombres_muejeres
              subCat=generos.groupby('Tipo').get_group('Abierto')
              genero='Male'
              hombres_mujeres(genero,subCat)

            elif resp==3:
              #se obtienen las disciplinas en la subcategoria aguas y se envian a la funcion hombres_muejeres
              subCat=generos.groupby('Tipo').get_group('Agua')
              genero='Male'
              hombres_mujeres(genero,subCat)

          elif resp==2:
            print("---------------------------")
            print("Hay tres subcategorias")
            print("1.Cerrado")
            print("2.Abierto")
            print("3.Aguas")
            resp=int(input("Escoja alguna: "))
            print("---------------------------")

            if resp==1:
              #se obtienen las disciplinas en la subcategoria cerrado y se envian a la funcion hombres_muejeres
              subCat=generos.groupby('Tipo').get_group('Cerrado')
              genero='Female'
              hombres_mujeres(genero,subCat)

            elif resp==2:
              #se obtienen las disciplinas en la subcategoria abierto y se envian a la funcion hombres_muejeres
              subCat=generos.groupby('Tipo').get_group('Abierto')
              genero='Female'
              hombres_mujeres(genero,subCat)

            elif resp==3:
              #se obtienen las disciplinas en la subcategoria aguas y se envian a la funcion hombres_muejeres
              subCat=generos.groupby('Tipo').get_group('Agua')
              genero='Female'
              hombres_mujeres(genero,subCat)
        
          elif resp==3:
            print("---------------------------")
            print("Hay tres subcategorias")
            print("1.Cerrado")
            print("2.Abierto")
            print("3.Aguas")
            resp=int(input("Escoja alguna: "))
            print("---------------------------")

            if resp==1:
              #se obtienen las disciplinas en la subcategoria cerrado y se envian a la funcion hombresMujeresPie
              subCat=generos.groupby('Tipo').get_group('Cerrado')
              hombresMujeresPie(subCat)

            elif resp==2:
              #se obtienen las disciplinas en la subcategoria abierto y se envian a la funcion hombresMujeresPie
              subCat=generos.groupby('Tipo').get_group('Abierto')
              hombresMujeresPie(subCat)

            elif resp==3:
              #se obtienen las disciplinas en la subcategoria aguas y se envian a la funcion hombresMujeresPie
              subCat=generos.groupby('Tipo').get_group('Agua')
              hombresMujeresPie(subCat)

          elif resp==4:
            break
            
    #submenú de la tercera opción
      elif resp==3:
        while True:
          print("---------------------------")
          print("Hay tres subcategorias")
          print("1.Cerrado")
          print("2.Abierto")
          print("3.Aguas")
          print("4.Salir")
          print("---------------------------")
          resp=int(input("Escoja alguna: "))


          if resp==1:
            #se obtienen las disciplinas en la subcategoria cerrado y se envian a la funcion categorias
            subCat=generos.groupby('Tipo').get_group('Cerrado')
            print("Los deportes cerrados son: ")
            categorias(subCat)

          elif resp==2:
            #se obtienen las disciplinas en la subcategoria abierto y se envian a la funcion categorias
            subCat=generos.groupby('Tipo').get_group('Abierto')
            print("Los deportes abiertos son: ")
            categorias(subCat)

          elif resp==3:
            #se obtienen las disciplinas en la subcategoria aguas y se envian a la funcion categorias
            subCat=generos.groupby('Tipo').get_group('Agua')
            print("Los deportes de agua son: ")
            categorias(subCat)

          elif resp==4:
            #regresa al menu anterior
            break

      elif resp == 4:
        while True:
          print("---------------------------")
          print("1.Atletas")
          print("2.Entrenadores")
          print("3.Volver al menu principal")
          resp = int(input("Escoja alguna: "))
          print("---------------------------")

          if resp==1:
            DatosAtletas()

          elif resp==2:
            DatosEntrenadores()

          elif resp==3:
            break

      elif resp == 5:
        #termina el programa
        print("----------------------------------")
        print("Gracias por usar nuestro programa")
        print("¡Nos vemos pronto! :D")
        print("----------------------------------")
        break 

      else:
        print("===========================")
        print("INGRESE UN NÚMERO DEL NEMÚ")
        print("===========================")

    except ValueError:
       #en caso de ingresar un caracter no valido
       print("===========================")
       print("INGRESE UN NÚMERO DEL NEMÚ")  
       print("===========================")
main()