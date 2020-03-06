import unittest
from knights import solvable, findstart, findpath

class TestKnights(unittest.TestCase):
    def test_solvable_onestepcase(self):
        self.assertTrue(solvable((3, 4), {(2, 2)}))
        self.assertTrue(solvable((4, 3), {(2, 2)}))

    def test_solvable_bookexample(self):
        pawns = {(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4), (5,5), (5,6), (5,7), (6,5), (6,7), (7,5), (7,6), (7,7)}
        self.assertTrue(solvable((1,1), pawns))
        self.assertTrue(solvable((1,1), pawns))
        self.assertFalse(solvable((2,7), pawns))

    def test_findstart_onestep_nearcorner(self):
        pawns = {(2,2)}
        expected_solutions = {(1,4), (3,4), (4,3), (4,1)}
        self.assertEqual(findstart(pawns), expected_solutions)

    def test_findstart_onestep_inmiddle(self):
        pawns = {(3,4)}
        expected_solutions = {(1,3), (2,2), (1,5), (2,6), (4,6), (5,5), (5,3), (4,2)}
        self.assertEqual(findstart(pawns), expected_solutions)

    def test_findstart_bookexample(self):
        pawns = {(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4), (5,5), (5,6), (5,7), (6,5), (6,7), (7,5), (7,6), (7,7)}
        solutions = findstart(pawns)
        for start in [(1, 3), (4, 8), (2, 1), (1, 6), (5, 1), (8, 5)]:
            self.assertTrue(start in solutions)
            flipped = (start[1], start[0])
            self.assertTrue(flipped in solutions)
        self.assertEqual(len(solutions), 30)
        for start in [(2, 7), (7, 3), (4, 7), (2, 6), (3, 3), (8, 2)]:
            self.assertTrue(start not in solutions)
            flipped = (start[1], start[0])
            self.assertTrue(flipped not in solutions)

    def test_findpath_onestepexample(self):
        self.assertEqual(findpath((6,6), {(7,8)}), [(6,6), (7,8)])

    def test_findpath_twostepexample(self):
        self.assertEqual(findpath((8,7), {(6,6), (7,8)}), [(8,7), (6,6), (7,8)])

    def test_findpath_bookexample(self):
        pawns = {(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4),
                 (5,5), (5,6), (5,7), (6,5), (6,7), (7,5), (7,6), (7,7)}
        solutions = {(6, 4), (5, 4), (4, 5), (1, 4), (8, 7), (3, 5), (5, 3)}
        for start in solutions:
            path = findpath(start, pawns)
            # it starts at the start
            self.assertEqual(path[0], start)
            # it contains all the pawns and nothing else
            self.assertEqual(pawns, set(path[1:]))
            # all the moves are valid
            for i in range(len(path) - 1):
                p, q = path[i], path[i + 1]
                horizdiff, vertdiff = p[0] - q[0], p[1] - q[1]
                self.assertEqual({abs(vertdiff), abs(horizdiff)}, {1,2})

if __name__ == '__main__':
    unittest.main()
