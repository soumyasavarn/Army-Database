from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from functions import *
import random
import os
from datetime import datetime

def generate_bill(officer,arrears,month,year):
    def onLaterPages(canvas, doc):
        width, height = letter
        # Adjust the following path to where your image is located
        image_path = os.path.join(os.getcwd(), 'qr_image.png')
        # Adjust these dimensions as needed
        image_width = 2.0 * inch
        image_height = 1.0 * inch
        # Draw the image at the bottom right corner
        canvas.drawImage(image_path, width - image_width - 50, 50, width=image_width, height=image_height)
    ind = 0
    for i in range(0,len(officer)):
        if officer[i]==':':
            ind=i
            break
    
    name=officer[i+2:]
    uid=officer[0:i-1]

    month_dict_inv = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
    }

    name_tmp=name.replace(" ","_")
    # Create a SimpleDocTemplate object for the PDF
    pdf_filename = os.path.join(os.getcwd(), f'mess_bill_{name_tmp}.pdf')  # Ensuring the directory is writable
    pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)

    
    # Get the current date
    current_date = datetime.now()

    # Extract the month and year
    current_month = str(current_date.month)
    current_year = str(current_date.year)
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Define table data and style for the first table
    month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
    }
    data1 = [
        ["", "",  "OFERS MESS : 621 EME BN", ""],
        ["Name: ",name, "Bill Month: ", month + " "+current_year, "Bill Date:", current_date],
        ["Unit: ", get_unit(uid), "Bill no.:", random.randint(100,1000)],
        [],
        [],
    ]

    table_style1 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ])

    table1 = Table(data1, style=table_style1)

    month=month_dict_inv[month]
    print (month)
    total_bill=get_total_bill(officer,arrears,month,year)
    print (total_bill)
    # Define table data and style for the second table, ensuring Rupee symbol usage
    data2=[]
    data2.append(["Ser", "Description", "Amount", "Remarks"])
    for i in total_bill:
        data2.append(i)      
     
    data2.append([])
    data2.append([])
    
    table_style2 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Ensuring Rupee symbol display
        ('BOTTOMPADDING', (0, 0), (-1, 0), 18),
    ])


    table2 = Table(data2, style=table_style2)


    data3=[
    ["Payment be made through POS machine/ Bank Acct / QR Code :-"],
    ["A/c Name - OFFRS MESS ACCT 621 EME BN"],
    ["A/c No - 34328506911"],
    ["IFSC: SBIN0016944"],
    ["Branch - SBI, CHANGSARI"],
    ]

    table_style3 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Ensuring Rupee symbol display
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ])
    table3 = Table(data3, style=table_style3)

    # Elements to build in the PDF (add the table and the QR code image if needed)
    elements = [table1, table2, table3]

    # Build the PDF
    pdf.build(elements, onLaterPages=onLaterPages)

    ret = []
    ret.append("PDF generated at:" + pdf_filename)
    ret.append(f'mess_bill_{name_tmp}.pdf')

    
    return ret
