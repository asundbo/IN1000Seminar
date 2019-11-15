from node import Node


class Rack:
    # oppretter et rack der det senere kan plasseres noder
    #
    def __init__(self):
        pass

    # Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
        pass

    # Henter antall noder i racket
    # @return antall noder
    def getAntNoder(self):
        pass

    # Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def antProsessorer(self):
        pass

    # Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        pass
