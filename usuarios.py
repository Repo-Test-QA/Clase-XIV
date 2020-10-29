import unittest


class TestUsuarios(unittest.TestCase):

    def test_usuario_creado(self):
        usuario = 'Carlos'
        self.assertEqual(usuario, 'Carlos')

    def test_usuario_no_creado(self):
        respuesta = 'El usuario no ha sido creado'
        self.assertEqual(respuesta, 'El usuario no ha sido creado')

# No vamos a agregar el main, por que quien va a ejecutar es la suite
#if __name__ == '__main__':
#    unittest.main()
