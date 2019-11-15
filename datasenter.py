from regneklynge import Regneklynge

## Klasse for representasjon av et datasenter
#
class Datasenter:

	## Oppretter et datasenter
	#
	def __init__(self):
            self._ordbok = {}

	## Leser inn data om en regneklynge fra fil og legger
	# den til i ordboken
	# @param filnavn filene der dataene for regneklyngen ligger
	def lesInnRegneklynge(self, filnavn):
            fil = open(filnavn, "r")
            fil_liste = []
            for linje in fil:
                regneklynge = []
                for element in linje.split():
                    regneklynge.append(element)
                fil_liste.append(regneklynge)
            antall_rack = int(fil_liste[0][0])
            self._ordbok[filnavn] = Regneklynge(antall_rack)


	## Skriver ut informasjon om alle regneklyngene
	#
	def skrivUtAlleRegneklynger(self):
		pass

	## Skriver ut informasjon om en spesifikk regeklynge
	# @param navn navnet på regnekyngen
	def skrivUtRegneklynge(self, navn):
		pass


datasenter = Datasenter()
datasenter.lesInnRegneklynge("abel.txt")
print(datasenter._ordbok)
