from models.igdb import IGDB
from models.gamespot import GameSpot
from models.reviews.gamespot_review import GamespotReview
import json
import datetime as dt
from bs4 import BeautifulSoup


# api = IGDB('IGDB_API_KEY')
# result = api.games_by_name('God of War')
# for game in result.body:
#     if 'published_at' in game:
#         published = dt.datetime.utcfromtimestamp(game['published_at']).strftime('%Y-%m-%d')
#     else:
#         published = ''
#     print("Retrieved: " + str(game["name"]) + ' ' + str(game["game"])+' '+published)

# api = IGDB('IGDB_API_KEY')
# result = api.games((1942, 1941), ['name', 'rating'])
# for game in result.body:
#     print("Retrieved: " + str(game["name"]) + ' ' + str(game["rating"]))

# Write to CSV
# gs = GameSpot('GAMESPOT_API_KEY')
# result = gs.get_review().body
# with open('../data/rdr_gamespot_test.json', 'w') as fp:
#     json.dump(result, fp)

# Open CSV
# with open('../data/rdr_gamespot_test.json') as f:
#     data = json.load(f)['results'][0]

gs = GameSpot('GAMESPOT_API_KEY')
data = gs.get_review(2546091).body['results'][0]
gs_review = GamespotReview(data)
print(gs_review.game)
print(gs_review.title)
print(gs_review.review)
gs_review.get_word_count()