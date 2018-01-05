class Pet:
    #Create two variables kind and color; assign values
    kind = 'animal'
    color = 'brown'
    def __init__(self, name):#In the constructor, initialize the pets name
        self.name = name #Print the name of the pet and that it is doing tricks
    def do_tricks(self):
        print(self.name + " " + "is doing tricks")
    def speak (self):
        pass

    def climb(self):
        pass
    def jump(self):
        pass
    def __call__(self,roll_action):
        pass
pet_obj = Pet("Shiro")
class Jumper:
    'This is a mixin class for jump'
    def jump(self):
        #Create jump method that prints that a Pet is jumping and the pets name
        print('{} is jumping'.format(self.name))
jump_obj = Jumper()
class Dog(Jumper,Pet):
    kind = 'canine'#You will need to inherit for this to work

    #Change kind to canine

    def __str__(self):
        return('This is a dog named {}'.format(self.name))#Return the name and description of dog

    def __call__(self, action):
        return '{} is rolling over \n'.format(self.name)
        #Rollover action prints the name of the dog and that it is rolling over
        #Owner action returns the name of the owner
        
dog_obj = Dog('Tyson')
class BigDog(Dog):  #You will need to inherit for this to work
    color = 'tan'# Change the color to tan

    def __str__(self):
        return('{} is a big dog'.format(self.name))# Return the name and description of BigDog

    def speak(self):       
        print('{} says Woof!'.format(self.name))# Print dogs name and what it says
bigd_obj = BigDog('Cleo')
class SmallDog(Dog):  #You will need to inherit for this to work
    color = 'brindle'
    # Change the color to brindle

    def __str__(self):
        return('{} is a small dog'.format(self.name))#Return the name and description of SmallDog

    def speak(self):       
        print('{} says wooofyy!'.format(self.name))# Print dogs name and what it says
smalld_obj = SmallDog('Cleo')
class Cat(Jumper, Pet):  #You will need to inherit for this to work
    kind = 'Feline'
    #Change the kind to feline

    def __str__(self):
        return ('{} is a cat with soft fur'.format(self.name)) #Return the name and description of cat

    def speak(self):
        return ('{} speaks cutely with a meow'.format(self.name))# Print cats name and what it says

    def climb(self):
        print ('{} is climbing the trees'.format(self.name)) #Prints the name of the cat and that it is climbing
cat_obj = Cat ('Tylor')

class HouseCat(Cat):  #You will need to inherit for this to work
    color = 'white'#Change the color to white

    def __str__(self):
        return ('{} is a cat with white fur'.format(self.name))#Return the name and description of cat

    def speak(self):
        return ('{} is a cat which says meeowww'.format(self.name))# Print cats name and what it says

housecat_obj = HouseCat('Carlee')

for k in [pet_obj, dog_obj, bigd_obj, smalld_obj, cat_obj, housecat_obj]:
    print(k.__str__())
    print(k.kind)
    print(k.color)
    k.do_tricks()
    k.speak()
    k.jump()

    if isinstance(k, Dog):
        print(k.__call__(action="owner") + "My owner is Vidya")
        print("-----------------------------------------")
    elif isinstance(k, Cat):
        print(k.climb())
        print("-----------------------------------------")
    ###########################################

#EXERCISE YOUR CODE

#    1. Instantiate each class(except jumper)
#    2. Create a list of the instantiated objects
#    3. Loop through the objects
#    4. Print __str__
#    5. print the kind of pet
#    6. Print the Color of the pet
#    7. Have the pet do tricks
#    8. if applicable, print rollover action and the owners name
#    9. If applicable, have the pet climb
#   10. To separate each pet print underscores
