# NFT Enabling tools [personal consumption] 
Use it for nft sniping during reveal (dyor and nfa - only to be used as fun personal project)

**Background** 
NFT Launches coincide with NFT Reveal where a selective group (1% of total collection) are deemed as RARE or special deriving more value from the market. 
It is always unknown prior to NFT Reveal which specific ID's(images) are usually rare, special, average or common. Good document on understand NFT Rarity (https://cointelegraph.com/news/what-is-nft-rarity-and-how-to-calculate-it)

Post a nft launch, rare nft's used to quickly get sniped, bought or taken by other participants who were super quick to spot which nft's were rare (Manually).

What did i do ?
Went through multiple iterations to quickly understand whats rarest in the collection to buy from Opensea (the then premier destination for NFT'S).

**Iteration 1**

1) Built Rarity Analyser: Collects all 10,000 images and runs a rarity analyzer to figure out the top nft's in a particular collection.
Pros:
 - Got exact ranks 
 - Knew top 10, top 20, top 100 and commons in a structured way
 - Could buy as soon as results were out.
Cons:
 -  Too slow, needed entire collection to be revelead and then 3-4 mins to run the analyzer.
 -  ould only buy if extremely lucky.
 -  Had to manually buy it.


**Iteration 2**

1) Realized do not need to spend entire resources to run analyzer on the entire collection. If i knew a keyword "Lasers", "Ghost" , "ICE" which were among the top rarest traits. All i needed was to look at when these rare terms popped up and execute the buy on Opensea

Pros:
 - Excellent to find rares. Much faster than running full rarity analyzer.
 - Specific keyword find allowed me to only go after the rarest.
Cons:
 - Could only go after 1 rare at a time, so had to wait until its found. [Worked with engineering to built Parallel spin-ups to catch multiple rare words]
 - Projects also stopped sharing rare keywords prior to launch which impacted this method

**Iteration 3**
Invovled solving the cons and making the system more efficient and faster. Key goals involved
1) Automated buying from Opensea via api once a rare image is found (if available to buy)
2) Bid 2x floor on Opensea if no option to buy
3) Run parallel threads across nft collection to go after multiple rare words. 
