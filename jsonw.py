# Importamos la librería json
import json

with open("client.json") as client:
    # Lo que se muestre identado es lo que voy a realizar con el archivo
    # Vamos a leer el archivo y lo pasamos a un diccionario
    client_dict = json.loads(client.read())     # Va a leer el archivo de cliente
                                                # lo va a cargar como un json y lo
                                                # va a pasar al diccionario.
# Verificamos que trae el diccionario (todo)
# Trae toda la información del json
print(client_dict)
# Como es un diccionario, quiero traer el valor del atributo name, muestra Peter
print(client_dict['name'])
# Quiero traer lainfromación del elemento interest, en este caso tiene
# una colección, una lista con 3 elementos
print(client_dict['interest'])
# De tal lista quiero que me traiga el 3er elemento, recordemos que agregamos el índice
print(client_dict['interest'][2])
# Dentro del diccionario client_dict, existe el diccionario last_articles, quiero
# que me traiga tal diccionario
print(client_dict['last articles'])
# Ahora quiero traerme el valor del atributo clothes, el cual esta en el diccionario
# last articles, el cual esta dentro del diccionario cliente_dict
print(client_dict['last articles']['clothes'])

# También, podemos trabajar de esta manera, cargamos el archivo como json y lo pasamos al dict
#with open("client.json") as client:
#   client_dict = json.load(client)


# Ahora yo quiero escribir un json, porque hay datos que voy a necesitar mas adelante
# Necesito variables con ciertos datos, los deseo guardar, porque van a servir para
# otras pruebas, creamos el diccionario person_dict
person_dict = {"name": "Clark",
               "last name": "Kent",
               "nickname": "Superman",
               "Languages": ["Kriptonian", "English"]
               }
# Vamos a escribir un nuevo archivo customer.json y la informacion que tengo en mi diccionario
# person.dict se la voy a pasar.
with open('customer.json', 'w') as customer:
    # Le mandamos lo que tenemos en nuestro diccionario, le pasamos
    #         diccionario  archivo
    json.dump(person_dict, customer)
#Ejecutamos, se va a crear el archivo customer.json y se va a mostrar la información
#que tiene el diccionario


# Ahora ya podemos leer el nuevo archivo con su información
with open('customer.json') as customer:
    customer_dict = json.load(customer)

# Verificamos
print(customer_dict)

