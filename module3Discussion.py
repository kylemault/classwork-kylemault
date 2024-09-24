class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!\n")

# Creating instances
user1 = User("Will", "Smith", 30, "will@example.com", "New York")
user2 = User("John", "Johnson", 25, "John@example.com", "Los Angeles")
user3 = User("Charlie", "Williams", 35, "charlie@example.com", "Chicago")
user4 = User("Brown", "Brown", 28, "Brown@example.com", "Miami")
user5 = User("Kyle", "Davis", 40, "kyle@example.com", "Seattle")

# Calling methods for each user
for user in [user1, user2, user3, user4, user5]:
    user.describe_user()
    user.greet_user()
