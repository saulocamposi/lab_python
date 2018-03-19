class Person:
    name = "Person Name"

    def change_name(self, name_param):
        self.name = name_param

person = Person()
print (person.name)
person.change_name("Saulera")
print (person.name)

class Hello:
    hello = "hello"

hello = Hello()
print (Hello.hello)
