
import pandas as pd
import streamlit as st
import plotly.express as px
import joblib 
from sklearn.cluster import KMeans




x=joblib.load("./models/credit_model.joblib")

st.title('credit segmentation')
with st.sidebar:


    st.markdown("[How Credit Segmentation Works?](#hh1)",unsafe_allow_html=True)

    st.markdown("[what is kmeans?](#shh1)",unsafe_allow_html=True)

    st.markdown("[what is random forest](#shh3)",unsafe_allow_html=True)

    st.markdown("[Calculate Score](#shh2)",unsafe_allow_html=True)
    

    st.html("<h4>Created By</h4>")
    st.html("<h5>Harshith HS (21CS040)</h5><h5>Jinuth Gowda BC(21CS040)</h5>")
    


st.header('How Credit Segmentation Works?',anchor='hh1')

st.write('''Segmentation in the context of data analysis or marketing involves dividing a heterogeneous population into smaller, more homogeneous groups based on shared characteristics or behaviors. This process aims to understand different segments' needs and preferences more effectively, enabling targeted strategies or interventions tailored to each group's specific attributes.''')


st.subheader("what is kmeans?",anchor='shh1')
st.write('''K-means segmentation partitions data into k clusters based on similarities in attributes like credit scores. It begins by randomly initializing  k  centroids, assigning each data point to the nearest centroid, then refining centroids based on mean values of assigned points. This iterative process minimizes intra-cluster variance until centroids stabilize. The outcome assigns each individual to a cluster representing similar creditworthiness, aiding in targeted financial strategies and risk assessment.''')

st.subheader("what is random forest?",anchor='shh3')
st.write('''Random Forest Regression works by training multiple decision trees on different random subsets of the data and averaging their predictions. Each tree is constructed by selecting random subsets of features at each split, reducing correlation between individual trees and improving generalization. During prediction, the ensemble of trees collectively predicts the output by averaging or taking the majority vote. This method is effective in handling complex relationships in data, reducing overfitting compared to individual decision trees, and providing robust predictions.''')






st.subheader("Calculate Score",anchor="shh2")
default_value=st.radio(label="select options",options=["external file","internal file"],horizontal=True)



st.write(default_value)

if default_value=='internal file':
    
    #ex_data=ex_data1.dropna(how="all")
    data=pd.read_csv("credit data.csv")

    
    if True:
       

    
        st.write(data.head())

        pr=st.button("submit")

        if pr:
        

        # Calculate credit scores using the complete FICO formula
            # credit_scores = []

            # for index, row in data.iterrows():
            
            #     Annual_Income=row["Annual_Income"]
            #     Num_Bank_Accounts=row["Num_Bank_Accounts"]
            #     Num_Credit_Card=row["Num_Credit_Card"]
            #     Interest_Rate=row["Interest_Rate"]
            #     Num_of_Loan=row["Num_of_Loan"]
            #     Delay_from_due_date=row["Delay_from_due_date"]
            #     Num_of_Delayed_Payment=row["Num_of_Delayed_Payment"]
            #     Changed_Credit_Limit=row["Changed_Credit_Limit"]
            #     Num_Credit_Inquiries=row["Num_Credit_Inquiries"]
            #     Outstanding_Debt=row["Outstanding_Debt"]
            #     Total_EMI_per_month=row["Total_EMI_per_month"]
            #     Credit_History_Age_Months=row["Credit_History_Age_Months"]
            #     Credit_Mix_Encoded=row["Credit_Mix_Encoded"]
            #     Total_Num_Accounts=row["Total_Num_Accounts"]
            #     Debt_Per_Account=row["Debt_Per_Account"]
            #     Debt_to_Income_Ratio=row["Debt_to_Income_Ratio"]
            #     Delayed_Payments_Per_Account=row["Delayed_Payments_Per_Account"]
                
            #     output=pd.DataFrame([{"Annual_Income":Annual_Income,
            #         "Num_Bank_Accounts":Num_Bank_Accounts,
            #         "Num_Credit_Card" :Num_Credit_Card,
            #         "Interest_Rate":Interest_Rate,
            #         "Num_of_Loan":Num_of_Loan,
            #         "Delay_from_due_date":Delay_from_due_date,
            #         "Num_of_Delayed_Payment":Num_of_Delayed_Payment,
            #         "Changed_Credit_Limit":Changed_Credit_Limit,
            #         "Num_Credit_Inquiries":Num_Credit_Inquiries,
            #         "Outstanding_Debt":Outstanding_Debt,
            #         "Total_EMI_per_month":Total_EMI_per_month,
            #         "Credit_History_Age_Months":Credit_History_Age_Months,
            #         "Credit_Mix_Encoded":Credit_Mix_Encoded,
            #         "Total_Num_Accounts":Total_Num_Accounts,
            #         "Debt_Per_Account":Debt_Per_Account,
            #         "Debt_to_Income_Ratio":Debt_to_Income_Ratio,
            #         "Delayed_Payments_Per_Account":Delayed_Payments_Per_Account}])


            #     # Apply the FICO formula to calculate the credit score
            #     y_pred=x.predict(output)
                
            #     credit_scores.append(300*(y_pred[0]+1))

            # # Add the credit scores as a new column to the DataFrame
            
            # data['CS'] = credit_scores
            st.write(data)

            X_test=data
            kmeans=KMeans(n_clusters=4,n_init=10,random_state=42)
            x=X_test[['Credit_Score']]
            k_p=kmeans.fit_predict(x)
            X_test['cluster']=k_p
            X_test['cluster']=X_test['cluster'].map({1: 'Very Low', 
                                       0: 'Low',
                                       3: "Good",
                                        2: 'Excellent'})

