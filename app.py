import streamlit as st
import joblib as jb

st.set_option('deprecation.showPyplotGlobalUse', False)
#1 .Title and Subheader
# st.title('Data Analysis hey there')
# st.subheader('Data Analysis with Python')

def main():
   html_temp = """ 
    <div style ="background-color:lightblue;padding:10px"> 
    <h2 style ="color:black;text-align:center;">Health Insurance  Prediction ML App</h2> 
    </div> 
    """
   st.markdown(html_temp, unsafe_allow_html = True) 
   model = jb.load('health_prediction_model')
   age = st.number_input('Enter Your Age' , 18 , 100)
   gender = st.selectbox('Gender' , ('Male','Female'))
   if gender=='Male':
       p2=1
   else:
        p2=0
   Bmi = st.number_input('Enter your BMI Value')
   child= st.number_input('Enter Number Of Children' , 0 , 4)
   smoker =st.selectbox('Smoker',('Yes' , 'No'))
   if smoker=='Yes':
       p3=1
   else:
       p3=0
   Region = st.selectbox('Select Your Region',('southwest', 'southeast', 'northwest', 'northeast'))
   if Region=='southwest':
       p4=1
   elif Region=='southeast':
       p4=2
   elif Region=='northwest':
       p4=3
   else:
       p4=4
   if st.button('Predict'):
        pred=model.predict([[age,p2,Bmi,child,p3,p4]])
        st.success('Your Insurance Cost is ${}'.format(round(pred[0],2)))
# streamlit run Health_Insurance_app.py --global.dataFrameSerialization legacy



if __name__ =='__main__':
    main()


