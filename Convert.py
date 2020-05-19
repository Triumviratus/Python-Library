#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

def hanoi(start, middle, finish, discs):
    if discs > 0:
        hanoi(start, finish, middle, discs - 1)
        print("Move disc", discs, "from", start, "to", finish)
        hanoi(middle, start, finish, discs - 1)

hanoi("a", "b", "c", 4)
print()

def factorial(n):
    if n == 0: # Base Case
        return 1
    else:
        return factorial(n-1)*n

for i in range(11):
    print(i, factorial(i))

def convert(base_10_number, new_base):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base_10_number < new_base:
        return convert_string[base_10_number]
    else:
        return convert(base_10_number // new_base, new_base) \
               + convert_string[base_10_number % new_base]

    print(convert(100, 10))
    print(convert(100, 2))
    print(convert(100, 36))

print()
