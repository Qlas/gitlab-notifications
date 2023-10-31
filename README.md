# GitLab Notifications

Send gitlab notifications easily without GitLab Premium

## Usage

### Prepare environment variables

```sh
cp example.env .env
```

- `GITLAB_URL` - url to your gitlab instance
- `GITLAB_TOKEN` - your personal access token with read access
- `SMTP_EMAIL` - sender email address
- `SMTP_PASSWORD` - password to email
- `SMTP_SERVER` - smtp server address from which emails will be sent
- `SMTP_PORT` - smtp server port

### Prepare your email

1. Validate the `template.html` file to see if it meets your requirements
   > **_NOTE:_** You shouldn't change the `template.html` file
   > after sending the first email.
2. Prepare `content.html` file
3. Run program in preview mode:

   ```sh
   poetry run python send_email.py --preview
   ```

   This should create a `preview.html` file containing a content of the email message.

4. Run program to send an email to **all** regular users

   > **_NOTE:_** it will exclude `external`, `bots` and `inactive` users.

   ```sh
   poetry run python send_email.py
   ```

   > **_NOTE:_** A confirmation request will be displayed, this is the last moment to cancel the request.
