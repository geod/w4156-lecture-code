from lectures.testing.theory.nationality import Nationality


class LegalToDrinkCalculatorWithTwoBugs:
    """
    https://en.wikipedia.org/wiki/U.S._history_of_alcohol_minimum_purchase_age_by_state
    http://news.bbc.co.uk/2/hi/uk_news/6598867.stm
    """

    @staticmethod
    def is_legal(age: int, nationality: Nationality) -> bool:
        """
        NOTE - this sample code has (at least one) intentional bug which is the legal age in Britain is 18
        (Would also write this differently but is coded this way for the purposes of demonstrating coverage)
        :param age: age of person buying alcohol
        :param nationality: nationality of the individual buying the alcohol
        :return:
        """
        legal = True
        if (Nationality.American == nationality and age >= 21) or (Nationality.British == nationality and age >= 16):
            legal = True
        return legal
