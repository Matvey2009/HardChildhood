from enum import Enum
from Zerg import Zerg
from Terran import Terran
from Protoss import Protoss


class Factory():
    """ Паттерны фабрики """
    class Race(Enum):
        """Вложенный класс"""
        ZERG = 0,
        TERRAN = 1,
        PROTOSS = 2

    factort_digt = {
        Race.ZERG: Zerg,
        Race.TERRAN: Terran,
        Race.PROTOSS: Protoss
    }

    def new_unit(self, race):
        return self.factort_digt[race]()
