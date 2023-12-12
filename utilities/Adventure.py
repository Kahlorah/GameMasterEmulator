import os
import random
import utilities.FateQuestion as FQ
from utilities.MeaningTables import MeaningTables as MT
import utilities.RandomEvent as RE
import utilities.Scene as SC
import pickle

MT = MT()


class Adventure:

    def __init__(self, title):
        self.Title = title
        self.CF = 5
        self.Threads = {}
        self.NPCs = {}

    def pick_npc(self):
        if not self.NPCs:
            return None
        return random.choice(list(self.NPCs.keys()))

    def pick_thread(self):
        if not self.Threads:
            return None
        return random.choice(list(self.Threads.keys()))

    def increase_cf(self):
        if self.CF < 9:
            self.CF = self.CF + 1
        message = "Current Chaos Factor: " + str(self.CF)
        return message

    def decrease_cf(self):
        if self.CF > 1:
            self.CF = self.CF - 1
        message = "Current Chaos Factor: " + str(self.CF)
        return message

    def show_cf(self):
        message = "Current Chaos Factor: " + str(self.CF)
        return message

    def set_cf(self, CF):
        self.CF = CF
        message = "Current Chaos Factor: " + str(self.CF)
        return message

    def add_npc(self,npc,description):
        self.NPCs[npc] = description
        message = "NPC Updated!"
        return message

    def remove_npc(self,npc):
        del self.NPCs[npc]
        message = "NPC Removed!"
        return message

    def add_thread(self,thread,description):
        self.Threads[thread] = description
        message = "Thread Updated!"
        return message

    def remove_thread(self,thread):
        del self.Threads[thread]
        message = "Thread Removed!"
        return message

    def show_npcs(self):
        if not self.NPCs:
            message = "The list is now empty."
        else:
            message = "NPCs:"
            for i in list(self.NPCs.items()):
                description = i[1]
                if description == "":
                    message = message + "\n" + i[0]
                else:
                    message = message + "\n" + i[0] + ": " + i[1]
        return message

    def show_npc(self, npc):
        if npc in self.NPCs:
            description = self.NPCs[npc]
            if description == "":
                message = "This NPC has no description."
            else:
                message = npc + ": " + self.NPCs[npc]
        else:
            message = "Can't find such an NPC."
        return message

    def show_threads(self):
        if not self.Threads:
            message = "The list is now empty."
        else:
            message = "Threads:"
            for i in list(self.Threads.items()):
                description = i[1]
                if description == "":
                    message = message + "\n" + i[0]
                else:
                    message = message + "\n" + i[0] + ": " + i[1]
        return message

    def show_thread(self, thread):
        if thread in self.Threads:
            description = self.Threads[thread]
            if description == "":
                message = "This Thread has no description."
            else:
                message = thread + ": " + self.Threads[thread]
        else:
            message = "Can't find such a Thread."
        return message

    def fate_question(self, certainty):
        certainty = getattr(FQ.Certainty, certainty, None)
        if certainty is None:
            message = "Please make sure you entered correct Certainty Level: \n"
            message = message + self.certainty()
        else:
            message = FQ.fate_question(self, certainty)
        return message

    def pick_words(self, table_name, num_of_words):
        table = getattr(MT, table_name, None)
        if table is None:
            message = "Please make sure you entered the correct table name. Available tables are:\n"
            message = message + self.meaning_tables()
        else:
            message = MT.pick_words(table, num_of_words)
        return message

    def event_description(self):
        message = RE.event_description()
        return message

    def event_action(self):
        message = RE.event_action()
        return message

    def get_prompt(self):
        message = RE.get_prompt()
        return message

    def random_event(self):
        message = RE.random_event(self)
        return message

    def generate_scene(self):
        message = SC.generate_scene()
        return message

    def scene_adjustment(self):
        message = SC.scene_adjustment()
        return message

    def next_scene(self):
        message = SC.next_scene(self)
        return message

    def save_adventure(self):
        file_name = "saves\\" + self.Title + ".pkl"
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)
        message = "Adventure Saved!"
        return message

    def load_adventure(self,title):
        file_name = "saves\\" + title + ".pkl"
        with open(file_name, 'rb') as file:
            loaded_instance = pickle.load(file)
        message = "Adventure Loaded!"
        return message, loaded_instance

    def list_saves(self):
        files = []
        for filename in os.listdir("saves"):
            path = os.path.join("saves", filename)
            if os.path.isfile(path):
                files.append(filename.split(".")[0])
        return files

    def del_save(self, title):
        file_path = "saves\\" + title + ".pkl"
        os.remove(file_path)
        message = "Adventure Deleted!"
        return message

    def meaning_tables(self):
        text = "ADVENTURE_TONE, ALIEN_SPECIES, ANIMAL_ACTION, ARMY, CAVERN,\n"
        text = text + "CHARACTER, CHARACTER_ACTION_COMBAT, CHARACTER_ACTION_GENERAL,\n"
        text = text + "CHARACTER_APPEARANCE, CHARACTER_BACKGROUND, CHARACTER_CONVERSATION,\n"
        text = text + "CHARACTER_DESCRIPTORS, CHARACTER_IDENTITY, CHARACTER_MOTIVATION,\n"
        text = text + "CHARACTER_PERSONALITY, CHARACTER_SKILL, CHARACTER_TRAIT, CITY,\n"
        text = text + "CIVILIZATION, CREATURE, CREATURE_ABILITY, CRYPTIC_MESSAGE,\n"
        text = text + "CURSE, DOMICILE, DUNGEON, FOREST, GOD, LEGEND, LOCATION,\n"
        text = text + "LOOT, MAGIC_ITEM, MUTATION, NAME, NOBLE_HOUSE, OBJECT,\n"
        text = text + "PLOT_TWIST, POWER, SMELL, SOUND, SPELL_EFFECT, STARSHIP,\n"
        text = text + "TERRAIN, TRAP, UNDEAD, VISION"
        return text

    def certainty(self):
        text = "CERTAIN, NEARLY_CERTAIN, VERY_LIKELY, LIKELY, NORMAL,\n"
        text = text + "UNLIKELY, VERY_UNLIKELY, NEARLY_IMPOSSIBLE, IMPOSSIBLE"
        return text
