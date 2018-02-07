# To extract the Invoice date and Invoice no from the data file.

input_file = open("C:/Users/29890/Desktop/OCR/ABBYY/invoice8.txt", "rt")


for each in input_file:
    if "Invoice Number" in each:
        Inv_number = each.split(("Invoice Number"), 1)[1]
    if "Invoice No" in each:
        Inv_number = each.split(("Invoice No"),1)[1]
    if "Invoice Date" in each:
        Inv_date = each.split("Invoice Date", 1)[1]

        

output_file = open("output1.txt","w+")

Inv_number = "Invoice Number" + str(Inv_number)
Inv_date = "Invoice date" + str(Inv_date)
output_file.write(Inv_number)
output_file.write(Inv_date)

input_file.close()
output_file.close()
    
         

