import argparse
from fetch_papers import fetch_papers, get_paper_details, save_to_csv

parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
parser.add_argument("query", type=str, help="Search query for PubMed")
parser.add_argument("--max", type=int, default=5, help="Number of results to fetch")

args = parser.parse_args()

paper_ids = fetch_papers(args.query, max_results=args.max)
papers = [get_paper_details(paper_id) for paper_id in paper_ids]

save_to_csv(papers, "pubmed_results.csv")
print("Results saved to pubmed_results.csv")
