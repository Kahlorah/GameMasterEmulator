import random
from utilities.MeaningTables import MeaningTables as MT
from utilities import RandomEvent as RE

MT = MT()


def generate_scene():
    who = MT.pick_words(MT.CHARACTER, 3) + "\n"
    what = RE.get_prompt() + "\n"
    where = MT.pick_words(MT.LOCATION, 3) + "\n"
    why = RE.event_action()
    return "WHO: " + who + "WHAT: " + what + "WHERE: " + where + "WHY: " + why


def scene_adjustment():
    adjustment_list = ["Remove A Character", "Add A Character", "Reduce/Remove An Activity", "Increase An Activity",
            "Remove An Object", "Add An Object"]
    rd_num = random.randint(1, 10)
    if rd_num <= 6:
        return random.choice(adjustment_list)
    else:
        choices = random.sample(adjustment_list, 2)
        return choices[0] + ", " + choices[1]


def next_scene(adventure):
    rd_num = random.randint(1, 10)
    if rd_num < adventure.CF:
        return "Expected Scene: things goes on as expected."
    elif rd_num % 2 != 0:
        l1 = "Altered Scene: things doesn't go on as expected."
        l2 = "Adjustment: " + scene_adjustment()
        return l1 + "\n" + l2
    else:
        l1 = "Interrupt Scene: something else entirely happens."
        l2 = RE.random_event(adventure)
        return l1 + "\n" + l2


