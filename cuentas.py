import unittest


class TestCuentas(unittest.TestCase):

    def test_cuenta_creada(self):
        cuenta = 12345
        self.assertEqual(cuenta, 12345)

# No vamos a agregar el main, por que quien va a ejecutar es la suite