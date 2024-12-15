import asyncio
import json
from pathlib import Path

import requests
from requests.status_codes import codes

import aiohttp

from bs4 import BeautifulSoup

def google_search(query) -> bool:
    url = f"{search_url_base}{query}"
    response = requests.get(url)

    if response.status_code != codes.ok:
        print(f"Error: {response.status_code}")
        return False
    else:
        data = response.json()
        print(json.dumps(data, indent=2))
        return True
    
async def download_page() -> None:
    # response = requests.get("https://www.bbc.co.uk/news/articles/c0ewlxvlw81o")
    # Open a session
    async with aiohttp.ClientSession() as session:
        # Send the request
        async with session.get("https://www.bbc.co.uk/news/articles/c0ewlxvlw81o") as response:

            if response.status == codes.ok:
                # response.encoding = response.apparent_encoding
                response_text = await response.text()
                bs = BeautifulSoup(response_text, "html.parser")
                if bs.title is not None:
                    print(bs.title.text)

                # print(response.encoding)
                # print(response.apparent_encoding)
                print(bs.original_encoding)

                paragraphs = bs.find_all("p")
                paragraphs = [paragraph.get_text() for paragraph in paragraphs]
                print(paragraphs[-1])

                body = "\n".join(paragraphs)

                with open("out.html", "w", encoding="utf8") as output_file:
                    try:
                        # output_file.write(bs.get_text(separator="\n"))
                        output_file.write(body)
                    except Exception as e:
                        print(f"Error {e}")

                print("File downloaded OK")

            else:
                print("Error downloading URL")


if __name__ == "__main__":
    with open(Path('secrets/google-search-key.json'), 'r', encoding='utf8') as secretFile:
        try:
            data = json.load(secretFile)
        except json.JSONDecodeError:
            print("Error: Could not load the google search key")
            exit(1)

        google_api_key = data['key']
        google_cx = data['cx']
        search_url_base = f'https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx={google_cx}&q='

    print(google_search("python ordered enum"))
    asyncio.run(download_page())
