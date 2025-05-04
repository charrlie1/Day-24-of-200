import datetime


class Person:

    #This class defines an abstract data type representing a person.
    #It contains the data  and the operations that can be performed on that data."
    
    def __init__(self, first, last, birthday):
        
        #Initializes a Person object.
        
        self.first_name = first
        self.last_name = last
        self.birthday = birthday

    def get_full_name(self):
        
       # Returns the person's full name.

        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        """
        #Calculates and returns the person's current age in years.
        """
        today = datetime.date.today()
        age = today.year - self.birthday.year
        if today.month < self.birthday.month or (today.month == self.birthday.month and today.day < self.birthday.day):
            age -= 1
        return age

    def __lt__(self, other):
        """
        Defines the less than (<) operator for Person objects.

        provides an abstract way to compare two Person objects based on their last names. The user doesn't need to know the
        details of this comparison logic; they can simply use the '<'
        operator.
        """
        if self.last_name < other.last_name:
            return True
        elif self.last_name > other.last_name:
            return False
        else:  # Last names are the same, compare first names
            return self.first_name < other.first_name

    def __str__(self):

        return f"{self.get_full_name()}, born {self.birthday.strftime('%Y-%m-%d')}"

# Example Usage 
person1 = Person("Charles", "toluwanimi", datetime.date(2005, 4, 30))
person2 = Person("Tony", "stark", datetime.date(2006, 5, 24))

print(person1.get_full_name())  # Interacting through the get_full_name() interface
print(f"{person1.get_full_name()} is {person1.get_age()} years old.") # Using the get_age() interface
print(person1) # Using the __str__() interface
print(person1 < person2) # Using the __lt__() interface for comparison        """
        if self.last_name < other.last_name:
            return True
        elif self.last_name > other.last_name:
            return False
        else:  # Last names are the same, compare first names
            return self.first_name < other.first_name

    def __str__(self):
        return f"{self.get_full_name()}, born {self.birthday.strftime('%Y-%m-%d')}"
