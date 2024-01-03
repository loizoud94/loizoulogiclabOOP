### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    """Class representing emails"""
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Declare the class variable, with default value, for emails.
    has_been_read = False
    is_spam = False

    # Create the method to change the class variables for instances.
    def mark_as_read(self):
        """Class method to mark emails as read"""
        self.has_been_read = True

    def mark_as_unread(self):
        """Class method to mark emails as unread"""
        self.has_been_read = False

    def mark_as_spam(self):
        """Class method to mark emails as spam"""
        self.is_spam = True

    def mark_as_normal(self):
        """Class method to unmark emails as spam"""
        self.is_spam = False


# --- Lists --- #
# Initialise empty lists to store the email objects.
    inbox = []
    junk_folder = []
    deleted_folder = []

# --- Functions --- #
# Build out the required functions for your program.

    def populate_inbox(self, folder):
        """Class method to populate the selected inbox"""

        email_items = Email(self.email_address, self.subject_line, self.email_content)
        if folder == "inbox":
            Email.inbox.append(email_items)
        elif folder == "junk_folder":
            Email.junk_folder.append(email_items)
        elif folder == "deleted_folder":
            Email.deleted_folder.append(email_items)


    # Create a function which prints the email’s subject_line, along with a corresponding number
    def list_emails(self):
        """Class method to print each email's subject line"""
        for index, email in enumerate(Email.inbox):
            print(f"{index}\t{email.subject_line}")
            
        print()

    # Create a function which displays a selected email. 
    def read_email(self, index):
        """Class method to display emails and mark as read"""
        email_instance = Email.inbox[index]

        print(f"From:\t\t{email_instance.email_address}\nSubject:\t{email_instance.subject_line}\n\n{email_instance.email_content}")

    # Once displayed, call the class method to set its 'has_been_read' variable to True.
        email_instance.mark_as_read()
        print(f"Email from {email_instance.email_address} marked as read.\n")

        # mini menu created to execute different actions on the emails
        mini_menu = True
        while mini_menu == True:
            user_input = input('''Choose from the following email actions:
            d - Enter 'd' to delete this email.
            j - Enter 'j' to mark this email as spam and send to the junk folder.
            u - Enter 'u' to mark this email as unread.
            Enter anything else to continue without executing any email actions.
            ''').lower()
            if user_input == 'u':
                email_instance.mark_as_unread()
                mini_menu = False

            
            elif user_input == 'j':
                email_instance.mark_as_spam()
                email_instance.populate_inbox("junk_folder")
                Email.inbox.remove(email_instance)
                mini_menu = False
            
            elif user_input == 'd':
                email_instance.populate_inbox("deleted_folder")
                Email.inbox.remove(email_instance)
                mini_menu = False
            
            else:
                mini_menu = False

# Create 3 sample emails and add it to the Inbox list.
sample_email1 = Email(email_address = "kingshrewd@farseers.com",
                subject_line = "Assassin's Apprentice",
                email_content = "Don't do what you can't undo, until you've considered what you can't do once you've done it.")
sample_email2 = Email(email_address = "chade@farseers.com",
                subject_line = "Royal Assassin",
                email_content = "Most prisons are of our own making. A man makes his own freedom, too.")
sample_email3 = Email(email_address = "golden.fool@farseers.com",
                subject_line = "Assassin's Quest",
                email_content = "Fitz fixes feist's fits. Fat suffices.")

sample_email1.populate_inbox("inbox")
sample_email2.populate_inbox("inbox")
sample_email3.populate_inbox("inbox")

# --- Email Program --- #

menu = True

while menu is True:
    user_choice = (input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. View junk folder
    4. View deleted folder
    5. Quit application

    Enter selection: '''))

    # option to read any email in the inbox  
    if user_choice == '1':
        print("Inbox:")
        Email.list_emails(Email.inbox)
        
        view_email = None
        while view_email is None:
            try:
                view_email = int(input("Please enter the index number of the email you would like to view: "))
                while view_email not in range(len(Email.inbox)):
                    try:
                        view_email = int(input(f"Please enter a valid index number in range 0-{len(Email.inbox) - 1}: "))
                    except ValueError:
                        print("Invalid input. Please try again.\n")
                        continue
            except ValueError:
                print("Invalid input. Please try again.\n")
                continue
        print()
        Email.read_email(Email, view_email)


    # displays list of unread emails
    elif user_choice == '2':
        print("\nUnread emails:\n")

        count = 0
        for email in Email.inbox:
            if not email.has_been_read:
                count += 1
                print(f"\t{email.subject_line}")

        if count == 0:
            print("You are up to date! There are no unread emails.")

    # displays list of emails in junk folder
    elif user_choice == '3':

        print("\nJunk folder:\n")

        for index, email in enumerate(Email.junk_folder):
            print(f"{index}\t{email.subject_line}")
        
        print()

        if len(Email.junk_folder) == 0:
            print("Junk folder is empty.")

        # mini menu to move emails back to inbox or return to main menu
        else:
            mini_menu = True
            while mini_menu is True:
                try:
                    move_email = int(input(f'''Please enter the index number of an email if you would like to move it to Inbox
Or enter {len(Email.junk_folder)} to exit the junk folder. '''))
                    mini_menu = False
                    while move_email not in range(len(Email.junk_folder) + 1):
                        try:
                            move_email = int(input(f"Please enter a valid index number in range 0-{len(Email.junk_folder)}: "))
                        except ValueError:
                            print("Invalid input. Please try again.\n")
                            continue
                except ValueError:
                    print("Invalid input. Please try again.\n")
                    continue
            if move_email == len(Email.junk_folder):
                continue

            email_instance = Email.junk_folder[move_email]
            email_instance.mark_as_normal()
            email_instance.populate_inbox("inbox")
            Email.junk_folder.remove(email_instance)


    # displays list of deleted emails
    elif user_choice == '4':

        print("\nDeleted folder:\n")

        for index, email in enumerate(Email.deleted_folder):
            print(f"{index}\t{email.subject_line}")

        if len(Email.deleted_folder) == 0:
            print("Deleted folder is empty.")

        # mini menu to execute actions on items in deleted folder.    
        else:
            mini_menu = True
            while mini_menu is True:
                try:
                    move_email = int(input(f'''\nPlease enter the index number of an email if you would like to retrieve or permanently delete it.
Alternatively, enter {len(Email.deleted_folder)} to exit the deleted folder. '''))
                    mini_menu = False
                    while move_email not in range(len(Email.deleted_folder) + 1):
                        try:
                            move_email = int(input(f"Please enter a valid index number in range 0-{len(Email.deleted_folder)}: "))
                        except ValueError:
                            print("Invalid inpout. Please try again \n")
                            continue
                except ValueError:
                    print("Invalid input. Please try again.\n")
                    continue
            if move_email == len(Email.deleted_folder):
                continue

            email_instance = Email.deleted_folder[move_email]

            user_input = input(f'''\nEnter d to permanently delete {email_instance.subject_line} or enter m to move it back to Inbox. \n''')

            if user_input == 'd':
                Email.deleted_folder.remove(email_instance)

            elif user_input == 'm':
                email_instance.populate_inbox("inbox")
                Email.deleted_folder.remove(email_instance)

            else:
                print("Invalid input. Please try again.")

        

    elif user_choice == '5':

        print("\nClosing application.\n")

        menu = False

    else:
        print("Oops - incorrect input. Please try again")

# End of program