filename = "sales_log.txt"

while True:
   print("========================================")
   print("     SALES RECORD MANAGEMENT SYSTEM     ")
   print("========================================")
   print("1. Add Sale Record")
   print("2. View All Records & Summary Statistics")
   print("3. Clear All Sales Data")
   print("4. Exit System")
   print("========================================")

   option = 0

   try:
       option = input("Select Option (1-4): ")
       option = int(option)
       if 5 > option > 0:
           break
       else:
           continue
   except ValueError:
       print(f'\n"{option}" IS NOT A REAL OPTION VALUE. PLEASE TRY AGAIN.\n')
       continue

if option == 1:
   while True:
       print("\n1. Add Record.")
       item_name = input("Enter Name: ")
       sold_quantity = input("Enter Quantity Sold (integer): ")
       price_per_unit = input("Enter Price Per Unit (float): ")
       try:
           sold_quantity = int(sold_quantity)
           price_per_unit = float(price_per_unit)
           break
       except ValueError:
           print("\nINVALID INPUT. PLEASE RETRY AGAIN.\n")
           continue


   total_amount = sold_quantity * price_per_unit


   sold_quantity = str(sold_quantity)
   price_per_unit = str(price_per_unit)
   total_amount = str(total_amount)


   new_record = f"{item_name}, {sold_quantity}, {price_per_unit}, {total_amount}"


   try:
       with open(filename, "a") as f:
           f.write("\n")
           f.write(new_record)
           print("Sale Record Is Saved Successfully.")
   except FileNotFoundError:
       print("Error: File does not exist.")


if option == 2:
   print("\n2. View All Records And Statistics")
   try:
       with open(filename, "r") as f:
           for line in f:
               records = line.split(",")
               item_name = records[0]
               quantity = records[1]
               price_per_unit = records[2]
               total_amount = records[3]
               print(f"Item Name: {item_name} Quantity: {quantity} Price Per Unity: {price_per_unit} Total Amount: {total_amount}")


   except FileNotFoundError:
       print("Sale Record Is Saved Successfully")


if option == 3:
   with open(filename, "w3") as f:
       f.write("")


if option == 4:
   print("Thanks For Using the Sales Record Management System!.")
   exit()

