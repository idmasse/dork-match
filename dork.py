from googleapiclient.discovery import build
import json
import os
import time
from dotenv import load_dotenv
from urls import urls
from googleapiclient.errors import HttpError

load_dotenv()

api_key = os.getenv('API_KEY')
cse_id = os.getenv('CSE_ID')

def google_custom_search(query, api_key, cse_id):
    service = build("customsearch", "v1", developerKey=api_key)  # build the service
    try:
        res = service.cse().list(q=query, cx=cse_id, num=1).execute()
        return res.get('items', [])[0] if 'items' in res else None  # return just the first result
    except HttpError as e:
        if e.resp.status == 429:
            print("rate limit error retry in 60s")
            time.sleep(60)  # wait for 60s then retry
            return google_custom_search(query, api_key, cse_id)  # retry
        else:
            raise e  # re-raise the exception if it's not a rate limit error

with open('search_results.json', 'w') as file: # file for results
    results_dict = {}

    for query in urls:
        results = google_custom_search(query, api_key, cse_id)  # run ssearch
        results_dict[query] = results  # add results to dict

        print(f"results for: {query}")
        print(results)
        print("-" * 40)

        time.sleep(0.6) # avoid hitting the rate limit

    json.dump(results_dict, file, indent=4) # write to json
print("results saved to search_results.json")

# if result:
#     print(f"Title: {result['title']}")
#     print(f"Link: {result['link']}")
#     print(f"Snippet: {result['snippet']}")
# else:
#     print("No results found.")
