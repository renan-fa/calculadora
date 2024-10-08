import unittest

from calculadora import (
    adicionar, 
    subtrair, 
    multiplicar, 
    dividir, 
    exponenciacao, 
    radiciacao, 
    porcentagem, 
    fatorial                         
)

class TestCalculadora(unittest.TestCase):


    def test_adicionar(self):
  
        self.assertEqual(adicionar(10, 5), 15)


        self.assertEqual(adicionar(-1, 1), 0)

 
        self.assertEqual(adicionar(-1, -1), -2)

    def test_subtrair(self):
        
        self.assertEqual(subtrair(10, 5), 5)


        self.assertEqual(subtrair(1, 1), 0)


        self.assertEqual(subtrair(-1,1), -2)

    def test_multiplicar(self):

        self.assertEqual(multiplicar(5, 5), 25)


        self.assertEqual(multiplicar(-1, 1), -1)


        self.assertEqual(multiplicar(-1, -1), 1)
       
    def test_dividir(self):
        
        self.assertEqual(dividir(5, 5), 1)


        self.assertEqual(dividir(-25, 5), -5)


        self.assertEqual(dividir(-25, -5), 5)

    def test_exponenciacao(self):

        self.assertEqual(exponenciacao(4, 4), 256)

        
        self.assertEqual(exponenciacao(4, -1), 0.25)


        self.assertEqual(exponenciacao(-4, 2), 16)


    def test_radiciacao(self):
        
        self.assertEqual(radiciacao(25), 5)


        self.assertEqual(radiciacao(256), 16)


        self.assertEqual(radiciacao(1024), 32)


    def test_porcentagem(self):
        
        self.assertEqual(porcentagem(100, 20), 20)


        self.assertEqual(porcentagem(1000, 1), 10)


        self.assertEqual(porcentagem(10000, 1), 100)

    def test_fatorial(self):

        self.assertEqual(fatorial(5), 120)

        
        self.assertEqual(fatorial(10), 3628800)


        self.assertEqual(fatorial(4), 24)

if __name__ == '__main__':
    unittest.main()
