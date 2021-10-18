width = 6
row = 4
character = "*"
row_count = 0

while row_count < row:
    width_count = 0
    while width_count < width:
        if row_count == 0 or row_count == row - 1:
            print(character, end = "")
        else:
            if width_count == 0 or width_count == width - 1:
                print(character, end = "")
            else:
                print(" ", end = "")
        width_count += 1
    row_count += 1
    print()