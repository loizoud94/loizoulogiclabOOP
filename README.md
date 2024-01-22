# loizoulogiclabOOP

## Overview
The OOP Email Simulator is a Python program that simulates basic email functionality using Object-Oriented Programming (OOP) concepts. It allows users to create, manage, and interact with email objects, organized into folders such as Inbox, Junk Folder, and Deleted Folder. The program provides a simple command-line interface to perform actions like reading emails, marking as read or unread, moving to different folders, and deleting emails.

## Getting Started
To use the OOP Email Simulator, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/loizoud94/loizoulogiclabOOP.git
   cd loizoulogiclapOOP
   ```

2. **Run the Program:**
   ```bash
   python email.py


## Features
- **Email Class:**
  - Represents individual emails with attributes like email address, subject line, and content.
  - Provides methods to mark emails as read, unread, spam, or normal.

- **Folders:**
  - Inbox, Junk Folder, and Deleted Folder are implemented as lists to store email objects.

- **Functions:**
  - `populate_inbox`: Populates the selected folder with a given email.
  - `list_emails`: Prints the subject line of each email in the specified folder.
  - `read_email`: Displays the content of a selected email, allowing actions like marking as read, unread, spam, or deleting.

- **Sample Emails:**
  - Three sample emails are created and added to the Inbox for demonstration purposes.

## Usage
1. **Read an Email:**
   - Select option 1 to view and interact with emails in the Inbox.
    ![image](https://github.com/loizoud94/loizoulogiclabOOP/assets/152619396/46d9e509-0b41-4786-908f-e1053e2b6f8c)

2. **View Unread Emails:**
   - Select option 2 to display a list of unread emails in the Inbox.

   <img width="220" alt="Screenshot 2024-01-19 at 17 31 42" src="https://github.com/loizoud94/loizoulogiclabOOP/assets/152619396/b2cbf644-4df6-4616-883e-1e8ab953b020">


3. **View Junk Folder:**
   - Select option 3 to view emails in the Junk Folder. Move emails back to the Inbox if needed.
   
     <img width="235" alt="Screenshot 2024-01-19 at 17 31 57" src="https://github.com/loizoud94/loizoulogiclabOOP/assets/152619396/2113c115-415c-4e97-8d4f-5eff8ddeb094">


4. **View Deleted Folder:**
   - Select option 4 to view emails in the Deleted Folder. Retrieve or permanently delete emails as desired.
<img width="242" alt="Screenshot 2024-01-19 at 17 32 12" src="https://github.com/loizoud94/loizoulogiclabOOP/assets/152619396/70977302-f88d-4a3b-acb3-be351db478bb">


5. **Quit Application:**
   - Select option 5 to exit the program.

## Contributing
If you would like to contribute to the development of the OOP Email Simulator, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them.
4. Push the changes to your fork.
5. Open a pull request to the main repository.

## License
This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

## Acknowledgments
Special thanks to the contributors and users who provide feedback and support to improve the OOP Email Simulator.

Feel free to explore, modify, and enhance the program to suit your needs. Happy coding!
```
