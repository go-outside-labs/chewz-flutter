import requests


# TODO: add this to an env file
TRANSACTION_SEARCH_API_URL = 'https://api.yelp.com/v3/transactions/{}/search'
SEARCH_API_URL = 'https://api.yelp.com/v3/businesses/search'

categories = ['acaibowls', 'bagels', 'bakeries', 'bento', 'bubbletea', 'coffee', 'fooddeliveryservices', 'foodtrucks', 'icecream', 'juicebar', 'poke', 'smokehouse']

cuisines = ['afghan', 'african', 'newamerican', 'tradamerican', 'arabian', 'argentine', 'asianfusion', 'australian', 'austrian', 'baguettes', 'bbq', 'belgian', 'bistro', 'breakfast_brunch', 'brazilian', 'british', 'buffets', 'burgers', 'cafes', 'cafeteria', 'cambodian', 'canadian', 'caribbean', 'catalan', 'cheesesteaks', 'chickenshop', 'chicken_wings', 'chilean', 'chinese', 'comfortfood', 'creperies', 'cuban', 'delis', 'diners', 'dumplings', 'eastern_european', 'ethiopian', 'hotdogs', 'filipino', 'fishnchips', 'flatbread', 'french', 'german', 'greek', 'gluten-free', 'hawaiian', 'hotdog', 'indonesian', 'international', 'italian', 'japanese', 'korean', 'kosher', 'latin', 'raw_food', 'mexican', 'mediterranean', 'meatballs', 'mideastern', 'modern_european', 'newmexican', 'milkbars', 'persian', 'opensandwiches', 'pizza', 'pita', 'portugueses', 'potatoes', 'rice', 'russian', 'salad', 'sandwiches', 'seafood', 'signature_cuisine', 'soup', 'spanish', 'supper_clubs', 'steak', 'sushi', 'tapas', 'thai', 'tex-mex', 'turkish']

categories.extend(cuisines)


class YelpAPI:

    def __init__(self, api_key, timeout_s=None):

        self._api_key = api_key
        self._timeout_s = timeout_s
        self._yelp_session = requests.Session()
        self._headers = {'Authorization': 'Bearer {}'.format(self._api_key)}

    def search_query(self, **kwargs):

        if not kwargs.get('location') and (not kwargs.get('latitude') or not kwargs.get('longitude')):
            raise ValueError('A valid latitude/longitude combinatiop must be provided.')

        return self._query(SEARCH_API_URL, **kwargs)

    def transaction_search_query(self, transaction_type, **kwargs):

        if not transaction_type:
            raise ValueError('A valid transaction type (parameter "transaction_type") must be provided.')

        if not kwargs.get('location') and (not kwargs.get('latitude') or not kwargs.get('longitude')):
            raise ValueError('A valid latitude/longitude combination must be provided.')

        return self._query(TRANSACTION_SEARCH_API_URL.format(transaction_type), **kwargs)

    @staticmethod
    def _get_clean_parameters(kwargs):
        return dict((k, v) for k, v in kwargs.items() if v is not None)

    def _query(self, url, **kwargs):

        parameters = YelpAPI._get_clean_parameters(kwargs)
        response = self._yelp_session.get(
            url,
            headers=self._headers,
            params=parameters,
            timeout=self._timeout_s,
        )
        response_json = response.json()

        if 'error' in response_json:
            raise (response_json)

        return response_json