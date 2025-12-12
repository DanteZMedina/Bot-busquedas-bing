import pytest
from pages.bing_search_page import BingSearchPage
from data.bing_queries import QUERIES
from utils.throttling import between_searches


@pytest.mark.parametrize("query", QUERIES)
def test_bing_controlled_searches(driver, query):
    bing = BingSearchPage(driver)

    bing.open()
    bing.search(query)

    assert query.split()[0].lower() in driver.title.lower()

    between_searches()