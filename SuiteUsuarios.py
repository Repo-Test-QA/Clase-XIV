import unittest
# importar los archivos de pruebas que queremos que sean parte de nuestra suite
import usuarios
import usuariosSearch
import cuentas

# Necesitamos un loader, es el lugar donde se van a cargar tales pruebas
loader = unittest.TestLoader()
# Se van a cargar en nuestra test suite
suite = unittest.TestSuite()

# Agregamos las pruebas que van a ser cargadas en nuestra suite
suite.addTest(loader.loadTestsFromModule(usuarios))
suite.addTest(loader.loadTestsFromModule(usuariosSearch))
# Podemos agregar un archivo con sus pruebas de esta manera opcional
#             archivo    clase         método
suite.addTest(cuentas.TestCuentas('test_cuenta_creada'))

# Por tanto, una ves que tengamos cargada en nuestra suite todo lo que yo le voy a mandar
# Vamos a ejecutar la suite. Si agregamos verbosity nivel 3, se muestra mas detalle.
runner = unittest.TextTestRunner(verbosity=3)
# Luego de ejecutar vamos a mostrar los resultados
result = runner.run(suite)
# Se ejecutaron los 5 casos de pruebas de los tres archivos, porque el tercero tiene 1 TC





