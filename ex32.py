the_count = [1, 2, 3, 4, 5]
fruits = ['oranges', 'apples', 'apricots', 'bananas']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"a fruit of type: {fruit}")    

for i in change:
    print(f"i got {i}")    

element = []    

for i in range(0,6):
    print(f"adding {i} to the list")
    element.append(i)

for i in element:
    print(f"element was: {i}")    
    