from smtplib import SMTP
import os
import dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

dotenv.load_dotenv()

class Email:
    def __init__(self):
        self.SMTP_EMAIL = os.environ.get("POST_EMAIL")
        self.SMTP_PASSWORD = os.environ.get("POST_PASSWORD")

    def send_email(self, user_email, total, staff):
        print(total, staff)
        subject = "Успішне замовлення!"
        jokes = [
            "Ваше замовлення прибуде десь... а, ми студенти, нікому не ясно коли ж воно прибуде)",
            "Саміра вже на шляху! Скоро вона усе доставить!)", 
            "Йой, дякую Вам за покупку, було приємно мати справу саме з Вами!)",
            "Ми ретельно пакуємо ваше замовлення, але якщо знайдете всередині шпаргалки на екзамен, прохання - верніть власнику!)",
            "Небо синє... троянди червоні... а студенти-пакувальники невтомні!)",
            "Доставка від нас — як сесія: довго готуєшся, але результат того вартий!)",
            "Дякуємо за покупку! Тепер у вас офіційний мерч, а у нас — ще більше причин любити наш універ!)",
            "Ваше замовлення відправлено! Якщо прийде — значить, це Ваш знак перевестися в наш універ)",
            "Цей мерч принесе вам купу коштів!!! Якщо ні — повернемо гроші... жартую, не повернемо)",
            "Ваше замовлення в дорозі. Якщо не приїде — то ми запустимо нову програму у нас в університеті! 'Складнощі доставки товарів')",
            "Наш мерч — як твоя присутність на парах: тебе рідко бачать, але якщо вже побачили)...",
            "Ти купив наш мерч? Тепер ти офіційно частина цього хаосу, з яким ми переживаємо сесію... принаймні виглядаєш стильно, поки стресуєш!",
            "Під час покупки, ви підписали домовленість: більше ніколи не носитимете інші бренди! тільки ItStep!)",
            "Цей мерч настільки крутий, що навіть викладачі почнуть тебе поважати... а ось твоя оцінка, на жаль, не зміниться!",
            "Тепер ти виглядаєш, як студент, який витратив всі гроші на мерч замість того, щоб заплатити за борги перед університетом!"
        ]

        if isinstance(staff, str):
            staff = staff.split(',')

        staff_items_html = "".join(
            f"<li style='margin-bottom: 10px; color: #555; font-size: 14px;'>"
            f"<b>{item.strip()}</b>"
            f"</li>" for item in staff
        )

        random_int = random.randint(0, len(jokes) - 1)
        jokes_on_page = jokes[random_int]
        
        html_body = f"""
            <html>
                <body style="font-family: 'Montserrat', sans-serif; background: #f9f9f9; padding: 20px;">
                    <div style="max-width: 600px; margin: auto; background: white; border-radius: 10px; padding: 20px; box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);">
                        <div style="text-align: center;">
                            <img src="https://drive.google.com/thumbnail?id=1gDQVkjaL6sjFDJ2HFbpOfU9RGS-24mzQ&sz=w400" alt="Logo" style="width: 150px; margin-bottom: 20px;" />
                            <h1 style="color: #333;">Ваше замовлення успішно прийняте в обробку! 👀</h1>
                        </div>
                        <div style="margin-top: 20px; border-top: 1px solid #ddd; padding-top: 20px;">
                            <h3 style="color: #444;">Ваші товари:</h3>
                            <ul style="list-style-type: none; padding: 0;">
                                {staff_items_html}
                            </ul>
                            <p style="color: #444; font-weight: bold; font-size: 16px;">Фінальна сума: <span style="color: #28a745;">₴{total}</span></p>
                        </div>
                        <div style="margin-top: 20px; text-align: center; color: #888; font-size: 12px;">
                            Очікуйте на зворотній зв'язок, та підтвердження вашого замовлення!
                        </div>
                        <div style="text-align: center; margin-top: 30px;">
                            <a href="http://127.0.0.1:5000" style="background: #007bff; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px; font-size: 16px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);">Перейти до каталогу</a>
                        </div>
                        <div style="margin-top: 20px; text-align: center; color: #888; font-size: 12px;">
                           Жарт дня: {jokes_on_page}
                        </div>

                    </div>
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

