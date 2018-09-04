class User:
    def __init__(self, name="", number_of_tacos=5, score=0):
        """Creates an object of a type of user."""
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def get_name(self):
        """Get name."""
        return self.name

    def get_score(self):
        """Get score."""
        return self.score

    def update_number_of_tacos(self, n):
        """Update number of tacos."""
        self.number_of_tacos = n

    def __str__(self):
        """Creates string method"""
        return "{}, {} points, {} tacos left.".format(self.name, self.score, self.number_of_tacos)

    def give_tacos(self, other_user, tacos, points):
        """Give tacos and points from one user to another."""
        self.number_of_tacos -= tacos
        other_user.number_of_tacos += tacos
        self.score -= points
        other_user.score += points


user_one = User(name="Luke", number_of_tacos=10, score=20)
user_two = User("Tom", 30, 50)
user_two.give_tacos(user_one, 1, 1)
print(user_one)
print(user_two)
