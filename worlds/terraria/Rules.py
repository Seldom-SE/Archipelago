def hardmode_ores(player, state, fishing, alt_prog):
    return state.has("Hardmode", player) and (fishing or not alt_prog or state.has_any({"Post-Eye of Cthulhu", "Post-The Twins", "Post-The Destroyer", "Post-Skeletron Prime", "Post-Golem"}, player))

def plantera(player, state):
    state.has_all({"Hardmode", "Post-The Twins", "Post-The Destroyer", "Post-Skeletron Prime"}, player)

def frost_moon(player, state, fishing, alt_prog):
    return state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player) and hardmode_ores(player, state, fishing, alt_prog)

# `fishing` allows really grindy fishing, like fishing achievements and fishing for a specific crate drop
# `alt_prog` makes many alterations to the progression to make the game better for randomization. This includes:
# * Guide requires Post-Eye of Cthulhu and does not spawn in new worlds
# * Dryad requires Post-King Slime instead of her usual requirements
# * Slime Crown is crafted at Imbuing Station instead of Demon Altar
# * Hive cannot be mined until Post-Deerclops
# * Deer Thing is crafted at Alchemy Table instead of Demon Altar
# * Haemorrhaxe requires Post-Golem
# * Mechanical Eye requires a Hive
# * Mechanical Worm requires a Defender Medal
# These rules contain redundancies to avoid bugs when adding new features
def get_rules(player, fishing, alt_prog):
    return {
        "King Slime": lambda state: not alt_prog or state.has("Post-Queen Bee", player),
        "Old One's Army Tier 1": lambda state: state.has("Post-Eater of Worlds or Brain of Cthulhu", player),
        "Queen Bee": lambda state: not alt_prog or state.has("Post-Deerclops", player),
        "Deerclops": lambda state: not alt_prog or state.has("Post-Skeletron", player),
        "Wall of Flesh": lambda state: not alt_prog or state.has("Post-Eye of Cthulhu", player),
        "Pirate Invasion": lambda state: state.has("Hardmode", player),
        "Queen Slime": lambda state: state.has("Hardmode", player),
        "The Twins": lambda state: (not alt_prog or state.has("Post-Deerclops")) and state.has("Hardmode", player) and hardmode_ores(player, state, fishing, alt_prog),
        "The Destroyer": lambda state: (not alt_prog or state.has("Post-Eater of Worlds or Brain of Cthulhu")) and state.has("Hardmode", player) and hardmode_ores(player, state, fishing, alt_prog),
        "Skeletron Prime": lambda state: state.has_all({"Post-Skeletron", "Hardmode"}, player) and hardmode_ores(player, state, fishing, alt_prog),
        "Old One's Army Tier 2": lambda state: state.has_any({"Post-The Twins", "Post-The Destroyer", "Post-Skeletron Prime", "Post-Golem"}, player) and state.has_all({"Post-Eater of Worlds or Brain of Cthulhu", "Hardmode"}, player),
        "Plantera": lambda state: plantera(player, state),
        "Duke Fishron": lambda state: state.has("Hardmode", player),
        "Frost Legion": lambda state: state.has_all("Hardmode", player) and frost_moon(player, state, fishing, alt_prog),
        "Golem": lambda state: state.has_all({"Hardmode", "Post-Plantera"}, player) and (plantera(player, state) or state.has("Post-Golem", player)),
        "Old One's Army Tier 3": lambda state: state.has_all({"Post-Eater of Worlds or Brain of Cthulhu", "Hardmode", "Post-Golem"}, player),
        "Martian Madness": lambda state: state.has_all({"Hardmode", "Post-Golem"}, player), # You are here
        "Mourning Wood": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Pumpking": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Everscream": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Santa-NK1": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Ice Queen": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Empress of Light": lambda state: state.has_all({"Hardmode", "Post-Plantera"}, player),
        "Lunatic Cultist": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Golem"}, player),
        "Lunar Events": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Golem"}, player),
        "Moon Lord": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Golem"}, player),
        "Zenith": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-The Twins", "Post-The Destroyer", "Post-Skeletron Prime", "Post-Plantera", "Post-Golem"}, player),
        "Dungeon Heist": lambda state: state.has("Post-Skeletron", player),
        "Boots of the Hero": lambda state: state.has("Post-Goblin Army", player),
        "Head in the Clouds": lambda state: fishing or state.has("Hardmode", player),
        "Begone, Evil!": lambda state: state.has("Hardmode", player),
        "Extra Shiny!": lambda state: state.has("Hardmode", player),
        "Drax Attax": lambda state: state.has_all({"Post-Skeletron", "Hardmode"}, player),
        "Photosynthesis": lambda state: state.has_all({"Post-Skeletron", "Hardmode"}, player),
        "Get a Life": lambda state: state.has("Hardmode", player),
        "Kill the Sun": lambda state: state.has("Hardmode", player),
        "Mecha Mayhem": lambda state: state.has_all({"Post-Skeletron", "Hardmode"}, player),
        "Prismancer": lambda state: state.has("Hardmode", player),
        "It Can Talk?!": lambda state: state.has("Hardmode", player),
        "Gelatin World Tour": lambda state: state.has_all({"Post-Skeletron", "Hardmode"}, player),
        "Topped Off": lambda state: state.has("Hardmode", player),
        "Don't Dread on Me": lambda state: state.has("Hardmode", player),
        "Temple Raider": lambda state: state.has_all({"Hardmode", "Post-The Twins", "Post-The Destroyer", "Post-Skeletron Prime"}, player),
        "Robbing the Grave": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Baleful Harvest": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Ice Scream": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Sword of the Hero": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Big Booty": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Real Estate Agent": lambda state: state.has_all({"Post-Goblin Army", "Post-Eater of Worlds or Brain of Cthulhu", "Post-Queen Bee", "Post-Skeletron", "Hardmode", "Post-Pirate Invasion", "Post-Plantera"}, player) and state.has_any({"Post-The Twins", "Post-The Destroyer", "Post-Skeletron Prime"}, player),
        "Rainbows and Unicorns": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Plantera"}, player),
        "Sick Throw": lambda state: state.has_all({"Post-Skeletron", "Hardmode", "Post-Golem"}, player),
        "You and What Army?": lambda state: state.has_any({"Post-Queen Bee", "Post-Plantera"}, player) and state.has_all({"Post-Skeletron", "Hardmode", "Post-Golem"}, player),
    }

