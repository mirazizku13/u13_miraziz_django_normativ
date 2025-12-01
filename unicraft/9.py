class User:
    def __init__(self, first_name, last_name, username, email, phone, bio = None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone = phone
        self.bio = bio

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.username} {self.email} {self.phone}'


    def update_email(self, new_email):
        self.email = new_email

    def update_phone(self, new_phone):
        self.phone = new_phone


user1 = User('miraziz', 'mirabdullayev', 'mirazizk', 'miraziz2008@yandex.com', '+998(99)887-66-65')
user2 = User('aziz','davlatov','azizk', 'aziz@gamil.com', '+998(98)584-41-63')
print("user1---------------------------------user1")
print(user1.get_full_name())
print(user1.get_info())
user1.update_email('mirazizmorabdullayev@gmail.com')
user1.update_phone('+998(97)404-83-00')
print("user2---------------------------------user2")
print(user1.get_info())
print(user2.get_full_name())
print(user2.get_info())
user2.update_email('azizk@yandex.com')
user2.update_phone('+998(88)408-42-00')
print(user2.get_info())
print(f'user1 = {user1.get_info()}')
print(f'user2 = {user2.get_info()}')



ism = input("sizning sizmingiz: ")
familiya = input("sizning familiyangiz: ")
user_ismi = input("sizning userismi: ")
email = input("sizning email: ")
telifon_raqam = input("sizning telifon_raqam: ")

user3 = User(ism, familiya, user_ismi, email, telifon_raqam)
print(user3.get_info())

