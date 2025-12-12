from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import os


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver_path = os.path.join(
        os.path.dirname(__file__),
        "msedgedriver.exe"
    )

    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=options)

    return driver