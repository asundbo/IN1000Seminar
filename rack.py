from node import Node


class Rack:
    # oppretter et rack der det senere kan plasseres noder
    #
    def __init__(self, maxAntallNoder):
        self._maxAntallNoder = maxAntallNoder
        self._listeMedNoder = []

    # Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
        self._listeMedNoder.append(node)

    # Henter antall noder i racket
    # @return antall noder

    def getAntNoder(self):
        return len(self._listeMedNoder)

    # Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def antProsessorer(self):
        tempAntPros = 0

        for node in self._listeMedNoder:
            tempAntPros += node.antProsessorer()

        return tempAntPros

    # Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        antallNoder = 0
        krav = paakrevdMinne

        for node in self._listeMedNoder:
            if node.nokMinne(krav) is True:
                antallNoder += 1

        return antallNoder
