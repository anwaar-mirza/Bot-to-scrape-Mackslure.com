from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from threading import Thread
import pandas as pd
import time
import os



class MackslaureData:
    def __init__(self):
        user_agent = UserAgent()
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument(f"user-agent={user_agent.random}")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 5)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.get('https://mackslure.com/products')
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def select_product_to_scrape(self, product_to_scrape):
        try:
            choice = self.wait.until(EC.presence_of_element_located((By.XPATH, f'//li[@class="collection__item"]//span[contains(text(), "{product_to_scrape}")]')))
            self.action.click(choice).perform()
        except:
            print("Fail to Open Product to Scrape......")
    
    def get_product_links(self):
        links = []
        while True:
            try:
                self.driver.execute_script("document.body.style.zoom='25%'")
                product_links = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "products-per-row-4")]//a[@class="productitem--image-link"]')))
                for p in product_links:
                    links.append(p.get_attribute('href'))

                next_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Go to next page"]')))
                self.action.click(next_btn).perform()
                time.sleep(2)
            except:
                break

        return list(set(links))
    
    def land_targeted_page(self, page_url):
        self.driver.get(page_url)
        self.driver.implicitly_wait(5)
        self.driver.execute_script("document.body.style.zoom='25%'")

    def get_listing_title(self):
        try:
            title = self.wait.until(EC.presence_of_element_located((By.XPATH, '//h1[@class="product-title"]'))).text
            return title
        except:
            return None
        
    def get_price(self):
        try:
            price = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-pricing"]//div[@class="price__current  "]'))).text.split('\n')[1]
            return price
        except:
            return None

    def get_varients(self):
        try:
            dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="data-variant-option-0"]')))
            self.action.click(dropdown).perform()
            time.sleep(0.5)
            options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//select[@id="data-variant-option-0"]/option')))
            options = [o.text.strip() for o in options]
            options = ", ".join(options)
            self.action.click(dropdown).perform()
            return options
        except:
            print("Fail to get varients......")
            return None
    
    def get_size(self):
        try:
            dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="data-variant-option-1"]')))
            self.action.click(dropdown).perform()
            time.sleep(0.5)
            sizes = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//select[@id="data-variant-option-1"]/option')))
            sizes = [s.text.strip() for s in sizes]
            sizes = ", ".join(sizes)
            return sizes
        except:
            print("Fail to get sizes......")
            return None
        
    def get_description(self):
        try:
            description = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-description rte"]//p'))).text
            return description.strip()
        except:
            return None
        
    def get_images(self):
        try:
            images = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="product-gallery--media-thumbnail-img-wrapper"]/img')))
            images = [i.get_attribute('src').replace('100x75', '800x600') for i in images]
            images = ", ".join(images)
            return images
        except:
            return None
        
    def current_url(self):
        return self.driver.current_url.strip()



def choice_to_scrape(choice):
    if choice == 1:
        return "Trout Lures"
    elif choice == 2:
        return "Walleye Lures"
    elif choice == 3:
        return "Kokanee Lures"
    elif choice == 4:
        return "Salmon Lures"
    elif choice == 5:
        return "Ice Fishing"
    elif choice == 6:
        return "Attractors"
    elif choice == 7:
        return "Components"
    else:
        print("Invalid Choice")
        return 0
    



def execution_process(ch):
    choice = choice_to_scrape(ch)
    if choice != 0:
        bot = MackslaureData()
        path = os.getcwd()
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(path, f"{choice}-{timestamp}.csv")
        bot.select_product_to_scrape(choice)
        results = bot.get_product_links()
        for r in results:
            data_dict = {}
            bot.land_targeted_page(r)
            data_dict['Title'] = bot.get_listing_title()
            data_dict['Price'] = bot.get_price()
            data_dict['Varients'] = bot.get_varients()
            data_dict['Size'] = bot.get_size()
            data_dict['Description'] = bot.get_description()
            data_dict['Images'] = bot.get_images()
            data_dict['Listing Url'] = bot.current_url()
            p = pd.DataFrame([data_dict])
            p.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)
    else:
        pass
    
th1 = Thread(target=execution_process, args=(1, ))
th2 = Thread(target=execution_process, args=(2, ))
th3 = Thread(target=execution_process, args=(3, ))
th4 = Thread(target=execution_process, args=(4, ))
th5 = Thread(target=execution_process, args=(5, ))
th6 = Thread(target=execution_process, args=(6, ))
th7 = Thread(target=execution_process, args=(7, ))

th1.start()
time.sleep(10)
th2.start()
time.sleep(10)
th3.start()
time.sleep(10)
th4.start()
time.sleep(10)
th5.start()
time.sleep(10)
th6.start()
time.sleep(10)
th7.start()
time.sleep(10)
