price = int(input("enter price :"))
discount = int(input("enter discont percent "))

discount_amount = (discount/100)

final_price = price - (price * discount_amount)

print(f"your final price is {final_price}")
