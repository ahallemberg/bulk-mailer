import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient, subject, body):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(message)

def main():
    for email in RECIPIENTS:
        try:
            send_email(email, EMAIL_SUBJECT, EMAIL_TEMPLATE)
            print(f"Email sent successfully to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}: {str(e)}")

if __name__ == "__main__":
    main()
