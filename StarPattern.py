# Basic Way
# for i in range(3):
#     print("***")
# print("   ")
# for i in range(3):
#     if i == 1:
#         print("* *")
#     else:
#         print("***")
# print("   ")
# for i in range(3):
#     if i == 1:
#         print(" * ")
#     else:
#         print("* *")
print("   ")
for x in range(3):
    for y in range(3):
        print("*", end =" ")
    print()
print("   ")



for x in range(3):
    for y in range(3):
        if y == 1 and x == 1:
            print(" ", end =" ")
        else:
            print("*", end =" ")
    print()
print("   ")
for x in range(3):
    for y in range(3):
        if ((x == 0 or x == 2) and (y == 1)) or (x == 1 and (y == 0 or y == 2)):
            print(" ", end =" ")
        else:
            print("*", end =" ")
    print()