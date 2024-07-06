# SHA-1 Password Cracker

## Summary

This project demonstrates the importance of password security by creating a password cracker that can identify passwords hashed using the SHA-1 algorithm. The cracker compares hashed passwords against a list of the top 10,000 commonly used passwords, optionally using salts for added complexity.

## Description

Passwords should never be stored in plain text. Instead, they should be stored as hashes to protect them in case the password list is discovered. However, not all hashing algorithms are equally secure. This project focuses on SHA-1, an older and less secure hashing algorithm.

The password cracker function reads a list of the top 10,000 passwords from a file and compares the SHA-1 hashes of these passwords to a given hash. If a match is found, the function returns the original password. If the hash does not match any of the top 10,000 passwords, the function returns "PASSWORD NOT IN DATABASE".

Optionally, the function can use salts from another file. If salts are used, each salt is appended and prepended to each password before hashing and comparing.

## Getting Started

### Prerequisites

- Python 3.x
- `hashlib` library (comes with Python standard library)

### Files

- `password_cracker.py`: Contains the main function to crack SHA-1 hashed passwords.
- `main.py`: For testing the password cracker function.
- `test_module.py`: Unit tests for the password cracker function.
- `top-10000-passwords.txt`: List of the top 10,000 commonly used passwords.
- `known-salts.txt`: List of known salts to use when `use_salts` is set to True.

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/sha1-password-cracker.git
   cd sha1-password-cracker

2. Ensure you have `top-10000-passwords.txt` and `known-salts.txt` in the project directory.

### Usage

1. Without salt:
  ```python
  from password_cracker import crack_sha1_hash
  sha1_hash = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
  password = crack_sha1_hash(sha1_hash)
  print(password)  # Output: "password"

2. With salt:
  ```python
  from password_cracker import crack_sha1_hash
  sha1_hash = "53d8b3dc9d39f0184144674e310185e41a87ffd5"
  password = crack_sha1_hash(sha1_hash, use_salts=True)
  print(password)  # Output: "superman"
