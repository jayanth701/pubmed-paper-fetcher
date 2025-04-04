import requests
import pandas as pd
import re
import argparse
from typing import List, Dict

def fetch_papers(query: str, max_results: int = 50) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": max_results}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("esearchresult", {}).get("idlist", [])

def get_paper_details(paper_id: str) -> Dict[str, str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    response = requests.get(url, params={"db": "pubmed", "id": paper_id, "retmode": "json"})
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

def extract_non_academic_authors(result: Dict) -> str:
    authors = result.get("authors", [])
    return ", ".join(a for a in authors if not is_academic(a)) or "None"

def extract_company_affiliations(result: Dict) -> str:
    affiliations = result.get("affiliations", [])
    return ", ".join(a for a in affiliations if is_company(a)) or "None"

def extract_email(result: Dict) -> str:
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(result))
    return emails[0] if emails else "Not Available"

def is_academic(author: str) -> bool:
    return any(x in author.lower() for x in ["university", "college", "institute", "school"])

def is_company(affiliation: str) -> bool:
    return any(x in affiliation.lower() for x in ["inc", "ltd", "pharma", "biotech"])

def save_to_csv(papers: List[Dict[str, str]], filename: str) -> None:
    pd.DataFrame(papers).to_csv(filename, index=False)

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, default="papers.csv")
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    try:
        papers = [get_paper_details(pid) for pid in fetch_papers(args.query)]
        save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
