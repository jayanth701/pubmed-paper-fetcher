import argparse
from pubmed_fetcher.fetch_papers import fetch_papers, get_paper_details, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and extract details.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-o", "--output", type=str, default="papers.csv", help="Output CSV file")
    args = parser.parse_args()

    paper_ids = fetch_papers(args.query)
    papers = [get_paper_details(paper_id) for paper_id in paper_ids]
    save_to_csv(papers, args.output)
    print(f"Saved {len(papers)} papers to {args.output}")

if __name__ == "__main__":
    main()
