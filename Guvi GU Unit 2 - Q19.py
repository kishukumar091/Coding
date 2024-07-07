class Pet:
    def eat(self):
        pass
    
    def sleep(self):
        pass
    
    def make_sound(self):
        pass

class Cat(Pet):
    def eat(self):
        print("Cat is eating.")

    def sleep(self):
        print("Cat is sleeping.")

    def make_sound(self):
        print("Cat is purring.")

class Dog(Pet):
    def eat(self):
        print("Dog is eating.")

    def sleep(self):
        print("Dog is sleeping.")

    def make_sound(self):
        print("Dog is wagging its tail.")

class Bird(Pet):
    def eat(self):
        print("Bird is eating.")

    def sleep(self):
        print("Bird is sleeping.")

    def make_sound(self):
        print("Bird is chirping.")

# Main program
def main():
    while True:
        
        pet_type = input("").lower()
        
        if pet_type == 'quit':
            print("Quitting the program.")
            break
        
        elif pet_type not in ['cat', 'dog', 'bird']:
            print("Invalid input. Please enter a valid pet type (cat/dog/bird).")
            continue

        pet_action = input("").lower()
        if pet_action == 'quit':
            print("Quitting the program.")
            break
        elif pet_action not in ['eat', 'sleep', 'make_sound']:
            print("Invalid input. Please enter a valid action (eat/sleep/make_sound/quit).")
            continue

        if pet_type == 'cat':
            cat = Cat()
            if pet_action == 'eat':
                cat.eat()
            elif pet_action == 'sleep':
                cat.sleep()
            elif pet_action == 'make_sound':
                cat.make_sound()

        elif pet_type == 'dog':
            dog = Dog()
            if pet_action == 'eat':
                dog.eat()
            elif pet_action == 'sleep':
                dog.sleep()
            elif pet_action == 'make_sound':
                dog.make_sound()

        elif pet_type == 'bird':
            bird = Bird()
            if pet_action == 'eat':
                bird.eat()
            elif pet_action == 'sleep':
                bird.sleep()
            elif pet_action == 'make_sound':
                bird.make_sound()
            
        
if __name__ == "__main__":
    main()
