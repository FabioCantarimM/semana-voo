import os
from selenium import webdriver

class BrowserProvider:
    
    browser = None
    options = webdriver.ChromeOptions()

    def get_browser(self, args: list[str] = None, headless: bool = True):
        new_arg = args
        if args == None:
            new_arg = self.default_args()
        self.set_options(new_arg)
        self.is_headless(headless)
        self.browser = webdriver.Chrome(options=self.options)
        return self.browser

    def set_options(self, args):
        if args:
            for arg in args:
                self.options.add_argument(arg)

    def is_headless(self, headless: bool):
        n_headless = os.getenv("HEADLESS")
        if n_headless is None:
            self.options.add_argument("--headless")



    def default_args(self):
        return [
        "--no-sandbox",
        "--disable-gpu",
        "--disable-setuid-sandbox",
        "--disable-web-security",
        "--disable-dev-shm-usage",
        "--memory-pressure-off",
        "--ignore-certificate-errors",
        "--disable-features=site-per-process",
        "--incognito",
        "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        ]