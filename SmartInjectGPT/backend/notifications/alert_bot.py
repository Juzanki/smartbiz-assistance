# AlertBot — Notification and Emergency Channel for SmartInjectGPT

import logging
import smtplib
import requests
from email.message import EmailMessage
from typing import Optional
from datetime import datetime

class AlertBot:
    def __init__(
        self,
        email_sender: str,
        email_password: str,
        emergency_phone: Optional[str] = None,
        emergency_whatsapp_api: Optional[str] = None
    ):
        self.email_sender = email_sender
        self.email_password = email_password
        self.emergency_phone = emergency_phone
        self.emergency_whatsapp_api = emergency_whatsapp_api

    def send_email_alert(self, subject: str, body: str, to_email: str):
        try:
            msg = EmailMessage()
            msg.set_content(body)
            msg["Subject"] = subject
            msg["From"] = self.email_sender
            msg["To"] = to_email

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(self.email_sender, self.email_password)
            server.send_message(msg)
            server.quit()

            logging.info(f"[EMAIL ALERT] Sent to {to_email}: {subject}")
            return True
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            return False

    def send_whatsapp_alert(self, message: str):
        if not self.emergency_whatsapp_api or not self.emergency_phone:
            logging.warning("WhatsApp alert not configured.")
            return False

        try:
            payload = {
                "to": self.emergency_phone,
                "message": message
            }
            response = requests.post(self.emergency_whatsapp_api, json=payload)
            if response.status_code == 200:
                logging.info(f"[WHATSAPP ALERT] Sent to {self.emergency_phone}")
                return True
            else:
                logging.error(f"WhatsApp alert failed: {response.status_code}")
                return False
        except Exception as e:
            logging.error(f"Exception during WhatsApp alert: {e}")
            return False

    def log_and_notify(self, title: str, details: str, to_email: Optional[str] = None):
        timestamp = datetime.utcnow().isoformat()
        alert_msg = f"[{timestamp}] {title.upper()}\n\n{details}"

        logging.warning(alert_msg)
        if to_email:
            self.send_email_alert(title, alert_msg, to_email)
        self.send_whatsapp_alert(alert_msg)
