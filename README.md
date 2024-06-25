# Python CRUD Application for Data Pasien
A comprehensive Python application for managing patient data with Create, Read, Update, and Delete (CRUD) operations.
## Business Understanding
This project caters to healthcare industry, specifically addressing the need to manage patient data efficiently. This application provides a robust solution for efficient data management and data validation and error checking with an user-friendly interface.

Benefits:
1) Efficient Data Management : Streamlines the process of storing (create), retrieving (read), updating (update), and deleting (delete) patient data.
2) User-Friendly Interface : Simple and intuitive interface for healthcare professionals to use.
3) Data Validation and Error-Checking: Implements features for data validation and error-checking to minimize human errors case during data input.

Target Users:
This application is designed for healthcare's administration representative to manage latest patients data.

## Features
1) Create
   -) Add new patient data entries to the data pasien application, which specifies NIK, Name, Gender, Birthdate, Phone Number, and Address
   -) Implement validations rules to ensure data consistency and accuracy (e.g. NIK must be 16 digit) 
2) Read
   -) Search & retrieve specific product information by NIK and Phone Contact
   -) Display comprehensive patien data detail in a user-friendly format
3) Update
   -) Modify existing patient data to apply changes (exclude NIK)
   -) Provide clear information or error messages for any update (either success or fail)
4) Delete
   -) Provide data removal optional with a specific key only (NIK) and a verification for data removal

# Installation
1) Prerequisites: Python version 3.7 or later

# Usage
1) Run the application : python.capstone.py
2) CRUD Operations :
   a) Create : Add new data patient to program (NIK, Name, Gender, Birthdate, Phone Number, Address)
   b) Read   : Display all patient data or specific patient data (by NIK or Phone Number)
   c) Update : Modify all patient data (Exclude NIK)
   d) Delete : Remove specific patient data by NIK
# Data Model
This project uses dictionary data to store patient data in list data. The following data keys are containing:
1) NIK (Integer, Primary Key) : Unique Identifier for each patient
2) Nama (Char) : Name of patient
3) Gender (Char) : Gender of patient
4) Birthdate (Integer) : Birthdate of patient
5) Phone Number (Integer) : Phone Number of patient
6) Address (Varchar) : Address of patient

