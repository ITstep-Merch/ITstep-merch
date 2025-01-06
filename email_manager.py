from smtplib import SMTP
import os
import dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dotenv.load_dotenv()

class Email:
    def __init__(self):
        self.SMTP_EMAIL = os.environ.get("POST_EMAIL")
        self.SMTP_PASSWORD = os.environ.get("POST_PASSWORD")

    def send_email(self, user_email, total, staff):
        print(total, staff)
        subject = "Успішне замовлення!"
        
        # HTML тіло листа
        html_body = f"""
        <html>
            <body>
                <img src="https://drive.google.com/thumbnail?id=1gDQVkjaL6sjFDJ2HFbpOfU9RGS-24mzQ&sz=w400" alt="Logo" style = "width: 250px;"/>
                <h1 style="color: black;">Ваше замовлення успішно прийняте в обробку!👀</h1>
                <h3>Ваші товари: {staff}</h3>
                <p style="color: black;">Фінальна сума: ${total}</p>
                <p style="color: #999;">Очікуйте на зворотній зв'язок, та підтвердження вашого замовлення!😄</p>
                <a href="http://127.0.0.1:5000">Перейти до каталогу</a>
            </body>
        </html>
        """
        
        # Формування листа
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = self.SMTP_EMAIL
        msg["To"] = user_email

        # Текстові частини листа
        part1 = MIMEText(html_body, "plain")
        part2 = MIMEText(html_body, "html")

        msg.attach(part1)
        msg.attach(part2)

        # Надсилання листа через SMTP
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.SMTP_EMAIL, self.SMTP_PASSWORD)
            connection.sendmail(from_addr=self.SMTP_EMAIL, to_addrs=user_email, msg=msg.as_string())
