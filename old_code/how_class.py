class Circle:
    def __init__(self, diameter):  # __ (Double Underscore) Known as Dunder.
        print("New circle with diameter: {diameter}".format(diameter=diameter))

    def area(self, radius):
        pi = 3.14
        return pi * radius ** 2


circle = Circle()

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)
