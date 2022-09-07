# Prediction of Hospital readmission of Diabetic patients & Imporatance of HBA1c test

## Business problem statement (GOALS)

### Business Problem Understanding

Hospitals engaging in any model are likely to face penalties if their providers cannot improve hospital readmission rates. To combat growing costs, payers across the industry are adding hospital readmission quality measures to their value-based reimbursement programs. In recent years, government agencies and healthcare systems are increasingly focused on 30-day readmission rates as a way to improve quality and also determine the complexity of patient populations.
To avoid value-based penalties (disincentives), Hospitals should reduce readmission rates by identifying the Diabetic patients who are having high probability of early re-admission compared to other patients who do not have Diabetes.

### Business Objective

The main objective of our work is to come up with the predictive model which helps Hospital Management systems to predict the risk of early readmission of patients who are having Diabetes Mellitus which can further address to escape value based penalty and better patient care.

- The need for glucose level monitoring like HBA1c test.
- Better patient engagement, Transitional care & close post-discharge follow-up with the intention of reducing early readmission

### Scope of the project 

As cost of inpatient care & readmission rates are higher in patients with diabetes Mellitus (DM) compared to other diagnosis. So, it makes perfect sense for the hospital management that, focusing on reducing cost of readmission in case of Diabetic patients to avoid value-based penalties from the government. 

### Limitations of project

-	Our model is not capable of accounting the factors such as socio-economic characteristics of patient, 
- With most efforts focused on reducing readmissions, there is a potential to overlook the stress and vulnerability of patients.

## Color Reference

| Attribute         |    type       |                       Information                                 |
| ----------------- | ------------- |------------------------------------------------------------------ |
| Encounter ID | Numeric  | Unique identifier of an encounter  |
| Patient number | Numeric  | Unique identifier of a patient  |
| Race | Nominal  | Values: Caucasian, Asian, African American, Hispanic, and other  |
| Gender | Nominal  | Values: male, female, and unknown/invalid  | 
| Age | Nominal  | Grouped in 10-year intervals: (0, 10), (10, 20), ..., (90, 100) |
| Weight | Numeric  | Weight in pounds.  |
| Admission type | Nominal  | 'Integer identifier corresponding to 9 distinct values, 
| | |                for example, emergency,urgent, elective, newborn, and not available. |
| Discharge disposition | Nominal  | 'Integer identifier corresponding to 29 distinct values, 
| | | for example, discharged to home, expired, and not available. |
| Admission source | Nominal  | 'Integer identifier corresponding to 21 distinct values,
| |  | for example, physician referral, emergency room, and transfer from a hospital.|
| Time in hospital | Numeric  | 'Integer number of days between admission and discharge. |
| Payer code | Nominal  | 'Integer identifier corresponding to 17 distinct values, for example, 
| | | Blue Cross\\Blue, Shield, Medicare, and self-pay. |

| Medical specialty | Nominal  | 
| Number of lab procedures | Numeric  | 
| Number of procedures | Numeric  | 
| Number of medications | Numeric  | 
| Number of outpatient visits | Numeric  | 
| Number of emergency visits | Numeric  | 
| Number of inpatient visits | Numeric  | 
| Diagnosis 1 | Nominal  | 
| Diagnosis 2 | Nominal  | 
| Diagnosis 3 | Nominal  | 
| Number of diagnoses | Numeric  | 
| Glucose serum test result | Nominal  | 
| A1c test result | Nominal  | 
| Change of medications | Nominal  | 
| Diabetes medications | Nominal  | 
| 23 features for medications | Nominal  | 
| Readmitted | Nominal  | 


