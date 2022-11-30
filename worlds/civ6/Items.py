from BaseClasses import Item, ItemClassification, Location

class Civ6Item(Item):
    game = "Civilization VI"
    classification = ItemClassification.useful

    def __init__(self, name: str):
        self.name = name
        self.id = item_name_to_id.get(name)


class Civ6Location(Location):
    game = "Civilization VI"

    def __init__(self, player: int, name = "", code = None, parent = None):
        super(Civ6Location, self).__init__(player, name, code, parent)
        self.event = code is None

location_items = [
    # Techs

    # Ancient
    ("Tech Ancient 1.1", "Pottery"),
    ("Tech Ancient 1.2", "Animal Husbandry"),
    ("Tech Ancient 1.3", "Mining"),
    ("Tech Ancient 2.1", "Sailing"),
    ("Tech Ancient 2.2", "Astrology"),
    ("Tech Ancient 2.3", "Irrigation"),
    ("Tech Ancient 2.4", "Writing"),
    ("Tech Ancient 2.5", "Archery"),
    ("Tech Ancient 3.1", "Masonry"),
    ("Tech Ancient 3.2", "Bronze Working"),
    ("Tech Ancient 3.3", "Wheel"),

    # Classical
    ("Tech Classical 1.1", "Celestial Navigation"),
    ("Tech Classical 1.2", "Currency"),
    ("Tech Classical 1.3", "Horseback Riding"),
    ("Tech Classical 1.4", "Iron Working"),
    ("Tech Classical 2.1", "Shipbuilding"),
    ("Tech Classical 2.2", "Mathematics"),
    ("Tech Classical 2.3", "Construction"),
    ("Tech Classical 2.4", "Engineering"),

    # Medieval
    ("Tech Medieval 1.1", "Buttress"),
    ("Tech Medieval 1.2", "Military Tactics"),
    ("Tech Medieval 1.3", "Apprenticeship"),
    ("Tech Medieval 1.4", "Machinery"),
    ("Tech Medieval 2.1", "Education"),
    ("Tech Medieval 2.2", "Stirrups"),
    ("Tech Medieval 2.3", "Military Engineering"),
    ("Tech Medieval 2.4", "Castles"),

    # Renaissance
    ("Tech Renaissance 1.1", "Cartography"),
    ("Tech Renaissance 1.2", "Mass Production"),
    ("Tech Renaissance 1.3", "Banking"),
    ("Tech Renaissance 1.4", "Gunpowder"),
    ("Tech Renaissance 1.5", "Printing"),
    ("Tech Renaissance 2.1", "Square Rigging"),
    ("Tech Renaissance 2.2", "Astronomy"),
    ("Tech Renaissance 2.3", "Metal Casting"),
    ("Tech Renaissance 2.4", "Siege Tactics"),

    # Industrial
    ("Tech Industrial 1.1", "Industrialization"),
    ("Tech Industrial 1.2", "Scientific Theory"),
    ("Tech Industrial 1.3", "Ballistics"),
    ("Tech Industrial 1.4", "Military Science"),
    ("Tech Industrial 2.1", "Steam Power"),
    ("Tech Industrial 2.2", "Sanitation"),
    ("Tech Industrial 2.3", "Economics"),
    ("Tech Industrial 2.4", "Rifling"),

    # Modern
    ("Tech Modern 1.1", "Flight"),
    ("Tech Modern 1.2", "Replaceable Parts"),
    ("Tech Modern 1.3", "Steel"),
    ("Tech Modern 1.4", "Refining"),
    ("Tech Modern 2.1", "Electricity"),
    ("Tech Modern 2.2", "Radio"),
    ("Tech Modern 2.3", "Chemistry"),
    ("Tech Modern 2.4", "Combustion"),

    # Atomic
    ("Tech Atomic 1.1", "Advanced Flight"),
    ("Tech Atomic 1.2", "Rocketry"),
    ("Tech Atomic 1.3", "Advanced Ballistics"),
    ("Tech Atomic 1.4", "Combined Arms"),
    ("Tech Atomic 1.5", "Plastics"),
    ("Tech Atomic 2.1", "Computers"),
    ("Tech Atomic 2.2", "Nuclear Fission"),
    ("Tech Atomic 2.3", "Synthetic Materials"),

    # Information
    ("Tech Information 1.1", "Telecommunications"),
    ("Tech Information 1.2", "Satellites"),
    ("Tech Information 1.3", "Guidance Systems"),
    ("Tech Information 1.4", "Lasers"),
    ("Tech Information 1.5", "Composites"),
    ("Tech Information 1.6", "Stealth Technology"),
    ("Tech Information 2.1", "Robotics"),
    ("Tech Information 2.2", "Nuclear Fusion"),
    ("Tech Information 2.3", "Nanotechnology"),

    # Future
    ("Tech Future I", "Advanced AI"),
    ("Tech Future A", "Advanced Power Cells"),
    ("Tech Future C", "Cybernetics"),
    ("Tech Future O", "Offworld Mission"),
    ("Tech Future P", "Predictive Systems"),
    ("Tech Future S", "Seasteads"),
    ("Tech Future M", "Smart Materials"),

    # Civics

    # Ancient
    ("Civic Ancient 1.1", "Code of Laws"),
    ("Civic Ancient 2.1", "Craftsmanship"),
    ("Civic Ancient 2.2", "Foreign Trade"),
    ("Civic Ancient 3.1", "Military Tradition"),
    ("Civic Ancient 3.2", "State Workforce"),
    ("Civic Ancient 3.3", "Early Empire"),
    ("Civic Ancient 3.4", "Mysticism"),

    # Classical
    ("Civic Classical 1.1", "Games and Recreation"),
    ("Civic Classical 1.2", "Political Philosophy"),
    ("Civic Classical 1.3", "Drama and Poetry"),
    ("Civic Classical 2.1", "Military Training"),
    ("Civic Classical 2.2", "Defensive Tactics"),
    ("Civic Classical 2.3", "Recorded History"),
    ("Civic Classical 2.4", "Theology"),

    # Medieval
    ("Civic Medieval 1.1", "Naval Tradition"),
    ("Civic Medieval 1.2", "Feudalism"),
    ("Civic Medieval 1.3", "Civil Service"),
    ("Civic Medieval 2.1", "Mercenaries"),
    ("Civic Medieval 2.2", "Medieval Faires"),
    ("Civic Medieval 2.3", "Guilds"),
    ("Civic Medieval 2.4", "Divine Right"),

    # Renaissance
    ("Civic Renaissance 1.1", "Exploration"),
    ("Civic Renaissance 1.2", "Humanism"),
    ("Civic Renaissance 1.3", "Diplomatic Service"),
    ("Civic Renaissance 1.4", "Reformed Church"),
    ("Civic Renaissance 2.1", "Mercantilism"),
    ("Civic Renaissance 2.2", "The Enlightenment"),

    # Industrial
    ("Civic Industrial 1.1", "Colonialism"),
    ("Civic Industrial 1.2", "Civil Engineering"),
    ("Civic Industrial 1.3", "Nationalism"),
    ("Civic Industrial 1.4", "Opera and Ballet"),
    ("Civic Industrial 2.1", "Natural History"),
    ("Civic Industrial 2.2", "Urbanization"),
    ("Civic Industrial 2.3", "Scorched Earth"),

    # Modern
    ("Civic Modern 1.1", "Conservation"),
    ("Civic Modern 1.2", "Mass Media"),
    ("Civic Modern 1.3", "Mobilization"),
    ("Civic Modern 2.1", "Capitalism"),
    ("Civic Modern 2.2", "Ideology"),
    ("Civic Modern 3.1", "Nuclear Program"),
    ("Civic Modern 3.2", "Suffrage"),
    ("Civic Modern 3.3", "Totalitarianism"),
    ("Civic Modern 3.4", "Class Struggle"),

    # Atomic
    ("Civic Atomic 1.1", "Cultural Heritage"),
    ("Civic Atomic 1.2", "Cold War"),
    ("Civic Atomic 1.3", "Professional Sports"),
    ("Civic Atomic 2.1", "Rapid Development"),
    ("Civic Atomic 2.2", "Space Race"),

    # Information
    ("Civic Information 1.1", "Environmentalism"),
    ("Civic Information 1.2", "Globalization"),
    ("Civic Information 1.3", "Social Media"),
    ("Civic Information 2.1", "Near Future Governance"),
    ("Civic Information 2.2", "Venture Politics"),
    ("Civic Information 2.3", "Distributed Sovereignty"),
    ("Civic Information 2.4", "Optimization Imperative"),

    # Future
    ("Civic Future I", "Information Warfare"),
    ("Civic Future G", "Global Warming Mitigation"),
    ("Civic Future C", "Cultural Hegemony"),
    ("Civic Future S", "Smart Power Doctrine"),
    ("Civic Future E", "Exodus Imperative"),
]