#Visualize the segments using Plotly
            fig = px.scatter(X_test, x=X_test.index, y='Credit_Score', color='cluster',
                color_discrete_sequence=['green', 'blue', 'yellow', 'red'])
            fig.update_layout(
                xaxis_title='Customer Index',
                yaxis_title='Credit Score',
                title='Customer Segmentation based on Credit Scores'
            )
            st.plotly_chart(fig)


            st.download_button("download",
                               data.to_csv(),
                               mime='text/csv'
                               )

elif default_value=='external file':

    
    df=st.file_uploader(label="enter csv file:",type=['csv','xlsx'])

    if df:
        try:
            data=pd.read_csv(df)
        except Exception as e:
            data=pd.read_excel(df)

    
        st.write(data.head())

        pr=st.button("submit")

        if pr:
        

            # Calculate credit scores using the complete FICO formula
            credit_scores = []

            for index, row in data.iterrows():
            
                Annual_Income=row["Annual_Income"]
                Num_Bank_Accounts=row["Num_Bank_Accounts"]
                Num_Credit_Card=row["Num_Credit_Card"]
                Interest_Rate=row["Interest_Rate"]
                Num_of_Loan=row["Num_of_Loan"]
                Delay_from_due_date=row["Delay_from_due_date"]
                Num_of_Delayed_Payment=row["Num_of_Delayed_Payment"]
                Changed_Credit_Limit=row["Changed_Credit_Limit"]
                Num_Credit_Inquiries=row["Num_Credit_Inquiries"]
                Outstanding_Debt=row["Outstanding_Debt"]
                Total_EMI_per_month=row["Total_EMI_per_month"]
                Credit_History_Age_Months=row["Credit_History_Age_Months"]
                Credit_Mix_Encoded=row["Credit_Mix_Encoded"]
                Total_Num_Accounts=row["Total_Num_Accounts"]
                Debt_Per_Account=row["Debt_Per_Account"]
                Debt_to_Income_Ratio=row["Debt_to_Income_Ratio"]
                Delayed_Payments_Per_Account=row["Delayed_Payments_Per_Account"]

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


                # Apply the FICO formula to calculate the credit score
                y_pred=x.predict(output)
                credit_scores.append(300*(y_pred[0]+1))
                

            # Add the credit scores as a new column to the DataFrame
            data['Credit_Score'] = credit_scores
            st.write(data)

            X_test=data
            kmeans=KMeans(n_clusters=4,n_init=10,random_state=42)
            x=X_test[['Credit_Score']]
            k_p=kmeans.fit_predict(x)
            X_test['cluster']=k_p
            X_test['cluster']=X_test['cluster'].map({1: 'Very Low', 
                                       0: 'Low',
                                       3: "Good",
                                        2: 'Excellent'})

#Visualize the segments using Plotly
            fig = px.scatter(X_test, x=X_test.index, y='Credit_Score', color='cluster',
                color_discrete_sequence=['green', 'blue', 'yellow', 'red'])
            fig.update_layout(
                xaxis_title='Customer Index',
                yaxis_title='Credit Score',
                title='Customer Segmentation based on Credit Scores'
            )
            st.plotly_chart(fig)
            st.download_button("download",
                               data.to_csv(),
                               mime='text/csv'
                               )









    




