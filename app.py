import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

current_datetime = datetime.now()
folder_name = current_datetime.strftime('%H_%M_%d_%m_%Y')  # Format the current date and time for directory name

# Define the main directory to save articles
main_directory = "Saved_Articles"

# Create the main directory if it doesn't exist (simplified using os.makedirs)
os.makedirs(main_directory, exist_ok=True)

# Create a subdirectory with the current date and time format inside the main directory
subdirectory_path = os.path.join(main_directory, folder_name)
os.makedirs(subdirectory_path, exist_ok=True)

# --- FIX: Removed space and added the missing '&' after the API key ---
url = "https://content.guardianapis.com/technology/artificialintelligenceai?api-key=b196335e-cf7b-4c34-b431-227f267a8c44&type=article&page=1"

print("Contacting The Guardian API...")
response = requests.get(url)  # Fetch data from the URL

# Only try to parse the data if the request was actually successful (Status Code 200)
if response.status_code == 200:
    x = response.json()  # Convert the response to JSON format
    
    # Verify that the expected 'response' data actually exists
    if 'response' in x and 'results' in x['response']:
        web_urls = [item['webUrl'] for item in x['response']['results']]
        print(f"Found {len(web_urls)} articles. Downloading now...")

        def save_content_to_file(article_url, folder, filename):
            try:
                res = requests.get(article_url)
                if res.status_code == 200:
                    soup = BeautifulSoup(res.text, 'html.parser')

                    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as file:
                        for header in soup.find_all(['h1']):
                            file.write("Title: " + header.text + '\n' * 5)
                        for paragraph in soup.find_all('p'):
                            file.write(paragraph.text + '\n')
                else:
                    print("Failed to retrieve the page:", article_url)
            except Exception as e:
                print("An error occurred:", e)

        for index, article_url in enumerate(web_urls):
            filename = f'article_{index}.txt'  # Create a unique filename for each article
            save_content_to_file(article_url, subdirectory_path, filename)  # Save the content
            print(f"Successfully saved: {filename}")
            
        print("\nAll done! Check your 'Saved_Articles' folder.")
        
    else:
        print("The API accepted your key, but didn't return the expected format.")
        print("Raw API Response:", x)
else:
    print(f"API Request Failed! Status Code: {response.status_code}")
    print("Error Details:", response.text)