import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import json

def load_json_config() -> dict: 
    file_path = os.path.join(os.path.dirname(__file__), "mail-config.json")
    with open(file_path, "r", encoding="utf-8") as f: 
        return json.load(f)

def load_template(file_name: str) -> str: 
    with open(os.path.join(os.path.dirname(__file__), file_name), encoding="utf-8") as f: 
        return f.read()

def send_email(smtp_server: str, smtp_port: int, sender: str, sender_password: str, recipient: dict, subject: str, body: str) -> None:
    # special replacements for template
    body = body.replace('{recipient}', recipient["mail"])
    body = body.replace('{subject}', subject)
    body = body.replace('{sender}', sender)
    for field in recipient["fields"]: 
        replace_part = "{" + field["name"] + "}"
        body = body.replace(replace_part, field["value"])

    # create message
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient["mail"]
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, sender_password)
        server.send_message(message)

def main() -> None:
    load_dotenv()
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = os.getenv("SMTP_PORT")
    SENDER_MAIL = os.getenv("SENDER_MAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    _cfg = load_json_config()
    RECIPIENTS: dict = _cfg["recipients"]
    SUBJECT = _cfg["subject"]
    TEMPLATE = load_template(_cfg["template"])

    for recipient in RECIPIENTS:
        try:
            send_email(SMTP_SERVER, SMTP_PORT, SENDER_MAIL, SENDER_PASSWORD, recipient, SUBJECT, TEMPLATE)
            print(f"Email sent successfully to {recipient["mail"]}")
        except Exception as e:
            print(f"Failed to send email to {recipient["mail"]}: {str(e)}")
            raise e

if __name__ == "__main__":
    main()
