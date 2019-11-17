from datasenter import Datasenter

data = Datasenter()

filer = ["abel.txt", "saga.txt"]

for fil in filer:
    data.lesInnRegneklynge(fil)

data.skrivUtAlleRegneklynger()
