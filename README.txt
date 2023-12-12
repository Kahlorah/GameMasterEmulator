This is a random prompt generator for solo RPG playing based on MythicGME 2e.
The main.py calls registers a discord bot that responds to message commands in discord channels.

1. Asking Fate Questions
    Use Fate Questions to learn new details about your adventure. If you think an expectation should be tested because it
    is important or uncertain, then ask a Fate Question.
    Fate Check:
    1) FORM A QUESTION: Ask a Yes/No question.
    2) ASSIGN ODDS: Give the Odds of the Question being a Yes: 50/50, Likely, Very Likely, Nearly Certain, Certain, Unlikely,
        Very Unlikely, Nearly Impossible, or Impossible.
    3) GET MODIFIERS: Determine modifiers for the Odds, adding them together.
    4) ROLL 2D10: Roll 2d10, adding them together and apply the modifiers to the roll.
        - The answer is Yes with a modified roll total of 11 or more.
        - A total of 18-20 is an Exceptional Yes.
        - A result of 10 or less is a No.
        - A result of 2-4 is an Exceptional No.
        - RANDOM EVENT: If you rolled a double-digit (11, 22, 33, etc.) and the single digit value of that number
          is equal to or less than the current CF (Chaos Factor), then a Random Event happens.
    5) INTERPRET THE RESULTS

2. Generating Random Events
    1) DETERMINE EVENT FOCUS: Roll 1d100 on the Random Event Focus Table to discover what the Random Event is about.
    2) DETERMINE EVENT MEANING: Choose a Meaning Table that fits the Random Event best and roll for two inspirational words.
        Use the words to help interpret the Random Event.
    3) INTERPRET: Combining the adventure Context, the Event Focus, and the Meaning words, come up with an interpretation
        that makes sense to you.
    4) ROLLING ON LISTS: Random Events will sometimes require you to roll on the Threads List or Characters List to select a
        specific Thread or Character.

3. First Scene
    Choose a method to develop the first Scene of an adventure.
    1) RANDOM EVENT: Generate a Random Event to form the start of the Scene.
    2) MEANING TABLES: Choose Meaning Tables and roll as many word pairs as you need for inspiration.
    3) 4W: Roll on the Meaning Tables in a structured way to get the Who, What, Where, and Why of a Scene.
        - Who: Characters Elements Meaning Table.
        - What: Actions Meaning Tables.
        - Where: Locations Elements Meaning Table.
        - Why: Actions Meaning Tables.

4. What is the Next Scene?
    Roll 1d10 to test the next Scene.
    1) EXPECTED SCENE: Decide how you think the next Scene will begin.
    2) ALTERED SCENE: If you roll the CF or less and the number is odd, then the Scene is an Altered Scene.
        Generate an Altered Scene by modifying your Expected Scene. Use one of the strategies below:
        - MEANING TABLES: Choose a Meaning Table and roll for a word pair as inspiration.
        - SCENE ADJUSTMENT TABLE: Roll 1d10 on the Scene Adjustment Table.
    3) INTERRUPT SCENE: If you roll the CF or less and the number is even, then the Scene is an Interrupt Scene.
        Generate a Random Event and use that as the basis for the start of the Scene.

5. Generating NPC Behavior
    1) MEANING TABLE: If you have no expectation for what an NPC will do, then roll a word pair on a Meaning Table of
        your choice for inspiration.
    2) EXPECTATION AND CRUCIAL: If you have an idea of what the NPC will do, and the action is important to your adventure,
        then frame the action as a Fate Question.

6. End Of Scene Bookkeeping
    1) EDIT LIST ELEMENTS: Add new Threads and NPCs that were important in the Scene to the Threads and Characters Lists.
        Remove Threads and Characters from the Lists that are no longer relevant to the adventure.
    2) ADJUST THE CHAOS FACTOR: If the Player Character was mostly in control of the Scene then apply a -1 modifier to
        the Chaos Factor, to a minimum of 1. If the Player Character was mostly not in control during the Scene then
        apply a +1 modifier to the Chaos Factor to a maximum of 9.

