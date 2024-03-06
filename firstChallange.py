# Created by Rendy Elang Lesmana - TI23I - 20230040044

nodles = 10000
meat = 50000
garlic = 11000
discount = 10000

print("Welcome to Rendy market")
print("Here is our price list: ")
print("Nodles: ", nodles)
print("Meat: ", meat)
print("Garlic: ", garlic)

customer_money = int(input("Input your money: "))
decision = int(input("Do you want to buy all? 1 for yes, 0 for no.: "))

if (decision == 1):
    if customer_money >= 61000:
        buy_all = nodles + meat + garlic
        total_cost_with_discount = buy_all - discount
        remaining_money = customer_money - total_cost_with_discount
        print("You buyed nodles, meat, and garlic with total cost: ", buy_all)
        print("But you got discount = ", discount)
        print("So your total shopping after getting a discount is", total_cost_with_discount)
        print("So, your remaining money is", remaining_money)
        print("Thank you for coming to our market")
    else:
        print("Sorry your money is not enough")
else:
    print("You don't buy anything. Thank you for coming to our market")