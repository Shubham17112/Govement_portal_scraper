## Screen Shots


<img width="1532" height="573" alt="image" src="https://github.com/user-attachments/assets/66163ffb-030a-428d-8642-f41ebb3c097b" />
<img width="1596" height="780" alt="image" src="https://github.com/user-attachments/assets/ab611129-0782-4d57-ac61-e8e34d275c0e" />
<img width="1386" height="791" alt="image" src="https://github.com/user-attachments/assets/eb0c64ed-eb4e-4179-9761-d3e14dd1ebbb" />
<img width="1002" height="350" alt="image" src="https://github.com/user-attachments/assets/f17cef6e-195c-41e6-b3c7-c2bc19e4d0a6" />
<img width="214" height="359" alt="image" src="https://github.com/user-attachments/assets/7cf9a9d1-2beb-4104-99e6-46c392d089f5" />
<img width="1208" height="737" alt="image" src="https://github.com/user-attachments/assets/ca870b5c-cf75-4418-a7fb-04b40dd0df5f" />
<img width="1394" height="864" alt="image" src="https://github.com/user-attachments/assets/402f7ae0-e28f-46f5-8fe9-7c247a477d82" />


# HCRaj Judgments Scraper

The **HCRaj Judgments Scraper** is a Python script that automates the process of scraping and downloading judgment PDFs from the Rajasthan High Court website (`hcraj.nic.in`). Using **Selenium**, it navigates the website, fills out search forms, handles manual captcha entry, and organizes downloaded PDFs and metadata into a CSV file.

## Features

- **Automated Form Submission**: Fills date ranges and form fields automatically.
- **Manual Captcha Handling**: Prompts users to enter the captcha code from a downloaded image.
- **Bulk PDF Download**: Downloads all judgment PDFs from search results.
- **Metadata Export**: Saves details (Sr.No., Case Details, Order Date, PDF filename) to `downloaded_judgments.csv`.
- **Organized Storage**: Stores PDFs in a `judgments_pdfs` directory.
- **Dependency Management**: Includes a `requirements.txt` file for easy setup.

## Prerequisites

Before running the script, ensure you have:

- **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package manager (included with Python).
- **Google Chrome**: The script uses ChromeDriver to control a Chrome browser.
- **ChromeDriver**: Must match your Chrome browser version (see Setup section).

## Setup and Installation

Follow these steps to set up the project:

### Step 1: Save the Script
Save the Python script (`your_script_name.py`) to a local folder.

### Step 2: Create and Populate `requirements.txt`
Navigate to the project directory in your terminal or command prompt and run:

```bash
pip freeze > requirements.txt
```

This generates a `requirements.txt` file listing required packages (e.g., `selenium`, `pandas`).

### Step 3: Install Dependencies
Install the required libraries using:

```bash
pip install -r requirements.txt
```

### Step 4: Download and Configure ChromeDriver
1. Check your Chrome browser version by navigating to `chrome://version/` in Chrome.
2. Download the matching ChromeDriver from [googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/).
3. Update the `driver` service path in the script to point to `chromedriver.exe`. For example:

```python
# Original line:
# service=Service(r"C:\Users\shubham\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Update to your path:
service=Service(r"C:\path\to\your\chromedriver.exe")
```

## How to Run the Script

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script:

```bash
python your_script_name.py
```

### Execution Flow
- A headless Chrome browser opens and navigates to the search page.
- The script fills in the date range and selects the "Reportable" option.
- A `captcha.png` file is saved in the project directory.
- You’ll be prompted to enter the captcha code from the image.
- After submitting the captcha, the script scrapes the results table and downloads PDFs to the `judgments_pdfs` folder.
- Metadata is saved to `downloaded_judgments.csv`.

## Troubleshooting

- **Error: `'chromedriver' executable needs to be in PATH`**
  - Ensure the ChromeDriver path in the script is correct.
  - Verify ChromeDriver matches your Chrome version.
- **Error: `No results table found`**
  - Likely due to incorrect captcha entry or no results for the selected dates. Retry with the correct captcha or different dates.
- **Error: `'str' object has no attribute 'get_attribute'`**
  - The website’s HTML structure may have changed. Update the script’s XPath or selectors to match the new structure.
- **General Issues**
  - Ensure all dependencies are installed (`pip install -r requirements.txt`).
  - Verify your internet connection is stable.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows the project’s style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Additional Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/): For advanced Selenium usage.
- [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/): For the latest ChromeDriver versions.
- [Rajasthan High Court Website](https://hcraj.nic.in): The target website for scraping.
