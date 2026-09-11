import urllib.request
import urllib.parse
import re

def get_domain(query):
    url = 'https://www.bing.com/search?q=' + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'href="(https?://[^"]+)"', html)
        if match:
            return match.group(1)
    except Exception as e:
        print(f"Error {query}: {e}")
    return None

print("蛙蛙写作 ->", get_domain('蛙蛙写作 官网'))
print("Laper ->", get_domain('Laper 官网'))
