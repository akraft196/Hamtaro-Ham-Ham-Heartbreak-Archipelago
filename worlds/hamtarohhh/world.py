from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions
from . import options as test_options

class HamHamHeartbreakWorld(World):
    game = "Hamtaro Ham Ham Heartbreak"

    options_dataclass = test_options.TestingOptions
    options: test_options.TestingOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Sunny Peaks Bottom Left"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.HamHamHeartbreakItem:
        return items.create_item_with_correct_classification(self, name)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "test_option"
        )