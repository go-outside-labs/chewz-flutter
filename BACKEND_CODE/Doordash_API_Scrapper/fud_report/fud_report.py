# encoding=utf8

import csv
import sys
import json
from pprint import pprint
from geopy.geocoders import Nominatim

from doordash import query_doordash_by_location, find_restaurants_with_menu
from YelpAPI import YelpAPI, categories


# TODO: ADD BELOW TO AN ENV VARIABLE
# REMOVE HARD-CODED API KEY
api_key = 'LATVI7yLSOrwSKEv-RzC7iDRGQFYbipjTh2rYSby-ag6UHbDFOCq7hp4alFyTnL6POxhTlKqBNq4jCY-tD6WLpStA3WgLRjZRZG4SXM9UO2_HmEcg1aYpmiWiPobXXYx'
google_api_key='AIzaSyCGQRmllZFJSIQ7wzgR3ggyNgO7bTxze0Y'
timeout_s = 10000
filter_by_rating = True
limit = 50 #can't be more than 50 or generates an error
radius = 1000# 40000 #24140 for 15 miles. Max is 40000 or 25 miles
address = "3113 Yale Ave Los Angeles"
yelp_report_name = '../reports/yelp{}.csv'.format(''.join(address))
doordash_report_name = '../reports/doordash{}.json'.format(''.join(address))
min_rating = 3.5
#####



def generate_yelp_report_by_address():

    biz_dict = {}
    unique_restaurant_ids = set()

    for category in categories:
        response = yelp_api.search_query(term=category, location=address, sort_by='rating', limit=50, radius=radius)

        businesses = response['businesses']
        print('Found {0} places for category {1} in a radius of {2} meters around {3}.'.format(len(businesses), category, radius, address))

        for biz in businesses:
                biz_id = biz['id']

                # Check whether it is in the list already
                if biz_id in unique_restaurant_ids:
                    continue
                else:
                    unique_restaurant_ids.add(biz_id)

                # Clean up multi-category responses
                biz_cat = [x.values() for x in biz['categories']][0][0]

                # Add a string to biz that have empty price
                if not 'price' in biz:
                    biz['price'] = '-'

                # Filter ratings
                if filter_by_rating:
                    if int(biz['rating']) < min_rating:
                        continue

                # Save restaurant data
                biz_dict[biz_id] = []
                biz_dict[biz_id].append(u''.join(biz['alias']).encode('utf-8').strip())
                biz_dict[biz_id].append(biz_cat)
                biz_dict[biz_id].append(biz['price'])
                biz_dict[biz_id].append(biz['rating'])
                biz_dict[biz_id].append(biz['distance'])
                biz_dict[biz_id].append(biz['url'])

    return biz_dict


def generate_doordash_report_by_coordinates():

    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print("Coordinates for {0} are Lat: {1}, Lon: {2}".format(address, location.latitude, location.longitude))
    return query_doordash_by_location(location.latitude, location.longitude)


if __name__ == "__main__":

    # TODO: add an argparse menu here instead
    GENERATE_YELP_REPORT = False
    GENERATE_DOORDH_REPORT = True
    GENERATE_AGGREGATE_REPORT = False

    if GENERATE_YELP_REPORT:
        yelp_api = YelpAPI(api_key, timeout_s)

        biz_dict_yelp = generate_yelp_report_by_address()

        f = open(yelp_report_name, 'w')
        f.write('Restaurant Name, Category, Price, Rating, Distances, Biz url, Latitude, Longitude\n')

        for biz_id, biz_data in biz_dict_yelp.items():
            for item in biz_data:
                f.write('{}, '.format(item))
            f.write('\n')

        f.close()


    if GENERATE_DOORDH_REPORT:

            dd_report = generate_doordash_report_by_coordinates()
            find_restaurants_with_menu(dd_report)

            with open(doordash_report_name, 'w') as f:
                json.dump(dd_report, f)

            print
            print("Report saved at {}".format(doordash_report_name))



    if GENERATE_AGGREGATE_REPORT:

        count = 0
        with open(yelp_report_name) as yfile:
            ydata = csv.reader(yfile, delimiter=',')
            for row in ydata:

                with open(doordash_report_name) as ddfile:
                    ddata = csv.reader(ddfile, delimiter=',')

                    for row_ in ddata:
                        if row[0].find(row_[0]) == 0 or row_[0].find(row[0]) == 0:
                            print row[0], row_[0]
                            count = count +1

        print "Grubhub & Yelp match: {}".format(count)



