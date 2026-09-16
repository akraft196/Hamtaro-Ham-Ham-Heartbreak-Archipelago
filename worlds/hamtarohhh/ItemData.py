from BaseClasses import Item, ItemClassification
import typing

baseAddress = 0x3002178
dictionaryAddress = 0x30037C0

class ItemData:
    itemID: int
    progression: ItemClassification
    gameItemID: int = 0x0
    itemFlag: int = 0x0
    memoryAddress: int = 0x0

def initItemData (itemID, progression, gameItemID, itemFlag, memoryAddress):
    newItem = ItemData()
    newItem.itemID = itemID
    newItem.progression = progression
    newItem.gameItemID = gameItemID
    newItem.itemFlag = itemFlag
    newItem.memoryAddress = memoryAddress
    return newItem

hamchatItemData: typing.Dict[str, ItemData] = {
    "Blushie": initItemData(1, ItemClassification.progression_deprioritized_skip_balancing, 0x3C, 0x4, baseAddress),
    "Heyhoo": initItemData(2, ItemClassification.progression, 0x30, 0x400, baseAddress + 6),
    "Bluhoo": initItemData(3, ItemClassification.progression, 0x2D, 0x8, baseAddress + 6)
}