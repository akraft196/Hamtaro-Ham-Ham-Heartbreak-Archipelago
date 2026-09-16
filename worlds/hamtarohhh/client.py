from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from . import ItemData

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

TESTING = True

class HamHamHeartbreakClient(BizHawkClient):
    if TESTING:
        print("entering client")
    game = "Hamtaro Ham Ham Heartbreak"
    system = "GBA"

    local_checked_locations: set[int]
    goal_flag: bool
    dictionary_offset: int

    def initialize_client(self):
        self.local_checked_locations = set()
        self.goal_flag = False
        self.dictionary_offset = 10

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        await bizhawk.display_message(ctx.bizhawk_ctx, "entering validate_rom")
        try:
            # Check ROM name/patch version
            if TESTING:
                await bizhawk.display_message(ctx.bizhawk_ctx, "checking rom")
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0xA0, 9, "ROM")]))[0]).decode("ascii")
            if TESTING:
                await bizhawk.display_message(ctx.bizhawk_ctx, rom_name)
            if rom_name != "HAMUTARO":
                if TESTING:
                    await bizhawk.display_message(ctx.bizhawk_ctx,"invalid rom {0}", rom_name)
                return False  # Not a MYGAME ROM
        except bizhawk.RequestFailedError:
            if TESTING:
                print("Request failed")
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

            if hamchats[0] != 0:
                self.local_checked_locations.add(2)
                write_result = await bizhawk.write(ctx.bizhawk_ctx,
                [(ItemData.dictionaryAddress + self.dictionary_offset, [0x30], "IWRAM")])

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            if TESTING:
                print("Request failed")
            pass


