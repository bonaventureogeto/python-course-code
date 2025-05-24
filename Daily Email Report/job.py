import schedule
import time
from daily_report import generate_sales_report, send_email


def job():
    report = generate_sales_report()
    send_email(report)


schedule.every().day.at("08:00").do(job)


if __name__ == "__main__":
    print("Scheduler started. Print Ctrl+c to exit")
    while True:
        schedule.run_pending()
        time.sleep(30)
