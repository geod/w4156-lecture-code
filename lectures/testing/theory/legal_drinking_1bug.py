from lectures.testing.theory.nationality import Nationality


class LegalToDrinkCalculatorWithOneBug:

    @staticmethod
    def is_legal(age: int, nationality: Nationality) -> bool:
        """
        :param age: age of person buying alcohol
        :param nationality: nationality of the individual buying the alcohol
        :return:
        """
        legal = False
        if (Nationality.American == nationality and age >= 21) or (Nationality.British == nationality and age >= 16):
            legal = True
        return legal


