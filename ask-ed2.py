# Gasoline information stored in a dictionary
gas_prices = {
    "RON95": 2.05,
    "RON97": 3.95,
    "DIESEL": 2.15,
}

# Output table
for gas, price in gas_prices.items():
    print(f"{gas}: RM{price}")

# Ask the user to input an amount of money and a quantity of gasoline
Jumlah_wang = float(input("Masukkan jumlah_wang: "))
myhd = int(input("Masukkan minyak_yang_hendak_diisi: "))

# Prompt the user to input a gasoline number
choice = input("Enter choice (RON95/RON97/DIESEL):")

# Call function to calculate the number of liters of gasoline to add
def divide(x, y):
    return x / y

num = gas_prices[choice]
Bilangan_liter = divide(myhd, num)

# Calculate the user's remaining money
Baki_wang = Jumlah_wang - myhd

# Output the result
print("------------------------------------------------------------------------------")
print(f"type petron: {choice}")
print(f"Baki_wang ialah {Baki_wang}")
print(f"Bilangan_liter ialah {Bilangan_liter}")

