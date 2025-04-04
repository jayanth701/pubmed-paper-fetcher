# pubmed-paper-fetcher
A Python tool to fetch research papers from PubMed, extract author details, and save the results in a structured format

1.Clone this repository:
2.Install Dependencies

Run the fetcher script with a search query
Example:
This will fetch **research papers related to machine learning** and save them in `papers.csv`.
 
Project Structure:
 pubmed-paper-fetcher/
│── pubmed_fetcher/
│   │── __init__.py
│   │── fetch_papers.py
│   │── utils.py
│── scripts/
│   │── run_fetcher.py
│── requirements.txt
│── README.md
│── .gitignore


Features
- Fetches research papers from **PubMed API**.
- Extracts details like **title, publication date, authors, affiliations, and emails**.
- Filters **non-academic authors and company affiliations**.
- Saves results to **CSV file**.

 Contributing
Contributions are welcome!  
If you find any bugs or want to add features, feel free to open an issue or a pull request.

 License
This project is open-source under the **MIT License**.


