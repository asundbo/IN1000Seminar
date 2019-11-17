from node import Node


class Rack:
    def __init__(self, maxAntallNoder):
        self._maxAntallNoder = maxAntallNoder
        self._listeMedNoder = []

    def settInn(self, node):
        "Plasserer en ny node inn i racket"
        self._listeMedNoder.append(node)

    def getAntNoder(self):
        return len(self._listeMedNoder)

    def antProsessorer(self):
        tempAntPros = 0  # Variabel som inneholder antall prosessorer

        for node in self._listeMedNoder:
            tempAntPros += node.antProsessorer()
        return tempAntPros

    def noderMedNokMinne(self, paakrevdMinne):
        "Beregner antall noder i racket med minne over gitt grense"
        antallNoder = 0
        krav = paakrevdMinne

        for node in self._listeMedNoder:
            if node.nokMinne(krav) is True:
                antallNoder += 1

        return antallNoder
