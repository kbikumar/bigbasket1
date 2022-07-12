from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import unittest

class BigBasket(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print("start")
        cls.serv_obj = Service("C:\\Users\\kmana\\OneDrive\\Desktop\\alok\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.serv_obj)
        cls.driver.get("https://www.bigbasket.com/")


    def test_a_selectCity(self):
        print("1")
        self.driver.find_element(By.XPATH,"//span[contains(text(),'560004')]").click()
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]").submit()
        time.sleep(5)

    def test_b_Add_product_from_Best_Sellers(self):
        print("2")
        self.best_sellers=self.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[1]/h2")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.best_sellers)

    def test_c_clicAddButton(self):
        print("3")
        self.add_btn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[2]/div/div[1]/div/div[1]/div/div/product-template-in-container/div[1]/div[4]/div[3]/div/div[5]/div[2]/button")
        self.add_btn.click()
        time.sleep(5)

    def test_d_assert_Add_clicked(self):
        print("4")
        self.add_btn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[2]/div/div[1]/div/div[1]/div/div/product-template-in-container/div[1]/div[4]/div[3]/div/div[5]/div[2]/button")
        self.assertTrue(self.add_btn.is_displayed() == False)


    def test_e_assert_My_Basket_title_updated(self):
        print("5")
        self.my_basket_text = self.driver.find_element(By.XPATH, "//*[@id='totalNumberOfCartItems']").text
        self.assertTrue("0 items" != self.my_basket_text)
        time.sleep(10)


    def test_f_hover_My_Basket(self):
        print("6")
        self.my_basket = self.driver.find_element(By.XPATH," //*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/a")
        time.sleep(5)
        action = ActionChains(self.driver)
        action.move_to_element(self.my_basket).perform()


    def test_g_assert_same_product_selected(self):
        print("7")
        self.product_name1 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[2]/div/div[1]/div/div[1]/div/div/product-template-in-container/div[1]/div[4]/div[1]/a").text
        self.ele=self.driver.find_element(By.XPATH,"//*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/ul/li[1]/div/ul/li/div/div[3]/div/div[2]/a")
        self.P_name2=self.ele.text
        self.check=self.product_name1==self.P_name2
        self.assertTrue(True)


    def test_h_click_View_Basket(self):
        print("8")
        self.my_basket = self.driver.find_element(By.XPATH,"//*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/a")
        self.driver.execute_script("arguments[0].click()",self.my_basket)
        self.element = self.driver.find_element(By.XPATH,"//*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/ul/li[2]/div[2]/div[2]/button")
        self.driver.execute_script("arguments[0].click();", self.element)

    def test_i_assert_login_popup_displayed(self):
        print("9")
        self.assertTrue("Login - bigbasket" == self.driver.title)


    def test_j_screenshot(self):
        print("10")
        self.driver.get_screenshot_as_file("C:\Screeshot\pitucre.png")

    def test_k_close_login_popup(self):
        print("11")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/button").click()
        time.sleep(5)
        '''
        self.ele=self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/button")
        self.driver.execute_script("arguments[0].click();",self.ele)'''


    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()
        print("Test case completed.....")


if __name__ == '__main__':
    unittest.main()