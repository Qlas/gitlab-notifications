import argparse

import gitlab

from utils.email_client import EmailClient
from utils.settings import Settings


def prepare_message() -> str:
    with open("template.html", "r", encoding="utf-8") as file:
        template = file.read()

    with open("content.html", "r", encoding="utf-8") as file:
        content = file.read()

    return template.format(content=content)


def get_gitlab_users_email(url: str, token: str) -> list[str]:
    with gitlab.Gitlab(url=url, private_token=token) as gl:
        return [
            user.email
            for user in gl.users.list(iterator=True, active=True, without_project_bots=True, exclude_external=True)
        ]


def preview() -> None:
    content = prepare_message()
    with open("preview.html", "w+", encoding="utf-8") as file:
        file.write(content)


def parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--preview", action="store_true", help="Preview the content of an email.")

    return parser.parse_args()


def confirmation() -> bool:
    prompt = input("Do you want to continue?\n").lower()

    return prompt in ("y", "yes", "1")


def main() -> None:
    settings = Settings()  # type: ignore
    arguments = parser()

    if arguments.preview:
        preview()
        return None

    emails = get_gitlab_users_email(settings.url, settings.token)

    print(f"You will send email to {len(emails)} accounts.\nRecipients: {", ".join(emails)}")

    if not confirmation():
        print("The email has not been sent.")
        return None

    with EmailClient(settings.smtp_email, settings.smtp_server, settings.smtp_port, settings.smtp_password) as server:
        server.send_email(emails, prepare_message())

    print("The email has been sent.")


if __name__ == "__main__":
    main()
