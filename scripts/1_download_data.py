# 1_download_data.py
import os
import time
import requests, zipfile, io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm

# ---------------- CONFIG ----------------
RAW_DATA_PATH = r"D:\Guvi Projects\cricsheet_project\New folder\data\raw"
URL = "https://cricsheet.org/matches/"

# Create folders if not exist
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# ---------------- SELENIUM SETUP ----------------
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Auto-manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# ---------------- SCRAPING ----------------
driver.get(URL)
time.sleep(3)  # wait for page load

# Find all download links for ZIP files
links = driver.find_elements(By.XPATH, "//a[contains(@href,'.zip')]")

# Only required formats
FORMATS = {
    "odis_json.zip": "ODIs",
    "t20s_json.zip": "T20s",
    "tests_json.zip": "Tests"
}

for link in links:
    href = link.get_attribute("href")
    filename = href.split("/")[-1]

    if filename.lower() in FORMATS:
        format_name = FORMATS[filename.lower()]
        save_folder = os.path.join(RAW_DATA_PATH, filename.replace(".zip", ""))
        os.makedirs(save_folder, exist_ok=True)

        # Download the ZIP
        print(f"\nDownloading {format_name} ({filename}) ...")
        r = requests.get(href)
        if r.status_code == 200:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            file_list = z.namelist()

            # Progress bar for extraction
            for member in tqdm(file_list, desc=f"Extracting {format_name}", unit="file"):
                z.extract(member, save_folder)

            print(f"✅ Extracted {format_name} to {save_folder}")
        else:
            print(f"❌ Failed to download {filename}")

driver.quit()
print("\nAll ODI, T20, and Test JSON matches downloaded successfully!")
