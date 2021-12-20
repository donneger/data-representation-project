# Data Representation Project 2021
Repository for GMIT Data Representation Project 2021

This repository holds the complete project data and program code for the DR Course Winter 2021.

## Summary
The purpose of this project is to create a web application in Flask using RESTful API's that links to a database table and allows for CRUD operations through a web page. 

I have created a gym class booking application that:
- Displays the list and details of class bookings for a fictitious gym, Gerrys Gym. 
- Allows for bookings to be created and classes and instructors to be selected for each booking. 
- Allows individual bookings to be seleced and any of the details updated.
- Allows for individual bookings to be deleted. 

All of these activities are interfaced to a bookings table on a mySQL database. 

### Page Screenshots

This is the main page of the booking system. 
![MainPage](/images/MainPageImage.png)

Create/Update Form
![CRUDPage](/images/Create_UpdatePageImage.png)

## Running the Program
The following steps should be carried out to extract and run the program.

1. Python, mySQL and FLASK must be installed on your machine. 
   - If Python requires installation the best way to install is by installiong Anaconda, this contains a full python installation and all of the libraries needed to run the code. Anaconda can be installed from following [Anaconda_Link](https://www.anaconda.com/distribution/), follow the site instructions to download and install. 
   - If needed install mySQL from the following [mySQL_Link](https://www.mysql.com/products/community/), follow thw site instructions to install. 
   - Use "pip install Flask" to install FLASK if not already installed. 

2. Download the complete project repository to your your machine. 
3. If you already have a database schema called ***datarepresentation*** on your machine this step can be skipped.
  -  Run the program pysqlcreatedb.py, this will create a schema in your mySQL instance called "datarepresentation"
4. To create the database table for the gym bookings details run the program pysqlcreatetable.py. This will create a table called gymbookings in the datarepresentation schema. 
5. 
