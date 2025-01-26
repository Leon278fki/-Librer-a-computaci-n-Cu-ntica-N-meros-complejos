import unittest
from funcionesComplejos import sumaC, multiplicacionC, divisionC, moduloC, conjugadoC, polaresC, cartesianasC

class TestFunciones(unittest.TestCase):
    
    def test_sumaComplejos(self):
        self.assertEqual(sumaC((2, 3),(1,1)), (3,4))
        self.assertEqual(sumaC((1, 3),(1,0)), (2,3))
        self.assertEqual(sumaC((4, 0),(0,1)), (4,1))
    
    def test_restarComplejos(self):
        self.assertEqual(sumaC((2, 3),(-1,-1)), (1,2))
        self.assertEqual(sumaC((1, 3),(-1,0)), (0,3))
        self.assertEqual(sumaC((4, 0),(0,-1)), (4,-1))

    def test_multiplicacionComplejos(self):
        self.assertEqual(multiplicacionC((2, 1),(1,4)), (-2,9))
        self.assertEqual(multiplicacionC((4, 1),(1,1)), (3,5))
        self.assertEqual(multiplicacionC((4, 2),(1,0)), (1,0))

    def test_divisionComplejos(self):
        self.assertEqual(divisionC((0, 2),(1,3)), (0.6,0.2))
        self.assertEqual(divisionC((4, 1),(1,1)), (2.5,-1.5))
        self.assertEqual(divisionC((4, 2),(1,0)), (4,2))

    def test_moduloComplejos(self):
        self.assertEqual(moduloC(2, 1), 2.23606797749979)
        self.assertEqual(moduloC(4, 2), 4.47213595499958)
        self.assertEqual(moduloC(3, 4), 5)

    def test_conjugadoComplejos(self):
        self.assertEqual(conjugadoC(2, 1), (2,-1))
        self.assertEqual(conjugadoC(3, 2), (3,-2))
        self.assertEqual(conjugadoC(2, 0), (2,0))

    def test_polaresComplejos(self):
        self.assertEqual(polaresC(4, 2), (4.472,0.464))
        self.assertEqual(polaresC(3, 2), (3.606,0.588))
        self.assertEqual(polaresC(2, 0), (2,0))

    def test_polaresComplejos(self):
        self.assertEqual((cartesianasC(4.472,0.464),(4, 2))
        self.assertEqual(cartesianasC(3.606,0.588),(3, 2))
        self.assertEqual(cartesianasC(2,0),(2, 0))

if __name__ == '__main__':
    unittest.main()
