from Options import Choice, Option, Range, ItemSet
import typing


class Goal(Choice):
    """The victory condition for your run. Stuff after the goal will not be shuffled."""
    display_name = "Goal"
    option_wall_of_flesh = 0
    option_plantera = 1
    option_moon_lord = 2
    option_zenith = 3
    default = 2


class Achievements(Choice):
    """
    Adds checks upon collecting achievements. Achievements for clearing bosses and events are excluded.
    "Exclude Grindy" also excludes fishing achievements.
    """
    display_name = "Achievements"
    option_none = 0
    option_exclude_grindy = 1
    option_exclude_fishing = 2
    option_all = 3
    default = 1


class BasicItemsWeight(Range):
    """
    Applies if you have achievements enabled.
    This determines the chance of extra items added to the pool being basic items
    (those not created by combining accessories).
    """
    range_end = 100
    default = 0


class CombinationAccessoryWeight(Range):
    """
    Applies if you have achievements enabled.
    This determines the chance of extra items added to the pool being combination accessories.
    """
    range_end = 100
    default = 100


class FiftySilverWeight(Range):
    """
    Applies if you have achievements enabled.
    This determines the chance of extra items added to the pool being "50 Silver."
    """
    range_end = 100
    default = 0


class GuaranteedItems(ItemSet):
    """
    Applies if you have achievements enabled.
    Items placed in this list will be guaranteed to be added to the item pool (if they all fit).
    """


options: typing.Dict[str, type(Option)] = {
    "goal": Goal,
    "achievements": Achievements,
    "basic_items_weight": BasicItemsWeight,
    "combination_accessory_weight": CombinationAccessoryWeight,
    "fifty_silver_weight": FiftySilverWeight,
    "guaranteed_items": GuaranteedItems
}
