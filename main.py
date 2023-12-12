import discord
from utilities.Adventure import Adventure
import re

a = Adventure("default")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    global a

    if message.author == client.user:
        return

    if message.content.startswith("$new_adventure"):
        split = message.content.split(',')
        if len(split) == 1:
            a = Adventure("default")
        else:
            title = split[1].strip()
            a = Adventure(title)
        await message.channel.send("New adventure created!")

    if message.content == "$save":
        a.save_adventure()
        await message.channel.send("Adventure saved!")

    if message.content == "$view_saves":
        saves = a.list_saves()
        text = "List of all saves:"
        for f in saves:
            text = text + "\n" + f
        await message.channel.send(text)

    if message.content.startswith("$del_save"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify the name of the adventure you wish to delete."
        else:
            list_saves = a.list_saves()
            title = split[1].strip()
            if title in list_saves:
                a.del_save(title)
                text = "Adventure " + "\"" + title + "\" has been deleted!"
            else:
                text = "No such save file found."
        await message.channel.send(text)

    if message.content.startswith("$load"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify the name of the adventure you wish to load."
        else:
            list_saves = a.list_saves()
            title = split[1].strip()
            if title in list_saves:
                a = a.load_adventure(title)[1]
                text = "Adventure " + "\"" + title + "\" has been loaded!"
            else:
                text = "No such save file found."
        await message.channel.send(text)

    if message.content.startswith("$fate"):
        split = message.content.split(',')
        if len(split) == 1:
            certainty = "NORMAL"
        else:
            certainty = message.content.split(',')[1].strip().upper()
        await message.channel.send(a.fate_question(certainty))

    if message.content == "$meaning_tables":
        await message.channel.send(a.meaning_tables())

    if message.content == "$certainty_level":
        await message.channel.send(a.certainty())

    if message.content.startswith("$pick"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify the name of the table you wish to pick words from. Available tables are:\n"
            text = text + a.meaning_tables()
        elif len(split) == 2:
            table_name = split[1].strip().upper()
            num_of_words = 3
            text = a.pick_words(table_name, num_of_words)
        else:
            table_name = split[1].strip().upper()
            num_of_words = split[2].strip()
            if re.match(r'^\d+$', num_of_words):
                num_of_words = int(num_of_words)
                text = a.pick_words(table_name, num_of_words)
            else:
                text = "Please enter a valid integer as the number of words you wish to pick."

        await message.channel.send(text)

    if message.content == "$event_prompt":
        await message.channel.send(a.get_prompt())

    if message.content == "$random_event":
        await message.channel.send(a.random_event())

    if message.content == "$new_scene":
        await message.channel.send(a.generate_scene())

    if message.content == "$adjust_scene":
        await message.channel.send(a.scene_adjustment())

    if message.content == "$next_scene":
        await message.channel.send(a.next_scene())

    if message.content == "$pick_npc":
        npc = a.pick_npc()
        if npc == None:
            text = "NPC list is empty."
        else:
            text = "Picked NPC: " + npc
        await message.channel.send(text)

    if message.content == "$pick_thread":
        thread = a.pick_thread()
        if thread == None:
            text = "Thread list is empty."
        else:
            text = "Picked thread: " + thread
        await message.channel.send(text)

    if message.content == "$show_cf":
        await message.channel.send(a.show_cf())

    if message.content == "$inc_cf":
        await message.channel.send(a.increase_cf())

    if message.content == "$dec_cf":
        await message.channel.send(a.decrease_cf())

    if message.content.startswith("$set_cf"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify a Chaos Factor value."
        else:
            CF = split[1].strip()
            if re.match(r'^\d+$', CF):
                text = a.set_cf(int(CF))
            else:
                text = "Please enter a valid Chaos Factor value."
        await message.channel.send(text)

    if message.content.startswith("$update_npc"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify the NPC info."
        elif len(split) == 2:
            name = split[1].strip()
            description = ""
            a.add_npc(name, description)
            text = "NPC " + name + " updated!"
        else:
            name = split[1].strip()
            description = split[2].strip()
            a.add_npc(name, description)
            text = "NPC " + name + " updated!"
        await message.channel.send(text)

    if message.content.startswith("$update_thread"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify the Thread info."
        elif len(split) == 2:
            name = split[1].strip()
            description = ""
            a.add_thread(name, description)
            text = "Thread updated!"
        else:
            name = split[1].strip()
            description = split[2].strip()
            a.add_thread(name, description)
            text = "Thread " + name + " updated!"
        await message.channel.send(text)

    if message.content == "$show_all_npcs":
        await message.channel.send(a.show_npcs())

    if message.content == "$show_all_threads":
        await message.channel.send(a.show_threads())

    if message.content.startswith("$show_npc"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify NPC name."
        else:
            name = split[1].strip()
            text = a.show_npc(name)
        await message.channel.send(text)

    if message.content.startswith("$show_thread"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify Thread name."
        else:
            name = split[1].strip()
            text = a.show_thread(name)
        await message.channel.send(text)

    if message.content.startswith("$del_thread"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify Thread name."
        else:
            name = split[1].strip()
            text = a.remove_thread(name)
        await message.channel.send(text)

    if message.content.startswith("$del_npc"):
        split = message.content.split(',')
        if len(split) == 1:
            text = "Please specify NPC name."
        else:
            name = split[1].strip()
            text = a.remove_npc(name)
        await message.channel.send(text)

    if message.content.startswith("$commands"):
        commands_list1 = "- Fate Question: \n"
        commands_list1 = commands_list1 + "Ask Fate Question:\n"
        commands_list1 = commands_list1 + "    $fate, (CERTAINTY)\n"
        commands_list1 = commands_list1 + "Check Certainty Level list:\n"
        commands_list1 = commands_list1 + "    $certainty_level\n"
        commands_list1 = commands_list1 + "- Roll on Meaning Tables:\n"
        commands_list1 = commands_list1 + "Roll on a specific meaning table:\n"
        commands_list1 = commands_list1 + "    $pick, TABLE_NAME, (NUM_OF_WORDS)\n"
        commands_list1 = commands_list1 + "Check Meaning Table list:\n"
        commands_list1 = commands_list1 + "    $meaning_tables\n"
        commands_list1 = commands_list1 + "- Random Event:\n"
        commands_list1 = commands_list1 + "Get a Random Event Prompt:\n"
        commands_list1 = commands_list1 + "    $event_prompt\n"
        commands_list1 = commands_list1 + "Generate a Random Event:\n"
        commands_list1 = commands_list1 + "    $random_event\n"
        commands_list1 = commands_list1 + "- Scenes:\n"
        commands_list1 = commands_list1 + "Generate a Random Scene:\n"
        commands_list1 = commands_list1 + "    $new_scene\n"
        commands_list1 = commands_list1 + "Get a Scene Adjustment:\n"
        commands_list1 = commands_list1 + "    $adjust_scene\n"
        commands_list1 = commands_list1 + "Get Next Scene:\n"
        commands_list1 = commands_list1 + "    $next_scene\n"

        commands_list2 = "- Adventure Management:\n"
        commands_list2 = commands_list2 + "Create a new adventure:\n"
        commands_list2 = commands_list2 + "    $new_adventure, (ADVENTURE_NAME)\n"
        commands_list2 = commands_list2 + "Save Adventure:\n"
        commands_list2 = commands_list2 + "    $save\n"
        commands_list2 = commands_list2 + "Load Adventure:\n"
        commands_list2 = commands_list2 + "    $load, (ADVENTURE_NAME)\n"
        commands_list2 = commands_list2 + "Delete Adventure:\n"
        commands_list2 = commands_list2 + "    $del_save, (ADVENTURE_NAME)\n"
        commands_list2 = commands_list2 + "View all current saves:\n"
        commands_list2 = commands_list2 + "    $view_saves\n"
        commands_list2 = commands_list2 + "Pick a random NPC:\n"
        commands_list2 = commands_list2 + "    $pick_npc\n"
        commands_list2 = commands_list2 + "Pick a random Thread:\n"
        commands_list2 = commands_list2 + "    $pick_thread\n"
        commands_list2 = commands_list2 + "Show current CF:\n"
        commands_list2 = commands_list2 + "    $show_cf\n"
        commands_list2 = commands_list2 + "Increase CF:\n"
        commands_list2 = commands_list2 + "    $increase_cf\n"
        commands_list2 = commands_list2 + "Decrease CF:\n"
        commands_list2 = commands_list2 + "    $decrease_cf\n"
        commands_list2 = commands_list2 + "Set CF:\n"
        commands_list2 = commands_list2 + "    $set_cf, CF\n"
        commands_list2 = commands_list2 + "Add/Edit NPC:\n"
        commands_list2 = commands_list2 + "    $update_npc, NPC_NAME, (NPC_DESCRIPTION)\n"
        commands_list2 = commands_list2 + "Show specific NPC info:\n"
        commands_list2 = commands_list2 + "    $show_npc, NPC_NAME\n"
        commands_list2 = commands_list2 + "Delete NPC:\n"
        commands_list2 = commands_list2 + "    $del_npc, NPC_NAME\n"
        commands_list2 = commands_list2 + "Add/Edit Thread:\n"
        commands_list2 = commands_list2 + "    $update_thread, THREAD_NAME, (THREAD_DESCRIPTION)\n"
        commands_list2 = commands_list2 + "Show specific Thread info:\n"
        commands_list2 = commands_list2 + "    $show_thread, THREAD_NAME\n"
        commands_list2 = commands_list2 + "Delete Thread:\n"
        commands_list2 = commands_list2 + "    $del_thread, THREAD_NAME\n"
        commands_list2 = commands_list2 + "Show all NPCs:\n"
        commands_list2 = commands_list2 + "    $show_all_npcs\n"
        commands_list2 = commands_list2 + "Show all Threads:\n"
        commands_list2 = commands_list2 + "    $show_all_threads\n"

        await message.channel.send(commands_list1)
        await message.channel.send(commands_list2)

TOKEN = 'MTE4MzU3NTI2MTE2NjQ0MDU3MA.GwPe9a.j6oEvSstCG5fKFxyfkraKNEb38KQIWOXVkRV0U'

client.run(TOKEN)
