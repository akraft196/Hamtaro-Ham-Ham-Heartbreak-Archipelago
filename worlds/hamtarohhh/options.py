from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions

class TestOption(Toggle):
    display_name = "TestOption"

@dataclass
class TestingOptions(PerGameCommonOptions):
    test_option: TestOption