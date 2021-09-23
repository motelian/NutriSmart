from collections import namedtuple

#every 1gr protein equals to 4 calories
#every 1gr carb equals to 4 calories
#every 1gr fat equals to 8 calories
def convert(calories, decomp):
    '''This func converts the macro decomposition into grams'''
    prt = .01*decomp[0]*calories/4
    carb = .01*decomp[1]*calories/4
    fat = .01*decomp[2]*calories/9
    goal_df = {'cat':['calories', 'protein', 'carb', 'fat'], 'value':[calories,prt,carb,fat]}
    return goal_df

def agg_macro(food_macro):
    ''' This function calculates the total macro decomposition

    ::food_macro:: list of food dictionaries containing macro info
    for each food item
    '''
    consumed = {'cat':['calories', 'protein', 'carb', 'fat'], 'value':[0]*4}
    for food_item in food_macro:
        consumed['value'][0] += food_item['nf_calories']
        consumed['value'][1] += food_item['nf_protein']
        consumed['value'][2] += food_item['nf_total_carbohydrate']
        consumed['value'][3] += food_item['nf_total_fat']

    return consumed