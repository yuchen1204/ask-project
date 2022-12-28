# Table
import math
table = [['PETRON','HARGA','NO'], ['RON95','RM2.05','1'], ['RON97','RM3.95','2'], ['DIESEL','RM2.15','3']]

# Output table
for row in table:
    print(row)

# Ask user to input amount of money and quantity of gasoline
Jumlah_wang = float(input("Masukkan jumlah_wang: "))
myhd = int(input("Masukkan minyak_yang_hendak_diisi: "))

# Prompt user to input gasoline number
choice = input('Enter choice(1/2/3):')

# Call function to calculate number of liters of gasoline to add
def divide(x,y):
    return x / y

if choice == '1':
    num = 2.05
elif choice == '2':
    num = 3.95
elif choice == '3':
    num = 2.15
else:
    print('something with wrong')

Bilangan_liter = math.ceil(divide(myhd, num))

# Calculate user's remaining money
Baki_wang = Jumlah_wang - myhd

# Determine type of gasoline user has selected
if choice == '1':
    type_pt = 'RON95'
elif choice == '2':
    type_pt = 'RON97'
elif choice == '3':
    type_pt = 'DIESEL'

#Output result

print('------------------------------------------------------------------------------')
print(f'type petron: {type_pt}')
print(f'Baki_wang ialah {Baki_wang}')
print(f'Bilangan_liter ialah {Bilangan_liter}')
