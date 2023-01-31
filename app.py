#py -m streamlit run app.py
import random
import streamlit as st
from streamlit_option_menu import option_menu
tab1, tab2, tab3,tab4 = st.tabs(["מחשבון", "שאלות ותשובות", "קצת עלינו","תרומות"])
with tab1:
    st.title("מחשבון")
with tab2:
    st.title("שאלות ותשובות")
with tab3:
    st.title("עלינו")
with tab4:
    st.title("תרומות" )
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



