# #py -m streamlit run app.py
import streamlit as st
tab1, tab2, tab3,tab4 = st.tabs(["מחשבון", "שאלות ותשובות", "קצת עלינו","תרומות"])
def check_tip():
    if indexRate==15:
        x=print_results(15)
    elif indexRate>10 and indexRate<15:
        x=print_results(10)
    elif indexRate>5 and indexRate<10:
        x=print_results(5)
    elif indexRate>0 and indexRate<5:
        x=print_results(1)
    else:
        x=print_results(0)
    st.write(f"the total price is {x}")
    return x
def print_results(percent_max):
    total_price=float(st.number_input("Enter price"))
    x=total_price+(total_price*percent_max/100)
    return x

with tab1:
    st.title("מחשבון")
    st.title("percentage calculator")
    st.write("these questions are for how satisfied you are (rate from 1-5 while 1 is the lowest and 5 is the highest)")
    serviceRate=st.slider("how was the service?",max_value=5,min_value=1)
    quickFoodRate=st.slider("how fast the food arrived?",max_value=5,min_value=1)
    totalCost=st.slider("was the cost reasonable?(depending on where you were)",max_value=5,min_value=1)
    indexRate=serviceRate+quickFoodRate+totalCost
    button=st.button("press me when you done",on_click=check_tip())
with tab2:
    st.title("שאלות ותשובות")
    
with tab3:
    st.title("עלינו")
with tab4:
    st.title("תרומות" )
 
#chat GPT
# import streamlit as st
# def print_results(percent_max):
#     total_price=float(st.number_input("Enter price"))
#     x=total_price+(total_price*percent_max/100)
#     return x
# def check_tip():
#     if indexRate==15:
#         x=print_results(15)
#     elif indexRate>10 and indexRate<15:
#         x=print_results(10)
#     elif indexRate>5 and indexRate<10:
#         x=print_results(5)
#     elif indexRate>0 and indexRate<5:
#         x=print_results(1)
#     else:
#         x=print_results(0)
#     st.write(f"the price is {x}")
#     return x
# tab1, tab2, tab3,tab4 = st.tabs(["מחשבון", "שאלות ותשובות", "קצת עלינו","תרומות"])
# with tab1:
#     st.title("מחשבון")
#     st.title("percentage calculator")
#     st.write("these questions are for how satisfied you are (rate from 1-5 while 1 is the lowest and 5 is the highest)")
#     serviceRate=st.slider("how was the service?",max_value=5,min_value=1)
#     quickFoodRate=st.slider("how fast the food arrived?",max_value=5,min_value=1)
#     totalCost=st.slider("was the cost reasonable?(depending on where you were)",max_value=5,min_value=1)
#     indexRate=serviceRate+quickFoodRate+totalCost
#     button=st.button("press me when you done",on_click=check_tip)
# with tab2:
#     st.title("שאלות ותשובות")
# with tab3:
#     st.title("עלינו")
# with tab4:
#     st.title("תרומות" )
   
    






