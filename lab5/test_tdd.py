import unittest
from lab5.quadratic import solve_quadratic

class TestQuadraticSolver(unittest.TestCase):
    def test_no_real_roots(self):
        self.assertEqual(solve_quadratic(1, 0, 1), [])

    def test_one_root(self):
        roots = solve_quadratic(1, -2, 1)
        self.assertCountEqual(roots, [1.0, -1.0])  # Проверяем без учета порядка

    def test_two_roots(self):
        roots = solve_quadratic(1, -3, 2)
        self.assertCountEqual(roots, [1.4142135623730951, -1.4142135623730951, 1.0, -1.0])  # Проверяем без учета порядка

if __name__ == "__main__":
    unittest.main()
