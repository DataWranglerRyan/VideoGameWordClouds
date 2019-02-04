import unittest
from models.igdb import IGDB


class TestIGDB(unittest.TestCase):
    def setUp(self):
        self.igdb = IGDB('IGDB_API_KEY')

    def tearDown(self):
        pass

    def test_games(self):
        # Test Single Game works
        game = self.igdb.games(1942)
        self.assertTrue(game.body[0]["name"] == 'The Witcher 3: Wild Hunt' and len(game.body) == 1)
        # Test Multiple Games work with list
        self.assertTrue(len(self.igdb.games([1942, 2941]).body) == 2)
        # Test Multiple Games work with tuple
        self.assertTrue(len(self.igdb.games((1942, 2941)).body) == 2)
        # Test Field parameter
        self.assertTrue(list(self.igdb.games(1942, 'name').body[0].keys()) == ['id', 'name'])
        # Test Multiple Field parameter
        self.assertTrue(list(self.igdb.games(1942, ('name', 'rating')).body[0].keys()) == ['id', 'name', 'rating'])

if __name__ == '__main__':
    unittest.main()
