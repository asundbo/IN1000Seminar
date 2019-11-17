from node import Node
from rack import Rack


class Regneklynge:
    def __init__(self, maxNoderPerRack):
        self._listeMedRack = []
        self._maxNoderPerRack = maxNoderPerRack
        self._sisteLedig = 0  # Vi lager det har pga metoden "leggTilNoder"
        # Vi trenger den å være i konstrukten så det ikke blir nullet i metoden som bruker datasenter
        # + vi kan kalle metoden mange ganger

    def settInnNode(self, node):
        # Vi har lagt vår egen metode som gjør det
        pass

    def antProsessorer(self):
        "Beregner totalt antall prosessorer i hele regneklyngen"
        antall = 0  # temp variable
        for rack in self._listeMedRack:
            antall += rack.antProsessorer()
            # Rack is not a list istelf, we cannot iterate over it
            # Therefore we have to use the rack method

        return antall

    def noderMedNokMinne(self, paakrevdMinne):
        "Beregner antall noder i regneklyngen med minne over angitt grense"
        noderMedNok = 0

        for rack in self._listeMedRack:
            noderMedNok += rack.noderMedNokMinne(paakrevdMinne)

        return noderMedNok

    def antRacks(self):
        "Henter antall racks i regneklyngen"
        return len(self._listeMedRack)

    def leggTilNoder(self, antallNoder, MinnerPerNode, ProcPerNode):
        maxIRack = self._maxNoderPerRack

        # We need to make a first rack first!
        if len(self._listeMedRack) == 0:
            self._listeMedRack.append(Rack(maxIRack))

        for i in range(0, antallNoder):
            sisteRack = self._listeMedRack[self._sisteLedig]

            if sisteRack.getAntNoder() < maxIRack:
                # Previously we had maxIRack - 1 and <= but that was a mistake
                # becasue we add a node anyway, we cannot use =
                sisteRack.settInn(Node(MinnerPerNode, ProcPerNode))

            elif sisteRack.getAntNoder() >= maxIRack:
                self._listeMedRack.append(Rack(maxIRack))
                self._sisteLedig += 1
                self._listeMedRack[self._sisteLedig].settInn(Node(MinnerPerNode, ProcPerNode))
