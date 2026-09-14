from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import HamHamHeartbreakWorld


def create_and_connect_regions(world: "HamHamHeartbreakWorld") -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: "HamHamHeartbreakWorld") -> None:
    sp_entrance = Region("Sunny Peaks Entrance", world.player, world.multiworld)
    sp_bottom_left = Region("Sunny Peaks Bottom Left", world.player, world.multiworld)

    regions = [sp_entrance, sp_bottom_left]

    world.multiworld.regions += regions

def connect_regions(world: "HamHamHeartbreakWorld") -> None:
    sp_entrance = world.get_region("Sunny Peaks Entrance")
    sp_bottom_left = world.get_region("Sunny Peaks Bottom Left")

    sp_entrance.connect(sp_bottom_left)
    sp_bottom_left.connect(sp_entrance)