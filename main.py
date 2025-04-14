# Assignment: 3
# Course: PROG23199
# Submission date: 2025-04-13
# Name: Imanuel Chatur
# Sheridan ID: 991637637
# Instructors name: Syed Tanbeer
import random
import threading
import time

from Animal import Animal
from ZooManager import ZooManager

# Declare lock and global food_count
food_count = 0
lock = threading.RLock()


def list_animals_imanuel():
    """
    Description:
        Pre-generated list of animals

    :returns
        animal_list (Animal): List of animals
    """
    animal_list = [
        Animal("Elephant", 15),
        Animal("Giraffe", 9),
        Animal("Horse", 5),
        Animal("Zebra", 5),
        Animal("Deer", 3)]
    return animal_list


def most_hungry_imanuel(animal_list):
    most_hungry = max(a.get_hungry_count() for a in animal_list)
    most_hungry_list = [a for a in animal_list if a.get_hungry_count() == most_hungry]
    return most_hungry_list


def most_amount_fed_imanuel(animal_list):
    most_fed = max(a.get_feed_count() for a in animal_list)
    most_fed_list = [a for a in animal_list if a.get_feed_count() == most_fed]
    return most_fed_list


def feeding_task(cond, animal_list, count):
    global food_count

    for i in range(count):
        with cond:
            rand_animal = random.choice(animal_list)
            hungry_count = rand_animal.get_hungry_count() + 1
            feed_count = rand_animal.get_feed_count()

            while rand_animal.get_required_food() > food_count:
                print(f'Wait for food: {rand_animal.get_name()} got hungry, not enough food')
                hungry_count += 1
                cond.wait()

            print(f"Feed {rand_animal.get_name()}: {food_count} Kg", end="")
            feed_count += 1
            food_count -= rand_animal.get_required_food()
            print(f"---> Stock: {food_count} Kg")

            rand_animal.set_hungry_count(hungry_count)
            rand_animal.set_feeding_count(feed_count)


def deposit_task(cond):
    global food_count

    while True:
        with cond:
            if not any(t.is_alive() for t in threading.enumerate() if t.name == "Feeding Thread"):
                break

            print(f"\tAdd food: {food_count} Kg ---> ", end="")
            food_count += random.randint(1, 20)
            print(f"Stock: {food_count} Kg")

            cond.notify_all()  # Notify
            time.sleep(.5)


def display_animals(animal_list):
    print("-" * 20, ": Animal Feeding Summary :", "-" * 20)
    for a in animal_list:
        print(a)
    print("The highest amount of food consumed by: ", end="")
    most_fed = most_amount_fed_imanuel(animal_list)
    print(", ".join(a.get_name() for a in most_fed))
    print("The most hungry animal: ", end="")
    most_hungry = most_hungry_imanuel(animal_list)
    print(", ".join(a.get_name() for a in most_hungry))


    total_food = sum(map(lambda animal: animal.calculate_food_consumed(), animal_list))
    print(f"Total food consumed by all {sum(a.get_feed_count() for a in animal_list)} animals: "
          f"{total_food} Kg")

def main():
    animal_list = list_animals_imanuel()
    print(f"Zoo Animal Feeding System\nDeveloped by: Imanuel Chatur\nStudent Number: 991637637")
    print("-" * 50)

    feed_count = int(input("Enter number of animals to be fed: "))
    print(f"------------------Feeding Begins------------------")

    # Thread work
    condition = threading.Condition(lock)
    feed = threading.Thread(name="Feeding Thread",
                            target=feeding_task,
                            args=(condition, animal_list, feed_count,))
    deposit = threading.Thread(name="Deposit Thread",
                               target=deposit_task,
                               args=(condition,))
    feed.start()
    deposit.start()

    feed.join()
    deposit.join()

    # Database Management
    db = ZooManager()
    most_hungry_imanuel(animal_list)

    for a in animal_list:
        db.insert_animal(a.get_name(), a.get_hungry_count(), a.get_feed_count())
    display_animals(animal_list)


if "__main__" == __name__:
    main()
