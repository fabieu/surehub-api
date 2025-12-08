from enum import Enum


class LockMode(Enum):
    NONE = "none"
    BOTH = "both"
    IN = "in"
    OUT = "out"

    @property
    def mode_id(self) -> int:
        return {
            LockMode.NONE: 0,
            LockMode.IN: 1,
            LockMode.OUT: 2,
            LockMode.BOTH: 3,
        }[self]
