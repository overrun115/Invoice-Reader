import pdfplumber
import pandas as pd
import os


CurrentPath = os.path.dirname(os.path.abspath(__file__))
InvoiceList = os.path.join(CurrentPath, 'InvoiceList.xlsx')

# List
Client = []
IssueDate = []
DueDate = []
Subtotal = []
TaxRate = []
SalesTax = []
Total = []
InvoiceNumber = []

for filename in os.listdir(CurrentPath):
    if filename.endswith(".PDF") or filename.endswith(".pdf"):
        pdf_path = os.path.join(CurrentPath, filename)
        with pdfplumber.open(pdf_path) as pdf:                 
            for page in pdf.pages:
                text = page.extract_text()
                lines = text.split("\n")
                for i, line in enumerate(lines):
                    if line.startswith("BILL TO:"):
                        if i < len(lines) - 1:
                            client = lines[i+1]
                            Client.append(client)    
                    elif line.startswith("INVOICE NUMBER:"):
                        number = line.split()[-1]
                        InvoiceNumber.append(number)                                                
                    elif line.startswith('ISSUE DATE:'):
                        issue = line.split()[-1]
                        IssueDate.append(issue)
                    elif line.startswith('DUE DATE:'):
                        due = line.split()[-1]
                        DueDate.append(due)
                    elif line.startswith('SUBTOTAL'):
                        sub = line.split()[-1]
                        Subtotal.append(sub)
                    elif line.startswith('TAX RATE'):
                        rate = line.split()[-1]
                        TaxRate.append(rate)
                    elif line.startswith('SALES TAX'):
                        sales = line.split()[-1]
                        SalesTax.append(sales)
                    elif line.startswith('TOTAL'):
                        total = line.split()[-1]
                        Total.append(total)                                                                                                                                                                               

# Dict
dictInvoice = {'Client': Client,'Invoice Number': InvoiceNumber, 'Issue': IssueDate, 'Due': DueDate, 'Subtotal': Subtotal, 'Tax Rate': TaxRate, 'Sales Tax': SalesTax, 'Total': Total}

# DataFrame
DfInvoice = pd.DataFrame(dictInvoice)
DfInvoice.to_excel(InvoiceList, index=False)