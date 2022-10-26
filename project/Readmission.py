from datetime import datetime
from unicodedata import numeric
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
import datetime
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title='Diabetic Hospital Readmission',page_icon="🚑")
st.header("Prediction of Early hospital Re-admissions")

selected = option_menu(menu_title=None,options=["Prediction","Project","Diabetes info"],
icons=["house","book","envelope"],menu_icon="cast",default_index=0,
orientation='horizontal',
styles={
            "container": {"padding": "0!important", "background-color": "#DCE9FA","font-color":"#000"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#3399CC",
            "--hover-font-color": "white"},"nav-link-selected": {"background-color": "green"}})
if selected == "Prediction":
    features = dict()
    numerical = dict()
    numerical_df = pd.DataFrame(columns=['time_in_hospital', 'num_lab_procedures', 'num_procedures','num_medications', 
    'number_outpatient', 'number_emergency',
    'number_inpatient', 'number_diagnoses','Health_index','severity_of_disease'])

    st.markdown("##### Patient Information")
    dob1,dob2,dob3 = st.columns(3)
    with dob1:
        year = st.selectbox("Year",list(range(1900,2023)))
    with dob2:  
        month = st.selectbox("Month",['January','February','March','April','May','June','July','August','September','October','November','December'])
    with dob3: 
        if month == 'February':
            day = st.selectbox("Day",list(range(1,30)))
        elif month in ['April','June','September','November']:
            day = st.selectbox("Day",list(range(1,31)))
        else:
            day = st.selectbox("Day",list(range(1,32)))
    dob = str(dob1)+ str(dob2) + str(dob3)

    w,A = st.columns(2)
    with w:
        weight = st.number_input("weight",min_value=30,max_value=150,value=40,key='wt')
    with A:    
        Age = st.selectbox("Age",['0-10','10-20','20-30','30-40','40-50','50-60','60-70', '70-80', '80-90', '90-100'])    
        Age = "["+ Age +")"
        features['age'] = Age

    col1,col2,col3 = st.columns(3)
    with col1:
        unit = st.selectbox("Unit of weight",['Kilograms','Pounds'])
    with col2:
        gender = st.selectbox("gender",['Male','Female'])
        features['gender'] = gender
    with col3:
        race = st.selectbox("Race",['Caucasian', 'AfricanAmerican', 'Asian', 'Hispanic','Other'])
        features['race'] = race  

    admission_title = '<p style="font-family:sans-serif; color:Green; font-size: 25px;">Admission & discharge Information of patient</p>'
    st.markdown(admission_title,unsafe_allow_html=True)  
    # st.markdown("##### Admission & discharge Information")

    col4,col5,col6 = st.columns(3)
    with col4:
        Admission_source = st.selectbox("Source of Admission",['Referral','Emergency','other'])
        features['admission_source_id'] = Admission_source
    with col5:
        Admission_type = st.selectbox("Type of Admission",['Emergency','Urgent','Elective','others','No mention'])
        features['admission_type_id'] = Admission_type
    with col6:
        Discharge = st.selectbox("Type of Discharge",['Discharge','Transfer','Other'])
        features['discharge_disposition_id'] = Discharge

    col7,col8,col9 = st.columns(3)
    with col7:
        num_inpatient = st.number_input("Number of prior Inpatient admissions",min_value=0,value=0,key='num_inp')
        features['number_inpatient'] = num_inpatient
        numerical['number_inpatient'] = num_inpatient
    with col8:
        num_outpatient = st.number_input("Number of prior Outpatient visits",min_value=0,value=0,key='num_outp')
        features['number_outpatient'] = num_outpatient
        numerical['number_outpatient'] = num_outpatient
    with col9:
        num_emergency = st.number_input("Number of prior Emergency visits",min_value=0,value=0,key='num_emer')
        features['number_emergency'] = num_emergency
        numerical['number_emergency'] = num_emergency
    test_title = '<p style="font-family:sans-serif; color:Green; font-size: 25px;">Glucose Monitering Tests</p>'
    st.markdown(test_title,unsafe_allow_html=True)     
    # st.markdown("##### Glucose monitering tests")

    col10,col11= st.columns(2)
    with col10:
        HBA1c = st.selectbox("HBA1c test results",['No test done', 'greater than 7.0', 'greater than 8.0', 'Normal result'])
        if HBA1c == 'No test done':
            HBA1c = 'None'
        if HBA1c == 'Normal result':
            HBA1c = 'Norm'
        if HBA1c == 'greater than 7.0':
            HBA1c = '>7'
        if HBA1c == 'greater than 8.0':
            HBA1c = '>8'
        features['A1Cresult'] = HBA1c

    with col11:
        Serum_test = st.selectbox("Glucose serum test results",['No test done', 'greater than 300', 'Normal result','greater than 200'])
        if Serum_test == 'No test done':
            Serum_test = 'None'
        if Serum_test == 'Normal result':
            Serum_test = 'Norm'
        if Serum_test == 'greater than 300':
            Serum_test = '>300'
        if Serum_test == 'greater than 200':
            Serum_test = '>200'
        features['max_glu_serum'] = Serum_test


    diag_title = '<p style="font-family:sans-serif; color:Green; font-size: 25px;">Diagnoses and procedures</p>'
    st.markdown(diag_title,unsafe_allow_html=True)    

    # st.markdown("##### Diagnoses and procedures")

    col12,col13,col14 = st.columns(3)
    with col12:
        prim_diag = st.selectbox("Primary Diagnosis",['Diabetes', 'Neoplasms', 'circulatory', 'Respiratory','Injury', 'Musculoskeletal', 'Digestive', 'Genitourinary','other'])
        features['diagnosis_1'] = prim_diag
    with col13:
        sec_diag = st.selectbox("Secondary Diagnosis",['Diabetes', 'Neoplasms', 'circulatory', 'Respiratory','Injury', 'Musculoskeletal', 'Digestive', 'Genitourinary','other'])
        features['diagnosis_2'] = sec_diag
    with col14:
        add_sec_diag = st.selectbox("Additional secondary Diagnosis",['Diabetes', 'Neoplasms', 'circulatory', 'Respiratory','Injury', 'Musculoskeletal', 'Digestive', 'Genitourinary','other'])
        features['diagnosis_3'] = add_sec_diag

    col15,col16 = st.columns(2) 
    with col15:
        num_lab_proc = st.number_input("Number of lab procedures",min_value=0,value=0,key='number0')
        features['num_lab_procedures'] = num_lab_proc
        numerical['num_lab_procedures'] = num_lab_proc
    with col16:
        num_proc = st.number_input("Number of procedures other than lab procedures",min_value=0,value=0)
        features['num_procedures'] = num_proc
        numerical['num_procedures'] = num_proc
    col17,col18,col19 = st.columns(3) 
    with col17:
        hosp_time = st.number_input("Time spent in hospital in days",min_value=0,value=0,key='number2')
        features['time_in_hospital'] = hosp_time
        numerical['time_in_hospital'] = hosp_time
    with col18:
        num_med = st.number_input("Number of Medications (total)",min_value=0,value=0,key='number3')
        features['num_medications'] = num_med
        numerical['num_medications'] = num_med
    with col19:
        num_diag = st.number_input("Number of Diagnosis",min_value=0,value=0,key='number5')
        features['number_diagnoses'] = num_diag
        numerical['number_diagnoses'] = num_diag

    medication_title = '<p style="font-family:sans-serif; color:#E158C6; font-size: 25px;">Diabetic Medication and Dosage</p>'
    st.markdown(medication_title,unsafe_allow_html=True)

    features_medicine = ['metformin','insulin','repaglinide','nateglinide','chlorpropamide','glimepiride','glipizide','glyburide','tolbutamide','pioglitazone','rosiglitazone', 'acarbose', 'miglitol','tolazamide','glyburide-metformin', 'glipizide-metformin']
    Medication = st.multiselect("Medication",features_medicine)

    features_med_dict = dict()
    features_med_dict = features_med_dict.fromkeys(features_medicine)

    for index,med in enumerate(Medication):
        category = st.selectbox(f"Dosage of {med}",['No','Down','Steady','Up'])
        features_med_dict[med] = category
        features[med] = category

    col20,col21 = st.columns(2) 
    with col20:
        change_diabetes_med = st.selectbox("Change of Diabetic medication",['No change', 'Change'])
        change_diabetes_med = 'Ch' if change_diabetes_med == 'Change' else 'No'
        features['change'] = change_diabetes_med
    with col21:
        diab_med = st.selectbox("Taking diabetes medication ?",['No', 'Yes'])
        features['diabetesMed'] = diab_med

    for medicine in features_med_dict:
        if medicine not in features:
            features[medicine]='No'
        else:
            continue

    hospital_data = (numerical['number_outpatient'] + numerical['number_emergency'] + numerical['number_inpatient'])
    severity = (numerical['time_in_hospital'] + numerical['num_lab_procedures'] + numerical['num_procedures'] + numerical['num_medications'] + numerical['number_diagnoses'])
 
    numerical_df = numerical_df.append(numerical,ignore_index=True)
    numerical_df['Health_index'] = hospital_data
    numerical_df['severity_of_disease'] = severity

    with open('./serialization/scalar.pickle','rb') as scale:
        scaling = pickle.load(scale)
    with open('./serialization/Numeric_model.pickle','rb') as model:
        Model = pickle.load(model)

    data = scaling.transform(numerical_df)   
    # prediction = Model.predict(data)

    st.dataframe(numerical_df)

    # st.write(data)








