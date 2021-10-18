'''
def main():
    plant_seasion = {
        "blueberry": "fall or spring",
        "tomato": "spring",
        "pumpkin": "late spring",
        "cabbage": "spring or late summer",
        "strawberry": "early spring"
    }


    while True:
        user_input = input("Enter a plant name: ")
        user_input = user_input.lower()
        if user_input == "q":
            break
        if user_input in plant_seasion:
            print (plant_seasion[user_input])
        else:
            print("I don't know when to plant " + user_input)

if __name__ == "__main__":
    main()
'''

class Fence:
    def __init__(self, style, price_per_foot):
        self.style = style
        self.price_per_foot = price_per_foot

    def get_cost(self, length):
        length_min = 6
        length_max = 100
        discount = 20
        cost = length * self.price_per_foot
        if length < length_min:
            cost = length_min * self.price_per_foot
        elif length > length_max:
            cost = cost - discount
        return cost

