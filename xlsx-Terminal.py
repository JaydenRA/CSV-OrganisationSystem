import xlsxwriter

#definitions
workbook = xlsxwriter.Workbook('file.xlsx')
sheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
header = workbook.add_format({'bold': True, 'bg_color': '5f8fc7', 'font_color': 'ffffff'})

#Data 1
item_1 = input('Item one: ')
sale_1 = input('How much did you pay for item 1: ')
sales_1 = input('How much did you sell item 1 for: ')

#output Header
sheet.write('A1', 'Items', header)
sheet.write('B1', 'My Cost', header)
sheet.write('C1', 'Sale Cost', header)
sheet.write('D1', 'Profit', header)

#Output 1
sheet.write('A2', item_1, bold)
sheet.write('B2', sale_1)
sheet.write('C2', sales_1)
sheet.write('D2', '=sum(C2-B2)')

workbook.close()

print("You can find your excel document at this python script's save file")
