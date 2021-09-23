import streamlit as st 
def expander(food_dict, food_key, expander_handle):
    ''' This function creates an expandable bar in streamlit 
    and list all the food items user consumed for a specific 
    time in the day (e.g. Breakfast/Lunch/Dinner)'''

    name = food_dict['food_name'].capitalize() + ' '+ '('+food_dict['serving_unit']+')'
    qty = food_dict['serving_qty']
    
    with expander_handle:
        qty = st.text_input(name,value=str(qty),key=food_key)
    
    return float(qty)