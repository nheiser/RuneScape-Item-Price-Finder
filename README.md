# RuneScape-Item-Price-Finder
Personal project to practice threading and pulling data from JSON API's

API's used: 

https://rsbuddy.com/exchange/summary.json

-returns JSON data of all items in the game
-needed to extract the itemID from the item name

https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=X

-returns JSON data of the current price and price trends
-the value of X is the itemID
-needed to display the price to the user

A maximum of 10 items are shown at one time
Threads are used to speed up response time while waiting for the JSON data to be delivered
