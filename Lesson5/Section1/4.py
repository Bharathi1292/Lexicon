class userProfile:
    def __init__(self, **kwargs):
        self.username = kwargs.get("username", "Varma")
        self.email = kwargs.get("email", "Not Provided")
        self.age = kwargs.get("age", 40)

    def __str__(self):
        return (
            f"User Profile\n"
            f"Username: {self.username}\n"
            f"Email   : {self.email}\n"
            f"Age     : {self.age}"
        )
user1 = userProfile(username="Bharathi Dibbidi", email="dibbidibharathi@gmail.com")
user2 = userProfile(username="Mokshagna", age=20)
user3 = userProfile()

print(user1)
print()
print(user2)
print()
print(user3)
