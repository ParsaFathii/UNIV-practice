prices = {
    "pizza": 150000,
    "burger": 120000,
    "salad": 80000
}

food = input("please choose your food (pizza, burger, salad): ")

quantity = int(input("Which do you need: "))

total_price = prices[food] * quantity

offer = input("اگر کد تخفیف ندارید اینتر را بزنید")


discount1 = total_price * 0.15 if total_price > 300000 else 0
discount2 = total_price * 0.20 if offer == "OFF20" else 0


final_offer = max(discount1, discount2)
final_price = total_price - final_offer


print(final_price)
