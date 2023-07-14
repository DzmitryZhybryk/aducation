class Person:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @full_name.setter
    def full_name(self, value):
        name_surname = value.split(" ")
        self.first_name = name_surname[0]
        self.last_name = name_surname[1]


if __name__ == '__main__':
    p = Person(first_name="first_name", last_name="last_name")
    print(p.full_name)
    p.full_name = "test test1"
    print(p.full_name)
