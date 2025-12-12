import os
from datetime import datetime
import re


def sanitize_filename(text):
    return re.sub(r"[^a-zA-Z0-9_-]", "_", text)


def take_screenshot(driver, prefix, query):
    date_folder = datetime.now().strftime("%Y-%m-%d")
    base_path = os.path.join("reports", "screenshots", "bing", date_folder)
    os.makedirs(base_path, exist_ok=True)

    safe_query = sanitize_filename(query.lower())[:50]
    timestamp = datetime.now().strftime("%H%M%S")

    filename = f"{prefix}_{safe_query}_{timestamp}.png"
    filepath = os.path.join(base_path, filename)

    driver.save_screenshot(filepath)

    return filepath
