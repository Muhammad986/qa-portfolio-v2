from pathlib import Path

import pytest
from selenium import webdriver


@pytest.fixture()
def download_dir():
    path = Path("file_for_tests").resolve()
    path.mkdir(parents=True, exist_ok=True)

    for file in path.iterdir():
        if file.is_file():
            file.unlink()

    yield path

    for file in path.iterdir():
        if file.is_file():
            file.unlink()


@pytest.fixture
def driver(download_dir):
    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": str(download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
