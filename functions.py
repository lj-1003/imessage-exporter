#-------------IMPORTS--------------------------------
import sqlite3
import os
import shutil
import shlex
#----------------------------------------------------

def dataDirect():
    global db_path

    rawPath = input("Drag and drop the file here: ").strip().strip('"')

    # Convert shell-like string to proper path (handles quotes and \ escapes)
    newPath = shlex.split(rawPath)[0]

    # Expand ~ if user dragged something from home dir
    newPath = os.path.expanduser(newPath)

    copyLocation = "input"

    os.makedirs(copyLocation, exist_ok=True)
    shutil.copy(newPath, copyLocation)

    print(f"Copied {newPath} into {copyLocation}/")

    os.getcwd
    db_path = "input/sms.db"

   

def sqlQuery():
    global contact
    global baseQuery
    print("#" * 70)
    print("What phone number or email would you like to export messages from?")
    print()
    contact = input(">: ")
    print()

    baseQuery = f"""
    SELECT 
        --handle.id AS phone_number,
	    datetime(message.date / 1000000000 + 978307200, 'unixepoch', 'localtime') AS date,
	    message.is_from_me,
	    message.text
     FROM message
     JOIN chat_message_join ON message.ROWID = chat_message_join.message_id
     JOIN chat ON chat_message_join.chat_id = chat.ROWID
     JOIN chat_handle_join ON chat.ROWID = chat_handle_join.chat_id
     JOIN handle ON chat_handle_join.handle_id = handle.ROWID
     WHERE handle.id = '{contact}'   
     AND chat.ROWID IN (
        SELECT chat_id
        FROM chat_handle_join
        GROUP BY chat_id
        HAVING COUNT(handle_id) = 1   -- only chats with 1 participant (not groups)
    )
     ORDER BY message.date DESC;
"""

    #print(baseQuery)

def dothething():
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    cursor.execute(baseQuery)
    rows = cursor.fetchall()
    count = 0

    for row in rows:
        count +=1
    
    print(f"{count} messages found.")
    if count > 0:
        os.makedirs("output", exist_ok=True)
        abbyeTexts = open(f"output/{contact}_messages_backup.txt", "w")
        for row in rows:
            abbyeTexts.write(str(row))
            abbyeTexts.write("\n")
            abbyeTexts.write("\n")
        abbyeTexts.close()
        print(f"{count} messages exported.")
    elif count < 1:
        print("please retry with a different phone number or email.")
    # Close the connection
    cursor.close()
    conn.close()
    print("#" * 70)

    