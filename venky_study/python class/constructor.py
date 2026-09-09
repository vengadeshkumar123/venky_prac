class userDetails:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

user1 = userDetails(1, "vengadesh", "karur")
user2 = userDetails(2, "sudhiksha", "chennai")
print(user1.__dict__)
print(user2.__dict__)
        