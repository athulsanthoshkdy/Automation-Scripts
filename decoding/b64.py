import tkinter as tk
from tkinter import messagebox
import base64
import urllib.parse
import re
import requests

# Function to scrape the webpage and find the inspect URL
def find_inspect_url(page_url: str) -> str:
    try:
        # Simulate a browser request using headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers"
        }

        # Create a session to persist cookies (if necessary)
        session = requests.Session()
        
        # Send the request with headers
        response = session.get(page_url, headers=headers)

        # Check the status code
        if response.status_code == 200:
            # Get the page content
            page_content = response.text

            # Search for the inspect URL pattern using regex
            match = re.search(r'https://masahub\.click/wp-content/plugins/clean-tube-player/public/player-x\.php\?q=[a-zA-Z0-9+/=]+', page_content)

            if match:
                # Return the found inspect URL
                return match.group(0)
            else:
                return "Inspect URL not found in the page."
        else:
            # Handle unsuccessful status codes (404, 500, etc.)
            return f"Failed to fetch the page. Status code: {response.status_code}"
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Function to process the inspect URL and extract the final video URL
def extract_video_url():
    # Get the URL entered by the user
    url_to_scrape = url_entry.get()

    if not url_to_scrape:
        messagebox.showwarning("Input Error", "Please enter a valid URL to scrape.")
        return

    # Find inspect URL from the webpage
    inspect_url = find_inspect_url(url_to_scrape)

    if "Failed" in inspect_url or "Error" in inspect_url:
        messagebox.showerror("Scraping Error", inspect_url)
        return

    # Base URL to remove from the inspect URL
    base_url = "https://masahub.click/wp-content/plugins/clean-tube-player/public/player-x.php?q="

    # Remove the base URL to get the Base64 encoded string
    base64_encoded_str = inspect_url.replace(base_url, "")

    try:
        # Decode the Base64 string
        decoded_str = base64.b64decode(base64_encoded_str).decode('utf-8')

        # Extract the video URL from the decoded string
        start_index = decoded_str.find('src="') + len('src="')
        end_index = decoded_str.find('"', start_index)

        video_url = decoded_str[start_index:end_index]

        # Extract the second "https" in the URL to get the full video URL
        first_https_index = video_url.find("https")
        second_https_index = video_url.find("https", first_https_index + 1)

        https_url = video_url[second_https_index:]

        # Extract the part until ".mp4" and clean up the URL
        mp4_index = https_url.find(".mp4")
        cleaned_url = https_url[:mp4_index + len(".mp4")]

        # Decode the URL (URL decode)
        decoded_url = urllib.parse.unquote(cleaned_url)

        # Display the decoded video URL in the result box
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Decoded Video URL:\n{decoded_url}")

    except Exception as e:
        messagebox.showerror("Decoding Error", f"Error occurred while decoding the URL: {str(e)}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Video URL Extractor")

# Create UI components
url_label = tk.Label(root, text="Enter the URL to scrape:")
url_label.pack(padx=20, pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=20, pady=5)

extract_button = tk.Button(root, text="Extract Video URL", command=extract_video_url)
extract_button.pack(padx=20, pady=10)

result_label = tk.Label(root, text="Extracted Video URL:")
result_label.pack(padx=20, pady=5)

result_text = tk.Text(root, width=60, height=10)
result_text.pack(padx=20, pady=5)

# Run the Tkinter main loop
root.mainloop()
