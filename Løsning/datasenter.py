from regneklynge import Regneklynge


class Datasenter:
    def __init__(self):
        self._ordbok = {}

    def lesInnRegneklynge(self, filnavn):
        "Leser inn data om en regneklynge fra fil og legger den til i ordboken"
        navn = filnavn[:-4]  # Navnet til klyngen
        filKlynge = open(filnavn)
        liste = []  # Pga første linje i filen er anderledes enn de anderledes
        # Trenger vi en liste for å behandle dem
        for linje in filKlynge:
            liste.append(linje)

        maxInRack = int(liste[0])
        r = Regneklynge(maxInRack)

        # Ny liste med bare minnedetaljer og antall noder og prosessorer
        nyListe = []
        nyListe = liste.copy()
        nyListe.pop(0)

        for linje in nyListe:
            biter = linje.split(" ")
            noder = int(biter[0])
            minne = int(biter[1])
            pros = int(biter[2])
            r.leggTilNoder(noder, minne, pros)

        # Legger til klyngen til ordboka
        self._ordbok[navn] = r  # SELF._ !!!!!!!!!!

    def skrivUtAlleRegneklynger(self):
        for key in self._ordbok:
            print()  # Extra linje
            self.skrivUtRegneklynge(key)
            # Key er en streng så vi kan passe den til metoden

    def skrivUtRegneklynge(self, navn):
        "Skriver ut informasjon om en spesifikk regeklynge"
        klynge = self._ordbok[navn]

        racks = klynge.antRacks()
        antProcs = klynge.antProsessorer()
        n32 = klynge.noderMedNokMinne(32)
        n64 = klynge.noderMedNokMinne(64)
        n128 = klynge.noderMedNokMinne(128)

        print(f"Informasjon om regneklyngen {navn}")
        # HUSK å LUKKE ""
        print(f"Antall rack: {racks} \nAntall prosessorer: {antProcs} \nNoder med minst 32 GB: {n32} \nNoder med minst 64 GB: {n64} \nNoder med minst 128 GB: {n128}")
