import random
import threading
import time

from Animal import Animal
from ZooManager import ZooManager

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


def most_hungry_imanuel(animal_list):
    hungry_list = {a.get_name(): a.get_hungry_count() for a in animal_list}
    print(hungry_list)
    return hungry_list


def most_amount_fed_imanuel():
    pass


def feeding_task(cond, animal_list, count):
    global food_count

    for i in range(count):
        with cond:
            rand_animal = random.choice(animal_list)
            rand_animal.set_hungry_count()

            while rand_animal.get_required_food() > food_count:
                print(f'Wait for food: {rand_animal.get_name()} got hungry, not enough food')
                rand_animal.set_hungry_count(1)
                cond.wait()

            print(f"Feed {rand_animal.get_name()}: {food_count}", end="")
            rand_animal.set_feeding_count(10)
            food_count -= rand_animal.get_required_food()
            print(f"---> Stock: {food_count}")


def deposit_task(cond):
    global food_count

    while True:
        with cond:
            if not any(t.is_alive() for t in threading.enumerate() if t.name == "Feeding Thread"):
                print("Task is finito!")
                break

            print(f"\tAdd food: {food_count} Kg ---> ", end="")
            food_count += random.randint(1, 20)
            print(f"Stock: {food_count} Kg")

            cond.notify_all()  #Notify
            time.sleep(.5)


def main():
    #Initialize
    animal_list = list_animals_imanuel()

    print(f"Zoo Animal Feeding System\nDeveloped by: Imanuel Chatur\nStudent Number: 991637637")
    print("-" * 50)

    feed_count = int(input("Enter number of animals to be fed: "))
    print(f"------------------Feeding Begins------------------")

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
    print("\n\nJobs done!")

    db = ZooManager()
    most_hungry_imanuel(animal_list)

    for a in animal_list:
        db.insert_animal(a.get_name(), a.get_hungry_count(), a.get_feed_count())

    print(db.get_animals())


if "__main__" == __name__:
    main()
