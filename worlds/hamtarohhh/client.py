from typing import TYPE_CHECKING

from NetUtils import ClientStatus

from worlds._bizhawk.client import BizHawkClient
import worlds._bizhawk as bizhawk

from . import ItemData

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

TESTING = True


class HamHamHeartbreakClient(BizHawkClient):
    if TESTING:
        print("entering client")
    game = "Hamtaro Ham Ham Heartbreak"
    system = "GBA"
    patch_suffix = ".apextension"

    local_checked_locations: set[int]
    goal_flag: bool
    dictionary_offset: 10

    def initialize_client(self):
        self.local_checked_locations = set()
        self.goal_flag = False

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            if TESTING:
                print("checking rom")
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0xA0, 9, "ROM")]))[0]).decode("ascii")
            if TESTING:
                print(rom_name)
            if rom_name != "HAMUTARO":
                if TESTING:
                    print("invalid rom {0}", rom_name)
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

            if (hamchats[0] != 0):
                local_checked_locations.add("Heyhoo")
                write_result = await bizhawk.write(ctx, [(ItemData.dictionaryAddress + dictionary_offset, "IWRAM")])

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            if TESTING:
                print("Request failed")
            pass


