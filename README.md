# Data Representation Project 2021
Repository for GMIT Data Representation Project 2021

This repository holds the complete project data and program code for the DR Course Winter 2021.

## 1. Summary
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

This is the Create/Update Form that is used for creating new bookings or updating existing bookings. 
![CRUDPage](/images/Create_UpdatePageImage.png)

## 2. Running the Program
The following steps should be carried out to extract and run the program.

1. Python, mySQL and FLASK must be installed on your machine. 
   - If Python requires installation the best way to install is by installiong Anaconda, this contains a full python installation and all of the libraries needed to run the code. Anaconda can be installed from following [Anaconda_Link](https://www.anaconda.com/distribution/), follow the site instructions to download and install. 
   - If needed install mySQL from the following [mySQL_Link](https://www.mysql.com/products/community/), follow thw site instructions to install. 
   - Use "pip install Flask" to install FLASK if not already installed. 
2. Download the complete project repository to your your machine. 
3. If you already have a database schema called ***datarepresentation*** on your machine this step can be skipped.
   - Run the program pysqlcreatedb.py, this will create a schema in your mySQL instance called **datarepresentation**
4. To create the database table for the gym bookings details run the program **pysqlcreatetable.py**. This will create a table called **gymbookings** in the **datarepresentation schema**. 
5. Run the program **gymserver.py**. This is the main server program that runs the gym booking server. Open any browser and navigate to http://127.0.0.1:5000/ to access the gym booking system. 
   - Code for the Web interface and program is stored in the folder **staticpages** as **index.html**. 
   - The Code for the server interface functions is held in the DAO program **gymDAO.py**. 
      - ** Note in my instance of mySQL the user = 'root', password = 'root'. 
      - If your system setup is different change the details in the db class in the gymDAO.py program per below.**

    class GymDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = 'localhost',
        **user = 'root',**
        **password = 'root',**
        database = 'datarepresentation'
        )

## 3. Operating the Program
On first starting the gymbookings table will be empty, therefore no bookings will be visible. 
1. Create a Booking
   - A new booking is created by selecting the **Create Gym Class Booking**.
   - Selecting this brings up a class booking form. The user fills in the members name, age, selects class from the form dropdown, class date, class time and selects the instructor from the form dropdown. The Booking ID is automatically updated. 
   - Click **Create Booking** and the user is returned to the main page, the booking is stored on the server and is displayed in the bookings table. 
   - User can also click **Cancel** if booking is not proceeding, the form will be cleared and user is returned to the main page. 
   - As each new booking is created it will display on the main page table. 

 2. Update Booking.
    - Each booking has an option to be updated by selecting  **Update Booking** in the booking record. 
    - The update booking form is shown with the details of the booking displayed. Here the user can update any of the booking details and selects **Update** to proceed or **Cancel** to discard the changes and return to the main page. 
    - The updated booking will be shown in the main page bookings table. 
  
3. Delete Booking
   - Any booking can be deleted, this removes the booking from the table and the database server. 
