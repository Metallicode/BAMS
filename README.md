# BAMS
Bank Account Management System

Objective: To create a terminal-based application that allows users to manage their bank accounts.

## Basic Application Template:

Welcome screen with the name of the Bank.

An interactive menu with options such as:

a. Create a new account

b. Login to an existing account

c. Exit

## Functionality:

Create a new account: Prompt the user for their name, an initial deposit amount, and then generate a random account number for the user. Store this information.

Login to an existing account: Ask for the account number. Once logged in, provide another menu with options:

a. Check Balance

b. Deposit

c. Withdraw

d. Log out

Each time a user logs in, they should be greeted by their name.

The system should be able to handle multiple user accounts.

## User Stories:

The user starts the program and sees the welcome screen.
They choose to create an account or log into an existing one.
Once logged in, they can perform a series of actions like checking their balance, depositing money, or withdrawing funds.
For deposits and withdrawals, the system should ask for the amount and then confirm the action.
The user should be able to log out and return to the main menu.



## Implementation Tips:

You can use dictionaries to store account information. The account number can be the key, and the value can be another dictionary containing the user's name, balance, etc.
Use loops to keep the menu running until the user chooses to exit.
When prompting the user for input, ensure you handle potential errors, e.g., if they try to withdraw more money than they have.

# Good Luck!
