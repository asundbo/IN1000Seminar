from regneklynge import Regneklynge


class Datasenter:

    # Oppretter et datasenter
    #
    def __init__(self):
        self._ordbok = {}

    # Leser inn data om en regneklynge fra fil og legger
    # den til i ordboken
    # @param filnavn filene der dataene for regneklyngen ligger
    def lesInnRegneklynge(self, filnavn):
        navn = filnavn[:-4]
        filKlynge = open(filnavn)
        liste = []
        for linje in filKlynge:
            liste.append(linje)

        maxInRack = int(liste[0])
        r = Regneklynge(maxInRack)

        nyListe = []
        nyListe = liste.copy()
        nyListe.pop(0)

        for linje in nyListe:
            biter = linje.split(" ")
            noder = int(biter[0])
            minne = int(biter[1])
            pros = int(biter[2])
            r.leggTilNoder(noder, minne, pros)

        self._ordbok[navn] = r  # SELF._ !!!!!!!!!!

    # Skriver ut informasjon om alle regneklyngene
    #
    def skrivUtAlleRegneklynger(self):
        for key in self._ordbok:
            print()
            self.skrivUtRegneklynge(key)

    # Skriver ut informasjon om en spesifikk regeklynge
    # @param navn navnet på regnekyngen

    def skrivUtRegneklynge(self, navn):
        klynge = self._ordbok[navn]

        racks = klynge.antRacks()
        antProcs = klynge.antProsessorer()
        n32 = klynge.noderMedNokMinne(32)
        n64 = klynge.noderMedNokMinne(64)
        n128 = klynge.noderMedNokMinne(128)

        print(f"Informasjon om regneklyngen {navn}")
        # HUSK å LUKKE ""
        print(f"Antall rack: {racks} \nAntall prosessorer: {antProcs} \nNoder med minst 32 GB: {n32} \nNoder med minst 64 GB: {n64} \nNoder med minst 128 GB: {n128}")
