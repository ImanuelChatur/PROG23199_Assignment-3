import random
import threading
import time

from Animal import Animal

animal_list = []
food_count = 0
lock = threading.RLock()


def list_animals_imanuel():
    global animal_list

    animal_list = [
        Animal("Elephant", 15),
        Animal("Giraffe", 9),
        Animal("Horse", 5),
        Animal("Zebra", 5),
        Animal("Deer", 3)]


def most_hungry_imanuel():
    pass


def most_amount_fed_imanuel():
    pass


def feeding_task(cond):
    while True:
        with cond:
            lock.acquire()
            time.sleep(.5)
            print("Feeding Task Started")
            #pick random animal
            print(random.choice(animal_list).get_name())
            #feed it
            lock.release()


def deposit_task(cond):
    global food_count
    while True:
        with cond:
            time.sleep(.5)
            print("Deposit Task Started")
            #deposit random amount of food


def main():
    #Initialize
    list_animals_imanuel()

    print(f"Zoo Animal Feeding System\nDeveloped by: Imanuel Chatur\nStudent Number: 991637637")
    print("-"*50)
    feed_count = int(input("Enter number of animals to be fed: "))

    condition = threading.Condition(lock)

    feed = threading.Thread(name="Feeding Thread", target=feeding_task(condition), args=(condition,))
    deposit = threading.Thread(name="Deposit Thread", target=deposit_task(condition), args=(condition,))

    feed.start()
    deposit.start()

    feed.join()
    deposit.join()


if "__main__" == __name__:
    main()
