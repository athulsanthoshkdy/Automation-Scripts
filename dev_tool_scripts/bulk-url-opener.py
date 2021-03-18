import webbrowser

def open_urls(urls):
    for url in urls:
        webbrowser.open(url)

urls = ["https://www.google.com", "https://www.stackoverflow.com"]
open_urls(urls)
