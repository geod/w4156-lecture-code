from enum import Enum, auto


class Mood(Enum):
    Joyful = auto()
    Grumpy = auto()
    Irritated = auto()
    Hulk = auto()


class MoodCalculator:

    def calculate_mood(self, sleep_deprivation: int, blood_sugar: int) -> Mood:
        """
        Calculate humans Mood based on  and blood sugar
        :param sleep_deprivation: hours since last nap. Must be within 0 and 36 inclusive
        :param blood_sugar: glucose mmol/L. Must be within 70 to 90 inclusive
        :return: mood
        """
        if not 0 <= sleep_deprivation <= 36:
            raise ValueError("Sleep Deprivation:%s not within valid range (%s,%s)" % (sleep_deprivation, 0, 36))

        # TODO - student to complete the rest of the function and write the tests




