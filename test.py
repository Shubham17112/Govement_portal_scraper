# Install dependencies first
# !pip install selenium pandas requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
import pandas as pd
from datetime import datetime, timedelta
import requests

# ------------------- CONFIG -------------------
BASE_URL = "https://hcraj.nic.in/cishcraj-jdp/JudgementFilters/"
DOWNLOAD_DIR = "judgments_pdfs"
CSV_FILE = "downloaded_judgments.csv"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ------------------- DATES -------------------
today = datetime.today()
# from_date_str = (today - timedelta(days=10)).strftime("%d/%m/%Y")
# to_date_str = today.strftime("%d/%m/%Y")
from_date_str = ("01/09/2025")
to_date_str = ("11/09/2025")

# ------------------- CHROME OPTIONS -------------------
chrome_options = Options()
chrome_options.add_argument("--headless")  # optional
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(r"C:\Users\shubham\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"),
    options=chrome_options
)
wait = WebDriverWait(driver, 20)

driver.get(BASE_URL)

# ------------------- FILL FORM -------------------
wait.until(EC.presence_of_element_located((By.ID, "partyFromDate"))).send_keys(from_date_str)
wait.until(EC.presence_of_element_located((By.ID, "partyToDate"))).send_keys(to_date_str)

# ------------------- JUDGE SELECTION -------------------
# leave as default if not needed

# ------------------- REPORTABLE -------------------
driver.find_element(By.ID, "rpjudgeA").click()  # Reportable = YES

# ------------------- CAPTCHA -------------------
captcha_img = wait.until(EC.presence_of_element_located((By.ID, "captcha")))
captcha_img.screenshot("captcha.png")
captcha_code = input("Enter captcha code from captcha.png: ")
driver.find_element(By.ID, "txtCaptcha").send_keys(captcha_code)

# ------------------- SUBMIT -------------------
driver.find_element(By.ID, "btncasedetail1_1").click()

# ------------------- WAIT FOR RESULTS -------------------
try:
    table = wait.until(EC.presence_of_element_located((By.ID, "sample_1")))
    thead = table.find_element(By.TAG_NAME, "thead")
    headers = thead.find_elements(By.TAG_NAME, "th")
    columns = [th.text.strip() for th in headers]
    columns.append("PDF_File")
except:
    print("No results table found. Either no judgments or captcha was incorrect.")
    driver.quit()
    exit()
rows = table.find_elements(By.TAG_NAME, "tr")

# ------------------- LOAD PREVIOUSLY DOWNLOADED -------------------
if os.path.exists(CSV_FILE):
    df_prev = pd.read_csv(CSV_FILE)
    downloaded_ids = set(df_prev['Case Details'].astype(str).tolist())
else:
    df_prev = pd.DataFrame()
    downloaded_ids = set()


data_list = []

for row in rows[1:]:  # skip header
    cols = row.find_elements(By.TAG_NAME, "td")
    judgment_no = cols[0].text.strip()  # assuming first column is unique
    if judgment_no in downloaded_ids:
        continue  # skip already downloaded

    buttons = cols[-1].find_elements(By.TAG_NAME, "button")  # last td is Action
    download_btn = None
    for btn in buttons:
        if btn.get_attribute("onclick") and "DownloadOrdJud(this,'D')" in btn.get_attribute("onclick"):
            download_btn = btn
            break

    if not download_btn:
        continue  # or log an error

    caseno = download_btn.get_attribute("data-caseno")
    orderno = download_btn.get_attribute("data-orderno")
    cyear = download_btn.get_attribute("data-cyear")
    pdf_url = f"https://hcraj.nic.in/cishcraj-jdp/DownloadJudgement.aspx?caseno={caseno}&orderno={orderno}&cyear={cyear}&ftype=PDF"

    pdf_filename = f"{judgment_no}.pdf"
    pdf_path = os.path.join(DOWNLOAD_DIR, pdf_filename)

    # download pdf
r = requests.get(pdf_url, stream=True)
with open(pdf_path, "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

row_data = [col.text.strip() for col in cols]
row_data.append(pdf_filename)  # add PDF filename column
data_list.append(row_data)

# ------------------- SAVE TO CSV -------------------
headers = driver.find_element(By.ID, "sample_1").find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "th")
columns = [th.text.strip() for th in headers]
columns.append("PDF_File")

df_new = pd.DataFrame(data_list, columns=columns)

if not df_prev.empty:
    df_final = pd.concat([df_prev, df_new], ignore_index=True)
else:
    df_final = df_new

df_final.to_csv(CSV_FILE, index=False)
print(f"Data saved to {CSV_FILE}. PDFs in {DOWNLOAD_DIR}")

driver.quit()
