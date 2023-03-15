#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import streamlit as st
import pickle


# In[ ]:


#loading the saved model
load_model=pickle.load(open('/home/saurabh/trained_model.sav','rb'))


# In[ ]:


#creating function for predection
def weekely_sales_predict(input_data):
#     input_data=(45,0,9,2,118221,50,3.046,10000,10000,10000,10000,5,4,2012,15)
    #changing input data into numpy array
    np_array=np.asarray(input_data)
    #reshape array as we are predecting for one instance
    input_reshaped=np_array.reshape(1,-1)
    predict=loaded_model.predict(input_reshaped)
    return predict
def main():
    #giving title 
    st.title("WEEKELY SALES PREDECTION WEB APP")
    
    
    #getting input data from user
    store_number=st.text_input("which store do you want")
    holiday_status=st.text_input("status of weekely holiday")
    department_no=st.text_input("which department(1-98)")
    type_department=st.text_input("which type of department(1/2/3)")
    size_department=st.text_input("sq.ft size of your department")
    temprature_weekely_average =st.text_input("temperature")
    fuel_price_dollars=st.text_input("fuel_price")
    markdown1=st.text_input("offer1")
    markdown2=st.text_input("offer2")
    markdown3=st.text_input("offer3")
    markdown4=st.text_input("offer4")
    dayofweek=st.text_input("which day of week")
    month=st.text_input("which month")
    year=st.text_input("which year")
    date_day=st.text_input("which day_date")
    
    #code for predection
    sales= ''
    
    #creating button for predection
    
    if st.button("sales predection result"):
        sales=weekely_sales_predict([store_number,holiday_status,department_no,type_department,size_department,temprature_weekely_average ,fuel_price_dollars,markdown1,markdown2,markdown3,markdown4,dayofweek,month,year,date_day])
    
    
    st.success(sales)

    
    
if __name__ == '__main__':
    main()

