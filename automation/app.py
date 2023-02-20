import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver as ChromeDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        mobile_emulation = { "deviceName": "Samsung Galaxy S20 Ultra" }
        chrome_options = ChromeDriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.ch_driver=ChromeDriver.Chrome('chromedriver',options=chrome_options)


    def test_enter_cathaybk(self) -> None:
        self.ch_driver.get('https://www.cathaybk.com.tw/cathaybk')
        
        page_is_shown=WebDriverWait(self.ch_driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.cubre-o-indexKv__tree')))
        assert page_is_shown
        
        self.ch_driver.save_screenshot('homepage.png')

        el_tab = self.ch_driver.find_element(By.CLASS_NAME, 'cubre-a-burger')
        el_tab.click()
        el_menu_list = self.ch_driver.find_element(By.CSS_SELECTOR, ".cubre-o-nav__menu")
        List_isShown = WebDriverWait(self.ch_driver,3).until(EC.visibility_of(el_menu_list))
        assert List_isShown
        
        el_product_introduction = el_menu_list.find_element(By.CSS_SELECTOR, ".cubre-o-menu__btn")
        el_product_introduction.click()
        el_credit_card = self.ch_driver.find_element(By.XPATH, "//*[text()='信用卡']")
        credit_card_isShown = WebDriverWait(self.ch_driver,3).until(EC.visibility_of(el_credit_card))
        assert credit_card_isShown

        el_credit_card.click()
        el_credit_card_introduction = self.ch_driver.find_element(By.XPATH, "//*[text()='卡片介紹']")
        credit_card_introduction_isShown = WebDriverWait(self.ch_driver,3).until(EC.visibility_of(el_credit_card_introduction))
        assert credit_card_introduction_isShown

        el_credit_card_introduction.click()
        credit_card_page_title_isShown=WebDriverWait(self.ch_driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cubre-a-kvTitle")))
        assert credit_card_page_title_isShown
        
        el_deactivate_card_section = self.ch_driver.find_element(By.CSS_SELECTOR, "section[data-anchor-block='blockname06']")
        self.ch_driver.execute_script("arguments[0].scrollIntoView();", el_deactivate_card_section)
        deactivate_card_isShown=WebDriverWait(self.ch_driver,10).until(EC.visibility_of(el_deactivate_card_section))
        assert deactivate_card_isShown
        
        self.ch_driver.save_screenshot('deactivate_card_1.png')
        
        deactive_cards=el_deactivate_card_section.find_elements(By.CSS_SELECTOR,'.cubre-m-compareCard__pic')
        print('deactive card amont = ',len(deactive_cards))
        
        for idx in range(len(deactive_cards)-1):
            element = deactive_cards[idx]
            ActionChains(self.ch_driver).click_and_hold(element).move_by_offset(-200, 0).release().perform()
            wait=WebDriverWait(self.ch_driver,5)
            wait.until(EC.invisibility_of_element(element))

            banner_screenshot_path = f"deactivate_card_{idx+2}.png"
            self.ch_driver.save_screenshot(banner_screenshot_path)

        image_name_prefix = "deactivate_card_"
        image_file_extension = ".png"
        folder_path = str(os.getcwd())
        all_files = os.listdir(folder_path)
        image_files = [file for file in all_files if file.startswith(image_name_prefix) and file.endswith(image_file_extension)]
        image_count = len(image_files)
        print('image count = ',image_count)

        assert image_count == len(deactive_cards)



if __name__ == '__main__':
    unittest.main()
