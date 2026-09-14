from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from . import ItemData

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


class MyGameClient(BizHawkClient):
    game = "Hamtaro Ham Ham Heartbreak"
    system = "GBA"
    patch_suffix = ".apextension"

    local_checked_locations: Set[int]
    goal_flag: bool
    dictionary_offset: 10

    def initialize_client(self):
        self.local_checked_locations = set()
        self.goal_flag = False

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0xA0, 9, "ROM")]))[0]).decode("ascii")
            if rom_name != "HAMUTARO":
                return False  # Not a MYGAME ROM
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now

        # This is a MYGAME ROM
        ctx.game = self.game
        ctx.items_handling = 0b001
        ctx.want_slot_data = True

        return True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        try:
            hamchats = await bizhawk.read(ctx.bizhawk_ctx, [(0x300217E, 1, "IWRAM")])
            print(hamchats)

            if (hamchats[0] != 0):
                local_checked_locations.add("Heyhoo")
                write_result = await bizhawk.write(ctx, [(ItemData.dictionaryAddress + dictionary_offset, "IWRAM")])

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass


