""" Question 3.6 """


class AnimalShelter(object):
    class LinkedListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        self.cats_first = None
        self.cats_last = None
        self.dogs_first = None
        self.dogs_last = None
        self.time = 0

    def enqueue(self, animal):
        node = AnimalShelter.LinkedListNode([animal,self.time])
        if animal[0] == "cat":
            if not self.cats_first:
                self.cats_first = node
            else:
                self.cats_last.next = node
            self.cats_last = node
        elif animal[0] == "dog":
            if not self.dogs_first:
                self.dogs_first = node
            else:
                self.dogs_last.next = node
            self.dogs_last = node
        self.time += 1

    def dequeueDog(self):
        if not self.dogs_first:
            return None
        remove_node = self.dogs_first
        self.dogs_first = self.dogs_first.next
        if not self.dogs_first:
            self.dogs_last = None
        return remove_node.val

    def dequeueCat(self):
        if not self.cats_first:
            return None
        remove_node = self.cats_first
        self.cats_first = self.cats_first.next
        if not self.cats_first:
            self.cats_last = None
        return remove_node.val

    def peek_cats(self):
        if not self.cats_first:
            return None
        return self.cats_first.val

    def peek_dogs(self):
        if not self.dogs_first:
            return None
        return self.dogs_first.val

    def dequeueAny(self):
        first_dog = self.peek_dogs()
        first_cat = self.peek_cats()
        animal = None
        if not first_cat and not first_dog:
            return None
        elif not first_dog:
            animal = first_cat
        elif not first_cat:
            animal = first_dog
        else:
            if first_cat[1] > first_dog[1]:
                animal = first_dog
            else:
                animal = first_cat
        if animal[0][0] == "cat":
            return self.dequeueCat()
        else:
            return self.dequeueDog()

shelter = AnimalShelter()
shelter.enqueue(["cat", "cat1"])
shelter.enqueue(["dog", "dog1"])
shelter.enqueue(["cat", "cat2"])
shelter.enqueue(["dog", "dog2"])
shelter.enqueue(["cat", "cat3"])
shelter.enqueue(["cat", "cat4"])
shelter.enqueue(["dog", "dog3"])
shelter.enqueue(["dog", "dog4"])
print(shelter.dequeueAny())
print(shelter.dequeueAny())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
