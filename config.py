import os

# Database initialization
basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(basedir,"rvaapp", "data")
DATAFLIGHT = os.path.join(datadir, 'data_lieux.csv')
STRUCT = os.path.join(datadir, 'structureDF.csv')
DH = os.path.join(datadir, 'decalage_horaire.csv')
