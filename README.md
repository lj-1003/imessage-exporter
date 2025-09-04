# iTextPorter


## Description

Apple didn't make an easy way to export texts. This dirt simple program takes the sms.db file from your iTunes backup and can export an entire thread to a .txt file.

## Getting Started

### Executing program
1. Place your sms.db file in the "input" folder. The iTunes backup will have this file as random characters. It must be renamed to sms.db. Watch this video to find the file in your iTunes backup: https://www.youtube.com/watch?v=IgwcbTNIO9g.
2. Run "main.py"

### Program Instructions
2. Enter the phone number or email of the thread you want to export. Enter phone numbers in this format: +1555123456. This program does not store or send any numbers or emails.
3. If it locates the thread, the console will display the number of messages found, and it will export it to the "output" folder.

### Limitations
1. Cannot export attachments such as images, videos, etc. (yet)
2. Cannot export group threads (yet)

### Disclaimer
While I try to test multiple situations, errors are always possible. I am not responsible for any data loss that might occur. Keep a backup copy of your sms.db file just in case. 

## Authors

Levi Eck

## Acknowledgments

Inspiration, code snippets, etc.
* ChatGPT for helping me figure out to search through the sms.db file
