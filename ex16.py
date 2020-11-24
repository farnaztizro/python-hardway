from sys import argv
script, filename = argv

print(f"we're going to erase {filename}.")
print("if u don't want that hit CTRL-C.")
print("if u do want that, hit RETURN.")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("truncating the file, Good Bye!")
target.truncate()

print("now i'm goin to ask u for 3 lines.")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("i'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it.")
target.close()