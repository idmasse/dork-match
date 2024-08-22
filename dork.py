from googleapiclient.discovery import build
import json
import os
from dotenv import load_dotenv
from urls import urls

load_dotenv()

def google_custom_search(query, api_key, cse_id):
    service = build("customsearch", "v1", developerKey=api_key) # build the service
    res = service.cse().list(q=query, cx=cse_id, num=1).execute() 
    return res.get('items', [])[0] if 'items' in res else None # return just the first result 

api_key = os.getenv('API_KEY')
cse_id = os.getenv('CSE_ID')

# define the query -- this will be pulled from looker/convictiona/canal - brand url / parent product item title
# query = 'site:princesspolly.* "The Chloe Set Pink Stripe Lower Impact"'
# query = 'site:https://burstoralcare.* "Pro Sonic Toothbrush"'
# query = 'site:https://getnoosh.* "PLAY FREE HUGGING SEAMLESS TIGHTS"'

with open('search_results.json', 'w') as file:
    results_dict = {}

    for query in urls:
        results = google_custom_search(query, api_key, cse_id) # run the search
        results_dict[query] = results # add results to dict
        print(f"results for queryL {query}")
        print(results)
        print("-" * 40)

    json.dump(results_dict,file,indent=4)

print("results saved to search_results.json")

# if result:
#     print(f"Title: {result['title']}")
#     print(f"Link: {result['link']}")
#     print(f"Snippet: {result['snippet']}")
# else:
#     print("No results found.")
