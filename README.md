# Prediction of Hospital readmission of Diabetic patients & Imporatance of HBA1c test

## Business problem statement (GOALS)

### Business Problem Understanding

Hospitals engaging in any model are likely to face penalties if their providers cannot improve hospital readmission rates. To combat growing costs, payers across the industry are adding hospital readmission quality measures to their value-based reimbursement programs. In recent years, government agencies and healthcare systems are increasingly focused on 30-day readmission rates as a way to improve quality and also determine the complexity of patient populations.
To avoid value-based penalties (disincentives), Hospitals should reduce readmission rates by identifying the Diabetic patients who are having high probability of early re-admission compared to other patients who do not have Diabetes.

### Business Objective

The main objective of our work is to come up with the predictive model which helps Hospital Management systems to predict the risk of early readmission of patients who are having Diabetes Mellitus which can further address to escape value based penalty and better patient care.

- The need for glucose level monitoring like HBA1c test to detect in early stages.
- Proper medication and care for diabetic patients
- Better patient engagement, Transitional care & close post-discharge follow-up with the intention of reducing early readmission

### Scope of the project 

As cost of inpatient care & readmission rates are higher in patients with diabetes Mellitus (DM) compared to other diagnosis. So, it makes perfect sense for the hospital management that, focusing on reducing cost of readmission in case of Diabetic patients to avoid value-based penalties from the government. 

### Limitations of project

-	Our model is not capable of accounting the factors such as socio-economic characteristics of patient, 
- With most efforts focused on reducing readmissions, there is a potential to overlook the stress and vulnerability of patients.

## Data dictionary

| Attribute         |    type       |                       Information                                 |
| ----------------- | ------------- |------------------------------------------------------------------ |
| Encounter ID | Numeric  | Unique identifier of an encounter  |
| Patient number | Numeric  | Unique identifier of a patient  |
| Race | Nominal  | Values: Caucasian, Asian, African American, Hispanic, and other  |
| Gender | Nominal  | Values: male, female, and unknown/invalid  | 
| Age | Nominal  | Grouped in 10-year intervals: (0, 10), (10, 20), ..., (90, 100) |
| Weight | Numeric  | Weight in pounds.  |
| Admission type | Nominal  | 'Integer identifier corresponding to 9 distinct values, |
| | |                for example, emergency,urgent, elective, newborn, and not available. |
| Discharge disposition | Nominal  | 'Integer identifier corresponding to 29 distinct values, |
| | | for example, discharged to home, expired, and not available. |
| Admission source | Nominal  | 'Integer identifier corresponding to 21 distinct values,|
| |  | for example, physician referral, emergency room, and transfer from a hospital.|
| Time in hospital | Numeric  | 'Integer number of days between admission and discharge. |
| Payer code | Nominal  | 'Integer identifier corresponding to 17 distinct values, for example, |
| | | Blue Cross\\Blue, Shield, Medicare, and self-pay. |
| Medical specialty | Nominal  | Integer identifier of a specialty of the admitting physician, corresponding to 84 distinct values, |
| | |for example, cardiology, internal medicine, family\\general practice, and surgeon. |
| Number of lab procedures | Numeric  | Number of lab tests performed during the encounter. |
| Number of procedures | Numeric  | Number of procedures (other than lab tests) performed during the encounter. |
| Number of medications | Numeric  | Number of distinct generic names administered during the encounter. |
| Number of outpatient visits | Numeric  | 'Number of outpatient visits of the patient in the year preceding the encounter. |
| Number of emergency visits | Numeric  | 'Number of emergency visits of the patient in the year preceding the encounter. |
| Number of inpatient visits | Numeric  | Number of inpatient visits of the patient in the year preceding the encounter. |
| Diagnosis 1 | Nominal  | The primary diagnosis (coded as first three digits of ICD9); 848 distinct values. |
| Diagnosis 2 | Nominal  | Secondary diagnosis (coded as first three digits of ICD9); 923 distinct values. |
| Diagnosis 3 | Nominal  | Additional secondary diagnosis (coded as first three digits of ICD9); 954 distinct values. |
| Number of diagnoses | Numeric  | Number of diagnoses entered to the system. |
| Glucose serum test result | Nominal  | Indicates the range of the result or if the test was not taken. |
| | | Values: “>200,” “>300,”“normal,” and “none” if not measured. |
| A1c test result | Nominal  | Indicates the range of the result or if the test was not taken. |
| | | Values: “>8” if the result was greater than 8% | 
| | | “>7” if the result was greater than 7% but less than 8% | 
| | | “normal” if the result was less than 7%, and |
| | | “none” if not measured. |
| Change of medications | Nominal  | 'Indicates if there was a change in diabetic medications (either dosage or generic name). |
| | | Values: “change” and “no change”. |
| 23 features for medications | Nominal  | 'For the generic names: metformin, repaglinide, nateglinide, chlorpropamide,glimepiride, acetohexamide,|
| | | glipizide, glyburide, tolbutamide, pioglitazone, rosiglitazone, acarbose, miglitol, |
| | | troglitazone, tolazamide, examide, sitagliptin, insulin, glyburide-metformin, glipizide-metformin, |
| | | glimepiride-pioglitazone, metformin-rosiglitazone, and metformin-pioglitazone, |
| | | the feature indicates whether  the drug was prescribed or there was a change in the dosage. |
| | | Values: “up” if the dosage was increased during the encounter, | 
| | | “down” if the dosage was decreased, |
| | | “steady” if the dosage did not change, | 
| | | and “no” if the drug was not prescribed. |
| Diabetes medications | Nominal |'Indicates if there was any diabetic medication prescribed. Values: “yes” and “no”. |
| Readmitted | Nominal  | Days to inpatient readmission. |
| | | Values: “<30” if the patient was readmitted in less than 30 days,|
| | | “>30” if the patient was readmitted in more than 30 days,|
| | | and “No” for no record of readmission. |

