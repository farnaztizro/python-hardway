def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("that's enough for a party.\n")

print("give the function numbers directly:")    
cheese_and_crackers(20, 10)

print("or we can use variables from our script:")
amount_of_cheeses = 30
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheeses, amount_of_crackers)

print("we can even do math inside:")
cheese_and_crackers(20+20, 1+2)

print("and we can combile var and math:")
cheese_and_crackers(amount_of_cheeses+10, amount_of_crackers+20)