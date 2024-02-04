from resources import *
from model import *
def main():
    url = "x"
    
    html = get_html_page(url)
    print(html)
    description = extract_AptoidApp_from_html(html,SCRAPING_PATTERNS)
    print(description)



if __name__ == "__main__":
    main()