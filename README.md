# iMessage Exporter



## Description

Apple didn't create an easy way to export text message threads, and I'm not paying a subscription for third-party services like iMazing, so I made my own. This program takes the sms.db file from your iTunes backup and can export an entire thread to a .txt file.

This program is free and open source. 

## Getting Started

### Dependencies
```
pip install -r requirements.txt
```

### Executing program
1. Place your sms.db file in the "input" folder. The iTunes backup will have this file as random characters. It must be renamed to sms.db. Watch this video to find the file in your iTunes backup: https://www.youtube.com/watch?v=IgwcbTNIO9g.
2. Run "main.py"

### Program Instructions
1. Agree to the statements made.
2. Enter the phone number or email of the thread you want to export. Enter phone numbers in this format: +1555123456. This program does not store or send any numbers or emails.
3. If it locates the thread, the console will display the number of messages found, and it will export it to the "output" folder.

### Limitations
1. Cannot export attachments such as images, videos, etc. (yet)
2. Cannot export group threads (yet)

### Disclaimer
This program is under development, and while I try to test multiple situations, errors are always possible. I am not responsible for any data loss that might occur. Always have an extra copy of your sms.db file just in case. 

## Authors

Levi Eck

## Acknowledgments

Inspiration, code snippets, etc.
* ChatGPT for helping me figure out to search through the sms.db file
