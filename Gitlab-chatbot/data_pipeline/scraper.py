import requests
from bs4 import BeautifulSoup

def scrape_gitlab_page(url):
    # 1. Fetch the web page
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return None

    # 2. Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. Extract the text (finding all paragraph tags)
    paragraphs = soup.find_all('p')
    
    # 4. Combine paragraphs into a single text block
    page_text = "\n".join([para.get_text() for para in paragraphs])
    
    return page_text

if __name__ == "__main__":
    # Test with a main handbook page
    test_url = "https://handbook.gitlab.com/handbook/company/culture/"
    extracted_text = scrape_gitlab_page(test_url)
    
    print(f"Successfully extracted {len(extracted_text)} characters.")
    print("Preview:")
    print(extracted_text[:500]) # Print the first 500 characters