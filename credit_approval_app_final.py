import streamlit as st
import pandas as pd
import pickle

header = st.container()
features = st.container()
model = st.container()
  
#collecting user input
def user_input():
    col_1, col_2 = st.columns(2)
    debt = col_1.slider('How much Debt?', min_value=0.0, max_value=100.0)
    yearsEmployed = col_1.slider('Years of employment', min_value=0.0, max_value=100.0)
    priorDefault = col_2.selectbox('Prior default? True=1, False=0', options=[0,1], index=0)
    employed = col_2.selectbox('Employment status. True=1, False=0', options=[0,1], index=0)
    income = col_1.slider('Total income per year', min_value=10, max_value=100000)
    creditScore = col_2.slider("Customer's credit score", min_value=0, max_value=100)

    data = {'Debt': debt, 'YearsEmployed': yearsEmployed, 'PriorDefault': priorDefault, 'Employed': employed,'CreditScore': creditScore,'Income': income,}
    features = pd.DataFrame(data, index=[0])
    return features

with header:
    st.title("""
    Credit Approval Prediction App
    **This app predicts the approval status of credit card request**
    """)
    

with features:
    st.header('Features Input')
    st.write('Please input features')
    df = user_input()
    st.write("User Input Parameters")
    st.write(df)
    


with model:
    #loading saved model
    
    filename = "creditApproval_model2.sav"
    logreg3 = pickle.load(open(filename, 'rb'))

    def prediction():
        prediction = logreg3.predict(df)
        result = ''
        if prediction == 1:
            result = 'Approved'
        else:
            result = 'Rejected'
        return result
    #prediction button
    if st.button("Predict"): 
        result = prediction()
        st.success('Your request is {}'.format(result))
        