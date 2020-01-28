import sys
import requests
import random
from bs4 import BeautifulSoup
from datetime import datetime


##################################
# TODO: add this to an env file
TRANSACTION_SEARCH_API_URL = 'https://api.yelp.com/v3/transactions/{}/search'
SEARCH_API_URL = 'https://api.yelp.com/v3/businesses/search'
API_KEY = 'LATVI7yLSOrwSKEv-RzC7iDRGQFYbipjTh2rYSby-ag6UHbDFOCq7hp4alFyTnL6POxhTlKqBNq4jCY-tD6WLpStA3WgLRjZRZG4SXM9UO2_HmEcg1aYpmiWiPobXXYx'
LAT_TEST = 37.7670169511878
LON_TEST = -122.42184275
ADDRESS_TEST = "2100 Main Street Santa Monica"
RADIUS_TEST = 40000 #24140 for 15 miles. Max is 40000 or 25 miles
LIMIT = 50
timeout_s = 10000

date = datetime.today().strftime('%Y-%m-%d')
YELP_URL_FILE = "yelp_url_file_{}.txt".format(date)
RESTAURANTS_URL_FILE = "restaurant_url_file_{}.txt".format(date)
IG_HANDLES_FILE = "restaurant_igs_{}.txt".format(date)

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

categories = ['acaibowls', 'bagels', 'bakeries', 'bento', 'bubbletea', 'coffee', 'fooddeliveryservices', 'foodtrucks', 'icecream', 'juicebar', 'poke', 'smokehouse']

cuisines = ['afghan', 'african', 'newamerican', 'tradamerican', 'arabian', 'argentine', 'asianfusion', 'australian', 'austrian', 'baguettes', 'bbq', 'belgian', 'bistro', 'breakfast_brunch', 'brazilian', 'british', 'buffets', 'burgers', 'cafes', 'cafeteria', 'cambodian', 'canadian', 'caribbean', 'catalan', 'cheesesteaks', 'chickenshop', 'chicken_wings', 'chilean', 'chinese', 'comfortfood', 'creperies', 'cuban', 'delis', 'diners', 'dumplings', 'eastern_european', 'ethiopian', 'hotdogs', 'filipino', 'fishnchips', 'flatbread', 'french', 'german', 'greek', 'gluten-free', 'hawaiian', 'hotdog', 'indonesian', 'international', 'italian', 'japanese', 'korean', 'kosher', 'latin', 'raw_food', 'mexican', 'mediterranean', 'meatballs', 'mideastern', 'modern_european', 'newmexican', 'milkbars', 'persian', 'opensandwiches', 'pizza', 'pita', 'portugueses', 'potatoes', 'rice', 'russian', 'salad', 'sandwiches', 'seafood', 'signature_cuisine', 'soup', 'spanish', 'supper_clubs', 'steak', 'sushi', 'tapas', 'thai', 'tex-mex', 'turkish']

categories.extend(cuisines)
##################################


# TODO: moving these floating functions to a class/another file
def process_response(response):
    """
    """
    # TODO MOVE THIS TO CACHE OR DB ENTRY
    with open(YELP_URL_FILE, 'a') as f:

        for item in response['businesses']:

            # Extract Url
            url = item['url'].split("?")[0]

            f.write("{}\n".format(url))

            # Insert db data
            # results = db.insert(response)


# TODO: CLEAN THIS up
def extract_ig_from_restaurant_urls():
    """
    """
    ig_set = set()

    with open(RESTAURANTS_URL_FILE, 'r') as f:
        rest_urls = f.readlines()

        for url in rest_urls:
            page = requests.get('http://{}'.format(url.strip('\n')))

            soup = BeautifulSoup(page.content, 'html.parser')

            class_list_list = soup.find_all('a')

            for item in class_list_list:

                    item = item.get('href')

                    if item and "instagram" in item:
                        item = item.split('instagram.com/')[1]
                        item =  item.split('/')[0]
                        ig_set.add(item.strip('/n'))

    with open(IG_HANDLES_FILE, 'a') as f:
        for url in ig_set:
            if url:
                f.write("{}\n".format(url))


