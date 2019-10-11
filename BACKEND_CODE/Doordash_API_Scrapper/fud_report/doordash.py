#!/usr/bin/env python

import json
import requests
import urlparse

from pprint import pprint


# TODO: ADD THIS TO ENV FILE
BASE_URL = 'https://www.doordash.com'



def find_restaurants_with_menu(report):
    count_res = len(report)
    print("{} restaurants found.".format(count_res))
    print

    count_res_with_menu = 0
    count_res_with_no_menu = 0

    for item in report:
        ## Pretty print items
        print("{}".format(item["name"].encode('utf-8').strip()))
        print("     {}".format(item["address"]["printable_address"].encode('utf-8').strip()))
        print("     Url: {0}/{1}".format(BASE_URL, item["url"]))
        print("     slug: {}".format(item["slug"]))
        print("     Cousine(s): {}".format(item["description"].encode('utf-8').strip()))
        print("     Average rating: {}".format(item["average_rating"]))
        print("     Yelp rating: {}".format(item["yelp_rating"]))

        # Fix price
        price = item["price_range"]
        if price == 1:
            p = "$"
        elif price == 2:
            p = "$$"
        elif price == 3:
            p = "$$$"
        elif price == 4:
            p = "$$$$"
        elif price == 5:
            p = "$$$$$"
        else:
            p = price
        print("     Price range: {}".format(p))

        # Fix menu
        menu = item["menus"]
        if "popular_items" in menu[0].keys() and menu[0]["popular_items"] != None and menu[0]["popular_items"] != []:
            count_res_with_menu = count_res_with_menu + 1

            print
            print("     MENU:")
            for menu_items in menu:
                menu_items = menu_items["popular_items"]

                if menu_items:
                    for menu_subitems in menu_items:
                        print("         Item: {}".format(menu_subitems["name"].encode('utf-8').strip("\n")))
                        print("         Description: {}".format(menu_subitems["description"].encode('utf-8').strip()))
                        print("         Price: ${}".format(menu_subitems["price"]/100.))
                        print("         Picture: {}".format(menu_subitems["img_url"]))
                        print
        else:
            count_res_with_no_menu = count_res_with_no_menu + 1


        print
        print("------------------------------------------------------------------")
        print

    print("*** Restaurants with menu: {0}. Resturant without menu: {1}".format(count_res_with_menu, count_res_with_no_menu))




def query_doordash_by_location(latitude, longitude):
    url = urlparse.urljoin(BASE_URL, 'api/v2/restaurant/?lat={0}&lng={1}'.format(latitude, longitude))
    response = requests.get(url)

    return response.json()


if __name__ == "__main__":

    LATITUDE = 33.987735281
    LONGITUDE =  -118.448394161

    report = query_doordash_by_location(LATITUDE, LONGITUDE)

    find_restaurants_with_menu(report)