8. Methods:
    1) Adventure
        - Create a new adventure:
            from Adventure import Adventure
            a = Adventure(ADVENTURE_NAME)
        - Pick a random NPC:
            a.pick_npc()
        - Pick a random Thread:
            a.pick_thread()
        - Show current CF:
            a.show_cf()
        - Increase CF:
            a.increase_cf()
        - Decrease CF:
            a.decrease_cf()
        - Set CF:
            a.set_cf(CF)
        - Add/Edit NPC:
            a.add_npc(NPC_NAME, NPC_DESCRIPTION)
        - Find specific NPC:
            a.show_npc(NPC_NAME)
        - Remove NPC:
            a.remove_npc(NPC_NAME)
        - Add/Edit Thread:
            a.add_thread(THREAD_NAME, THREAD_DESCRIPTION)
        - Find specific Thread:
            a.show_thread(THREAD_NAME)
        - Remove Thread:
            a.remove_thread(THREAD_NAME)
        - Show all NPCs:
            a.show_npcs()
        - Show all Threads:
            a.show_threads()
    2) FateQuestion
        - Ask Fate Question:
            a.fate_question(CERTAINTY)
        - Certainty Levels:
            CERTAIN, NEARLY_CERTAIN, VERY_LIKELY, LIKELY, NORMAL, UNLIKELY, VERY_UNLIKELY, NEARLY_IMPOSSIBLE, IMPOSSIBLE
    3) MeaningTables:
        - Roll on a specific table:
            a.pick_words(TABLE_NAME, NUM_OF_WORDS)
        - Available Tables:
            ADVENTURE_TONE, ALIEN_SPECIES, ANIMAL_ACTION, ARMY, CAVERN, CHARACTER, CHARACTER_ACTION_COMBAT,
            CHARACTER_ACTION_GENERAL, CHARACTER_APPEARANCE, CHARACTER_BACKGROUND, CHARACTER_CONVERSATION,
            CHARACTER_DESCRIPTORS, CHARACTER_IDENTITY, CHARACTER_MOTIVATION, CHARACTER_PERSONALITY, CHARACTER_SKILL,
            CHARACTER_TRAIT, CITY, CIVILIZATION, CREATURE, CREATURE_ABILITY, CRYPTIC_MESSAGE, CURSE,
            DOMICILE, DUNGEON, FOREST, GOD, LEGEND, LOCATION, LOOT, MAGIC_ITEM, MUTATION, NAME, NOBLE_HOUSE,
            OBJECT, PLOT_TWIST, POWER, SMELL, SOUND, SPELL_EFFECT, STARSHIP, TERRAIN, TRAP, UNDEAD, VISION
    4) RandomEvent:
        - Get a Random Event Description:
            a.event_description()
        - Get a Random Event Action:
            a.event_action()
        - Get a Random Event Prompt (Description + Action):
            a.get_prompt()
        - Generate a Random Event:
            a.random_event()
    5) Scene:
        - Generate a Random Scene:
            a.generate_scene()
        - Get a Scene Adjustment:
            a.scene_adjustment()
        - Get Next Scene:
            a.next_scene()
    6) Save & Load:
        - Save Adventure:
            a.save_adventure()
        - Load Adventure:
            b = a.load_adventure(ADVENTURE_NAME)

9. Discord Commands
    - Fate Question:
        Ask Fate Question:
            $fate, (CERTAINTY)
        Check Certainty Level list:
            $certainty_level
    - Roll on Meaning Tables:
        Roll on a specific meaning table:
            $pick, TABLE_NAME, (NUM_OF_WORDS)
        Check Meaning Table list:
            $meaning_tables
    - Random Event:
        Get a Random Event Prompt:
            $event_prompt
        Generate a Random Event:
            $random_event
    - Scenes:
        Generate a Random Scene:
            $new_scene
        Get a Scene Adjustment:
            $adjust_scene
        Get Next Scene:
            $next_scene
    - Adventure Management:
        Create a new adventure:
            $new_adventure, (ADVENTURE_NAME)
        Save Adventure:
            $save
        Load Adventure:
            $load, (ADVENTURE_NAME)
        Delete Adventure:
            $del_save, (ADVENTURE_NAME)
        View all current saves:
            $view_saves
        Pick a random NPC:
            $pick_npc
        Pick a random Thread:
            $pick_thread
        Show current CF:
            $show_cf
        Increase CF:
            $increase_cf
        Decrease CF:
            $decrease_cf
        Set CF:
            $set_cf, CF
        Add/Edit NPC:
            $update_npc, NPC_NAME, (NPC_DESCRIPTION)
        Show specific NPC info:
            $show_npc, NPC_NAME
        Delete NPC:
            $del_npc, NPC_NAME
        Add/Edit Thread:
            $update_thread, THREAD_NAME, (THREAD_DESCRIPTION)
        Show specific Thread info:
            $show_thread, THREAD_NAME
        Delete Thread:
            $del_thread, THREAD_NAME
        Show all NPCs:
            $show_all_npcs
        Show all Threads:
            $show_all_threads