## Missing values

| Attribute	| Data_type |	Total_Entries	| Null_values	| Percent_Null_values |	Unique_values |
| --------- | --------- | --------------| ----------- | ------------------- | ------------- | 
| weight | object | 101766 | 98569 | 96.86 | 9 |
| medical_specialty | object | 101766 | 49949 | 49.08 | 72 |
| payer_code | object | 101766 | 40256 | 39.56 | 17 |
| race | object | 101766 | 2273 | 2.23 | 5 |
| Diagnosis1 | object | 101766 | 21 | 0.02 | 716 |
| Diagnosis2 | object | 101766 | 358 | 0.35 | 748 |
| Diagnosis3 | object | 101766 | 1423 | 1.40 | 789 |

## Exploratory Data Analysis

| *Readmission status*           |  *Redifining the objective (Binary classification)*
:-------------------------:|:-------------------------:
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/2.png)  |  ![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/3.png) 

| *Glucose Serum Test*           |  *HBA1c Test*
:-------------------------:|:-------------------------:
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/2.png)  |  ![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/3.png) 

| *HBA1c Diabetes level indicators*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/37.png)


| *Number of days a patient has spent his/her time in hospital during Treatment*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/11.png)

| *Top Medical speciality*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/13.png)

| *Number of Lab procedures*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/14.png)

| *Number of Lab procedures*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/15.png)

| *Number of Medications*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/18.png)

| *Number of Inpatient & Outpatient visits prior to present encounter*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/19.png)

| *Primary, Secondary & Additional Secondary diagnosis*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/22.png)

| *Number of Emergency visits prior to present encounter*           |  *Number of diagnosis entered into the system*
:-------------------------:|:-------------------------:
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/21-1.png)  |  ![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/26.png) 

| *Various Medications*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/31.png)

| *Medication change 'No' or 'change'*  |
|:-------------------------:|
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/33.png)

| *Diabetic Medication*           |  *Diabetic Medication with Target*
:-------------------------:|:-------------------------:
![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/47.png)  |  ![](https://github.com/Arvindhh931/Healthcare_Analyitics/blob/main/Visualizations/48.png) 

## Strategy for Imputation
- using patient_nbr attribute
   - Taking information from Some patients who have visited multiple times & not filled certain columns
- K-Nearest-Neighbour-imputer



