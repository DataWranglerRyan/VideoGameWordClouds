import requests
import json


class IGDB(object):
    __api_key = ""
    __api_url = "https://api-v3.igdb.com/"

    def __init__(self, api_key):
        self.__api_key = api_key

    def parse_field(self, fields):
        if isinstance(fields, list) or isinstance(fields, tuple):
            return ','.join(list(fields))
        else:
            return fields

    def parse_ids(self, ids):
        if isinstance(ids, list) or isinstance(ids, tuple):
            return tuple(ids)
        else:
            return ids

    def getRequest(self, url, body=""):
        headers = {
            'user-key': self.__api_key,
            'Accept': 'application/json'
        }
        r = requests.get(self.__api_url + url, headers=headers, data=body)
        r.body = json.loads(r.text)
        return r

    # GAMES
    def get_games_custom_query(self, body):
        r = self.getRequest("games", body)
        return r

    def get_search_custom_query(self, body):
        r = self.getRequest("search", body)
        return r

    def games(self, game_id, fields=None):
        if fields is None:
            fields = '*'
        body = """
        fields {1};
        where id = {0};
        """.format(self.parse_ids(game_id), self.parse_field(fields))
        r = self.get_games_custom_query(body)
        return r

    def games_by_name(self, game, fields=None):
        if fields is None:
            fields = '*'
        body = """
        fields {1};
        search "{0}";
        where game != null;
        """.format(self.parse_ids(game), self.parse_field(fields))
        r = self.get_search_custom_query(body)
        return r
