import multiprocessing as mp
import json
import os
import urllib.request
import pywhatkit
from datetime import datetime

LINKS = []

baseLink = "https://ikzttp.mypinata.cloud/ipfs/*" #Update This for collection
totalSupply = 20000 #Update This for collection
collectionName = "PixelBeanz" #Update This for collection
startingIndex = 0 #Update This for collection
keyWord = "Spirit"
numberOfDivisions = 20


for i in range(startingIndex,totalSupply):
    LINKS.append(baseLink + "/" + str(i))

def download(index, url):
    #print(index)
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
        response = urllib.request.urlopen(req)
        data = str(json.loads(response.read()))
        if keyWord in data:
            print("Found at")
            print(index)
    except urllib.error.HTTPError:
        print("Not Minted")

def setup(inputs):
    for index in range(inputs[0], inputs[1]):
        link = LINKS[index]
        download(index, link)

def main():
    pool = mp.Pool(mp.cpu_count())
    inputs=[]
    #inputs = [[0,1001],[1001,2001]]
    for curr in range(0, numberOfDivisions):
        innerList = []
        startingIndexForThis = int(curr * (totalSupply/numberOfDivisions))
        endingIndexForThis = int(startingIndexForThis + (totalSupply/numberOfDivisions))
        innerList.append(startingIndexForThis)
        innerList.append(endingIndexForThis)
        inputs.append(innerList)
    print(inputs)    

    pool.map(setup, inputs)
    #pool.apply(setup, args=(int(curr * (totalSupply/numberOfDivisions)), int(startingIndexForThis + (totalSupply/numberOfDivisions)))) for curr in range(0,numberOfDivisions)
    # for curr in range(0,numberOfDivisions):
    #     startingIndexForThis = int(curr * (totalSupply/numberOfDivisions))
    #     endingIndexForThis = int(startingIndexForThis + (totalSupply/numberOfDivisions))
    #     p+"curr" = Process(target=setup(startingIndexForThis, endingIndexForThis))
    #     p.start()
    

if __name__ == '__main__':
    main()