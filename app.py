# #py -m streamlit run app.py
import streamlit as st
q1="שאלה 1 : מה זה טיפ?"
q2="שאלה 2 :כמה מדויק מחשבון האחוזים?"
q3="שאלה 3 : מה המקסימום אחוזים של טיפ?"
q4="שאלה 4 : מה המינימום אחוזים של טיפ?"
q5="שאלה 5 : האם כלי מחשבון עצות זה חינמי לחלוטין?"
q6=" שאלה 6 : למה המחשבון שלנו שונה מאתרים אחרים?"
a1="תשובה 1 : תֶּשֶׁר הוא סכום כסף אותו נותן לקוח לעובד שממנו קיבל שירות, בנוסף על החשבון הקבוע, כאות הוקרה על השירות. גודל הסכום תלוי בנוהג המקובל באותו אזור, אופי והיקף השירות וכן איכותו. "
a2="תשובה 2 : המחשבון מדויק במידת הדיוק שאתה מזין."
a3="תשובה 3 : המקסימום טיפ הוא 15"
a4="תשובה 4 : מינימום טיפ זה 0"
a5="תשובה 5 : כן. כלי מחשבון העצות הוא לגמרי בחינם לשימוש. אינך צריך לשלם דבר כדי להשתמש בשירותים המוצעים על ידי כלי זה."
a6="תשובה 6 : המשבון שלנו שונה מאחרים בכך שלעומת אחרים הוא מחשב את אחוזי הטיפ לפי שאלות שביעות רצון המשתמש."



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
    st.markdown(f"<p dir='rtl'>{q1}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{a1}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{q2}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{a2}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{q3}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{a3}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{q4}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{a4}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{q5}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{a5}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{q6}</p>", unsafe_allow_html=True)
    st.markdown(f"<p dir='rtl'>{a6}</p>", unsafe_allow_html=True)
    
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
   
    






