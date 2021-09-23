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