import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as self.connection:
            self.connection.starttls()
            self.connection.login(user=MY_EMAIL, password=PASSWORD)

            msg = MIMEText(message)
            msg["Subject"] = "Lowest Flight Prices Available"
            msg["From"] = MY_EMAIL
            msg["To"] = RECIPIENT_EMAIL

            self.connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=msg.as_string()
            )


