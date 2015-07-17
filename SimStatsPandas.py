import pandas as pd, sys

def getSimStats(ifile, ofile):
    df = pd.read_csv(ifile)
    df.describe().to_csv(ofile)

##getSimStats(sys.argv[1], sys.argv[2])
getSimStats("run//SimResults.csv", "run//SimStatsPandas.csv")