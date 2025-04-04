import pytest
from pubmed_fetcher.fetch_papers import fetch_papers

def test_fetch_papers():
    assert len(fetch_papers("cancer research", max_results=5)) > 0
