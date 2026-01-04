import smtplib
import datetime as dt
import random


MY_EMAIL= "sivabalajimamidala1@gmail.com"
PASSWORD= "luzrmmwljyewgmid"

now=dt.datetime.now()
week_day=now.weekday() #mon-0,tue-1,.....sun-6
if week_day==6:
    with open(file="./quotes.txt", mode="r") as data_file:
        data = data_file.readlines()
        quote = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="sivabalajimamidala1@yahoo.com",
                msg=f"Subject:Monday Movitation quote\n\n {quote}"
            )

