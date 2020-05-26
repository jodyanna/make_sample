"""Class module for making sample data sets in different data structures"""

import random


class Human:
    first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Taylor', 'Charlotte', 'Amelia', 'Evelyn',
                   'Abigail', 'Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Jennifer', 'Maria', 'Susan',
                   'Margaret', 'Dorothy', 'Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah',
                   'Oliver', 'Jacob', 'John', 'Robert', 'Michael', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez',
                  'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson',
                  'Thompson', 'White', 'Lopez', 'Lee', 'Gonzalez', 'Harris', 'Clark']

    def __init__(self, first_name="John", last_name="Doe", telephone="630-555-0000"):
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone

    def __repr__(self):
        return f'Human(first_name="{self.first_name}", last_name="{self.last_name}", telephone="{self.telephone}")'

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.telephone}"

    def fullname(self):
        """Concatenate first and last name to create full name."""
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def set_first_names(cls, first_names):
        """Rewrite default first_names list with custom list.
        :param first_names: list of strings
        """
        cls.first_names = first_names

    @classmethod
    def set_last_names(cls, last_names):
        """Rewrite default l_names list with custom list.
        :param last_names: list of strings
        """
        cls.last_names = last_names

    @classmethod
    def add_first_name(cls, first_name):
        """Add new first name to first_names list
        :param first_name: string
        """
        if first_name in cls.first_names:
            print("Name already exists.")
        else:
            cls.first_names.append(first_name)

    @classmethod
    def add_last_name(cls, last_name):
        """Add new last name to l_names list
        :param last_name: string
        """
        if last_name in cls.last_names:
            print("Name already exists.")
        else:
            cls.last_names.append(last_name)

    @classmethod
    def add_full_name(cls, name):
        """Add both a new first and last name to respective list
        :param name: string
        """
        try:
            first_name, last_name = name.split(" ")
            cls.first_names.append(first_name)
            cls.last_names.append(last_name)
        except Exception as err:
            print(f"ERROR: {err}\nName input must be formatted as 'first last'. Ex: John Doe")


class Maker(Human):
    @classmethod
    def create_random_human(cls):
        """Create instance of Human with randomly generated attributes"""
        first_name = cls.first_names[random.randint(0, len(cls.first_names) - 1)]
        last_name = cls.last_names[random.randint(0, len(cls.last_names) - 1)]
        telephone = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}-{random.randint(0, 9)}" \
                    f"{random.randint(0, 9)}{random.randint(0, 9)}-{random.randint(0, 9)}{random.randint(0, 9)}" \
                    f"{random.randint(0, 9)}{random.randint(0, 9)}"
        return Human(first_name, last_name, telephone)

    @classmethod
    def create_multiple_random_humans(cls, count):
        """Create a list of multiple Human instances with randomly generated attributes"""
        return [cls.create_random_human() for _ in range(count)]
