baseAddress = 0x3002178
dictionaryAddress = 0x30037C0

class ItemData:
    itemID: str
    progression: ItemClassification
    gameItemID: int = 0x0
    itemFlag: int = 0x0
    memoryAddress: int = 0x0

hamchatItemData: typing.Dict[str, ItemData] = {
    "Blushie": ItemData(1, ItemClassification.progression_deprioritized_skip_balancing, 0x3C, 0x4, baseAddress),
    "Heyhoo": ItemData(2, ItemClassification.progression, 0x03, 0x400, baseAddress + 6),
    "Bluhoo": ItemData(3, ItemClassification.progression, 0x2D, 0x8, baseAddress + 6)
}