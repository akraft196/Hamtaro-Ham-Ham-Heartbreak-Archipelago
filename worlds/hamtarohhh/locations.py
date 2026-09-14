from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import HamHamHeartbreakWorld

LOCATION_NAME_TO_ID = {
    "Sunny Peaks Blushie": 1
}

class HamHamHeartbreakLocation(Location):
    game = "Hamtaro Ham Ham Heartbreak"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: "HamHamHeartbreakWorld"):
    create_regular_locations(world)

def create_regular_locations(world: "HamHamHeartbreakWorld"):
    sp_bottom_left = world.get_region("Sunny Peaks Bottom Left")

    sp_bottom_left_locations = get_location_names_with_ids(
        ["Sunny Peaks Blushie"]
    )
    sp_bottom_left.add_locations(sp_bottom_left_locations, HamHamHeartbreakLocation)