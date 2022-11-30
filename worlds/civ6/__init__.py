from BaseClasses import Entrance, Region, RegionType
from worlds.AutoWorld import World
from .Items import item_name_to_id, location_name_to_id, Civ6Item

class Civ6(World):
    """
    Civilization VI is a video game
    """

    game = "Civilization VI"

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    data_version = 0

    hidden = True

    def __init__(self, world, player: int):
        super(Civ6, self).__init__(world, player)

    def create_items(self) -> None:
        for item, _ in item_name_to_id:
            self.multiworld.itempool.append(self.create_item(item))

    def create_item(self, name: str) -> Civ6Item:
        return Civ6Item(name)

    def create_regions(self) -> None:
        menu = Region("Menu", RegionType.Generic, "Menu", self.player, self.multiworld)
        menu.exits = [Entrance(self.player, "")]

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = (
            lambda state: state.has("Victory", self.player)
        )