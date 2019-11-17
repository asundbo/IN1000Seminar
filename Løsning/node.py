class Node:

    def __init__(self, minne, antPros):
        "Oppretter en node med gitt minne-storrelse og antall prosessorer"
        self._minne = minne
        self._antPros = antPros

    def antProsessorer(self):
        "Henter antall prosessorer i noden"
        return self._antPros

    def nokMinne(self, paakrevdMinne):
        "Sjekker om noden har tilstrekkelig minne for et program"
        if self._minne >= paakrevdMinne:
            return True
        return False
