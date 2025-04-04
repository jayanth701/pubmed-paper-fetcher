import requests
import pandas as pd
from pubmed_fetcher.utils import extract_email, extract_company_affiliations, extract_non_academic_authors

def fetch_papers(query, max_results=50):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": max_results}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("esearchresult", {}).get("idlist", [])

def get_paper_details(paper_id):
    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {"db": "pubmed", "id": paper_id, "retmode": "json"}
    response = requests.get(details_url, params=params)
    response.raise_for_status()
    result = response.json().get("result", {}).get(paper_id, {})

    return {
        "PubmedID": paper_id,
        "Title": result.get("title", "Unknown"),
        "Publication Date": result.get("pubdate", "Unknown"),
        "Non-academic Author(s)": extract_non_academic_authors(result),
        "Company Affiliation(s)": extract_company_affiliations(result),
        "Corresponding Author Email": extract_email(result)
    }

def save_to_csv(papers, filename="papers.csv"):
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)

