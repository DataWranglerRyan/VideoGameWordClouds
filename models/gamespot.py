import requests
import json


class GameSpot(object):
    __api_format = "&format=json"
    __api_key = ""
    __api_url = "https://www.gamespot.com/api/"
    __ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    def __init__(self, api_key):
        self.__api_key = api_key

    def getRequest(self, url, filters=None, fields=None):
        payload = {
            'api_key': self.__api_key,
            'format': 'json'
        }
        if filters:
            payload['filter'] = filters
        if fields:
            payload['field_list'] = fields
        headers = {
            'User-Agent': self.__ua
        }
        url2 = self.__api_url + url
        r = requests.get(url2, params=payload, headers=headers)
        r.body = json.loads(r.text)
        return r

    '''
        Accepts a filter query in the form of 'field:value1|value2'
        Accepts a fields query in the form of 'field1,field2'
    '''
    def get_review_custom_query(self, filters=None, fields=None):
        r = self.getRequest("reviews/", filters, fields)
        return r

    '''
        Accepts a review_id as an integer to get  a single review or a list of reviews to get multiple reviews.
        Accepts a field name as a string to return only one field or a list to return multiple fields.
    '''
    def get_review(self, review_id, fields = None):
        if isinstance(review_id, list):
            review_id = '|'.join(list(map(str, review_id)))
        if isinstance(fields, list):
            fields = ','.join(fields)
        filters = 'id:' + str(review_id)
        return self.get_review_custom_query(filters, fields)

