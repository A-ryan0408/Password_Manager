# Password_Manager
Password Manager: Fusing Fernet's encryption &amp; MySQL storage for top security. Seamlessly access &amp; safeguard credentials across devices. Your ultimate digital guardian.

---

## Setup

1. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install required packages via `pip install mysql-connector-python cryptography`.

2. **MySQL Configuration**:
   - Make sure you have MySQL installed and running.
   - Create a database named `passwords`.
   - Create a table named `pwd` with columns: `account` (varchar(20)), `username` (varchar(256)), `password` (varchar(256)).

3. **Key Generation**:
   - Run the script initially with the `write_key()` function uncommented to generate a key for Fernet encryption.

## Usage

1. Run the script (`python your_script_name.py`).
2. Enter the Master Password (`DBMS` by default) to access the password manager.
3. Follow the prompts:
   - Press `1` to add a new password.
   - Press `2` to view saved passwords.
   - Press `3` to update saved passwords.
   - Press `4` to delete a password.
   - Press `5` to quit.

---
