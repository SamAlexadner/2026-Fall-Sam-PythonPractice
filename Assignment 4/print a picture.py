for row in range(7, 0, -1):
    for column in range(row):
        print("*", end="")  # I'm not sure about the spacing, so I follow the picture, not add space
        # print("*", end=" ")  # This is add space for assignment
    print()  # by hand changed line
print(".")

# for row in range(1):
#     print("*" * 7)
# for row in range(1):
#     print("*" * 6)
# for row in range(1):
#     print("*" * 5)
# for row in range(1):
#     print("*" * 4)
# for row in range(1):
#     print("*" * 3)
# for row in range(1):
#     print("*" * 2)
# for row in range(1):
#     print("*" * 1)
# for row in range(1):
#     print(".")

# for row in range(7, 0, -1):
#     print("*" * row)
# print(".")

# while (height:= int(input("Enter the height of the triangle: "))) < 2:
#     print("Input error, please enter a height greater than equal to 2.")
# for row in range(1, height + 1, 1):
#     print("*" * row)