from email.message import EmailMessage
from smtplib import SMTP
from typing import Any, Self


class EmailClient:
    def __init__(self, sender: str, address: str, port: int, password: str) -> None:
        self.sender = sender
        self.address = address
        self.port = port
        self.password = password

    def __enter__(self) -> Self:
        self.server = SMTP(self.address, self.port)
        self.server.starttls()
        self.server.login(self.sender, self.password)

        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        self.server.quit()

    def _prepare_header(self, subject: str, content: str, recipients: list[str]) -> EmailMessage:
        message = EmailMessage()
        message["Subject"] = subject
        message["From"] = self.sender
        message["To"] = self.sender
        message["Bcc"] = recipients
        message.set_content(content, subtype="html")
        return message

    def send_email(self, recipients: list[str], content: str, subject: str = "GitLab Notification") -> None:
        self.server.send_message(self._prepare_header(subject, content, recipients))
