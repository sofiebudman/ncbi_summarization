'''
Metapub
requests
beutiful soup
'''
from metapub import PubMedFetcher
import requests
from bs4 import BeautifulSoup

def fetchFromId(id):
    fetcher = PubMedFetcher() # constructs fetcher object

    try:
        article = fetcher.article_by_pmid(id)

        title = article.title
        abstract = article.abstract if article.abstract else "No abstract available."
        journal = article.journal
        #authors = ", ".join(article.authors)
        url = url = f"https://pubmed.ncbi.nlm.nih.gov/{id}/" #pub med ID

        full_text = fetchFromUrl(url)

        return {
            "PMID": id,
            "Title": title,
            "Journal": journal,
            #"Authors": authors,
            "Abstract": abstract,
            "Full Text URL": url,
            "Full Text": full_text
        }
    except Exception as e:
        return {"Error": f"Failed to retrieve article: {str(e)}"}
    
def fetchFromUrl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        out = "\n".join([p.get_text() for p in paragraphs])
        return out if out else "extraction failed"
    except Exception as e:
        return f"Error fetching full text: {str(e)}"






