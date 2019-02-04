from models.reviews.review import Review
from bs4 import BeautifulSoup


class GamespotReview(Review):
    def __init__(self, data):
        Review.__init__(self)
        self.data = data
        self.review = self.parse_review_text()
        self.title = data['title']
        self.author = data['authors']
        self.rating = data['score']
        self.game = data['game']['name']

    def parse_review_text(self):
        soup = BeautifulSoup(self.data['body'], 'html.parser')
        review = '\n'.join(soup.find_all(text=True))
        return review + ' ' + self.data['good'] + ' ' + self.data['bad']
