import smtplib
import datetime as dt
import pandas

name_place = "[NAME]"
from_email = YOUR_EMAIL
from_email_password = YOUR_PASSWORD

current_date = dt.datetime.now()
current_month = current_date.month
current_day_num = current_date.day

with open("dates.csv", "r") as dates:
    dates = pandas.read_csv("dates.csv")
    for (index, row) in dates.iterrows():
        if dates["month"][index] == current_month and dates["day"][index] == current_day_num:
            name = dates["name"][index]
            email = dates["email"][index]
            letter_for_today = f"{current_month}-{current_day_num}.txt"
            with open(letter_for_today, "r") as letter:
                chosen_letter = letter.read()
                updated_chosen_letter = chosen_letter.replace(name_place, name)
                letter_update = open("maslenitsa.txt", "w")
                letter_update.write(updated_chosen_letter)
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=from_email, password=from_email_password)
                connection.sendmail(from_addr=from_email, to_addrs=email, msg=f"Subject: Happy Day of Maslenitsa!\n\n{updated_chosen_letter}")
                connection.close()
                letter_update.close()