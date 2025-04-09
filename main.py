import random
import threading
import time

from Animal import Animal

food_count = 0
lock = threading.RLock()


def list_animals_imanuel():

    animal_list = [
        Animal("Elephant", 15),
        Animal("Giraffe", 9),
        Animal("Horse", 5),
        Animal("Zebra", 5),
        Animal("Deer", 3)]
    return animal_list


def most_hungry_imanuel():
    pass


def most_amount_fed_imanuel():
    pass


def feeding_task(cond, animal_list, count):
    global food_count

    for i in range(count):
        with cond:
            time.sleep(.5)
            #print("Feeding Task Started")
            #pick random animal, make it hungry
            print("SELECTING RANDOM ANIMAL!!!!!!!!")
            rand_animal= random.choice(animal_list)
            rand_animal.set_hungry_count()

            #While the food source is too low wait for deposit
            while rand_animal.get_required_food() > food_count:
                cond.notify_all()
                print(f'Food count is {food_count} but {rand_animal.get_name()}'
                      f' needs {rand_animal.get_required_food()}. refilling')
                cond.wait()
            print(f"Now feeding {rand_animal.get_name()}")
            rand_animal.set_feeding_count(10)
            food_count -= rand_animal.get_required_food()


def deposit_task(cond):
    global food_count
    while True:
        with cond:
            time.sleep(.05)
            #print("Deposit Task Started")
            #deposit random amount of food
            food_count += random.randint(1, 20)
            print("deposited: Food count is now ", food_count)
            time.sleep(.5)
            cond.notify_all()
            cond.wait()


def main():
    #Initialize
    animal_list = list_animals_imanuel()

    print(f"Zoo Animal Feeding System\nDeveloped by: Imanuel Chatur\nStudent Number: 991637637")
    print("-"*50)

    feed_count = int(input("Enter number of animals to be fed: "))

    condition = threading.Condition(lock)

    feed = threading.Thread(name="Feeding Thread",
                            target=feeding_task,
                            args=(condition,animal_list,feed_count,))

    deposit = threading.Thread(name="Deposit Thread",
                               target=deposit_task,
                               args=(condition,))

    feed.start()
    deposit.start()

    feed.join()
    deposit.join()


if "__main__" == __name__:
    main()
