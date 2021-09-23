import streamlit as st
import pandas as pd

# load libs from utils
from utils.speech_recog import recog_audio 
import utils.plot as plot
from utils.macro_calc import convert, agg_macro
import utils.nutrismart as ns
from utils.webpage_designer import expander
from utils.plot import macro_plot

def app():
    st.title('Welcome to the NutriSmart ! 👋')
    st.markdown("Sculpt your dream body with NutriSmart. NutriSmart is an AI-based calorie and macro counter app enabling effortless tracking of your nurition by simply TALKING into your microphone. \
You'll get a budget- and diet-specific food suggestions making it affordable and easy to reach your goal. No more typing in or searching food names !\
The focus is on your goals and health in an effortless and easiest way possible ! Enjoy")
    c1, c2 = st.columns([0.5,1]) 
    with c1:
        st.markdown("<h1 style='text-align: center; font-size:1.75em ; color: green;'>Fitness Goals</h1>", unsafe_allow_html=True)
        # TODO write a function for taking in the user's
        # input and save it into a named tuple for macros
        # e.g. macro.cal, macro.protein, ..
        cal = float(st.text_input("Calories (cal):",value="4000"))

        # TODO: restirct user entring ratios > 100% 
        rprt = float(st.text_input("Protein (%):", value="40"))
        rcarb = float(st.text_input("Carbs (%):", value="40"))
        rfat = float(st.text_input("Fat (%):", value="20"))

        # takes in macros from the user and returns the goal dataframe
        goal = pd.DataFrame(convert(cal, [rprt, rcarb, rfat]))

    with c2:
        st.markdown("<h1 style='text-align: center; font-size:1.75em ; color: green;'>Talk Food to Me</h1>", unsafe_allow_html=True)
        audio_on = st.selectbox("Speech recoginition mode",('off','on'))
        if audio_on =='off':
            recog_text = st.text_area("Please enter your daily food items", height = 2, value="e.g. for breakfast, I had two eggs and 1 avocado for lunch I had a 12 oz Ribeye steak with 2 medium potatoes and for dinner I had 1/2 cup of rice and 200 gr of chicken breasts")
        else:
            st.code("Please allow Google 5 seconds to recognize your voice.")
            recog_text = recog_audio()
            st.write("Recognized Text:\n"+recog_text)
                
        # use the Nutritionix API to extract food items and serving sizes
        nx_api = ns.creds()  
        food_list = ns.analyze(recog_text, nx_api)
        food_macros = ns.extract_macros(food_list)
        
        # TODO: if time of the day is not present in the 
        # recognized text remove it's correspoding expander
        bf = st.expander(label='Breakfast') 
        lch = st.expander(label='Lunch') 
        din = st.expander(label='Dinner') 

        for i,item in enumerate(food_macros):
            timestamp = item['consumed_at']
            meal_time = ns.part_of_day(timestamp)
            item_key =  item['food_name'] + '_' + str(i)

            if meal_time == 'Breakfast': 
                handle = bf
            elif meal_time == 'Lunch':
                handle = lch
            else:
                handle = din

            qty = expander(item, item_key, handle)
            # adjust the macros if user change the quantity of the food items
            if qty != item['serving_qty']:
                # this will change info in food_macros 
                # since dicts are mutable in python 
                item = ns.adjust_macros(qty, item)

        # calculate the total macro decomposition 
        consumed = pd.DataFrame(agg_macro(food_macros))
        show_macros = macro_plot(consumed,goal,plot_width=400)
        st.altair_chart(show_macros)

if __name__ == "__main__":
    app()