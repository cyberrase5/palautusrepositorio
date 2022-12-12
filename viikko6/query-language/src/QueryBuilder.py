from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self):
        self._matchers = None

    def build(self):
        return All(self._matchers)

    def playsIn(self, team):
        return PlaysIn()