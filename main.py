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

if option = 1
