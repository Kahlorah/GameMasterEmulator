import random
from utilities.MeaningTables import MeaningTables as MT

MT = MT()


def event_action():
    list1 = [
        "Abandon", "Accompany", "Activate", "Agree", "Ambush", "Arrive", "Assist", "Attack", "Attain", "Bargain",
        "Befriend", "Bestow", "Betray", "Block", "Break", "Carry", "Celebrate", "Change", "Close", "Combine",
        "Communicate", "Conceal", "Continue", "Control", "Create", "Deceive", "Decrease", "Defend", "Delay", "Deny",
        "Depart", "Deposit", "Destroy", "Dispute", "Disrupt", "Distrust", "Divide", "Drop", "Easy", "Energize",
        "Escape", "Expose", "Fail", "Fight", "Flee", "Free", "Guide", "Harm", "Heal", "Hinder", "Imitate", "Imprison",
        "Increase", "Indulge", "Inform", "Inquire", "Inspect", "Invade", "Leave", "Lure", "Misuse", "Move", "Neglect",
        "Observe", "Open", "Oppose", "Overthrow", "Praise", "Proceed", "Protect", "Punish", "Pursue", "Recruit",
        "Refuse","Release", "Relinquish", "Repair", "Repulse", "Return", "Reward", "Ruin", "Separate", "Start", "Stop",
        "Strange","Struggle", "Succeed", "Support", "Suppress", "Take", "Threaten", "Transform", "Trap", "Travel", "Triumph",
        "Truce", "Trust", "Use", "Usurp", "Waste"
    ]
    list2 = [
    "Advantage", "Adversity", "Agreement", "Animal", "Attention", "Balance", "Battle", "Benefits", "Building", "Burden",
    "Bureaucracy", "Business", "Chaos", "Comfort", "Completion", "Conflict", "Cooperation", "Danger", "Defense", "Depletion",
    "Disadvantage", "Distraction", "Elements", "Emotion", "Enemy", "Energy", "Environment", "Expectation", "Exterior",
    "Extravagance", "Failure", "Fame", "Fear", "Freedom", "Friend", "Goal", "Group", "Health", "Hindrance", "Home", "Hope",
    "Idea", "Illness", "Illusion", "Individual", "Information", "Innocent", "Intellect", "Interior", "Investment",
    "Leadership", "Legal", "Location", "Military", "Misfortune", "Mundane", "Nature", "Needs", "News", "Normal", "Object",
    "Obscurity", "Official", "Opposition", "Outside", "Pain", "Path", "Peace", "People", "Personal", "Physical", "Plot",
    "Portal", "Possessions", "Poverty", "Power", "Prison", "Project", "Protection", "Reassurance", "Representative",
    "Riches", "Safety", "Strength", "Success", "Suffering", "Surprise", "Tactic", "Technology", "Tension", "Time", "Trial",
    "Value", "Vehicle", "Victory", "Vulnerability", "Weapon", "Weather", "Work", "Wound"
]
    return list1[random.randint(1, 100) - 1] + " " + list2[random.randint(1, 100) - 1]


