# 表格
import math
table = [['PETRON','HARGA','NO'], ['RON95','RM2.05','1'], ['RON97','RM3.95','2'], ['DIESEL','RM2.15','3']]

# 输出表格
for row in table:
    print(row)

# 询问用户输入金额和要加油的数量
Jumlah_wang = float(input("Masukkan jumlah_wang: "))
myhd = int(input("Masukkan minyak_yang_hendak_diisi: "))

# 提示用户输入汽油的编号
choice = input('Enter choice(1/2/3):')

# 调用函数计算要加的汽油的升数
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

# 计算用户剩余的钱
Baki_wang = Jumlah_wang - myhd

# 确定用户选择的汽油的类型
if choice == '1':
    type_pt = 'RON95'
elif choice == '2':
    type_pt = 'RON97'
elif choice == '3':
    type_pt = 'DIESEL'

# 输出结果
print('------------------------------------------------------------------------------')
print(f'type petron: {type_pt}')
print(f'Baki_wang ialah {Baki_wang}')
print(f'Bilangan_liter ialah {Bilangan_liter}')

