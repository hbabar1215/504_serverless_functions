# Multi‑Cloud Serverless Function (HbA1c Levels)
The purpose of this assignment is to implement the same HTTP serverless function in two clouds. Our function will accept JSON input values describing HbA1c levels. Given an input, a binary classifier (abnormal or normal) will be produced in **Google Cloud Platform and Azure**. 

### Lab Rules
The American with Disabilities Act (ADA) has recently recommended HbA1c with a cut-point ≥6.5% for diagnosing diabetes. 
- Therefore, lab values with a HbA1c level **greater than or equal to 6.5** will have an `abnormal test result` and a diagnosis of `diabetes`. 
- Lab values **less than 6.5** will have a `normal test result`. 
- Source: Sherwani, S. I., Khan, H. A., Ekhzaimy, A., Masood, A., & Sakharkar, M. K. (2016). Significance of HbA1c Test in Diagnosis and Prognosis of Diabetic Patients. Biomarker insights, 11, 95–104. https://doi.org/10.4137/BMI.S38440 

## Google Cloud
- **Name**: hba1c-test-504
- **Region**: us-central1 
- **Base image**: Python 3.13 (Ubuntu 22)
- **Authentication**: Allow public access
- **Networking**: All (Allow direct access to your service from the internet)
