import pandas as pd
import streamlit as st
import warnings
import joblib 
warnings.filterwarnings("ignore", category=FutureWarning)




st.title('Credit Score Calculator')

with st.sidebar:

    st.markdown("[What is Credit Score?](#head)",unsafe_allow_html=True)

    st.markdown("[How it Works?](#sh1)",unsafe_allow_html=True)

    st.markdown("[How Our model  Works?](#sh2)",unsafe_allow_html=True)

    st.markdown("[Calculate Score](#sh3)",unsafe_allow_html=True)
    st.markdown("[Authors](#au)",unsafe_allow_html=True)


st.header("What is Credit Score?",anchor="head")

st.write('''Credit scoring is a statistical analysis performed by lenders and financial institutions to determine the creditworthiness of a person or a small, owner-operated business.
             Credit scoring is used by lenders to help decide whether to extend or deny credit. A credit score can impact your ability to qualify for financial products like mortgages, auto loans, credit cards, and private loans.''')

st.subheader("How it Works?",anchor="sh1")

st.write('''Credit scores are calculated using factors like payment history (35%), credit utilization (30%), length of credit history (15%), credit mix (10%), and new credit (10%). These elements determine your score, which ranges from 300 to 850, indicating your creditworthiness to lenders. Maintaining timely payments, low credit card balances relative to limits, and a diverse credit history can positively impact your score, while recent credit inquiries and high debt levels can lower it. Understanding and managing these factors can help you improve your credit score over time, making it easier to access loans and financial products with favorable terms.''')



st.subheader("How  Our model Works?",anchor="sh2")

st.write('''This project leverages machine learning techniques to predict credit scores effectively. It uses Random Forest for accurate score predictions by analyzing historical data such as payment history and credit utilization. Additionally, K-means clustering segments individuals based on their predicted scores, enabling tailored financial strategies and risk assessments. This approach enhances decision-making for financial institutions by providing insights into customer creditworthiness and optimizing customer relationship management.''')










x=joblib.load("./models/credit_model.joblib")




st.subheader("Calculate Score",anchor="sh3")
default_value=st.radio("select options",options=["nothing","check score","Ramesh","Suresh"],horizontal=True)
st.markdown(
    """

    <style>
        div[role=radiogroup] label:first-of-type{
            visibility:hidden;
            width:0px;
            height:0px;

        
        }
    </style>
""",unsafe_allow_html=True

)





def ex(s):

    with st.expander("Info"):

        st.write(s)





def gauge_chart (value:int):
    import plotly.graph_objects as go

    if value>=300 and value<450:
        colour = 'red'

    elif value>=450 and value<600:
        colour = 'orange'

    elif value>=600 and value<750:
        colour = 'yellow'

    elif value>=750 and value<=900:
        colour = 'green'
        

    else:
        colour = 'black'

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Credit Score", 'font': {'size': 24}},
        #delta = {'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
        gauge = {
            'axis': {'range': [300, 900], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': colour, 'thickness' : 1},
            'borderwidth': 0,
            'bordercolor': "gray",
            
            'steps': [
                {'range': [300, 900], 'color': 'grey'},
                ],
            }))
    
    
   
    st.plotly_chart(fig)
















if default_value=="Suresh":


    t1=pd.DataFrame([{"Annual_Income":11646,
                "Num_Bank_Accounts":6,
                "Num_Credit_Card" :3,
                "Interest_Rate":14,
                "Num_of_Loan":2,
                "Delay_from_due_date":14,
                "Num_of_Delayed_Payment":18,
                "Changed_Credit_Limit":9.33,
                "Num_Credit_Inquiries":6,
                "Outstanding_Debt":847.88,
                "Total_EMI_per_month":10.050598,
                "Credit_History_Age_Months":223,
                "Credit_Mix_Encoded":1,
                "Total_Num_Accounts":9,
                "Debt_Per_Account":94.208889,
                "Debt_to_Income_Ratio":0.072803,
                "Delayed_Payments_Per_Account":2.000000}])

    y_pred=x.predict(t1)
    y=int(300*(y_pred[0]+1))
    st.metric('**your score is**',int(300*(y_pred[0]+1)))


    if y>=300 and y<=500:
        st.html('<h2>you have poor score</h2>')

    elif y>=500 and y<=750:
        st.html('<h2>you have standard score</h2>')

    else:
        st.html('<h2>you have good score</h2>')


    st.write(t1)


    gauge_chart (y);



    




        

        




elif default_value=="Ramesh":


    t2=pd.DataFrame([{"Annual_Income":115023.36,
                "Num_Bank_Accounts":3,
                "Num_Credit_Card" :4,
                "Interest_Rate":1,
                "Num_of_Loan":2,
                "Delay_from_due_date":10,
                "Num_of_Delayed_Payment":4,
                "Changed_Credit_Limit":0.87,
                "Num_Credit_Inquiries":7,
                "Outstanding_Debt":1143.52,
                "Total_EMI_per_month":108.41342,
                "Credit_History_Age_Months":256,
                "Credit_Mix_Encoded":2,
                "Total_Num_Accounts":7,
                "Debt_Per_Account":163.36,
                "Debt_to_Income_Ratio":0.00114163,
                "Delayed_Payments_Per_Account":0.571428}])

    y_pred=x.predict(t2)

    y=int(300*(y_pred[0]+1))

    st.metric('**your score is**',int(300*(y_pred[0]+1)))


    if y>=300 and y<=500:
        st.html('<h2>you have poor score</h2>')

    elif y>=500 and y<=750:
        st.html('<h2>you have standard score</h2>')

    else:
        st.html('<h2>you have good score</h2>')

    st.write(t2)

    gauge_chart (y);
        

        


