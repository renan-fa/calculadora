import unittest
from calculadora import adicionar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_adicionar(self):
        self.assertEqual(adicionar(10, 5), 15)
        self.assertEqual(adicionar(-1, 1), 0)
        self.assertEqual(adicionar(-1, -1), -2)

    def test_subtrair(self):
        pass

    def test_multiplicar(self):
        pass

    def test_dividir(self):
        pass

if __name__ == '__main__':
    unittest.main()
