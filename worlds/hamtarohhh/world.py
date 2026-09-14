from worlds.AutoWorld import World

from . import items, locations, regions

class HamHamHeartbreakWorld(World):
    game = "Hamtaro Ham Ham Heartbreak"

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Sunny Peaks Bottom Left"

    def create_region(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.HamHamHeartbreakItem:
        return items.create_item_with_correct_classification(self, name)