# TODO: clean this up
def extract_url_from_yelp():
    """
    """

    url_set = set()

    with open(YELP_URL_FILE, 'r') as f:
        yelp_urls = f.readlines()

        for url in yelp_urls:
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')

            class_list = soup.find(class_='main-content-wrap--full')

            class_list_list = []
            try:
                class_list_list = class_list.find_all('a')
            except AttributeError:
                print "error"
                print class_list

            for item in class_list_list:
                try:
                    if "/biz_redir?" in item.get('href'):
                        try:
                            url = item.get('href')
                            url = url.split('/biz_redir?url=http%3A%2F%2F')[1].split('&website_link_type')[0].split('%2')[0]
                            url_set.add(url)

                        except IndexError:
                            try:
                                url = url.split('url=https%3A%2F%2F')[1].split('&website_link_type')[0].split('%2')[0]
                            except IndexError:
                                print "index error: {}".format(url)
                            pass

                # this happens when it's a yelp url, so we dont care
                except TypeError:
                    pass

    with open(RESTAURANTS_URL_FILE, 'a') as f:
        for url in url_set:
            f.write("{}\n".format(url))



class YelpAPI:

    def __init__(self, api_key, timeout_s=None):

        self.api_key = api_key
        self.timeout_s = timeout_s

        self.yelp_session = requests.Session()

        #user_agent = random.choice(user_agent_list)
        from fake_useragent import UserAgent
        ua = UserAgent()
        user_agent = ua.random
        self.headers = {'User-Agent': user_agent, 'Authorization': 'Bearer {}'.format(self.api_key)}

    def search_query(self, latitude, longitude):
        """
        """

        return self._query(SEARCH_API_URL, latitude, longitude)

    def transaction_search_query(self, transaction_type, latitude, longitude):
        """
        """

        if not transaction_type:
            raise ValueError('A valid transaction type (parameter "transaction_type") must be provided.')

        return self._query(TRANSACTION_SEARCH_API_URL.format(transaction_type), latitude, longitude)

    def get_coord_parameters(self, latitude, longitude, radius, limit):
        """
        """

        return {
                'latitude': latitude,
                'longitude': longitude,
                'term': 'restaurants',
                'radius': radius,
                'limit': limit
                }

    def get_address_parameters(self, address, radius, limit):
        """
        """

        return {
                'location': address,
                'term': 'restaurants',
                'radius': radius,
                'limit': limit
                }

    def query(self, url, parameters):
        """
        """

        response = self.yelp_session.get(
            url,
            headers=self.headers,
            params=parameters,
            timeout=self.timeout_s,
        )

        if response.status_code != 200:
            print "Response error: {}".format(response.status_code)
            return None
        else:
            response_json = response.json()

            return response_json




if __name__ == "__main__":

    yelp = YelpAPI(API_KEY)

    BY_LOCATION = False
    BY_ADDRESS = False
    EXTRACT_URL_FROM_YELP = False
    EXTRACT_IG = True


    # Get restaurant list by location or address
    if BY_LOCATION:
        parameters = yelp.get_coord_parameters(LAT_TEST, LON_TEST, RADIUS_TEST, LIMIT)
        response = yelp.query(SEARCH_API_URL, parameters)

    if BY_ADDRESS:
        parameters = yelp.get_address_parameters(ADDRESS_TEST, RADIUS_TEST, LIMIT)
        response = yelp.query(SEARCH_API_URL, parameters)
        process_response(response)

    # Get URLs
    if EXTRACT_URL_FROM_YELP:
        extract_url_from_yelp()

    # Get URLS
    if EXTRACT_IG:
        extract_ig_from_restaurant_urls()
