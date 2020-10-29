import unittest


class TestUsuariosBusqueda(unittest.TestCase):

    def test_busqueda_correcta(self):
        dato = True
        self.assertTrue(dato)

    def test_busqueda_incorrecta(self):
        dato = False
        self.assertFalse(dato)

# No vamos a agregar el main, por que quien va a ejecutar es la suite
#if __name__ == '__main__':
#    unittest.main()