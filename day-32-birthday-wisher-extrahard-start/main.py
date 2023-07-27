import datetime as dt
import pandas as pd
import smtplib
import os
import random

my_email = "marionbillgarcia12@gmail.com"
my_password = "nbusmsvizkitttwc"

df = pd.read_csv('birthdays.csv')
m = df.to_dict(orient="records")
letter = random.choice(os.listdir("letter_templates"))
path = f"letter_templates/{letter}"

now = dt.datetime.now()
current_month = now.month
current_day = now.weekday()

for people in m:
    if people['month'] == current_month and people['day'] == current_day:
        with open(path, 'r') as file:
            content = file.read()
            updated_content = content.replace('[NAME]', people['name'])
            print(updated_content)
            # with smtplib.SMTP("smtp.gmail.com") as connection:
            #     connection.starttls()
            #     connection.login(user=my_email, password=my_password)
            #     connection.sendmail(from_addr=my_email, to_addrs=f"{people['email']}",
            #                         msg=f"Subject:Happy Birthday\n\n{updated_content}")
    else:
        pass