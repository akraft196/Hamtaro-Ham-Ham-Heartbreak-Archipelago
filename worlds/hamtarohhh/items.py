from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import HamHamHeartbreakWorld

ITEM_NAME_TO_ID = {
    "Heyhoo": 2,
    "Sunflower Seeds": 87
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Heyhoo": ItemClassification.progression_skip_balancing,
    "Sunflower Seeds": ItemClassification.filler
}

class HamHamHeartbreakItem(Item):
    game = "Hamtaro Ham Ham Heartbreak"

def create_item_with_correct_classification(world: HamHamHeartbreakWorld, name: str) -> HamHamHeartbreakItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return HamHamHeartbreakItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: HamHamHeartbreakWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Heyhoo"),
        world.create_item("Sunflower Seeds")
    ]
    print(itempool)

    world.multiworld.itempool += itempool
    print(world.multiworld.itempool)