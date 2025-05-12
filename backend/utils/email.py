import smtplib
from email.mime.text import MIMEText
import random
import string

def generate_verification_code():
    return ''.join(random.choices(string.digits, k=6))

def send_verification_email(email, code):
    sender_email = "your_email@example.com"  # 替换为你的邮箱地址
    sender_password = "your_email_password"  # 替换为你的邮箱密码
    receiver_email = email

    message = MIMEText(f"Your verification code is: {code}")
    message["Subject"] = "Verification Code"
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.example.com", 587)  # 替换为你的 SMTP 服务器地址和端口
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False