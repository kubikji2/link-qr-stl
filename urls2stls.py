
FN = "urls/urls.txt"

# load urls
def load_urls():
    short_urls = []
    with open(FN,'r') as f:
        for line in f.readlines():
            entries = line.strip().split("/")
            entries.pop(-2)
            new_url = "/".join(entries)
            short_urls.append(new_url)
    return short_urls

def process_url(url):
    print(url)
    pass

if __name__=="__main__":
    
    for url in load_urls():
        process_url(url)