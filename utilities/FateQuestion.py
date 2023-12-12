from enum import Enum
import random
import utilities.RandomEvent as RE


class Certainty(Enum):
    CERTAIN = 5
    NEARLY_CERTAIN = 4
    VERY_LIKELY = 2
    LIKELY = 1
    NORMAL = 0
    UNLIKELY = -1
    VERY_UNLIKELY = -2
    NEARLY_IMPOSSIBLE = -4
    IMPOSSIBLE = -5


def fate_question(adventure, certainty):
    rd_num_one = random.randint(1, 10)
    rd_num_two = random.randint(1, 10)
    outcome = rd_num_one + rd_num_two + certainty.value
    if 18 < outcome < 20:
        l1 = "Exceptional Yes"
    elif outcome >= 11:
        l1 = "Yes"
    elif outcome > 4:
        l1 = "No"
    else:
        l1 = "Exception No"
    if rd_num_one == rd_num_two and rd_num_one <= adventure.CF:
        RE.random_event(adventure)
        l2 = "-----A Random Event is Triggered-----"
        l3 = RE.random_event(adventure)
        return l1 + "\n" + l2 + "\n" + l3
    else:
        return l1

