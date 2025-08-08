from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Set binary location if using Railway-provided Chromium (see notes)
    # chrome_options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.example.com")
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    main()
