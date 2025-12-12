from pages.home_page import HomePage


def test_open_example(driver):
    home = HomePage(driver)
    home.open("https://example.com")
    home.wait_for_title("Example")

    assert "Example" in driver.title