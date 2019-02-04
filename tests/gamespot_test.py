import unittest
from models.gamespot import GameSpot


class TestGameSpot(unittest.TestCase):
    def setUp(self):
        self.gs = GameSpot('GAMESPOT_API_KEY')

    def tearDown(self):
        pass

    def test_get_review(self):
        # Test Single Review works
        review = self.gs.get_review(6417019)
        self.assertTrue(review.body['results'][0]['title'] == 'Red Dead Redemption 2 Review - Wild Wild West')
        review = self.gs.get_review([6417019])
        self.assertTrue(review.body['results'][0]['title'] == 'Red Dead Redemption 2 Review - Wild Wild West')
        # Test Multiple Review works
        review = self.gs.get_review([6417019, 6417018])
        self.assertTrue(review.body['results'][1]['title'] == 'Red Dead Redemption 2 Review - Wild Wild West'
                        and review.body['results'][0]['title'] == 'NBA 2K Playgrounds 2 Review - Ball Another Day')
        # Test Single Field Parameter works
        review = self.gs.get_review(6417019, 'title')
        self.assertTrue(list(review.body['results'][0].keys()) == ['title'])
        # Test Multiple Field Parameter works
        review = self.gs.get_review(6417019, ['title', 'body'])
        self.assertTrue(list(review.body['results'][0].keys()) == ['title', 'body'])

if __name__ == '__main__':
    unittest.main()
