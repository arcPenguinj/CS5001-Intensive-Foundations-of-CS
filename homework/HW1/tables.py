'''
Yici Zhu
CS 5001, Fall 2020
it's a program calculating how many table can be assembled
test cases :
4 tops, 20 legs, 32 screws => 4 tables assembled. Leftover parts: 0 table tops, 4 legs, 0 screws.
20 tops, 88 legs, 166 screws => 20 tables assembled. Leftover parts: 0 table tops, 8 legs, 6 screws.
100 tops, 88 legs, 200 scews => 22 tables assembled. Leftover parts: 78 table tops, 0 legs, 24 screws.

'''

def main ():
    tabletop_number = int(input("Number of tops: "))
    leg_number = int(input("Number of legs: "))
    screw_number = int(input("Number of screws: "))

    top_per_table = tabletop_number / 1
    legs_per_table = leg_number / 4
    screw_per_table = screw_number / 8

    table_can_be_assembled = int(min(top_per_table, legs_per_table, screw_per_table))
    top_leftover = int(tabletop_number - table_can_be_assembled)
    leg_leftover = int(leg_number - table_can_be_assembled * 4)
    screw_leftover = int(screw_number - table_can_be_assembled * 8)

    print (str(table_can_be_assembled) + " tables assembled. Leftover parts: " + str(top_leftover) + " tops, " + str(leg_leftover) + " legs, " + str(screw_leftover) + " screws.")



if __name__ == "__main__":
    main()