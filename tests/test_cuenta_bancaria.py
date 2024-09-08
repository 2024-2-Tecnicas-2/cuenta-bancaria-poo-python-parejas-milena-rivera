import unittest
from cuenta_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaBancaria('Isaac Rivera ', '507232755 ', 1000.0)

    def test_ingresar(self):
        self.cuenta.ingresar(500.0)
        saldo_esperado = 1500.0
        saldo_actual = self.cuenta.get_saldo()
        self.assertEqual(saldo_esperado, saldo_actual, "El saldo despues de ingresar 500.0 deberia ser 1500.0 ")

    def test_retirar_exceso(self):
        with self.assertRaises(ValueError):
            self.cuenta.retirar(2000.0)

if __name__ == '__main__':
    unittest.main()