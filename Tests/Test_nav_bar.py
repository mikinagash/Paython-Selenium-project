from Pages.Home_page import HomePage
from Base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures('set_up')
class TestNavBar(Base):

    # def test_nav_bar(self):
    #     driver = self.driver
    #     All_nav_bar = HomePage(driver)
    #     All_nav_bar.enter_nuvbar()
        # if All_nav_bar.enter_nuvbar() == 'Login':
        #     WebDriverWait(driver, 5).until(EC.url_to_be('https://trip-yoetz.herokuapp.com/login'))


    def test_nav_bar_loop(self):
        driver = self.driver
        home = HomePage(driver)
        home.enter_nuvbar()



    def test_search_nav_bar(self):
        driver = self.driver
        home = HomePage(driver)
        home.search_correct("paris")
        assert "Discover Paris" == home.discoverParis_msg()








