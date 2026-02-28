##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
import os

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

birthdays_df = pd.read_csv("birthdays.csv")
print(birthdays_df)

todays_date = dt.datetime.now()
month = todays_date.month
day = todays_date.day

birthdays_dict = birthdays_df.set_index(['month', 'day']).to_dict(orient="index")

if (month, day) in birthdays_dict:
    email_recipient = birthdays_dict[(month,day)]
    recipient_name = email_recipient['name']
    recipient_address = email_recipient['email']

letter_selection = f"letter_templates/letter_{random.randint(1,3)}.txt"
print(letter_selection)
with open(letter_selection, "r") as letter:
    letter_content = letter.read()
    letter_content = letter_content.replace('[NAME]', recipient_name)


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=recipient_address,
                        msg=f"Subject:Happy Birthday\n\n{letter_content}")





