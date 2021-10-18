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
