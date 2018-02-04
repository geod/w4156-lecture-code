from typing import Dict, Tuple, List
from enum import Enum, auto


class FriendFoe(Enum):
    Friend = auto()
    Foe = auto()


class RadarSignature:

    def __init__(self, x: float, y: float, friend_foe: FriendFoe):
        """
        :param x: in coordinate system relative to our plane
        :param y: in coordinate system relative to our plane
        :param friend_foe: is the plane friendly or foe
        """
        self.x = x
        self.y = y
        self.friend_foe = friend_foe


class NearestEnemyFinder:

    def detect_nearest_enemy(self, number_targets, signatures: List[RadarSignature]) -> List[Tuple[RadarSignature]]:
        """
        Detect the nearest N enemy targets
        :param number_targets: the number of enemy targets to return
        :param signatures: a list of radar signatures of planes. Coordinate system based around our plane being (0,0)
        :return: the N nearest enemy targets. If there are less than N enemy radar then return the
        """

        # TODO - exercise for the student to write an implementation



