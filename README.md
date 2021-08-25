# Russian_Holiday_Week_of_Maslenitsa
Have you heard of the russian holiday week of Maslenitsa? By using this code, on each day of festivities, you will receive an email with fun facts about the holiday. 
Maslenitsa is a week long holiday lasting from February 28th to March 6th. 

# What is needed to run the code?
In this repository, I have created 7 text files, each including unique information that
is important to the specific day of celebration. I have also included a csv file that contains the month and day of each celebration day. 
To use this code, replace YOUR_NAME with the name of the person receiving the email, and replace the email: youremail@gmail.com, with the email you want the messages to be sent to.
In main.py, be sure to replace the variables from_email and from_email_password with your personal information. It may be necessary to go into the security settings of your email, and allow less secure apps to have access. Also be aware of your personal email server, as you may need to make changes for the variable of 
connection = smtplib.SMTP("smtp.gmail.com"). 
If your wish to automate this code, such that it is run everyday at a certain time, you would need to use PythonAnywhere, or some other form of online IDE. 

# Learning Concepts
- Accessing files, reading, writing, and manipulating 
- file paths
- smtplib module and sending email via Pycharm IDE
- datetime module and how to access the current day and month
- pandas module and how to navigate csv files

# Conclusion
This was a fun project for me, because I know now that I can check the day and month or time or year and have a message be sent to me, if the current date is the same as saved in the csv file. Have fun learning about Maslenitsa!
