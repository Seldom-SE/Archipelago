from BaseClasses import Location, Item

misc_items = [
    "50 Silver",
    "Victory",
]

prehardmode_items = [
    "Torch God's Favor",
    "Post-Goblin Army",
    "Post-King Slime",
    "Post-Eye of Cthulhu",
    "Post-Eater of Worlds or Brain of Cthulhu",
    "Post-Old One's Army Tier 1",
    "Post-Queen Bee",
    "Post-Skeletron",
    "Post-Deerclops",
]

post_wall_of_flesh_items = [
    "Hardmode",
    "Post-Pirate Invasion",
    "Post-Queen Slime",
    "Post-The Twins",
    "Post-The Destroyer",
    "Post-Skeletron Prime",
    "Post-Old One's Army Tier 2",
    "Post-Duke Fishron",
]

post_plantera_items = [
    "Post-Frost Legion",
    "Post-Plantera",
    "Post-Golem",
    "Post-Old One's Army Tier 3",
    "Post-Martian Madness",
    "Post-Mourning Wood",
    "Post-Pumpking",
    "Post-Everscream",
    "Post-Santa-NK1",
    "Post-Ice Queen",
    "Post-Empress of Light",
    "Post-Lunatic Cultist",
    "Post-Lunar Events",
]

post_moon_lord_items = [
    "Post-Moon Lord"
]

base_items = [
    "Adhesive Bandage",
    "Aglet",
    "Ancient Chisel",
    "Angler Earring",
    "Anklet of the Wind",
    "Apprentice's Scarf",
    "Armor Polish",
    "Balloon Pufferfish",
    "Band of Regeneration",
    "Band of Starpower",
    "Bezoar",
    "Black Belt",
    "Blindfold",
    "Blizzard in a Bottle",
    "Brick Layer",
    "Celestial Magnet",
    "Climbing Claws",
    "Cloud in a Bottle",
    "Cobalt Shield",
    "Compass",
    "Cross Necklace",
    "DPS Meter",
    "Demon Conch",
    "Depth Meter",
    "Discount Card",
    "Dunerider Boots",
    "Extendo Grip",
    "Eye of the Golem",
    "Fast Clock",
    "Feral Claws",
    "Fisherman's Pocket Guide",
    "Fledgling Wings",
    "Flesh Knuckles",
    "Flipper",
    "Flower Boots",
    "Flurry Boots",
    "Flying Carpet",
    "Frog Leg",
    "Frozen Turtle Shell",
    "Gold Ring",
    "Grappling Hook",
    "Hand Warmer",
    "Hercules Beetle",
    "Hermes Boots",
    "High Test Fishing Line",
    "Honey Comb",
    "Huntress's Buckler",
    "Ice Skates",
    "Inner Tube",
    "Jellyfish Necklace",
    "Lava Charm",
    "Lavaproof Fishing Hook",
    "Lifeform Analyzer",
    "Lucky Coin",
    "Lucky Horseshoe",
    "Magic Conch",
    "Magic Mirror",
    "Magic Quiver",
    "Magiluminescence",
    "Magma Stone",
    "Megaphone",
    "Metal Detector",
    "Monk's Belt",
    "Moon Charm",
    "Moon Stone",
    "Nature's Gift",
    "Nazar",
    "Necromantic Scroll",
    "Neptune's Shell",
    "Obsidian Rose",
    "Obsidian Skull",
    "Paint Sprayer",
    "Paladin's Shield",
    "Panic Necklace",
    "Philosopher's Stone",
    "Pocket Mirror",
    "Pocket Mirror",
    "Portable Cement Mixer",
    "Putrid Scent",
    "Pygmy Necklace",
    "Radar",
    "Ranger Emblem",
    "Red Counterweight",
    "Rifle Scope",
    "Rocket Boots",
    "Rod of Discord",
    "Sailfish Boots",
    "Sandstorm in a Bottle",
    "Sextant",
    "Shackle",
    "Shark Tooth Necklace",
    "Shiny Red Balloon",
    "Shoe Spikes",
    "Sorcerer Emblem",
    "Squire's Shield",
    "Star Cloak",
    "Step Stool",
    "Stopwatch",
    "Summoner Emblem",
    "Sun Stone",
    "Tabi",
    "Tackle Box",
    "Tally Counter",
    "Titan Glove",
    "Treasure Magnet",
    "Trifold Map",
    "Tsunami in a Bottle",
    "Vitamins",
    "Warrior Emblem",
    "Water Walking Boots",
    "Weather Radio",
    "White String",
    "Yoyo Glove",

]

