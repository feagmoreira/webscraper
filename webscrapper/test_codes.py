from resources import *
from model import *
def main():
    url = "https://pubg-new-state.en.aptoide.com/app"
    
    html = get_html_page(url)
    description = extract_AptoidApp_from_html(html,SCRAPING_PATTERNS)
    print(description)



if __name__ == "__main__":
    main()