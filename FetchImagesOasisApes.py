import os
import urllib.request
from retry import retry

machinePath = "/*machinePath*/"
LINKS = []

baseURI = "QmQbbX9ZcA8Dfay94vJZrmvohub1oQfLtZ791DzD8DLmMx" #Update This for collection
totalSupply = 1730 #Update This for collection (This should be 1 + total collection size)
collectionName = "Oasis Apes" #Update This for collection
startingIndexForLinks = 1
startingIndex = 1725 #Update This for collection

collectionFolderPath = machinePath + collectionName + "/" + "Images/"

for i in range(startingIndexForLinks,totalSupply):
    LINKS.append("https://ipfs.io/ipfs/"+baseURI + "/" + str(i) + ".png")

@retry(urllib.error.URLError, tries=4)
def download(index, itemNum, url):
    num = str(itemNum)
    path = collectionFolderPath + num + ".png"
    filename = path
    urllib.request.urlretrieve(url, filename)

def main():
    if not os.path.exists(collectionFolderPath):
        os.makedirs(collectionFolderPath)
    for index in range(startingIndex,totalSupply):
        link = LINKS[index]
        print(index, link)
        download(index, index+1, link)

if __name__ == '__main__':
    main()