def event_description():
    list1 = [
    "Adventurously", "Aggressively", "Anxiously", "Awkwardly", "Beautifully", "Bleakly", "Boldly", "Bravely", "Busily",
    "Calmly", "Carefully", "Carelessly", "Cautiously", "Ceaselessly", "Cheerfully", "Combatively", "Coolly", "Crazily",
    "Curiously", "Dangerously", "Defiantly", "Deliberately", "Delicately", "Delightfully", "Dimly", "Efficiently",
    "Emotionally", "Energetically", "Enormously", "Enthusiastically", "Excitedly", "Fearfully", "Ferociously", "Fiercely",
    "Foolishly", "Fortunately", "Frantically", "Freely", "Frighteningly", "Fully", "Generously", "Gently", "Gladly",
    "Gracefully", "Gratefully", "Happily", "Hastily", "Healthily", "Helpfully", "Helplessly", "Hopelessly", "Innocently",
    "Intensely", "Interestingly", "Irritatingly", "Joyfully", "Kindly", "Lazily", "Lightly", "Loosely", "Loudly",
    "Lovingly", "Loyally", "Majestically", "Meaningfully", "Mechanically", "Mildly", "Miserably", "Mockingly",
    "Mysteriously", "Naturally", "Neatly", "Nicely", "Oddly", "Offensively", "Officially", "Partially", "Passively",
    "Peacefully", "Perfectly", "Playfully", "Politely", "Positively", "Powerfully", "Quaintly", "Quarrelsomely", "Quietly",
    "Roughly", "Rudely", "Ruthlessly", "Slowly", "Softly", "Strangely", "Swiftly", "Threateningly", "Timidly", "Very",
    "Violently", "Wildly", "Yieldingly"
]
    list2 = [
    "Abnormal", "Amusing", "Artificial", "Average", "Beautiful", "Bizarre", "Boring", "Bright", "Broken", "Clean",
    "Cold", "Colorful", "Colorless", "Comforting", "Creepy", "Cute", "Damaged", "Dark", "Defeated", "Dirty",
    "Disagreeable", "Dry", "Dull", "Empty", "Enormous", "Extraordinary", "Extravagant", "Faded", "Familiar", "Fancy",
    "Feeble", "Festive", "Flawless", "Forlorn", "Fragile", "Fragrant", "Fresh", "Full", "Glorious", "Graceful", "Hard",
    "Harsh", "Healthy", "Heavy", "Historical", "Horrible", "Important", "Interesting", "Juvenile", "Lacking", "Large",
    "Lavish", "Lean", "Less", "Lethal", "Lively", "Lonely", "Lovely", "Magnificent", "Mature", "Messy", "Mighty",
    "Military", "Modern", "Mundane", "Mysterious", "Natural", "Normal", "Odd", "Old", "Pale", "Peaceful", "Petite",
    "Plain", "Poor", "Powerful", "Protective", "Quaint", "Rare", "Reassuring", "Remarkable", "Rotten", "Rough", "Ruined",
    "Rustic", "Scary", "Shocking", "Simple", "Small", "Smooth", "Soft", "Strong", "Stylish", "Unpleasant", "Valuable",
    "Vibrant", "Warm", "Watery", "Weak", "Young"
]
    return list1[random.randint(1, 100) - 1] + " " + list2[random.randint(1, 100) - 1]


def get_prompt():
    return event_action() + ", " + event_description()


def random_event(adventure):
    rd_num = random.randint(1, 100)
    if rd_num <= 5:
        l1 = "- Remote Event: \nSomething has happened that the PC were not present for."
        l2 = "- Prompt: \n"+ get_prompt()
        return l1 + "\n" + l2
    elif rd_num <= 10:
        l1 = "- Ambiguous Event: \nSomething has happened that is neither harmful nor helpful, at least not initially."
        l2 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2
    elif rd_num <= 20:
        l1 = "- New NPC: \nA new Non-Player Character enters the adventure."
        l2 = "- NPC Description: \n" + MT.pick_words(MT.CHARACTER, 3)
        l3 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2 + "\n" + l3
    elif rd_num <= 40:
        if not adventure.NPCs:
            return random_event(adventure)
        l1 = "- NPC Action: \nAn existing Non-Player Character does something that impacts the adventure."
        l2 = "- NPC: \n" + adventure.pick_npc()
        l3 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2 + "\n" + l3
    elif rd_num <= 45:
        if not adventure.NPCs:
            return random_event(adventure)
        l1 = "- NPC Negative: \nSomething bad happens to a Non-Player Character."
        l2 = "- NPC: \n" + adventure.pick_npc()
        l3 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2 + "\n" + l3
    elif rd_num <= 50:
        if not adventure.NPCs:
            return random_event(adventure)
        l1 = "- NPC Positive: \nSomething good happens to a Non-Player Character."
        l2 = "- NPC: \n" + adventure.pick_npc()
        l3 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2 + "\n" + l3
    elif rd_num <= 55:
        if not adventure.Threads:
            return random_event(adventure)
        l1 = "- Move Toward A Thread: \nThis event brings the PC one step closer to resolving an open Thread."
        l2 = "- Thread: \n" + adventure.pick_thread()
        l3 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2 + "\n" + l3
    elif rd_num <= 65:
        if not adventure.Threads:
            return random_event(adventure)
        l1 = "- Move Away From A Thread: \nA new hurdle or setback hinders the PC’s progress toward closing a Thread."
        l2 = "- Thread: \n" + adventure.pick_thread()
        l3 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2 + "\n" + l3
    elif rd_num <= 70:
        if not adventure.Threads:
            return random_event(adventure)
        l1 = "- Close A Thread: \nThis event brings about the closure of an open Thread."
        l2 = "- Thread: \n" + adventure.pick_thread()
        l3 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2 + "\n" + l3
    elif rd_num <= 80:
        l1 = "- PC Negative: \nSomething bad happens to the PC."
        l2 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2
    elif rd_num <= 85:
        l1 = "- PC Positive: \nSomething good happens to the PC."
        l2 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2
    else:
        l1 = "- Current Context: \nWhatever is happening in the Scene right now becomes the Focus for this Event."
        l2 = "- Prompt: \n" + get_prompt()
        return l1 + "\n" + l2

