import csv

item_1 = input('Item one: ')
sale_1 = float(input('How much did you pay for item 1: '))
sales_1 = float(input('How much did you sell item 1 for: '))


with open('file.csv', 'w', newline='') as f:
    fieldnames = ['Item Name', 'My Cost', 'Sale Cost', 'Profit']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    
    write.writeheader()
    write.writerow({'Item Name' : item_1, 'My Cost' : sale_1, 'Sale Cost' : sales_1, 'Profit' : sales_1 - sale_1})
    
