# Invoice-Reader
This Python script allows you to extract invoice data from PDF files and store it in an Excel spreadsheet.
# Python Invoice Reader

This Python script allows you to extract invoice data from PDF files and store it in an Excel spreadsheet. It uses the `pdfplumber` library for PDF extraction and `pandas` for creating and manipulating dataframes.

## Prerequisites

- Python 3.x
- `pdfplumber` library
- `pandas` library

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:

pip install pdfplumber pandas


## Usage

1. Place your PDF files in the same directory as the script.
2. Run the script using the following command:

python invoice_reader.py

3. The script will iterate over all the PDF files in the directory, extract relevant invoice data, and store it in an Excel spreadsheet named "InvoiceList.xlsx".

## How it works

1. The script first imports the necessary libraries: `pdfplumber`, `pandas`, and `os`.
2. It sets the current directory path and defines the name and path of the output Excel spreadsheet.
3. The script initializes empty lists to store the extracted invoice data.
4. It iterates over all the files in the current directory and checks if they have a ".pdf" or ".PDF" extension.
5. For each PDF file found, it opens it using `pdfplumber` and extracts the text content of each page.
6. The text content is split into lines, and the script searches for specific keywords to identify relevant invoice information.
7. The extracted data, such as client name, invoice number, issue date, due date, subtotal, tax rate, sales tax, and total, are appended to their respective lists.
8. After processing all the PDF files, the script creates a dictionary using the extracted lists.
9. The dictionary is then converted into a pandas DataFrame.
10. The DataFrame is saved as an Excel spreadsheet named "InvoiceList.xlsx" in the current directory.

Feel free to modify the code to fit your specific requirements.

**Note:** Make sure to install the required libraries and place the script in the same directory as the PDF files you want to process.

## License

This project is licensed under the [MIT License](LICENSE).