# post_plantera_locations = [
#     "Mourning Wood",
#     "Pumpking",
#     "Everscream",
#     "Santa-NK1",
#     "Ice Queen",
#     "Empress of Light",
#     "Lunatic Cultist",
#     "Lunar Events",
#     "Moon Lord",
# ]
# 
# post_moon_lord_locations = [
#     "Zenith",
# ]
# 
# prehardmode_achievements = [
#     "Timber!!",
#     "No Hobo",
#     "Stop! Hammer Time!",
#     "Ooo! Shiny!",
#     "Heart Breaker",
#     "Heavy Metal",
#     "I Am Loot!",
#     "Star Power",
#     "Hold on Tight!",
#     "Smashing, Poppet!",
#     "Where's My Honey?",
#     "Dungeon Heist",
#     "It's Getting Hot in Here",
#     "Miner for Fire",
#     "Like a Boss",
#     "Bloodbath",
#     "Not the Bees!",
#     "Jeepers Creepers",
#     "Funkytown",
#     "Into Orbit",
#     "Rock Bottom",
#     "Fashion Statement",
#     "Vehicular Manslaughter",
#     "Lucky Break",
#     "Throwing Lines",
#     "Dye Hard",
#     "The Cavalry",
#     "Completely Awesome",
#     "Til Death...",
#     "Watch Your Step!",
#     "You Can Do It!",
#     "Matching Attire",
#     "Benched",
#     "Quiet Neighborhood",
#     "Hot Reels!",
#     "Leading Landlord",
#     "Feeling Petty",
# ]
# 
# grindy_prehardmode_achievements = [
#     "Sticky Situation",
#     "There are Some Who Call Him...",
#     "Deceiver of Fools",
#     "Archaeologist",
#     "Pretty in Pink",
#     "Boots of the Hero",
#     "A Rather Blustery Day",
#     "Heliophobia",
#     "Jolly Jamboree",
#     "Dead Men Tell No Tales",
# ]
# 
# fishing_prehardmode_achievements = [
#     "Glorious Golden Pole",
#     "Servant-in-Training",
#     "10 Fishing Quests", # This achievement was intentionally renamed
#     "Trout Monkey",
#     "Fast and Fishious",
#     "Supreme Helper Minion!",
# ]
# 
# achievements_that_are_fishing_if_prehardmode = [
#     "Head in the Clouds",
# ]
# 
# post_wall_of_flesh_achievements = [
#     "Begone, Evil!",
#     "Extra Shiny!",
#     "Drax Attax",
#     "Photosynthesis",
#     "Get a Life",
#     "Kill the Sun",
#     "Mecha Mayhem",
#     "Prismancer",
#     "It Can Talk?!",
# ]
# 
# grindy_post_wall_of_flesh_achievements = [
#     "Gelatin World Tour",
#     "Topped Off",
#     "Don't Dread on Me",
# ]
# 
# post_plantera_achievements = [
#     "Temple Raider",
#     "Robbing the Grave",
#     "Baleful Harvest",
#     "Ice Scream",
#     "Sword of the Hero",
# ]
# 
# grindy_post_plantera_achievements = [
#     "Big Booty",
#     "Real Estate Agent",
#     "Rainbows and Unicorns",
# ]
# 
# post_moon_lord_achievements = [
#     "Sick Throw",
#     "You and What Army?",
# ]