# Bulk Mailer
Send bulk mails

## Config
Create a .env file and complete these configs

```
SMTP_SERVER=
SMTP_PORT=
SENDER_MAIL=
SENDER_PASSWORD=
```
For gmail:
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## Template 
In mail-conifg.json, the field "template" specify which template to use. Edit the template file to change the template

You can use these special placeholders in your template

- {recipient}
- {subject}
- {sender}

Also, the "fields" list in the recipients objects in mail-config.json, can contain field objects

```
{
    "name": "field-name", 
    "value": "actual-value" 
}
```

Which then can be used in the template the same way as the special placeholders recipient, subject and sender. 

NB: All the recipients should contain the same special fields, if not you should split up the bulk

## Gmail setup 
1. Go to your Google Account settings.
2. Select "Security" on the left.
3. Under "Signing in to Google," select "2-Step Verification" (you need to have this enabled).
4. At the bottom of the page, select "App passwords."
5. Choose "Mail" and "Other (Custom name)" from the dropdown menus.
6. Enter a name for the app (e.g., "Python Email Script") and click "Generate."
7. Use the 16-character code that appears as your SENDER_PASSWORD in .env (remove any spaces between the characters)