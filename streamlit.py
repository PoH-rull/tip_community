#py -m streamlit run Streamlit.py
import streamlit as st
import random
from streamlit_option_menu import option_menu
selected= option_menu(
        menu_title=None,
        options=["מחשבון","שאלות ותשובות","קצת עלינו","תרומות"],
        orientation="horizontal",
    )
if selected == "מחשבון":
    st.title("אתה בחרת במחשבון")
if selected == "שאלות ותשובות":
    st.title("אתה בחרת בשאלות ותשובות")
if selected == "קצת עלינו":
    st.title("אתה בחרת בקצת עלינו")
if selected == "תרומות":
    st.title("אתה בחרת בתרומות" )
def print_results(percent_max,percent_min):
    total_price=st.number_input("Enter price")
    st.write("Total price(with tip):")
    st.write(total_price+(total_price*random.randint(percent_min,percent_max)/100))

def main(button):
    if button == True:
        if indexRate==15:
            print_results(15,15)
        elif indexRate>10 and indexRate<15:
            print_results(10,14)
        elif indexRate>5 and indexRate<10:
            print_results(5,10)
        elif indexRate>0 and indexRate<5:
            print_results(1,5)
        else:
            print_results(0,0)


st.title("percentage calculator")
st.write("these questions are for how satisfied you are (rate from 1-5 while 1 is the lowest and 5 is the highest)")
serviceRate=st.number_input("how was the service?",step=1, max_value=5,min_value=1)
quickFoodRate=st.number_input("how fast the food arrived?",step=1, max_value=5,min_value=1)
totalCost=st.number_input("was the cost reasonable?(depending on where you were)",step=1, max_value=5,min_value=1)
# input_q4=st.slider("how much",max_value=5,min_value=1) 
indexRate=serviceRate+quickFoodRate+totalCost
button=st.button("press me when you done")

main(button)