root_items = [
    "Pottery",
    "Animal Husbandry",
    "Mining",
    "Sailing",
    "Astrology",
    "Code of Laws",
]

connections = {
    # Techs

    # Ancient
    "Pottery": [],
    "Animal Husbandry": [],
    "Mining": [],
    "Sailing": [],
    "Astrology": [],
    "Irrigation": [],
    "Writing": [],
    "Archery": [],
    "Masonry": [],
    "Bronze Working": [],
    "Wheel": [],

    # Classical
    "Celestial Navigation": [],
    "Currency": [],
    "Horseback Riding": [],
    "Iron Working": [],
    "Shipbuilding": [],
    "Mathematics": [],
    "Construction": [],
    "Engineering": [],

    # Medieval
    "Buttress": [],
    "Military Tactics": [],
    "Apprenticeship": [],
    "Machinery": [],
    "Education": [],
    "Stirrups": [],
    "Military Engineering": [],
    "Castles": [],

    # Renaissance
    "Cartography": [],
    "Mass Production": [],
    "Banking": [],
    "Gunpowder": [],
    "Printing": [],
    "Square Rigging": [],
    "Astronomy": [],
    "Metal Casting": [],
    "Siege Tactics": [],

    # Industrial
    "Industrialization": [],
    "Scientific Theory": [],
    "Ballistics": [],
    "Military Science": [],
    "Steam Power": [],
    "Sanitation": [],
    "Economics": [],
    "Rifling": [],

    # Modern
    "Flight": [],
    "Replaceable Parts": [],
    "Steel": [],
    "Refining": [],
    "Electricity": [],
    "Radio": [],
    "Chemistry": [],
    "Combustion": [],

    # Atomic
    "Advanced Flight": [],
    "Rocketry": [],
    "Advanced Ballistics": [],
    "Combined Arms": [],
    "Plastics": [],
    "Computers": [],
    "Nuclear Fission": [],
    "Synthetic Materials": [],

    # Information
    "Telecommunications": [],
    "Satellites": [],
    "Guidance Systems": [],
    "Lasers": [],
    "Composites": [],
    "Stealth Technology": [],
    "Robotics": [],
    "Nuclear Fusion": [],
    "Nanotechnology": [],

    # Future
    "Advanced AI": [],
    "Advanced Power Cells": [],
    "Cybernetics": [],
    "Offworld Mission": [],
    "Predictive Systems": [],
    "Seasteads": [],
    "Smart Materials": [],

    # Civics

    # Ancient
    "Code of Laws": [],
    "Craftsmanship": [],
    "Foreign Trade": [],
    "Military Tradition": [],
    "State Workforce": [],
    "Early Empire": [],
    "Mysticism": [],

    # Classical
    "Games and Recreation": [],
    "Political Philosophy": [],
    "Drama and Poetry": [],
    "Military Training": [],
    "Defensive Tactics": [],
    "Recorded History": [],
    "Theology": [],

    # Medieval
    "Naval Tradition": [],
    "Feudalism": [],
    "Civil Service": [],
    "Mercenaries": [],
    "Medieval Faires": [],
    "Guilds": [],
    "Divine Right": [],

    # Renaissance
    "Exploration": [],
    "Humanism": [],
    "Diplomatic Service": [],
    "Reformed Church": [],
    "Mercantilism": [],
    "The Enlightenment": [],

    # Industrial
    "Colonialism": [],
    "Civil Engineering": [],
    "Nationalism": [],
    "Opera and Ballet": [],
    "Natural History": [],
    "Urbanization": [],
    "Scorched Earth": [],

    # Modern
    "Conservation": [],
    "Mass Media": [],
    "Mobilization": [],
    "Capitalism": [],
    "Ideology": [],
    "Nuclear Program": [],
    "Suffrage": [],
    "Totalitarianism": [],
    "Class Struggle": [],

    # Atomic
    "Cultural Heritage": [],
    "Cold War": [],
    "Professional Sports": [],
    "Rapid Development": [],
    "Space Race": [],

    # Information
    "Environmentalism": [],
    "Globalization": [],
    "Social Media": [],
    "Near Future Governance": [],
    "Venture Politics": [],
    "Distributed Sovereignty": [],
    "Optimization Imperative": [],

    # Future
    "Information Warfare": [],
    "Global Warming Mitigation": [],
    "Cultural Hegemony": [],
    "Smart Power Doctrine": [],
    "Exodus Imperative": [],
}

base_id = 0xC60000
item_name_to_id: dict[str, int] = {}
location_name_to_id: dict[str, int] = {}

for i, location_item in enumerate(location_items):
    id = base_id + i
    item_name_to_id[location_items[1]] = id
    location_name_to_id[location_items[0]] = id
