import urllib.parse
import urllib.request

def ping_google(sitemap_url: str) -> None:
    ping_url = "https://www.google.com/ping?sitemap=" + urllib.parse.quote(sitemap_url, safe="")
    urllib.request.urlopen(ping_url, timeout=5)