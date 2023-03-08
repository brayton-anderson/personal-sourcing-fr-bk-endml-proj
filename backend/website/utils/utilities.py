import uuid
import random
import datetime


class Utilities:
    def utilfunc():
        uid = uuid.uuid4()
        return uid

    def generate_rand(n: int):
        first = random.randint(1, 9)
        first = str(first)
        nrs = [str(random.randrange(10)) for i in range(n - 1)]
        for i in range(len(nrs)):
            first += str(nrs[i])

        return str(first)

    def generate_username(name: str, n: int):
        names = name.lower().split(" ")
        fname = names[0]
        lname = names[1]
        number = Utilities.generate_rand(6)
        uid = Utilities.utilfunc()
        username = "-".join([fname, lname, str(number), str(uid)])

        return str(username)

    def compare_timestamp_data(dt1: int, dt2: int):
        t1 = datetime.datetime.fromtimestamp(dt1 / 1000)
        t2 = datetime.datetime.fromtimestamp(dt2 / 1000)
        diff = t2 - t1

        if diff == datetime.timedelta(days=1):
            return True
        else:
            return False

    def contains_word(words: str):
        list_of_words = words.split()
        if "Bachelor" in list_of_words:
            return 1
        elif "Bachelors" in list_of_words:
            return 1
        elif "Doctorate" in list_of_words:
            return 2
        elif "Master" in list_of_words:
            return 4
        elif "Masters" in list_of_words:
            return 4
        elif "MBA" in list_of_words:
            return 3
        elif "Secondary" in list_of_words:
            return 5
        else:
            return 6
