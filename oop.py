class Parrot:

    # class attribute
    name = ""
    age = 0
    color = "white"

    def eat(self, feed):
        print(" I am eating : ", feed)
        return

# create parrot1 object
parrot1 = Parrot()

parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(parrot1.name, "is", parrot1.age, "years old", parrot1.color)
print(parrot2.name, "is", parrot2.age, "years old", parrot2.color)

parrot1.color = "blue"

print(parrot1.name, "is", parrot1.age, "years old", parrot1.color)
print(parrot2.name, "is", parrot2.age, "years old", parrot2.color)

parrot1.eat("coffee")
parrot2.eat("bread")

