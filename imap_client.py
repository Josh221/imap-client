#Import required modules.
import imaplib
import email

#Store gmails imap server address in contant.
IMAP_SERVER = "imap.gmail.com"

#Function to authenticate users trying to log in.
def authenticate_user():
    while True:
        #Get user gmail address input.
        email_address = input('Enter your email address: ')
        #Get users password input.
        password = input('Enter your password: ')
        #Try login with credentials.
        try:
            imap.login(email_address, password)
            #If login successful then show user login successful.
            print(f"User {email_address} logged in successfully.")
            break
        except:
            #If login not successful then inform user and allow them to try again.
            print(f"Login for user {email_address} denied. Please check your credentials.")

#Function to list available inboxes to user.
def show_mailboxes():
    #Get list from imap server and display to user.
    mailboxes = imap.list()
    print(mailboxes)

#Function allows user to select a mailbox of choice.
def user_select_mailbox():
    #Call function to list available mailboxes.
    show_mailboxes()
    #Take users input of mailbox choice.
    return input("Type which mailbox you want to enter: ")

#Function to get users messages from imap server.
def get_messages():
    #Search for all available emails in mailbox and save an index of them in variable message_index.
    _, message_index = imap.search(None, "ALL")
    #Loop through email index and fetch every email.
    for message_num  in message_index[0].split():
        #Fetch email with index number and format.
        _, data = imap.fetch(message_num, "(RFC822)")
        #Extract the email message from the data recieved.
        message = email.message_from_bytes(data[0][1])
        #Print a preview of emails to user.
        print(f"- Msg Num: {message_num} | Frm: {message.get('From')} | Subj: {message.get('Subject')} | Date: {message.get('Date')} |")
    #Prompt user to select a message to display.
    message_num_picked = input(f"Enter a message number to preview message: ")

    #Loop through email index and fetch every email.
    for message_num  in message_index[0].split():
        #Fetch email with index number and format.
        _, data = imap.fetch(message_num, "(RFC822)")
        #Extract the email message from the data recieved.
        message = email.message_from_bytes(data[0][1])
        #If the email index number is the one user picked then display the message.
        if (f"b'{message_num_picked}'") ==  str(message_num):
            print(f"Frm: {message.get('From')}")
            print(f"To: {message.get('To')}")
            print(f"BBC: {message.get('BBC')}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            print(f"Date: {message.get('Date')}")
            print(f"Subject: {message.get('Subject')}")
            print("Content:")
            #Print the message content as plain text.
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    print(part.as_string())
   
    #Close the imap connection
    imap.close()


#Establish secure connection to an IMAP server.
imap = imaplib.IMAP4_SSL(IMAP_SERVER)
#Call function to log user in.
authenticate_user()
#Call function for user to select mailbox.
imap.select(user_select_mailbox())
#Call function to get & show messages from picked mailbox.
get_messages()





