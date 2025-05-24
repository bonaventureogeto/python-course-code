import os
import smtplib
import random
from datetime import date
from email.message import EmailMessage


def generate_sales_report():
    today = date.today().isoformat()
    total_sales = random.randint(1000, 10000)
    num_orders = random.randint(80, 200)
    avg_order = round(total_sales / num_orders, 2)

    report = (
        f"Daily sales report for {today}\n"
        f"------------------------------\n"
        f"Total sales {total_sales}\n"
        f"Number of orders {num_orders}\n"
        f"Average order value {avg_order}\n"
    )

    return report


EMAIL_ADDRESS = os.getenv("REPORTER_EMAIL")
EMAIL_PASSWORD = os.getenv("REPORTER_PASS")


def send_email(report_text):
    msg = EmailMessage()
    msg["Subject"] = "Your Daily Sales Report"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "manager@email.com"
    msg.set_content(report_text)

    # connect to gmail SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("Email sent!")
