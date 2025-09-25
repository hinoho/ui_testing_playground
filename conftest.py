import pytest
from playwright.sync_api import Page


@pytest.fixture
def open_page_fixture(page: Page):
    def _open_page_fixture(url: str):
        page.goto(url)
        page.wait_for_selector('#footer')
        return page
    return _open_page_fixture