from flask import Flask
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

app = Flask(__name__)

@app.route("/")
def home():
    # Configure Firefox options
    options = Options()
    options.add_argument("--headless")  # run headless
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    # Start geckodriver (downloads automatically if needed)
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get("https://example.com")
        title = driver.title
    finally:
        driver.quit()

    return f"Selenium (Firefox) fetched page title: {title}"

if __name__ == "__main__":
    # Bind to all interfaces so external port-forwarders can reach it
    app.run(host="0.0.0.0", port=8080)
