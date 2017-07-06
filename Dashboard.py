"""
By Eli and Youcef
Script that displays all companies acquired in the last 3 months
"""

"""
1) download the full crunchbase export from
   https://api.crunchbase.com/v/3/node_keys/node_keys.tar.gz?user_key=user_key
   (enter API key to begin download)
   
2) go to acquisitions.csv 
   (all acquisition UUIDs)
   
3) extract all the UUIDs of all Acquisitions in the last 3 months
   (use the updated_at column)
   
4) For each Acquistion UUID: 

   1) capture the price_usd payed
   2) make a call to the crunchbase API using the form
   https://api.crunchbase.com/v/3/acquisitions/:UUID/:acquiree to 
   identify the organization that was acquired
   3) capture the categories that the organization is in
   4) For each category: add key-category:value-price_usd to a dictionary

5) Display the dictionary   
"""