combination_items = [
    "Ankh Charm",
    "Ankh Shield",
    "Amber Horseshoe Balloon",
    "Amphibian Boots",
    "Arcane Flower",
    "Arctic Diving Gear",
    "Armor Bracing",
    "Avenger Emblem",
    "Bee Cloak",
    "Berserker's Glove",
    "Blizzard in a Balloon",
    "Blue Horseshoe Balloon",
    "Celestial Cuffs",
    "Celestial Emblem",
    "Celestial Stone",
    "Celestial Shell",
    "Charm of Myths",
    "Cloud in a Balloon",
    "Coin Ring",
    "Countercurse Mantra",
    "Destroyer Emblem",
    "Diving Gear",
    "Fairy Boots",
    "Fart in a Balloon",
    "Fart in a Jar",
    "Fire Gauntlet",
    "Frog Flipper",
    "Frog Gear",
    "Frog Webbing",
    "Frostspark Boots",
    "Greedy Ring",
    "Green Horseshoe Balloon",
    "Hellfire Treads",
    "Hero Shield",
    "Honey Balloon",
    "Jellyfish Diving Gear",
    "Lava Waders",
    "Lightning Boots",
    "Magic Cuffs",
    "Magnet Flower",
    "Magma Skull",
    "Mana Cloak",
    "Mana Flower",
    "Mana Regeneration Band",
    "Master Ninja Gear",
    "Mechanical Glove",
    "Medicated Bandage",
    "Molten Charm",
    "Molten Quiver",
    "Molten Skull Rose",
    "Moon Shell",
    "Neptune's Shell",
    "Obsidian Horseshoe",
    "Obsidian Shield",
    "Obsidian Skull Rose",
    "Obsidian Water Walking Boots",
    "Papyrus Scarab",
    "Pink Horseshoe Balloon",
    "Power Glove",
    "Recon Scope",
    "Sandstorm in a Balloon",
    "Sharkron Balloon",
    "Sniper Scope",
    "Spectre Boots",
    "Stalker's Quiver",
    "Star Veil",
    "Stinger Necklace",
    "Sweetheart Necklace",
    "Terraspark Boots",
    "The Plan",
    "Tiger Climbing Gear",
    "White Horseshoe Balloon",
    "Yellow Horseshoe Balloon",
    "Yoyo Bag",
]

# Debugging utility
precollected = []

prehardmode_locations = [
    "Torch God",
    "Goblin Army",
    "King Slime",
    "Eye of Cthulhu",
    "Eater of Worlds or Brain of Cthulhu",
    "Old One's Army Tier 1",
    "Queen Bee",
    "Skeletron",
    "Deerclops",
    "Wall of Flesh",
]

post_wall_of_flesh_locations = [
    "Pirate Invasion",
    "Queen Slime",
    "The Twins",
    "The Destroyer",
    "Skeletron Prime",
    "Old One's Army Tier 2",
    "Plantera",
    "Duke Fishron",
]

post_plantera_locations = [
    "Frost Legion",
    "Golem",
    "Old One's Army Tier 3",
    "Martian Madness",
    "Mourning Wood",
    "Pumpking",
    "Everscream",
    "Santa-NK1",
    "Ice Queen",
    "Empress of Light",
    "Lunatic Cultist",
    "Lunar Events",
    "Moon Lord",
]

post_moon_lord_locations = [
    "Zenith",
]

prehardmode_achievements = [
    "Timber!!",
    "No Hobo",
    "Stop! Hammer Time!",
    "Ooo! Shiny!",
    "Heart Breaker",
    "Heavy Metal",
    "I Am Loot!",
    "Star Power",
    "Hold on Tight!",
    "Smashing, Poppet!",
    "Where's My Honey?",
    "Dungeon Heist",
    "It's Getting Hot in Here",
    "Miner for Fire",
    "Like a Boss",
    "Bloodbath",
    "Not the Bees!",
    "Jeepers Creepers",
    "Funkytown",
    "Into Orbit",
    "Rock Bottom",
    "Fashion Statement",
    "Vehicular Manslaughter",
    "Lucky Break",
    "Throwing Lines",
    "Dye Hard",
    "The Cavalry",
    "Completely Awesome",
    "Til Death...",
    "Watch Your Step!",
    "You Can Do It!",
    "Matching Attire",
    "Benched",
    "Quiet Neighborhood",
    "Hot Reels!",
    "Leading Landlord",
    "Feeling Petty",
]

grindy_prehardmode_achievements = [
    "Sticky Situation",
    "There are Some Who Call Him...",
    "Deceiver of Fools",
    "Archaeologist",
    "Pretty in Pink",
    "Boots of the Hero",
    "A Rather Blustery Day",
    "Heliophobia",
    "Jolly Jamboree",
    "Dead Men Tell No Tales",
]

fishing_prehardmode_achievements = [
    "Glorious Golden Pole",
    "Servant-in-Training",
    "10 Fishing Quests", # This achievement was intentionally renamed
    "Trout Monkey",
    "Fast and Fishious",
    "Supreme Helper Minion!",
]

achievements_that_are_fishing_if_prehardmode = [
    "Head in the Clouds",
]

post_wall_of_flesh_achievements = [
    "Begone, Evil!",
    "Extra Shiny!",
    "Drax Attax",
    "Photosynthesis",
    "Get a Life",
    "Kill the Sun",
    "Mecha Mayhem",
    "Prismancer",
    "It Can Talk?!",
]

