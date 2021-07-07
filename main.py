# PROMPT: This python script should take a chemical(s) as an input then return what smell(s) that chemical might make.

# The Odorizer can be useful in the bottlenecks of the supply chain. For example, suppliers can optimize the transport
# of products by grouping together chemicals that smell alike; they can also inform themselves on the odors of
# potentially harmful chemicals, such as chlorine, which has an acrid odor similar to bleach and is highly toxic
# to humans when inhaled. This safety measure can also be applied to other bottlenecks on the supply chain: retail
# locations, waste management, and warehouses. The Odorizer may also serve as a predictive model for warehouse
# managers and suppliers. By establishing what certain similar chemicals smell like, potential clients can use this tool
# to predict what a new chemical may smell like before possessing the product, which may save capital along the way.

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
# gets rid of parser warning issue

data = pd.read_csv(r'/Users/maanas/Desktop/references.csv')
# data.head() unnecessary because I know data is in right format

for zid in data["zinc_id"]:
    scrape = requests.get("http://zinc15.docking.org/substances/" + str(zid) + ".xml")
    a = BeautifulSoup(scrape.content)

    scrape1 = requests.get("http://zinc15.docking.org/substances/" + str(zid) + "/")
    b = BeautifulSoup(scrape1.content)
    zinc = a.zinc_id.text
    print(a.zinc_id.text, b.findAll("td")[6].text)

# Chemical Knowledge - Assumptions: Carboxylic acids GENERALLY have an odor of "regurgitated milk" alcohols can
    # GENERALLY be fresh, floral, minty, or pungent aldehydes are GENERALLY citrus-y or buttery amines are GENERALLY
    # fishy esters are GENERALLY fruity aromatics are GENERALLY sweet smelling These are generalizations. There are
    # many exceptions to these rules. Benzene, for example, does not smell sweet; 2-heptanone smells like blue
    # cheese; Z-jasmone smells like jasmine. Therefore, this odorizer is not entirely accurate for complex molecules
    # like the ones included in the reference data set. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627536/
    odor = a.smiles.text
    if "C(=O)N" in odor:
        print("This molecule most likely smells fishy.") #amines and amides
    elif "cc" in odor:
        print("This molecule most likely smells sweet.") #aromatics
    elif "oH" in odor:
        print("This molecule can smell fresh, floral, minty, or pungent.") #alcohols
    elif "(=O)OC" in odor:
        print("This molecule most likely smells fruity") #ester
    elif "=O" in odor:
        print("This molecule can smell citrus-y or buttery") #aldehydes or ketones
    else:
        print("I'm not sure what this molecule smells like!")