elif default_value=="check score":


    with st.form(key="credit_form"):
        

        Num_Bank_Accounts=st.slider('Number of Bank Accounts',min_value=0,max_value=20)
        Num_Credit_Card=st.slider('Number of Credit Card',min_value=0,max_value=20)
        Num_of_Loan=st.slider('Num of Loan ',min_value=0,max_value=15)
        Credit_Mix_Encoded=2
        Total_Num_Accounts=st.slider('Total Num Accounts',min_value=1,max_value=20)
        Changed_Credit_Limit=5
        Num_Credit_Inquiries=3
        




        col1,col2,col3=st.columns([3,3,3])

        with col1:
            Annual_Income= (col1.number_input('Annual Income', min_value=100000.00, max_value=3000000.00)*3)/80
            Total_EMI_per_month=(col1.number_input('Total EMI per Month', min_value=0.00, max_value=300000.00))/80
            Credit_History_Age_Months=col1.number_input('Credit History Age Months',min_value=0)
            ex('''
            The number of credit history months-The length of time that accounts have been open and actively used for credit purposes.
            ''');
            

        with col2:
            Interest_Rate=col2.number_input('Interest Rate',min_value=0.00,max_value=30.00)
            Delay_from_due_date=col2.number_input('Delay from Due Date',min_value=0,max_value=50)
            #Num_of_Delayed_Payment=col2.number_input('Num of Delayed Payment',min_value=0,max_value=50)
            ex('''
            The delay from the due date- The number of days beyond the specified due date that a payment or project submission is made.
            ''');
            



        with col3:
            Num_of_Delayed_Payment=col3.number_input('Num of Delayed Payment',min_value=0,max_value=50)
            #Changed_Credit_Limit=col3.number_input('Changed Credit Limit', min_value=0.00, max_value=30.00)
            #Num_Credit_Inquiries=col3.number_input('Num Credit Inquiries', min_value=0, max_value=30)
            Outstanding_Debt=(col3.number_input('Outstanding Debt', min_value=0.00, max_value=300000.00))/80
            ex('''
            Outstanding debt-The total amount of money that a person or entity owes to creditors or lenders, which has not yet been fully repaid.
            ''');

        
            
        Delayed_Payments_Per_Account=Num_of_Delayed_Payment/Total_Num_Accounts
        Debt_to_Income_Ratio=Outstanding_Debt/Annual_Income
        Debt_Per_Account=Outstanding_Debt/Total_Num_Accounts

        



        sub=st.form_submit_button('submit')

        if sub:

            output=pd.DataFrame([{"Annual_Income":Annual_Income,
                "Num_Bank_Accounts":Num_Bank_Accounts,
                "Num_Credit_Card" :Num_Credit_Card,
                "Interest_Rate":Interest_Rate,
                "Num_of_Loan":Num_of_Loan,
                "Delay_from_due_date":Delay_from_due_date,
                "Num_of_Delayed_Payment":Num_of_Delayed_Payment,
                "Changed_Credit_Limit":Changed_Credit_Limit,
                "Num_Credit_Inquiries":Num_Credit_Inquiries,
                "Outstanding_Debt":Outstanding_Debt,
                "Total_EMI_per_month":Total_EMI_per_month,
                "Credit_History_Age_Months":Credit_History_Age_Months,
                "Credit_Mix_Encoded":Credit_Mix_Encoded,
                "Total_Num_Accounts":Total_Num_Accounts,
                "Debt_Per_Account":Debt_Per_Account,
                "Debt_to_Income_Ratio":Debt_to_Income_Ratio,
                "Delayed_Payments_Per_Account":Delayed_Payments_Per_Account}])
        
        
    
            

            y_pred=x.predict(output)

            

            y=int(300*(y_pred[0]+1))

            output['Credit_Score']=[y]

            st.metric('*your score is*',int(300*(y_pred[0]+1)))


            if y>=300 and y<=500:
                st.html('<h2>you have poor score</h2>')

            elif y>=500 and y<=750:
                st.html('<h2>you have standard score</h2>')

            else:
                st.html('<h2>you have good score</h2>')
 


            #updated_data=pd.concat([ex_data1,output],ignore_index=True)

            #st.write(updated_data)

            gauge_chart (y);

            #st.session_state['existing_data']=updated_data


            #conn.update(worksheet="credit data",data=updated_data)




st.subheader("Created By:",anchor='au')


st.html("<h5>Harshith HS (21CS034)</h5><h5>Jinuth Gowda BC(21CS040)</h5>")

    




        








