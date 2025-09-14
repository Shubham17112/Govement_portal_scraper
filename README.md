That's an excellent and very detailed `README.md` file you've already provided. It covers all the essential aspects of your project, from setup and installation to usage and troubleshooting. The structure is clear, and it uses Markdown effectively to organize the information.

Since you've already written a comprehensive `README.md`, I'll present it to you in a final, ready-to-use format. You can copy this content directly and save it as `README.md` in the root of your project directory.

-----

# HCRaj Judgments Scraper

This Python script automates the process of scraping and downloading judgments from the Rajasthan High Court website (`hcraj.nic.in`). It uses **Selenium** to navigate the website, handle form inputs (including a manual captcha), and download PDF files. The script saves metadata about the downloaded judgments to a **CSV file** and organizes the PDFs in a dedicated folder.

## Features

  * **Automated Form Submission**: Fills out the date range and other form fields automatically.
  * **Captcha Handling**: Prompts the user to manually enter the captcha code from an image.
  * **Bulk Download**: Iterates through the search results to download judgment PDF files.
  * **Dependency Management**: Creates a `requirements.txt` file for easy setup.
  * **Data Export**: Saves judgment details (Sr.No., Case Details, Order Date, PDF filename) to a CSV file.
  * **File Organization**: Stores all downloaded PDFs in a separate directory named `judgments_pdfs`.

-----

## Prerequisites

Before you can run this script, ensure you have the following installed:

  * **Python 3.x**: You can download it from the [official Python website](https://www.python.org/downloads/release/python-3100/).
  * **pip**: Python's package installer (usually comes with Python).

-----

## Setup and Installation

Follow these steps to get the script up and running on your local machine.

### Step 1: Clone the Repository (or save the script)

Save the Python script to a local folder on your computer.

### Step 2: Create a `requirements.txt` file

Navigate to the project directory in your terminal or command prompt and run the following command to create a list of required packages:

```bash
pip freeze > requirements.txt
```

### Step 3: Install Dependencies

Now, use the newly created `requirements.txt` file to install all the necessary libraries:

```bash
pip install -r requirements.txt
```

### Step 4: Download and Configure ChromeDriver

The script uses Selenium to control a Chrome browser. You'll need to download the WebDriver that matches your Chrome browser version.

1.  Find your Chrome browser version by going to `chrome://version/` in your address bar.
2.  Go to the [official ChromeDriver download page](https://googlechromelabs.github.io/chrome-for-testing/).
3.  Download the `chromedriver.exe` file that corresponds to your Chrome version.
4.  **Important**: Update the `driver` service path in the script with the location of the `chromedriver.exe` file.

<!-- end list -->

```python
# Original line in the script:
# service=Service(r"C:\Users\shubham\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"),

# Change it to your file path, for example:
service=Service(r"C:\path\to\your\chromedriver.exe"),
```

-----

## How to Run the Script

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved the script.
3.  Run the script using the Python interpreter:

<!-- end list -->

```bash
python your_script_name.py
```

### Script Execution Flow:

  * The script will open a headless Chrome browser.
  * It will load the search page, fill in the dates, and select the 'Reportable' option.
  * A **`captcha.png`** file will be saved in the same directory.
  * The script will **pause and prompt you to enter the captcha code** from the image.
  * After you enter the code, the script will submit the form, scrape the table of results, and begin downloading the PDF files.
  * Downloaded PDFs will be saved in a new folder named `judgments_pdfs`.
  * A CSV file named **`downloaded_judgments.csv`** will be created or updated with the metadata.

-----

## Troubleshooting

  * **`WebDriverException: Message: 'chromedriver' executable needs to be in PATH.`**: This means the path to `chromedriver.exe` in your script is incorrect. Double-check the path in `service=Service(...)`.
  * **`No results table found...`**: This usually happens if the captcha was entered incorrectly or the dates did not yield any results. Rerun the script and try the captcha again.
  * **`AttributeError: 'str' object has no attribute 'get_attribute'...`**: This error might occur if the HTML structure of the website changes. The XPath or selectors used to find elements might need to be updated.
