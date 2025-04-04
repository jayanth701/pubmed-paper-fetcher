import re
def extract_email(result):
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(result))
    return emails[0] if emails else "Not Available"
def extract_non_academic_authors(result):
    authors = result.get("authors", [])
    return ", ".join([author for author in authors if not is_academic(author)]) or "None"
def extract_company_affiliations(result):
    affiliations = result.get("affiliations", [])
    return ", ".join([aff for aff in affiliations if is_company(aff)]) or "None"
def is_academic(author):
    return any(keyword in author.lower() for keyword in ["university", "college", "institute", "school"])
def is_company(affiliation):
    return any(keyword in affiliation.lower() for keyword in ["inc", "ltd", "pharma", "biotech"])
