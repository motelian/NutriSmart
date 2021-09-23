import streamlit as st
import numpy as np
import pandas as pd

# load libs from utils
import utils.speech_recog as sr 
import utils.plot as plot
from utils.macro_calc import convert

def app():
    st.title('Welcome to the NutriSmart ! 👋')
    st.markdown("Sculpt your dream body with NutriSmart. NutriSmart is an AI-based calorie and macro counter app enabling effortless tracking of your nurition by simply TALKING into your microphone. \
You'll get a budget- and diet-specific food suggestions making it affordable and easy to reach your goal. No more typing in or searching food names !\
The focus is on your goals and health in an effortless and easiest way possible ! Enjoy")
    c1, c2 = st.beta_columns([0.5,1])
    with c1:
        st.markdown("<h1 style='text-align: center; font-size:1.75em ; color: green;'>Fitness Goals</h1>", unsafe_allow_html=True)
        # TODO define a named tuple for macros
        # e.g. macro.cal, macro.protein, ..
        cal = float(st.text_input("Calories (cal):",value="2000"))

        # TODO: restirct user entring ratios > 100% 
        rprt = float(st.text_input("Protein (%):", value="40"))
        rcarb = float(st.text_input("Carbs (%):", value="40"))
        rfat = float(st.text_input("Fat (%):", value="20"))

        # write a function that takes cal, prt, crb, fat from the user
        # and returns the goal dataframe
        goal = pd.DataFrame(convert(cal, [rprt, rcarb, rfat]))

    with c2:
        st.markdown("<h1 style='text-align: center; font-size:1.75em ; color: green;'>Talk Food to Me</h1>", unsafe_allow_html=True)
        audio_on = st.selectbox("Speech recoginition mode",('off','on'))
        if audio_on =='off':
            recog_text = st.text_area("Please enter your daily food items", height = 2, value="e.g. for breakfast, I had two eggs and 1 avocado for lunch I had a 12 oz Ribeye steak with 2 medium potatoes and for dinner I had 1/2 cup of rice and 200 gr of chicken breasts")
            
            # write a function that takes a food log and spits out the food items and their values
            # Alternative use the Edamam engine to process the food log and give you all the food 
            # items, calories, macros and use those values to calculate the macros

            # identify the time user consumed the food 
        else:
            pass

if __name__ == "__main__":
    cal = app()
    print(cal)