from selenium import webdriver

class Searched:
    def __init__(self):
        
        self.url = 'https://www.signal.bz/news'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    def scrapping(self):
        driver = webdriver.Chrome(options = self.options)
        driver.get(self.url)
        result = list()
        link = list()
        for i in range(2):
            for j in range(5):
                path = '//*[@id="app"]/div/main/div/section/section[1]/div[2]/div[' + str(i + 1) + ']/div['+ str(j + 1) + ']/a/span[2]'
                path_l = '//*[@id="app"]/div/main/div/section/section[1]/div[2]/div[' + str(i + 1) + ']/div['+ str(j + 1) + ']/a'
                result.append(driver.find_element_by_xpath(path).text)
                link.append(driver.find_element_by_xpath(path_l).get_attribute("href"))
        driver.close()
        return result, link








