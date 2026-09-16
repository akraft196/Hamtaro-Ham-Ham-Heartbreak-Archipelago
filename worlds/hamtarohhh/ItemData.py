from BaseClasses import Item, ItemClassification
import typing

baseAddress = 0x2178
dictionaryAddress = 0x37C0

class ItemData:
    itemID: int
    progression: ItemClassification
    gameItemID: int = 0x0
    itemFlag: int = 0x0
    offset: int = 0x0

def initItemData (itemID, progression, gameItemID, itemFlag, offset):
    newItem = ItemData()
    newItem.itemID = itemID
    newItem.progression = progression
    newItem.gameItemID = gameItemID
    newItem.itemFlag = itemFlag
    newItem.offset = offset
    return newItem

hamchatItemData: typing.Dict[str, ItemData] = {
    "Blushie": initItemData(1, ItemClassification.progression_deprioritized_skip_balancing, 0x3C, b'\x04', 8),
    "Heyhoo": initItemData(2, ItemClassification.progression, 0x30, b'\x40', 6),
    "Bluhoo": initItemData(3, ItemClassification.progression, 0x2D, b'\x08', 6),

}