import argparse

#from scipy.spatial import hamming
from Bio import SeqIO

def getGenes(gbfile):
    features = []
    for record in SeqIO.parse(gbfile, "genbank"):
        for f in record.features:
            print(f)
            if f.type == "CDS":
                features.append(f)
    return features

def variateGeneSet(features, percent):

def variateCDSrandom(CDS, percent):

def variateCDSsynoymous():
    break

def variateCDSnonsynon()
    break

def variator(gbfile, percent):
    genes = getGenes(gbfile)
    variatedGeneSet = variateGeneSet(genes, percent)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Vary genome within a given %')
    parser.add_argument("genbank", type=str, help="genbank input file")
    parser.add_argument("percentage", type=int, help = 'percent difference')
    args = parser.parse_args()
    gbfile = args.genbank
    percent = args.percent
    variator(gbfile, percent)
