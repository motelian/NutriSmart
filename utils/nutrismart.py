import json 
import os
import requests
from dotenv import load_dotenv, find_dotenv
from dateutil.parser import parse

def creds():
    '''Nutritionix API credentials '''
    load_dotenv(find_dotenv())
    secrets = dict()
    secrets['user_name'] = os.environ.get("USER_NAME")
    secrets['app_id'] = os.environ.get("APP_ID")
    secrets['app_key'] = os.environ.get("APP_KEY")
    return secrets

# process the recognized food text into json
def analyze(text, nx_api):
    ''' This function uses the Nutritionix nlp engine to extract food items, 
    quantities and their corresponding macros.'''

    username = nx_api['user_name']
    app_id = nx_api['app_id']
    app_key = nx_api['app_key']

    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {
        'accept': 'application/json',
        'x-app-id': app_id,#'2394a54f', #app_id,
        'x-app-key': app_key, #'4f22079aa9dee4d610a5afa1c6d286f3', #app_key,
        'x-remote-user-id': username, #'motevas2',#username,
        'Content-Type': 'application/json',
    }

    data = {"query": text, "timezone":"US/Eastern"}

    try:
        r = requests.post(url, headers=headers, json=data)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    
    test = r.json()
    print(username, app_id, app_key)
    print(headers)
    #print(test['id'],test['message'])

    return r.json()['foods']

# process the macros from food items
def extract_macros(foodlist):
    ''' This funtion returns a list of food dictionaries with the following 
    field items:

    food_name: egg
    serving_qty: 1
    serving_unit: large
    calories: 71.5 kCal
    protein: 6.28 grams
    carbs: 0.36 grams 
    fat: 4.76 grams
    time: '2021-09-23T12:00:00+00:00'
    photo: dict of photos with different res

    ::foodlist:: list of food dictionaries

    '''
    keys = ['food_name', 'serving_qty', 'serving_unit', 'nf_calories',\
         'nf_protein', 'nf_total_carbohydrate', 'nf_total_fat','consumed_at', 'photo']

    # extracted food items
    # TODO: check if the keys defined above can be found in food_list keys
    extrc = [{newkey: item[newkey] for newkey in keys} for item in foodlist]
    return extrc

def adjust_macros(user_qty, food_dict):
    keys = ['nf_calories', 'nf_protein', 'nf_total_carbohydrate', 'nf_total_fat']
    for key in keys:
        food_dict[key] = food_dict[key] * user_qty / food_dict['serving_qty']
    food_dict['serving_qty'] = user_qty
    return food_dict

def part_of_day(x):
    x = parse(x).hour
    # For some reason, there is a 4 hours offset from 
    # nutritionix US/Central to actual US/Central time
    x = x - 4
    if x >= 0 and x < 12:
        return 'Breakfast'
    elif x >= 12 and x < 16:
        return 'Lunch'
    else:
        return 'Dinner' 
