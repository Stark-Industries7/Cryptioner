# Cryptioner

Cryptioner is a simple Python class for encrypting and decrypting strings using a custom encryption key. This project has been extended to support encryption and decryption of text files (`.txt`) and word documents (`.docx`), providing a basic yet functional encryption tool for various file types.

## Features

- Encrypt a string using a custom or randomly generated encryption key.
- Decrypt the string back to its original form using the same encryption key.
- Encrypt and decrypt text files (`.txt`).
- Encrypt and decrypt word documents (`.docx`).

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.12.0
- `python-docx` library for handling word documents

Install `python-docx` via pip:

```sh
pip install python-docx
```

### Running the Program
1. Clone the repository or download the `cryptioner.py` file.
2. Open a terminal and navigate to the directory containing the `cryptioner.py` file.
3. Run the following command to start the program:

```sh
python cryptioner.py
```

## Usage

When you run the program, it will ask you to enter the path of a text or word file.
The program will generate a random encryption key, encrypt the file's content, save it to a new file, and then decrypt it back to the original content for demonstration.

## Example

```sh
------------------------Welcome To Cryptioner------------------------

Enter the path of your file (text or word): example.txt

Generated encryption key: AbCdE

The encrypted file has been saved as: example_encrypted.txt

The decrypted file has been saved as: example_decrypted.txt

Thank you for using Cryptioner!😉
```

## Code Overview

### The Cryptioner class has two main methods:

- Encrypt(): Joins the characters of the string with the encryption key.
- Decrypt(): Splits the encrypted string using the encryption key to retrieve the original string.

### File Handling Methods

- read_text_file(file_path): Reads the contents of a text file.
- write_text_file(file_path, content): Writes content to a text file.
- read_word_file(file_path): Reads the contents of a word file.
- write_word_file(file_path, content): Writes content to a word file.
