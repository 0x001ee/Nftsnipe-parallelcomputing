import json
import os
import urllib.request
from retry import retry

machinePath = "/*machinePath*/"
LINKS = []
WITH_KODA = []

baseLink = "https://api-next.niftykit.com/reveal/nS4C7n5XGLRwM3QfGoF0" #Update This for collection
totalSupply = 10000 #Update This for collection
collectionName = "Kitty" #Update This for collection
startingIndex = 0 #Update This for collection

masterMetadataFolderPath = machinePath + collectionName

if not os.path.exists(masterMetadataFolderPath):
        os.makedirs(masterMetadataFolderPath)

masterMetadataFilePath = masterMetadataFolderPath + "/" +"Master.json"

masterMetadataFile = open(masterMetadataFilePath, "w")

for i in range(startingIndex,totalSupply):
    LINKS.append(baseLink + "/" + str(i))

#@retry(urllib.error.URLError, tries=4)
def download(index, url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
        response = urllib.request.urlopen(req)
        data = str(json.loads(response.read()))
        #print(str(data))
        if "Legendary" in data:
            #WITH_KODA.append(index)
            print(index)
        #json.dump(data, masterMetadataFile);
        #if(index!=totalSupply-2):
        #    masterMetadataFile.write(",");
    except urllib.error.HTTPError:
        print("Not Minted")
    

def main():
    masterMetadataFile.write("[")
    for index, link in enumerate(LINKS):
        #print(index, link)
        download(index, link)

    masterMetadataFile.write("]")
    masterMetadataFile.close()

if __name__ == '__main__':
    main()