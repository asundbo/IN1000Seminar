from node import Node
from rack import Rack


class Regneklynge:
    # Oppretter en regneklynge og setter maks antall
    # det er plass til i et rack
    # @param noderPerRack max antall noder per rack
    def __init__(self, maxNoderPerRack):
        self._listeMedRack = []
        self._maxNoderPerRack = maxNoderPerRack

    # Plasserer en node inn i et rack med ledig plass, eller i et nytt
    # @param node referanse til noden som skal settes inn i datastrukturen
    def settInnNode(self, node):

        pass

    # Beregner totalt antall prosessorer i hele regneklyngen
    # @return totalt antall prosessorer
    def antProsessorer(self):
        pass

    # Beregner antall noder i regneklyngen med minne over angitt grense
    # @param paakrevdMinne hvor mye minne skal noder som telles med ha
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        pass

    # Henter antall racks i regneklyngen
    # @return antall racks
    def antRacks(self):
        pass

    def leggTilNoder(self, antallNoder, MinnerPerNode, ProcPerNode):
        maxIRack = self._maxNoderPerRack

        if len(self._listeMedRack) == 0:
            self._listeMedRack.append(Rack(maxIRack))

        # for rack in self._listeMedRack:
        #     if rack.getAntNoder <= maxIRack:
        sisteLedig = 0

        for i in range(0, antallNoder):
            sisteRack = self._listeMedRack[sisteLedig]
            if sisteRack.getAntNoder() <= maxIRack - 1:
                sisteRack.settInn(Node(MinnerPerNode, ProcPerNode))
                index = self._listeMedRack.index(sisteRack)
                print(f"Node added in rack {index}")
                print(sisteRack.getAntNoder())
            elif sisteRack.getAntNoder() > maxIRack - 1:
                self._listeMedRack.append(Rack(maxIRack))
                sisteLedig += 1
                print("Added new rack! snfhash")
                self._listeMedRack[sisteLedig].settInn(Node(MinnerPerNode, ProcPerNode))
                print("AND NEW NODE")
