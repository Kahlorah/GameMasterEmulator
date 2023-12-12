import random


class MeaningTables:

    def __init__(self):
        self.LOCATION = [
            "Abandoned", "Active", "Artistic", "Atmosphere", "Beautiful", "Bleak", "Bright", "Business", "Calm", "Charming",
            "Clean", "Cluttered", "Cold", "Colorful", "Colorless", "Confusing", "Cramped", "Creepy", "Crude", "Cute",
            "Damaged", "Dangerous", "Dark", "Delightful", "Dirty", "Domestic", "Empty", "Enclosed", "Enormous", "Entrance",
            "Exclusive", "Exposed", "Extravagant", "Familiar", "Fancy", "Festive", "Foreboding", "Fortunate", "Fragrant",
            "Frantic", "Frightening", "Full", "Harmful", "Helpful", "Horrible", "Important", "Impressive", "Inactive", "Intense",
            "Intriguing", "Lively", "Lonely", "Long", "Loud", "Meaningful", "Messy", "Mobile", "Modern", "Mundane", "Mysterious",
            "Natural", "New", "Occupied", "Odd", "Official", "Old", "Open", "Peaceful", "Personal", "Plain", "Portal",
            "Protected", "Protection", "Purposeful", "Quiet", "Reassuring", "Remote", "Resourceful", "Ruined", "Rustic",
            "Safe", "Services", "Simple", "Small", "Spacious", "Storage", "Strange", "Stylish", "Suspicious", "Tall",
            "Threatening", "Tranquil", "Unexpected", "Unpleasant", "Unusual", "Useful", "Warm", "Warning", "Watery", "Welcoming"
        ]
        self.OBJECT = [
            "Active", "Artistic", "Average", "Beautiful", "Bizarre", "Bright", "Clothing", "Clue", "Cold", "Colorful",
            "Communication", "Complicated", "Confusing", "Consumable", "Container", "Creepy", "Crude", "Cute", "Damaged",
            "Dangerous", "Deactivated", "Deliberate", "Delightful", "Desired", "Domestic", "Empty", "Energy", "Enormous",
            "Equipment", "Expected", "Expended", "Extravagant", "Faded", "Familiar", "Fancy", "Flora", "Fortunate", "Fragile",
            "Fragrant", "Frightening", "Garbage", "Guidance", "Hard", "Harmful", "Healing", "Heavy", "Helpful", "Horrible",
            "Important", "Inactive", "Information", "Intriguing", "Large", "Lethal", "Light", "Liquid", "Loud", "Majestic",
            "Meaningful", "Mechanical", "Modern", "Moving", "Multiple", "Mundane", "Mysterious", "Natural", "New", "Odd",
            "Official", "Old", "Ornamental", "Ornate", "Personal", "Powerful", "Prized", "Protection", "Rare", "Ready",
            "Reassuring", "Resource", "Ruined", "Small", "Soft", "Solitary", "Stolen", "Strange", "Stylish", "Threatening",
            "Tool", "Travel", "Unexpected", "Unpleasant", "Unusual", "Useful", "Useless", "Valuable", "Warm", "Weapon",
            "Wet", "Worn"
        ]
        self.CHARACTER = [
            "Accompanied", "Active", "Aggressive", "Ambush", "Animal", "Anxious", "Armed", "Beautiful", "Bold", "Busy",
            "Calm", "Careless", "Casual", "Cautious", "Classy", "Colorful", "Combative", "Crazy", "Creepy", "Curious",
            "Dangerous", "Deceitful", "Defeated", "Defiant", "Delightful", "Emotional", "Energetic", "Equipped", "Excited",
            "Expected", "Familiar", "Fast", "Feeble", "Feminine", "Ferocious", "Foe", "Foolish", "Fortunate", "Fragrant",
            "Frantic", "Friend", "Frightened", "Frightening", "Generous", "Glad", "Happy", "Harmful", "Helpful", "Helpless",
            "Hurt", "Important", "Inactive", "Influential", "Innocent", "Intense", "Knowledgeable", "Large", "Lonely",
            "Loud", "Loyal", "Masculine", "Mighty", "Miserable", "Multiple", "Mundane", "Mysterious", "Natural", "Odd", "Official",
            "Old", "Passive", "Peaceful", "Playful", "Powerful", "Professional", "Protected", "Protecting", "Questioning",
            "Quiet", "Reassuring", "Resourceful", "Seeking", "Skilled", "Slow", "Small", "Stealthy", "Strange", "Strong",
            "Tall", "Thieving", "Threatening", "Triumphant", "Unexpected", "Unnatural", "Unusual", "Violent", "Vocal",
            "Weak", "Wild", "Young"
        ]
        self.CHARACTER_ACTION_COMBAT = [
            "Abandon", "Abuse", "Aggressive", "Agree", "Ally", "Ambush", "Amuse", "Anger", "Antagonize", "Anxious",
            "Assist", "Attack", "Betray", "Block", "Bold", "Brave", "Break", "Calm", "Careless", "Carry",
            "Cautious", "Celebrate", "Change", "Charge", "Communicate", "Compete", "Control", "Crazy", "Cruel", "Damage",
            "Deceive", "Defend", "Defiant", "Delay", "Disrupt", "Divide", "Dominate", "Energetic", "Enthusiastic", "Expectation",
            "Fearful", "Ferocious", "Fierce", "Fight", "Flee", "Frantic", "Free", "Frightening", "Harm", "Harsh",
            "Hasty", "Hide", "Imitate", "Imprison", "Kill", "Lead", "Lethal", "Liberty", "Lie", "Loud", "Loyal",
            "Magic", "Mechanical", "Mighty", "Military", "Mock", "Move", "Mysterious", "Normal", "Odd", "Open",
            "Oppose", "Pain", "Path", "Prepare", "Punish", "Pursue", "Rough", "Rude", "Ruin", "Ruthless",
            "Simple", "Slow", "Spy", "Stop", "Strange", "Struggle", "Suppress", "Swift", "Take", "Technology",
            "Threaten", "Trick", "Truce", "Usurp", "Vehicle", "Vengeance", "Waste", "Weapon", "Withdraw"
        ]
        self.CHARACTER_ACTION_GENERAL = [
            "Abandon", "Aggressive", "Amusing", "Anger", "Antagonize", "Anxious", "Assist", "Bestow", "Betray", "Bizarre",
            "Block", "Bold", "Break", "Calm", "Care", "Careful", "Careless", "Celebrate", "Change", "Combative",
            "Communicate", "Control", "Crazy", "Creepy", "Dangerous", "Deceive", "Decrease", "Defiant", "Delay", "Disrupt",
            "Dominate", "Efficient", "Energetic", "Excited", "Expose", "Fearful", "Feeble", "Fierce", "Fight", "Foolish",
            "Frantic", "Frightening", "Generous", "Gentle", "Harm", "Harsh", "Hasty", "Helpful", "Imitate", "Important",
            "Imprison", "Increase", "Inspect", "Intense", "Juvenile", "Kind", "Lazy", "Leadership", "Lethal", "Loud",
            "Loyal", "Mature", "Meaningful", "Messy", "Move", "Mundane", "Mysterious", "Nice", "Normal", "Odd",
            "Official", "Open", "Oppose", "Passion", "Peace", "Playful", "Pleasures", "Possessions", "Punish", "Pursue",
            "Release", "Return", "Simple", "Slow", "Start", "Stop", "Strange", "Struggle", "Swift", "Tactics",
            "Take", "Technology", "Threatening", "Trust", "Violent", "Waste", "Weapons", "Wild", "Work", "Yield"
        ]
        self.CHARACTER_APPEARANCE = [
            "Abnormal", "Armed", "Aromatic", "Athletic", "Attractive", "Average", "Bald", "Beautiful", "Bizarre", "Brutish",
            "Casual", "Classy", "Clean", "Clothing", "Colorful", "Common", "Cool", "Creepy", "Cute", "Dainty", "Delicate",
            "Desperate", "Different", "Dirty", "Drab", "Elegant", "Equipment", "Exotic", "Expensive", "Extravagant", "Eyewear",
            "Familiar", "Fancy", "Features", "Feminine", "Festive", "Frail", "Hair", "Hairy", "Headwear", "Heavy", "Hurt",
            "Innocent", "Insignia", "Intense", "Interesting", "Intimidating", "Jewelry", "Large", "Lavish", "Lean", "Limbs",
            "Lithe", "Masculine", "Mature", "Messy", "Mighty", "Modern", "Mundane", "Muscular", "Mysterious", "Natural", "Neat",
            "Normal", "Odd", "Official", "Old", "Petite", "Piercing", "Powerful", "Professional", "Reassuring", "Regal",
            "Remarkable", "Rough", "Rustic", "Scar", "Scary", "Scented", "Scholarly", "Short", "Simple", "Sinister", "Small",
            "Smelly", "Stocky", "Strange", "Striking", "Strong", "Stylish", "Tall", "Tattoo", "Tools", "Trendy", "Unusual",
            "Very", "Weak", "Weapon", "Wounded", "Young"
        ]
        self.CHARACTER_BACKGROUND = [
            "Abandoned", "Abuse", "Academic", "Activity", "Adventurous", "Adversity", "Art", "Assist", "Average", "Bad",
            "Bizarre", "Bleak", "Bold", "Burden", "Business", "Care", "Career", "Chaotic", "Cheat", "Combat", "Commitment",
            "Community", "Competition", "Conflict", "Control", "Crime", "Damaged", "Danger", "Death", "Deceive", "Decrease",
            "Defeated", "Disaster", "Dispute", "Emotion", "Environment", "Escape", "Exile", "Experience", "Failure", "Faith",
            "Fame", "Family", "Fortunate", "Free", "Freedom", "Friend", "Gifts", "Good", "Guided", "Hard", "Harm", "Harsh",
            "Heal", "Helped", "Heroic", "Humble", "Humiliation", "Imprisonment", "Independent", "Inherit", "Injury",
            "Injustice", "Legal", "Loss", "Military", "Mistake", "Mundane", "Nature", "Outsider", "Person", "Place", "Poor",
            "Power", "Prestige", "Privilege", "Pursued", "Recruited", "Religion", "Rural", "Saved", "Search", "Seclusion",
            "Service", "Sheltered", "Skill", "Strange", "Successful", "Survival", "Tradition", "Training", "Trauma", "Travel",
            "Urban", "War", "Wealth", "Wild", "Work", "Wounded", "Youth"
        ]
        self.CHARACTER_CONVERSATION = [
            "Abuse", "Advice", "Aggressive", "Agree", "Amusing", "Angry", "Anxious", "Assist", "Awkward", "Betray",
            "Bizarre", "Bleak", "Bold", "Business", "Calm", "Careful", "Careless", "Cautious", "Cheerful", "Classy",
            "Cold", "Colorful", "Combative", "Crazy", "Creepy", "Curious", "Defiant", "Delightful", "Disagreeable", "Dispute",
            "Efficient", "Energetic", "Enthusiastic", "Excited", "Fearful", "Fierce", "Foolish", "Frantic", "Frightening",
            "Generous", "Gentle", "Glad", "Grateful", "Haggle", "Happy", "Harsh", "Hasty", "Helpful", "Helpless", "Hopeless",
            "Ideas", "Inform", "Innocent", "Inquire", "Intense", "Interesting", "Intolerance", "Irritating", "Joyful",
            "Judgmental", "Juvenile", "Kind", "Leadership", "Lie", "Loud", "Loving", "Loyal", "Macabre", "Mature", "Meaningful",
            "Miserable", "Mistrust", "Mocking", "Mundane", "Mysterious", "News", "Nice", "Normal", "Odd", "Offensive",
            "Official", "Oppose", "Peace", "Plans", "Playful", "Polite", "Positive", "Praise", "Quarrelsome", "Quiet",
            "Reassuring", "Refuse", "Rude", "Rumor", "Simple", "Threatening", "Truce", "Trust", "Warm", "Wild"
        ]
        self.CHARACTER_DESCRIPTORS = [
            "Abnormal", "Active", "Adventurous", "Aggressive", "Agreeable", "Ally", "Ancient", "Angry", "Anxious", "Armed",
            "Aromatic", "Arrogant", "Attractive", "Awkward", "Beautiful", "Bizarre", "Bleak", "Bold", "Brave", "Busy", "Calm",
            "Capable", "Careful", "Careless", "Caring", "Cautious", "Cheerful", "Classy", "Clean", "Clumsy", "Colorful",
            "Combative", "Commanding", "Common", "Competitive", "Confident", "Crazy", "Curious", "Dangerous", "Different",
            "Difficult", "Dirty", "Disagreeable", "Disciplined", "Educated", "Elegant", "Erratic", "Exotic", "Fancy", "Fast",
            "Foul", "Frightened", "Gentle", "Harmful", "Helpful", "Heroic", "Humorous", "Hurt", "Ignorant", "Impulsive",
            "Inept", "Informative", "Intelligent", "Interesting", "Intimidating", "Intrusive", "Large", "Loud", "Meek",
            "Naive", "Old", "Passive", "Polite", "Poor", "Powerful", "Powerless", "Primitive", "Principled", "Quiet",
            "Respectful", "Rough", "Rude", "Simple", "Skilled", "Slow", "Small", "Sneaky", "Sophisticated", "Strange",
            "Strong", "Supportive", "Surprising", "Sweet", "Trained", "Uniformed", "Unusual", "Weak", "Wealthy", "Wild",
            "Young"
        ]
        self.CHARACTER_IDENTITY = [
            "Abandoned", "Administrator", "Adventurous", "Adversary", "Advisor", "Ally", "Art", "Artist", "Assistant", "Athlete",
            "Authority", "Bureaucrat", "Business", "Combatant", "Competitor", "Controller", "Crafter", "Creator", "Criminal",
            "Deceiver", "Deliverer", "Dependent", "Driver/Pilot", "Elite", "Enemy", "Enforcer", "Engineer", "Entertainer",
            "Executive", "Expert", "Explorer", "Family", "Farmer", "Fighter", "Fixer", "Foreigner", "Friend", "Gambler",
            "Gatherer", "Guardian", "Healer", "Helpless", "Hero", "Hunter", "Information", "Innocent", "Inspector",
            "Intellectual", "Investigator", "Judge", "Killer", "Laborer", "Lackey", "Law", "Leader", "Legal", "Lost",
            "Mechanical", "Mediator", "Merchant", "Messenger", "Military", "Mundane", "Mystery", "Official", "Organizer",
            "Outsider", "Performer", "Persecutor", "Planner", "Pleaser", "Power", "Prisoner", "Professional", "Protector",
            "Public", "Punish", "Radical", "Religious", "Represent", "Rogue", "Ruffian", "Ruler", "Scholar", "Scientist",
            "Scout", "Servant", "Socialite", "Soldier", "Student", "Subverter", "Supporter", "Survivor", "Teacher", "Thief",
            "Trader", "Victim", "Villain", "Wanderer", "Warrior"
        ]
        self.CHARACTER_MOTIVATION = [
            "Adventure", "Adversity", "Ambition", "Anger", "Approval", "Art", "Attain", "Business", "Change", "Character",
            "Conflict", "Control", "Create", "Danger", "Death", "Deceive", "Destroy", "Diminish", "Disrupt", "Emotion",
            "Enemy", "Environment", "Escape", "Failure", "Fame", "Family", "Fear", "Fight", "Find", "Free", "Friend",
            "Goal", "Gratify", "Group", "Guide", "Guilt", "Hate", "Heal", "Help", "Hide", "Home", "Hope", "Idea", "Illness",
            "Important", "Imprison", "Increase", "Information", "Innocent", "Intellect", "Intolerance", "Investment",
            "Jealousy", "Joy", "Justice", "Leader", "Legal", "Loss", "Love", "Loyalty", "Malice", "Misfortune", "Mistrust",
            "Mundane", "Mysterious", "Nature", "Object", "Obligation", "Official", "Oppose", "Pain", "Passion", "Path",
            "Peace", "Physical", "Place", "Plan", "Pleasure", "Power", "Pride", "Protect", "Pursue", "Rare", "Recover",
            "Reveal", "Revenge", "Riches", "Safety", "Search", "Serve", "Start", "Stop", "Strange", "Struggle", "Success",
            "Suffering", "Support", "Take", "Transform", "Travel"
        ]
        self.CHARACTER_PERSONALITY = [
            "Active", "Adventurous", "Aggressive", "Agreeable", "Ambitious", "Amusing", "Angry", "Annoying", "Anxious",
            "Arrogant", "Average", "Awkward", "Bad", "Bitter", "Bold", "Brave", "Calm", "Careful", "Careless", "Classy",
            "Cold", "Collector", "Committed", "Competitive", "Confident", "Control", "Crazy", "Creative", "Crude",
            "Curious", "Deceptive", "Determined", "Devoted", "Disagreeable", "Dull", "Emotion", "Empathetic", "Fair",
            "Fastidious", "Follower", "Foolish", "Friendly", "Good", "Gourmet", "Greed", "Haunted", "Helpful", "Honest",
            "Honor", "Humble", "Humorous", "Inconsistent", "Independent", "Interesting", "Intolerant", "Irresponsible",
            "Knowledgeable", "Larcenous", "Leader", "Likable", "Loyal", "Manipulative", "Mercurial", "Naive", "Nervous",
            "Oblivious", "Obstinate", "Optimistic", "Perceptive", "Perfectionist", "Practical", "Prepared", "Principled",
            "Protect", "Quiet", "Quirky", "Rash", "Rational", "Respectful", "Responsible", "Restless", "Risk", "Rude",
            "Savvy", "Searching", "Selfish", "Selfless", "Shallow", "Social", "Strange", "Strong", "Studious", "Superstitious",
            "Tolerant", "Vindictive", "Vocal", "Wary", "Weak", "Wild", "Wise"
        ]
        self.CHARACTER_SKILL = [
            "Activity", "Adversity", "Agility", "Animals", "Art", "Assist", "Athletic", "Attack", "Attain", "Average",
            "Balance", "Beginner", "Bestow", "Block", "Business", "Change", "Combat", "Communicate", "Conflict", "Control",
            "Create", "Criminal", "Damage", "Danger", "Deceit", "Decrease", "Defense", "Develop", "Dispute", "Disrupt",
            "Domestic", "Dominate", "Driving", "Elements", "Energy", "Environment", "Experienced", "Expert", "Fight", "Free",
            "Guide", "Harm", "Heal", "Health", "Increase", "Inform", "Information", "Inquire", "Inspect", "Intellect",
            "Invade", "Investigative", "Knowledge", "Leadership", "Legal", "Lethal", "Lie", "Master", "Mechanical", "Medical",
            "Mental", "Military", "Motion", "Move", "Mundane", "Mysterious", "Nature", "Normal", "Obstacles", "Official",
            "Open", "Oppose", "Perception", "Practical", "Professional", "Ranged", "Release", "Rogue", "Ruin", "Simple",
            "Social", "Specialist", "Start", "Stop", "Strange", "Strength", "Struggle", "Suppress", "Take", "Technology",
            "Transform", "Travel", "Trick", "Usurp", "Vehicle", "Violence", "Water", "Weapon", "Weather", "Wounds"
        ]
        self.CHARACTER_TRAIT = [
            "Academic", "Adversity", "Animal", "Assist", "Attract", "Beautiful", "Benefits", "Bestow", "Bizarre", "Block",
            "Burden", "Combat", "Communicate", "Connection", "Control", "Create", "Criminal", "Damaged", "Dangerous",
            "Decrease", "Defense", "Delicate", "Different", "Dominate", "Driven", "Emotion", "Enemy", "Energy", "Environment",
            "Failure", "Fame", "Familiar", "Fast", "Feeble", "Flawless", "Focused", "Fortunate", "Friends", "Good", "Healthy",
            "Illness", "Impaired", "Increase", "Information", "Inspect", "Intellect", "Intense", "Interesting", "Lacking",
            "Large", "Leadership", "Legal", "Less", "Lethal", "Limited", "Loyal", "Mental", "Military", "Misfortune", "Missing",
            "Move", "Multi", "Nature", "Object", "Odd", "Old", "Partial", "Passion", "Perception", "Physical", "Poor",
            "Possessions", "Power", "Principles", "Public", "Rare", "Remarkable", "Resistant", "Resource", "Rich", "Sense",
            "Skill", "Small", "Social", "Specialized", "Spirit", "Strange", "Strong", "Suffering", "Technical", "Technology",
            "Tough", "Travel", "Trouble", "Trustworthy", "Unusual", "Very", "Weak", "Weapon", "Young"
        ]
        self.ADVENTURE_TONE = [
            "Action", "Activity", "Adventurous", "Adversity", "Aggressive", "Amusing", "Anxious", "Attainment", "Average",
            "Bizarre", "Bleak", "Bold", "Busy", "Calm", "Cheerful", "Colorful", "Combative", "Competitive", "Conflict",
            "Crazy", "Creepy", "Dangerous", "Dark", "Emotional", "Energetic", "Epic", "Evil", "Exterior", "Failure", "Fame",
            "Familiar", "Fearful", "Festive", "Fierce", "Fortunate", "Frantic", "Fresh", "Frightening", "Glorious", "Goals",
            "Hard", "Harsh", "Heavy", "Historical", "Hopeful", "Horrible", "Horror", "Important", "Inquire", "Inspect",
            "Intellect", "Intense", "Interesting", "Intrigue", "Lavish", "Legal", "Lethal", "Light", "Macabre","Magnificent",
            "Majestic", "Mature", "Meaningful", "Mechanical", "Messy", "Military", "Misfortune", "Mistrust", "Modern",
            "Mundane", "Mystery", "Natural", "Normal", "Odd", "Personal", "Physical", "Power", "Pursuit", "Quaint",
            "Random", "Rare", "Reassuring", "Remarkable", "Rough", "Rustic", "Scary", "Simple", "Slow", "Social", "Strange",
            "Strong", "Struggle", "Tension", "Travel", "Trials", "Vengeance", "Very", "Violent", "Warlike", "Wild"
        ]
        self.ALIEN_SPECIES = [
            "Advanced", "Aggressive", "Agile", "Amphibious", "Ancient", "Anxious", "Aquatic", "Arrogant", "Artistic", "Avian",
            "Beautiful", "Bizarre", "Carapace", "Clawed", "Colorful", "Combative", "Conquering", "Dangerous", "Declining",
            "Defensive", "Desperate", "Destructive", "Dominating", "Emotionless", "Enormous", "Exploitive", "Explorers",
            "Familiar", "Fast", "Feeble", "Feral", "Ferocious", "Friendly", "Frightening", "Fungal", "Furry", "Generous",
            "Gentle", "Glowing", "Graceful", "Harsh", "Helpful", "Humanoid", "Hungry", "Immortal", "Insectlike", "Insubstantial",
            "Intelligent", "Intimidating", "Large", "Lethal", "Levitating", "Liquid", "Mammalian", "Many-eyed", "Militaristic",
            "Mysterious", "Nightmarish", "Odd", "Oppressive", "Passive", "Peaceful", "Perfect", "Plant", "Powered", "Powerful",
            "Powers", "Primitive", "Prosperous", "Psychic", "Reptilian", "Robotic", "Scary", "Scientific", "Secretive",
            "Servitor", "Simple", "Skilled", "Slender", "Slow", "Small", "Smelly", "Strange", "Strong", "Suffering", "Tail",
            "Tall", "Technological", "Tentacled", "Threatening", "Toothy", "Travelers", "Treacherous", "Violent", "Warlike",
            "Wary", "Watery", "Weak", "Wings", "Wormish"
        ]
        self.ANIMAL_ACTION = [
            "Abandon", "Abnormal", "Aggressive", "Angry", "Anxious", "Assist", "Attack", "Befriend", "Bestow", "Bizarre",
            "Bold", "Break", "Busy", "Calm", "Careful", "Careless", "Cautious", "Ceaseless", "Change", "Combative", "Curious",
            "Dangerous", "Deliberate", "Disinterested", "Disrupt", "Distracted", "Dominate", "Energetic", "Excited", "Exotic",
            "Familiar", "Fearful", "Feeble", "Ferocious", "Fierce", "Fight", "Flee", "Follow", "Food", "Frantic", "Friendship",
            "Frightening", "Generous", "Gentle", "Graceful", "Harm", "Hasty", "Helpful", "Helpless", "Hungry", "Hunt",
            "Ignore", "Imitate", "Implore", "Imprison", "Inspect", "Intense", "Irritating", "Juvenile", "Lazy", "Leave",
            "Lethal", "Loud", "Loyal", "Messy", "Mistrust", "Move", "Mundane", "Mysterious", "Natural", "Neglect", "Normal",
            "Observe", "Odd", "Oppose", "Playful", "Protect", "Pursue", "Quiet", "Reassuring", "Release", "Return", "Scary",
            "Simple", "Slow", "Strange", "Struggle", "Swift", "Tactics", "Take", "Threatening", "Tranquil", "Transform",
            "Trick", "Trust", "Violent", "Warn", "Waste", "Wild", "Yield"
        ]
        self.ARMY = [
            "Active", "Aggressive", "Allies", "Ambush", "Animals", "Arrive", "Assist", "Average", "Betray", "Bizarre",
            "Block", "Bold", "Calm", "Careless", "Cautious", "Ceaseless", "Celebrate", "Colorful", "Communicate", "Creepy",
            "Deceive", "Defensive", "Defiant", "Delay", "Disorganized", "Divide", "Efficient", "Enemies", "Energy",
            "Failure",
            "Ferocious", "Fight", "Food", "Foolish", "Fortunate", "Frantic", "Fresh", "Frightening", "Helpful", "Helpless",
            "Illness", "Lacking", "Large", "Lavish", "Lazy", "Leadership", "Lethal", "Loud", "Loyal", "Mighty",
            "Mysterious",
            "Normal", "Path", "Persecute", "Power", "Problems", "Punish", "Pursue", "Quiet", "Ready", "Reassuring",
            "Recruit",
            "Release", "Riches", "Rough", "Ruin", "Ruthless", "Simple", "Skilled", "Slow", "Small", "Stalemate", "Start",
            "Stop", "Strange", "Strong", "Struggle", "Success", "Suffering", "Supplies", "Swift", "Tactics", "Take",
            "Technology", "Tension", "Testing", "Threatening", "Tired", "Travel", "Triumph", "Truce", "Trust", "Unequipped",
            "Unexpected", "Untrained", "Victory", "Violate", "Waste", "Weak", "Weapons"
        ]
        self.CAVERN = [
            "Activity", "Ancient", "Animals", "Aromatic", "Art", "Beautiful", "Bizarre", "Bleak", "Blocked", "Boulder",
            "Bright", "Cliff", "Climb", "Closed", "Cold", "Collapsed", "Colorful", "Cracked", "Cramped", "Crawl", "Creature",
            "Creepy", "Crumbling", "Curious", "Damaged", "Dangerous", "Dark", "Difficult", "Dirty", "Discouraging", "Dripping",
            "Dry", "Echo", "Elements", "Empty", "Enormous", "Exit", "Exotic", "Fall", "Flora", "Frightening", "Full", "Fungus",
            "Good", "Hard", "Harm", "Harsh", "Hole", "Huge", "Icy", "Interesting", "Large", "Ledge", "Lethal", "Light", "Loud",
            "Magnificent", "Message", "Messy", "Minerals", "Misfortune", "Mist", "Mysterious", "Natural", "Nature", "Normal",
            "Occupied", "Odd", "Open", "Path", "Plants", "Pool", "Quiet", "Reassuring", "Remarkable", "Riches", "River",
            "Rock", "Rough", "Scary", "Simple", "Slippery", "Slope", "Small", "Smelly", "Smooth", "Sounds", "Stalactites",
            "Strange", "Threatening", "Tight", "Tranquil", "Treasure", "Unnatural", "Unstable", "Untouched", "Warm", "Waste",
            "Water", "Windy"
        ]
        self.CITY = [
            "Activity", "Aggressive", "Aromatic", "Average", "Beautiful", "Bleak", "Block", "Bridge", "Bustling", "Calm",
            "Chaotic", "Clean", "Cold", "Colorful", "Commerce", "Conflict", "Control", "Crime", "Dangerous", "Dense",
            "Developed", "Dirty", "Efficient", "Energy", "Enormous", "Environment", "Extravagant", "Festive", "Flawless",
            "Frightening", "Government", "Happy", "Harsh", "Healthy", "Helpful", "Hills", "History", "Illness", "Important",
            "Impressive", "Industry", "Interesting", "Intrigues", "Isolated", "Lacking", "Lake", "Large", "Lavish",
            "Leadership", "Liberty", "Loud", "Magnificent", "Masses", "Meaningful", "Mechanical", "Messy", "Mighty",
            "Military", "Miserable", "Misfortune", "Modern", "Mountain", "Mundane", "Mysterious", "Nature", "Odd", "Old",
            "Oppress", "Opulence", "Peace", "Poor", "Powerful", "Protected", "Public", "Quiet", "Rare", "Reassuring",
            "Remarkable", "River", "Rough", "Ruined", "Rustic", "Simple", "Small", "Sparse", "Structures", "Struggle",
            "Success", "Suffering", "Technology", "Tension", "Travel", "Troubled", "Valuable", "Warm", "Water", "Weak",
            "Weather", "Wild", "Work"
        ]
        self.CIVILIZATION =[
            "Active", "Advanced", "Adventurous", "Aggressive", "Agricultural", "Ancient", "Angry", "Anxious", "Artistic",
            "Average", "Beautiful", "Bizarre", "Bleak", "Bold", "Bureaucratic", "Carefree", "Careful", "Careless", "Cautious",
            "Classy", "Clean", "Colorful", "Combative", "Commercial", "Competitive", "Constructive", "Controlling", "Crazy",
            "Creative", "Creepy", "Cruel", "Curious", "Dangerous", "Declining", "Defiant", "Delightful", "Developed",
            "Disagreeable", "Distrustful", "Dominant", "Dull", "Efficient", "Expanding", "Failed", "Famous", "Fearful",
            "Festive", "Free", "Generous", "Greedy", "Happy", "Healthy", "Helpful", "Helpless", "Historical", "Important",
            "Industrial", "Influential", "Intolerant", "Large", "Lawful", "Lawless", "Magnificent", "Mighty", "Militaristic",
            "Miserable", "Modern", "Mundane", "Mysterious", "Old", "Open", "Oppressive", "Peaceful", "Polite", "Poor",
            "Powerful", "Primitive", "Punitive", "Quaint", "Religious", "Ruined", "Rustic", "Ruthless", "Scary", "Simple",
            "Small", "Strange", "Strong", "Struggling", "Successful", "Suffering", "Suppressed", "Suspicious", "Treacherous",
            "Warlike", "Weak", "Wealthy", "Welcoming", "Wild", "Young"
        ]
        self.CREATURE = [
            "Aggressive", "Agile", "Air", "Alien", "Amorphous", "Animal", "Aquatic", "Armored", "Avian", "Beast", "Beautiful",
            "Body", "Bony", "Carapace", "Clawed", "Clothed", "Cold", "Color", "Composite", "Constructed", "Decayed", "Defensive",
            "Dripping", "Elements", "Exotic", "Extra Limbs", "Fangs", "Feminine", "Feral", "Filthy", "Fire", "Fungal", "Furry",
            "Gaunt", "Glowing", "Group", "Growling", "Healthy", "Horns", "Humanoid", "Inscribed", "Insect-like", "Insubstantial",
            "Intelligent", "Intimidating", "Large", "Levitating", "Limited", "Liquid", "Loud", "Mammalian", "Mandibles", "Masculine",
            "Mechanical", "Metallic", "Movement", "Multiple", "Mutant", "Natural", "Nature", "Nightmarish", "Object", "Odorous",
            "Passive", "Plant", "Reptilian", "Robotic", "Rooted", "Rough", "Shape", "Shifting", "Silent", "Simple", "Slender",
            "Small", "Solitary", "Spider-like", "Spiked", "Steaming", "Sticky", "Stinger", "Strange", "Strong", "Supernatural",
            "Tail", "Tentacled", "Tongue", "Toothy", "Transparent", "Tree-like", "Twisted", "Undead", "Unnatural", "Verbal",
            "Warm", "Weak", "Weapon", "Wings", "Wooden", "Wormish"
        ]
        self.CREATURE_ABILITY = [
            "Ambush", "Animate", "Armor", "Arrive", "Attach", "Attack", "Attract", "Bite", "Block", "Blunt", "Break", "Breath",
            "Carry", "Change", "Climb", "Cold", "Common", "Communicate", "Conceal", "Contact", "Control", "Create", "Damage",
            "Dark", "Death", "Deceive", "Decrease", "Defense", "Depower", "Detect", "Disrupt", "Distract", "Dominate", "Drain",
            "Element", "Energy", "Enhanced", "Entangle", "Environment", "Extra", "Fear", "Fight", "Fire", "Flight", "Harm",
            "Heal", "Illness", "Illusion", "Imitate", "Immune", "Imprison", "Increase", "Intelligent", "Itself", "Lethal", "Light",
            "Limited", "Mind", "Move", "Multiple", "Natural", "Normal", "Open", "Others", "Paralyze", "Physical", "Pierce", "Poison",
            "Power", "Protection", "Proximity", "Pursue", "Ranged", "Rechargeable", "Resistance", "Self-Sufficient", "Senses",
            "Skill", "Sleep", "Speed", "Spy", "Stealth", "Stop", "Strange", "Stun", "Substance", "Summon", "Suppress", "Swim", "Take",
            "Telepathy", "Touch", "Transform", "Travel", "Trick", "Uncommon", "Vision", "Vulnerable", "Weak", "Weapon"
        ]
        self.CRYPTIC_MESSAGE = [
            "Abandoned", "Activity", "Adventure", "Adversity", "Advice", "Allies", "Anger", "Bestow", "Betray", "Bizarre",
            "Bleak", "Business", "Care", "Colorful", "Communicate", "Conflict", "Creepy", "Damaged", "Danger", "Death", "Deceive",
            "Defiant", "Dispute", "Divide", "Emotions", "Enemies", "Environment", "Evil", "Expose", "Failure", "Fame", "Fear",
            "Fight", "Frantic", "Free", "Friendship", "Goals", "Good", "Guide", "Harm", "Help", "Helpful", "Hidden", "Hope",
            "Horrible", "Important", "Information", "Innocent", "Instruction", "Intrigues", "Language", "Leadership", "Legal",
            "Legend", "Liberty", "Lies", "Lost", "Love", "Malice", "Messy", "Misfortune", "Mistrust", "Move", "Mundane",
            "Mysterious", "Neglect", "Normal", "Obscured", "Official", "Old", "Oppose", "Partial", "Passion", "Plans",
            "Possessions", "Power", "Propose", "Punish", "Pursue", "Rare", "Reassuring", "Recipient", "Reveal", "Riches",
            "Riddle", "Rumor", "Secret", "Start", "Stop", "Strange", "Struggle", "Success", "Tension", "Threaten", "Truce",
            "Trust", "Unknown", "Vengeance", "Violence", "Warning"
        ]
        self.CURSE = [
            "Abandon", "Age", "Attract", "Bad", "Beauty", "Betray", "Bizarre", "Block", "Body", "Break", "Burden", "Business",
            "Change", "Compel", "Condemn", "Conflict", "Create", "Creepy", "Cruel", "Danger", "Death", "Decrease", "Delay",
            "Disrupt", "Divide", "Dominate", "Dreams", "Elements", "Emotions", "Enemies", "Energy", "Environment", "Evil",
            "Failure", "Fame", "Family", "Fate", "Fear", "Feeble", "Fight", "Friends", "Frightening", "Goals", "Good",
            "Gratify", "Guide", "Happiness", "Harm", "Health", "Helpless", "Home", "Illness", "Illusions", "Imprison",
            "Incapacity", "Information", "Intellect", "Ironic", "Jealously", "Joy", "Legal", "Lethal", "Liberty", "Limit",
            "Lonely", "Love", "Luck", "Malice", "Meaningful", "Miserable", "Misfortune", "Mistrust", "Mock", "Move", "Mundane",
            "Mysterious", "Nature", "Neglect", "Old", "Oppress", "Pain", "Passion", "Peace", "Permanent", "Possessions",
            "Punish", "Pursue", "Riches", "Ruin", "Senses", "Separate", "Start", "Stop", "Strange", "Struggle", "Success",
            "Temporary", "Vengeance", "Violence", "Weapon"
        ]
        self.DOMICILE = [
            "Abandoned", "Activity", "Animal", "Aromatic", "Art", "Average", "Beautiful", "Bizarre", "Bleak", "Busy", "Classy",
            "Clean", "Cluttered", "Cold", "Colorful", "Comfort", "Common", "Cramped", "Creepy", "Crowded", "Customized", "Cute",
            "Damaged", "Dangerous", "Dark", "Desolate", "Different", "Dirty", "Disagreeable", "Drab", "Dull", "Empty", "Enormous",
            "Expected", "Extravagant", "Faded", "Fancy", "Festive", "Food", "Frightening", "Full", "Home", "Investment", "Inviting",
            "Lacking", "Large", "Lavish", "Less", "Light", "Loud", "Magnificent", "Mechanical", "Messy", "Modern", "Mundane",
            "Mysterious", "Natural", "Neat", "Neglected", "Nondescript", "Normal", "Occupied", "Odd", "Open", "Oppressive",
            "Opulent", "Organized", "Plants", "Poor", "Portal", "Possessions", "Private", "Protection", "Quaint", "Reassuring",
            "Roomy", "Rough", "Ruined", "Rustic", "Scary", "Secure", "Security", "Simple", "Sleep", "Small", "Smelly", "Sparse",
            "Storage", "Strange", "Temporary", "Thoughtful", "Tidy", "Tools", "Tranquil", "Upgrade", "Utilitarian", "Valuables",
            "View", "Warm", "Water"
        ]
        self.DUNGEON = [
            "Abandoned", "Activity", "Adversity", "Ambush", "Ancient", "Animal", "Aromatic", "Art", "Beautiful", "Bizarre",
            "Bleak", "Chamber", "Clean", "Closed", "Cold", "Collapsed", "Colorful", "Creature", "Creepy", "Damaged", "Danger",
            "Dark", "Desolate", "Dirty", "Door", "Dry", "Elements", "Empty", "Encounter", "Enemies", "Enormous", "Evil", "Exit",
            "Extravagant", "Faded", "Familiar", "Fancy", "Fears", "Foreboding", "Full", "Furnishings", "Gate", "Good", "Harm",
            "Heavy", "Helpful", "Hole", "Important", "Information", "Interesting", "Large", "Lavish", "Lethal", "Light",
            "Magnificent", "Malice", "Meaningful", "Mechanical", "Messages", "Messy", "Mighty", "Military", "Misfortune", "Modern",
            "Mundane", "Mysterious", "Natural", "Neglect", "Normal", "Object", "Occupied", "Odd", "Open", "Passage", "Path", "Portal",
            "Possessions", "Quiet", "Rare", "Reassuring", "Remarkable", "Riches", "Room", "Rough", "Ruined", "Rustic", "Scary",
            "Simple", "Small", "Smelly", "Sound", "Stairs", "Stonework", "Technology", "Trap", "Treasure", "Unnatural", "Valuable",
            "Warm", "Watery"
        ]
        self.TRAP = [
            "Aggressive", "Allies", "Ambush", "Animals", "Animate", "Antagonize", "Aromatic", "Art", "Attach", "Attention",
            "Attract", "Balance", "Beautiful", "Bestow", "Betray", "Bizarre", "Blades", "Break", "Ceiling", "Change", "Choice",
            "Climb", "Cloud", "Cold", "Colorful", "Combative", "Communicate", "Confuse", "Constrain", "Control", "Create", "Creepy",
            "Crush", "Damaged", "Danger", "Dark", "Deceive", "Delay", "Deprive", "Disrupt", "Divide", "Door", "Drop", "Duplicate",
            "Elaborate", "Enemies", "Energy", "Fall", "Fear", "Fight", "Fire", "Floor", "Frightening", "Harm", "Heat", "Heavy",
            "Helpless", "Horrible", "Illusion", "Imprison", "Lethal", "Loud", "Lure", "Magic", "Mechanical", "Mental", "Messy",
            "Monster", "Natural", "Object", "Odd", "Old", "Pain", "Plants", "Portal", "Possessions", "Prison", "Projectile", "Riddle",
            "Scary", "Simple", "Sounds", "Stab", "Stop", "Strange", "Strangle", "Suppress", "Take", "Toxin", "Transform", "Transport",
            "Treasure", "Trials", "Trigger", "Unleash", "Wall", "Warning", "Water", "Weapon", "Wound"
        ]
        self.FOREST = [
            "Adversity", "Aggressive", "Ambush", "Ancient", "Animal", "Aromatic", "Art", "Assist", "Average", "Beautiful",
            "Bizarre", "Bleak", "Block", "Boulder", "Cave", "Chaotic", "Cliff", "Cold", "Colorful", "Combative", "Communicate",
            "Creepy", "Damaged", "Danger", "Dark", "Death", "Delicate", "Dry", "Elements", "Encounter", "Enormous", "Environment",
            "Fearful", "Feeble", "Fierce", "Food", "Fortunate", "Fresh", "Harsh", "Healthy", "Helpful", "Important", "Information",
            "Intense", "Interesting", "Lacking", "Lake", "Large", "Lean", "Ledge", "Lethal", "Loud", "Magnificent", "Majestic",
            "Masses", "Mature", "Message", "Mighty", "Mundane", "Mysterious", "Natural", "Nature", "Nondescript", "Normal", "Odd",
            "Old", "Path", "Peaceful", "Plants", "Pond", "Possessions", "Powerful", "Pursue", "Quiet", "Rare", "Reassuring",
            "Remarkable", "River", "Rocks", "Rough", "Ruined", "Scary", "Simple", "Slope", "Small", "Sounds", "Strange", "Strong",
            "Threatening", "Tranquil", "Tree", "Unusual", "Valuable", "Violent", "Warm", "Watery", "Weak", "Weather", "Wild", "Young"
        ]
        self.GOD = [
            "Active", "Alien", "Ancient", "Angelic", "Angry", "Animal", "Art", "Assist", "Attract", "Beautiful", "Bestow", "Betray",
            "Bizarre", "Capricious", "Colorful", "Combat", "Communicate", "Conflict", "Control", "Corruption", "Cosmic", "Create",
            "Creepy", "Cruel", "Cult", "Dangerous", "Dark", "Death", "Deceit", "Destroyer", "Disgusting", "Dominate", "Dreams",
            "Elements", "Emotions", "Enemies", "Energy", "Enormous", "Evil", "Feminine", "Fallen", "Fear", "Fertility", "Festive",
            "Fire", "Frightening", "Generous", "Gentle", "Gifts", "Glorious", "Good", "Guide", "Harm", "Harsh", "Heal", "Humanoid",
            "Illness", "Imprison", "Increase", "Jealous", "Justice", "Knowledge", "Liberty", "Life", "Light", "Love", "Magic",
            "Majestic", "Major", "Malice", "Masculine", "Mighty", "Military", "Minor", "Monstrous", "Mundane", "Mysterious", "Nature",
            "Night", "Oppress", "Pleasures", "Power", "Protector", "Punish", "Ruler", "Sacrifice", "Strange", "Strong", "Suppress",
            "Threatening", "Transform", "Underworld", "Violent", "War", "Warm", "Water", "Weak", "Weapon", "Weather", "Worshiped"
        ]
        self.LEGEND = [
            "Abandon", "Allies", "Anger", "Assist", "Attainment", "Befriend", "Bestow", "Betray", "Bizarre", "Block", "Brave",
            "Break", "Burden", "Carelessness", "Cataclysm", "Caution", "Change", "Conflict", "Control", "Create", "Crisis", "Damage",
            "Danger", "Deceive", "Decrease", "Defeated", "Defiant", "Delay", "Disrupt", "Divide", "Elements", "End", "Enemies",
            "Energy", "Evil", "Expose", "Failure", "Fame", "Fear", "Fight", "Find", "Free", "Friendship", "Frightening", "Good",
            "Guide", "Harm", "Heal", "Help", "Helpless", "Hero", "Hidden", "Historical", "Illness", "Important", "Imprison", "Increase",
            "Inform", "Innocent", "Intrigue", "Jealousy", "Judge", "Leadership", "Legal", "Lethal", "Liberty", "Loss", "Love", "Loyalty",
            "Masses", "Mighty", "Military", "Misfortune", "Monster", "Move", "Mundane", "Mysterious", "Natural", "Old", "Oppose", "Oppress",
            "Peace", "Plot", "Possessions", "Power", "Punish", "Pursue", "Release", "Return", "Riches", "Ruin", "Savior", "Stop", "Strange",
            "Struggle", "Theft", "Trust", "Usurp", "Vengeance", "Villain"
        ]
        self.MAGIC_ITEM = [
            "Animal", "Animate", "Area", "Armor", "Assist", "Attack", "Attract", "Benefit", "Bestow", "Block", "Book", "Change", "Clothing",
            "Cloud", "Cold", "Communication", "Container", "Control", "Create", "Curse", "Damage", "Death", "Deceit", "Decrease", "Defense",
            "Destroy", "Detect", "Dimensions", "Elements", "Emotion", "Energy", "Enhance", "Environment", "Escape", "Evil", "Explode", "Fear",
            "Fire", "Flight", "Food", "Gem", "Good", "Group", "Harm", "Heal", "Health", "Helpful", "Illness", "Illusion", "Imbue", "Imitate",
            "Increase", "Information", "Inhibit", "Instant", "Jewelry", "Lethal", "Life", "Light", "Limited", "Liquid", "Mental", "Monster",
            "Multi", "Nature", "Object", "Orb", "Others", "Physical", "Plants", "Poison", "Potion", "Power", "Ranged", "Resistance", "Restore",
            "Ring", "Rope", "Rune", "Safety", "Scroll", "Self", "Senses", "Skill", "Special", "Speed", "Spell", "Staff", "Strange", "Summon",
            "Sword", "Tool", "Transform", "Trap", "Travel", "Useful", "Utility", "Wand", "Water", "Weapon"
        ]
        self.MUTATION = [
            "Agility", "Animal", "Appearance", "Armor", "Assist", "Attach", "Attack", "Benefit", "Bestow", "Bizarre", "Block", "Body", "Change",
            "Claws", "Color", "Combat", "Communicate", "Conceal", "Constrain", "Control", "Create", "Damage", "Deceive", "Decrease", "Defect",
            "Defense", "Deformed", "Detect", "Diminish", "Disrupt", "Dominate", "Elements", "Energy", "Enhance", "Environment", "Expose", "Extra",
            "Eyes", "Fear", "Fight", "Fly", "Free", "Harm", "Heal", "Health", "Heat", "Helpful", "Horrible", "Imitate", "Immunity", "Imprison",
            "Increase", "Information", "Inspect", "Large", "Learn", "Lethal", "Limb", "Limit", "Mental", "Messy", "Move", "Nature", "Pain",
            "Partial", "Power", "Projectile", "Protection", "Ranged", "Recharge", "Release", "Replace", "Requirement", "Resistance", "Restore",
            "Reveal", "Scary", "Senses", "Simple", "Skill", "Stop", "Strange", "Strength", "Strong", "Struggle", "Suffer", "Suppress",
            "Surroundings", "Survive", "Swim", "Toxic", "Transform", "Travel", "Usurp", "Violence", "Vulnerability", "Warm", "Weak", "Weapon", "Wound"
        ]
        self.NAME = [
            "A", "Action", "Ah", "Ahg", "An", "Animal", "Ar", "As", "B", "Bah", "Be", "Bih", "Brah", "Col", "Color", "Cor", "Dah", "Deeds",
            "Del", "Drah", "Eee", "Eh", "Ei", "Ell", "Elements", "Emotion", "Ess", "Est", "Et", "Fah", "Fer", "Fi", "Floral", "Gah", "Go",
            "Grah", "Hee", "Ia", "Ick", "In", "Iss", "Je", "Ke", "Jen", "Kha", "Kr", "Lah", "Lee", "Len", "Lin", "Location", "Ly", "Mah",
            "Military", "Misdeed", "N", "Nah", "Nature", "Nee", "Nn", "Number", "Occupation", "Oh", "On", "Or", "Orn", "Oth", "Ow", "Ph",
            "Pr", "R", "Rah", "Ren", "Sah", "Se", "Sh", "Sha", "T", "Ta", "Tal", "Tar", "Th", "Thah", "Thoh", "Ti", "Time", "Tor", "Uh",
            "Va", "Vah", "Ve", "Vice", "Virtue", "Wah", "Wr", "X", "Y", "Yah", "Yuh", "Z"
        ]
        self.NOBLE_HOUSE = [
            "Aggressive", "Allies", "Anger", "Bestow", "Betray", "Bizarre", "Block", "Break", "Bureaucracy", "Cautious",
            "Change", "Commerce", "Compromise", "Conflict", "Connections", "Control", "Create", "Crisis", "Cruel", "Dangerous",
            "Death", "Deceit", "Defeat", "Defiant", "Disrupt", "Enemies", "Extravagant", "Faded", "Fame", "Family",
            "Headquarters", "Heirloom", "Hero", "History", "Home", "Important", "Imprison", "Increase", "Information",
            "Intrigue", "Investment", "Land", "Large", "Leadership", "Legal", "Leverage", "Liberty", "Love", "Loyal",
            "Magnificent", "Malice", "Mighty", "Military", "Misfortune", "Move", "Mysterious", "Neglect", "Old", "Oppose",
            "Oppress", "Overthrow", "Passion", "Peace", "Persecute", "Plans", "Politics", "Possessions", "Powerful", "Public",
            "Refuse", "Release", "Remarkable", "Return", "Riches", "Royalty", "Ruthless", "Secret", "Security", "Servant",
            "Spy", "Strange", "Strong", "Struggle", "Succession", "Suffering", "Suppress", "Tactics", "Tension", "Travel",
            "Trust", "Usurp", "Valuable", "Vengeance", "Victory", "Violence", "War", "Weak", "Wealth", "Weapon", "Young"
        ]
        self.PLOT_TWIST = [
            "Action", "Attack", "Bad", "Barrier", "Betray", "Business", "Change", "Character", "Conclude", "Conditional",
            "Conflict", "Connection", "Consequence", "Control", "Danger", "Death", "Delay", "Destroy", "Diminish", "Disaster",
            "Discover", "Emotion", "Enemy", "Enhance", "Enter", "Escape", "Evidence", "Failure", "Family", "Free", "Friend",
            "Good", "Group", "Harm", "Headquarters", "Help", "Helpless", "Hidden", "Idea", "Immediate", "Impending", "Important",
            "Incapacitate", "Information", "Injustice", "Leader", "Legal", "Lethal", "Lie", "Limit", "Location", "Lucky", "Mental",
            "Missing", "Mundane", "Mystery", "Necessary", "News", "Object", "Oppose", "Outcast", "Overcome", "Past", "Peace",
            "Personal", "Persuade", "Physical", "Plan", "Power", "Prepare", "Problem", "Promise", "Protect", "Public", "Pursue",
            "Rare", "Remote", "Repair", "Repeat", "Require", "Rescue", "Resource", "Response", "Reveal", "Revenge", "Reversal",
            "Reward", "Skill", "Social", "Solution", "Strange", "Success", "Tension", "Trap", "Travel", "Unknown", "Unlikely",
            "Unusual", "Urgent", "Useful"
        ]
        self.POWER = [
            "Absorb", "Adversity", "Alter", "Animate", "Assist", "Attach", "Attack", "Block", "Body", "Change",
            "Chemical", "Cold", "Colorful", "Combat", "Combine", "Communicate", "Control", "Cosmetic", "Create",
            "Creature", "Damage", "Dark", "Death", "Deceive", "Defense", "Delay", "Destroy", "Detect", "Dimensions",
            "Diminish", "Disrupt", "Distance", "Dominate", "Duplicate", "Electricity", "Elements", "Emission", "Emotion",
            "Enemies", "Energy", "Enhance", "Environment", "Explosion", "Extra", "Fire", "Flight", "Free", "Friend", "Harm",
            "Heal", "Heat", "Help", "Hide", "Illusion", "Imbue", "Immunity", "Increase", "Information", "Life", "Light", "Limb",
            "Limited", "Location", "Magic", "Major", "Manipulate", "Matter", "Mental", "Minor", "Natural", "Nature", "Object",
            "Others", "Physical", "Plants", "Poison", "Power", "Protect", "Radius", "Ranged", "Reflect", "Repel", "Resistance",
            "Reveal", "Self", "Sense", "Skill", "Spirit", "Stealth", "Strange", "Summon", "Switch", "Take", "Technology", "Time",
            "Transform", "Trap", "Travel", "Weapon", "Weather"
        ]
        self.LOOT = [
            "Abundance", "Activity", "Adversity", "Allies", "Animal", "Art", "Barrier", "Beauty", "Bizarre", "Bleak",
            "Broken", "Clean", "Clothes", "Comfort", "Communicate", "Competition", "Concealment", "Conflict", "Container",
            "Control", "Crisis", "Damaged", "Danger", "Death", "Dirty", "Disagreeable", "Disgusting", "Dispute", "Drink",
            "Elements", "Empty", "Enemies", "Energy", "Extravagance", "Failure", "Fear", "Fight", "Food", "Fresh", "Friendship",
            "Fuel", "Good", "Health", "Helpful", "Hope", "Important", "Information", "Joy", "Large", "Lavish", "Lean", "Less",
            "Lethal", "Mechanical", "Medicinal", "Messy", "Misfortune", "Mundane", "Mysterious", "Nature", "New", "Normal",
            "Odd", "Official", "Old", "Open", "Opposition", "Pain", "Peace", "Pleasures", "Portal", "Possessions", "Protection",
            "Reassuring", "Repairable", "Rotten", "Rough", "Ruined", "Scary", "Shelter", "Simple", "Small", "Smelly", "Strange",
            "Struggle", "Success", "Supply", "Technology", "Tool", "Travel", "Triumph", "Trouble", "Useless", "Valuable",
            "Vehicle", "Victory", "Violence", "Warm", "Waste", "Weapon"
        ]
        self.SMELL = [
            "Acrid", "Animal", "Antiseptic", "Aromatic", "Artificial", "Attractive", "Bad", "Bizarre", "Burnt", "Chemical",
            "Clean", "Comforting", "Cooking", "Decrepit", "Delicious", "Delightful", "Dirty", "Disagreeable", "Disgusting", "Dry",
            "Dull", "Earthy", "Electrical", "Evocative", "Faded", "Faint", "Familiar", "Fetid", "Fishy", "Floral", "Food", "Foul",
            "Fragrant", "Fresh", "Fruity", "Funky", "Good", "Grassy", "Gratifying", "Heady", "Heavy", "Herbal", "Horrible", "Humid",
            "Industrial", "Interesting", "Intoxicating", "Irritating", "Lacking", "Laden", "Malodorous", "Meaningful", "Medicinal",
            "Metallic", "Mildew", "Moist", "Mossy", "Musky", "Musty", "Mysterious", "Natural", "Nature", "Nauseating", "Normal", "Odd",
            "Odorless", "Offensive", "Overpowering", "Perfumed", "Pleasurable", "Powerful", "Pungent", "Punishing", "Putrid", "Rancid",
            "Reassuring", "Reek", "Rich", "Ripe", "Rot", "Rotten", "Savory", "Smelly", "Smokey", "Sour", "Stagnant", "Stale", "Stench",
            "Stinging", "Strange", "Strong", "Stuffy", "Sulphuric", "Sweet", "Warm", "Waste", "Watery", "Weak", "Weather", "Woody"
        ]
        self.SOUND = [
            "Activity", "Alarm", "Animal", "Approach", "Banging", "Battle", "Beep", "Bell", "Beseeching", "Bizarre",
            "Burning", "Busy", "Calm", "Ceaseless", "Celebrate", "Chaotic", "Cheerful", "Clang", "Combative", "Communicate",
            "Construction", "Conversation", "Crash", "Creaking", "Creepy", "Cries", "Damage", "Danger", "Disagreeable",
            "Distant", "Drip", "Echo", "Emotion", "Energetic", "Explosion", "Familiar", "Ferocious", "Footsteps", "Frantic",
            "Frightening", "Grinding", "Growl", "Hammering", "Helpful", "Imitate", "Important", "Indistinct", "Industry",
            "Information", "Innocent", "Intense", "Interesting", "Irritating", "Loud", "Machinery", "Meaningful", "Metallic",
            "Muffled", "Multiple", "Music", "Mysterious", "Natural", "Near", "Noisy", "Normal", "Odd", "Productivity", "Pursuit",
            "Quiet", "Reassuring", "Remarkable", "Rip", "Roar", "Rumbling", "Rustling", "Scary", "Scraping", "Scratching",
            "Simple", "Sizzle", "Slam", "Slow", "Soft", "Start", "Stop", "Strange", "Tapping", "Technology", "Threatening", "Thud",
            "Traffic", "Tranquil", "Uncertain", "Warning", "Water", "Weather", "Whirring", "Whistle", "Wild", "Wind"
        ]
        self.SPELL_EFFECT = [
            "Animal", "Animate", "Assist", "Attack", "Attract", "Bestow", "Bizarre", "Block", "Break", "Bright",
            "Burn", "Change", "Cloud", "Cold", "Communicate", "Conceal", "Conjure", "Control", "Counteract", "Create",
            "Creature", "Curse", "Damage", "Dark", "Death", "Deceive", "Decrease", "Defense", "Destroy", "Detect",
            "Diminish", "Disease", "Dominate", "Duplicate", "Earth", "Elements", "Emotion", "Enemies", "Energy",
            "Enhance", "Environment", "Expose", "Fire", "Fix", "Food", "Free", "Group", "Guide", "Hamper", "Harm",
            "Heal", "Helpful", "Ice", "Illusion", "Imbue", "Immunity", "Imprison", "Information", "Inspect", "Life",
            "Light", "Limitation", "Liquid", "Loud", "Manipulation", "Mind", "Nature", "Object", "Others", "Pain",
            "Physical", "Plant", "Poison", "Portal", "Powerful", "Protect", "Radius", "Ranged", "Resistance", "Restore",
            "Self", "Senses", "Shield", "Soul", "Strange", "Strength", "Stun", "Summon", "Time", "Transform", "Trap",
            "Travel", "Trigger", "Uncertain", "Undead", "Wall", "Water", "Weak", "Weapon", "Weather"
        ]
        self.STARSHIP = [
            "Activity", "Adversity", "Assist", "Automated", "Battle", "Beautiful", "Bestow", "Bleak", "Block", "Bright",
            "Business", "Clean", "Cold", "Colorful", "Combative", "Communicate", "Computer", "Contain", "Control", "Creepy",
            "Crew", "Damaged", "Danger", "Dark", "Death", "Defense", "Elaborate", "Empty", "Energy", "Engine", "Enormous",
            "Environment", "Escape", "Exit", "Exterior", "Fear", "Food", "Full", "Hall", "Health", "Helpful", "Important",
            "Information", "Inquire", "Interesting", "Lacking", "Large", "Lavish", "Lethal", "Loud", "Magnificent", "Maintenance",
            "Meaningful", "Mechanical", "Message", "Messy", "Mighty", "Military", "Modern", "Multiple", "Mundane", "Mysterious",
            "Natural", "Normal", "Odd", "Portal", "Possessions", "Power", "Powerful", "Prison", "Protection", "Quiet", "Rare",
            "Reassuring", "Remarkable", "Resources", "Room", "Rough", "Ruined", "Scary", "Security", "Simple", "Small", "Sounds",
            "Start", "Stop", "Storage", "Strange", "Supplies", "Survival", "System", "Tactics", "Technology", "Travel", "Unusual",
            "Valuable", "Vehicle", "Warm", "Weapon", "Work"
        ]
        self.TERRAIN = [
            "Abandoned", "Abundant", "Activity", "Advanced", "Allies", "Ancient", "Animals", "Atmosphere", "Barren", "Beautiful",
            "Bizarre", "Catastrophe", "Chaotic", "City", "Civilization", "Cliffs", "Clouds", "Cold", "Colorful", "Combative",
            "Communicate", "Conflict", "Damaged", "Danger", "Defense", "Desert", "Dry", "Dull", "Elements", "Empty", "Energy",
            "Enormous", "Environment", "Fertile", "Frightening", "Habitable", "Harsh", "Hazy", "Healthy", "Helpful", "Hostile",
            "Hot", "Intense", "Interesting", "Large", "Lethal", "Life", "Lovely", "Magnificent", "Masses", "Mechanical", "Message",
            "Mighty", "Misfortune", "Mountainous", "Multiple", "Mundane", "Mysterious", "Natural", "Nature", "Nondescript", "Ocean",
            "Odd", "Peaceful", "People", "Plants", "Populated", "Powerful", "Primitive", "Rain", "Rare", "Remarkable", "Resourceful",
            "Riches", "River", "Rocky", "Rough", "Ruined", "Ruins", "Sandy", "Scary", "Simple", "Small", "Strange", "Strong",
            "Technology", "Threatening", "Toxic", "Tranquil", "Trees", "Unusual", "Valuable", "Violent", "Warm", "Water", "Weak",
            "Weather", "Wild", "Windy", "Wonders"
        ]
        self.UNDEAD = [
            "Active", "Aggressive", "Angry", "Animal", "Anxious", "Attract", "Beautiful", "Bestow", "Bizarre", "Bleak",
            "Bold", "Bound", "Cold", "Combative", "Communicate", "Control", "Create", "Creepy", "Dangerous", "Dark",
            "Deceive", "Dirty", "Disgusting", "Elements", "Enemies", "Energy", "Environment", "Evil", "Fast", "Fear",
            "Fight", "Floating", "Friendly", "Frightening", "Glad", "Glow", "Goals", "Good", "Guide", "Harm", "Helpful",
            "Helpless", "Historical", "Horrible", "Hungry", "Imitate", "Information", "Insubstantial", "Intelligent",
            "Large", "Leadership", "Lethal", "Light", "Limited", "Lonely", "Love", "Macabre", "Malice", "Message", "Messy",
            "Mighty", "Mindless", "Miserable", "Misfortune", "Monstrous", "Mundane", "Odd", "Old", "Pain", "Pale", "Passive",
            "Possessions", "Possessive", "Powerful", "Powers", "Purposeful", "Pursue", "Quiet", "Resistant", "Rotting", "Scary",
            "Seeking", "Shambling", "Slow", "Small", "Smelly", "Strange", "Strong", "Threatening", "Tough", "Transform", "Travel",
            "Trick", "Vengeful", "Violent", "Weak", "Weakness", "Weapons", "Wounds", "Young"
        ]
        self.VISION = [
            "Activity", "Adversity", "Allies", "Assist", "Attainment", "Bizarre", "Bleak", "Catastrophe", "Celebrate",
            "Change", "Colorful", "Conflict", "Contact", "Control", "Creepy", "Crisis", "Cruelty", "Danger", "Dark",
            "Death", "Defeat", "Disruption", "Elements", "Emotions", "Enemies", "Energy", "Environment", "Event", "Evil",
            "Failure", "Fears", "Festive", "Fight", "Friendship", "Frightening", "Future", "Goals", "Good", "Guidance",
            "Harm", "Helpful", "Helpless", "Hint", "Hope", "Horrible", "Hurry", "Ideas", "Implore", "Important", "Incomplete",
            "Information", "Instruction", "Liberty", "Lies", "Love", "Malice", "Masses", "Mechanical", "Message", "Messy",
            "Military", "Misfortune", "Mundane", "Mysterious", "Natural", "Obscure", "Odd", "Oppose", "Path", "Peace",
            "People", "Place", "Plans", "Plot", "Positive", "Possessions", "Power", "Preventable", "Reassuring", "Riches",
            "Riddle", "Ruin", "Scary", "Simple", "Strange", "Struggle", "Success", "Suffering", "Suppress", "Tension",
            "Threat", "Time", "Travel", "Trouble", "Trust", "Uncertain", "Unsettling", "Violence", "Warning", "Weapon"
        ]

    def pick_words(self, table, num_of_selection):
        index = []
        for i in range(num_of_selection):
            num = random.randint(1, 100)
            while num in index:
                num = random.randint(1, 100)
            index.append(num)
        words = []
        for i in index:
            words.append(table[i - 1])
        outcome = ', '.join(words)
        return outcome