grindy_post_wall_of_flesh_achievements = [
    "Gelatin World Tour",
    "Topped Off",
    "Don't Dread on Me",
]

post_plantera_achievements = [
    "Temple Raider",
    "Robbing the Grave",
    "Baleful Harvest",
    "Ice Scream",
    "Sword of the Hero",
]

grindy_post_plantera_achievements = [
    "Big Booty",
    "Real Estate Agent",
    "Rainbows and Unicorns",
]

post_moon_lord_achievements = [
    "Sick Throw",
    "You and What Army?",
]


def register(names, name_to_id, next_id):
    for name in names:
        name_to_id[name] = next_id
        next_id += 1
    return next_id


def assign_ids():
    next_id = 0x7E0000

    item_name_to_id: dict[str, int] = {}
    location_name_to_id: dict[str, int] = {}

    next_id = register(misc_items, item_name_to_id, next_id)
    next_id = register(prehardmode_items, item_name_to_id, next_id)
    next_id = register(post_wall_of_flesh_items, item_name_to_id, next_id)
    next_id = register(post_plantera_items, item_name_to_id, next_id)
    next_id = register(post_moon_lord_items, item_name_to_id, next_id)
    next_id = register(base_items, item_name_to_id, next_id)
    next_id = register(combination_items, item_name_to_id, next_id)

    next_id = register(prehardmode_locations, location_name_to_id, next_id)
    next_id = register(post_wall_of_flesh_locations, location_name_to_id, next_id)
    next_id = register(post_plantera_locations, location_name_to_id, next_id)
    next_id = register(post_moon_lord_locations, location_name_to_id, next_id)
    next_id = register(prehardmode_achievements, location_name_to_id, next_id)
    next_id = register(grindy_prehardmode_achievements, location_name_to_id, next_id)
    next_id = register(fishing_prehardmode_achievements, location_name_to_id, next_id)
    next_id = register(achievements_that_are_fishing_if_prehardmode, location_name_to_id, next_id)
    next_id = register(post_wall_of_flesh_achievements, location_name_to_id, next_id)
    next_id = register(grindy_post_wall_of_flesh_achievements, location_name_to_id, next_id)
    next_id = register(post_plantera_achievements, location_name_to_id, next_id)
    next_id = register(grindy_post_plantera_achievements, location_name_to_id, next_id)
    next_id = register(post_moon_lord_achievements, location_name_to_id, next_id)

    return item_name_to_id, location_name_to_id


item_name_to_id, location_name_to_id = assign_ids()


class TerrariaItem(Item):
    game = "Terraria"


class TerrariaLocation(Location):
    game = "Terraria"


def get_items_locations(multiworld, player):

    goal = multiworld.goal[player].value
    achievements_opt = multiworld.achievements[player].value

    items = prehardmode_items.copy()
    if goal > 0:
        items += post_wall_of_flesh_items
    if goal > 1:
        items += post_plantera_items
    if goal > 2:
        items += post_moon_lord_items

    locations = prehardmode_locations.copy()
    if goal > 0:
        locations += post_wall_of_flesh_locations
    if goal > 1:
        locations += post_plantera_locations
    if goal > 2:
        locations += post_moon_lord_locations
    if achievements_opt > 0:
        locations += prehardmode_achievements
    if achievements_opt > 1:
        locations += grindy_prehardmode_achievements
    if achievements_opt > 2:
        locations += fishing_prehardmode_achievements
    if (goal > 0 and achievements_opt > 0) or achievements_opt > 2:
        locations += achievements_that_are_fishing_if_prehardmode
    if goal > 0 and achievements_opt > 0:
        locations += post_wall_of_flesh_achievements
    if goal > 0 and achievements_opt > 1:
        locations += grindy_post_wall_of_flesh_achievements
    if goal > 1 and achievements_opt > 0:
        locations += post_plantera_achievements
    if goal > 1 and achievements_opt > 1:
        locations += grindy_post_plantera_achievements
    if goal > 2 and achievements_opt > 0:
        locations += post_moon_lord_achievements

    base_item_list = base_items.copy()
    combination_item_list = combination_items.copy()

    choices = [base_item_list, combination_item_list, ["50 Silver"]]
    weights = [multiworld.basic_items_weight[player].value, multiworld.combination_accessory_weight[player].value,
               multiworld.fifty_silver_weight[player].value]
    guaranteed_items = list(multiworld.guaranteed_items[player].value)
    # sort before shuffling to ensure no unpredictable results from the set
    guaranteed_items.sort()
    multiworld.random.shuffle(guaranteed_items)

    while len(items) < len(locations) - 1:
        if guaranteed_items:
            items.append(guaranteed_items.pop())
        else:
            if len(choices[0]) == 0:
                weights[0] = 0
            if len(choices[1]) == 0:
                weights[1] = 0
            if weights == [0, 0, 0]:
                weights = [0, 0, 1]
            choice_list = multiworld.random.choices(choices, weights, k=1)[0]
            item = multiworld.random.choice(choice_list)
            if item != "50 Silver":
                choice_list.remove(item)
            items.append(item)

    return items, locations
