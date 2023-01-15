import time

# from selenium.webdriver.common.by import By

# from selenium.webdriver.common.by import By

# from selenium.webdriver.common.by import By

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

from Pages.Home_page import HomePage
from Pages.book_flight import BookFlight
from Pages.search_results import SearchResult
from utilities.Base_class import BaseClass


class TestMain(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.get_pop_up()
        self.verify_link_presence(homePage.to_click_on_from)
        homePage.toClickOnFrom()
        self.verify_link_presence(homePage.from_city)
        homePage.fromCity()
        time.sleep(2)
        homePage.selectDeparture()
        self.verify_link_presence(homePage.to_click_on_to)
        homePage.toClickOnTo()
        self.verify_clickable(homePage.to_city)
        homePage.toCity()
        time.sleep(2)
        homePage.selectDesignation()
        self.verify_clickable(homePage.to_click_on_date)
        homePage.toClickOnDate()
        self.verify_clickable(homePage.to_click_on_search)
        homePage.clickOnSearch()
        time.sleep(2)

        searchItem = SearchResult(self.driver)
        searchItem.is_popup_present()
        searchItem.clear_popup()
        # time.sleep(3)
        # searchItem.flightDetails()

        time.sleep(3)

        flight_list = []
        total_container = searchItem.get_total_container()
        for i in range(total_container):
            flight_list.append(searchItem.get_flight_details_by_index(i))

        print(len(flight_list))
        print(flight_list)
        print(flight_list[1]['price'])

        bookFlight = BookFlight(self.driver)
        bookFlight.viewPriceFair()
        time.sleep(2)
        bookFlight.selectMinimumPrice()
        windowsOpen = self.driver.window_handles
        self.driver.switch_to.window(windowsOpen[1])
        self.verify_clickable(bookFlight.select_promocode)
        bookFlight.selectPromoCode()
        self.verify_clickable(bookFlight.click_on_secure_trip)
        bookFlight.clickOnSecureTrip()
        time.sleep(2)
        self.verify_link_presence(bookFlight.click_on_add_new_adult)
        bookFlight.clickOnAddNewAdult()
        # time.sleep(5)
        self.verify_clickable(bookFlight.first_name)
        bookFlight.firstName()
        self.verify_clickable(bookFlight.last_name)
        bookFlight.lastName()
        self.verify_clickable(bookFlight.select_gender)
        bookFlight.selectGender()
        self.verify_clickable(bookFlight.to_click_on_wheelchair)
        bookFlight.clickOnWheelchair()
        # self.verify_clickable(bookFlight.select_wheelchair_not_required)
        # bookFlight.selectWheelchairNotReq()
        self.verify_clickable(bookFlight.select_mob_no)
        bookFlight.selectMobNo()
        self.verify_clickable(bookFlight.select_email)
        bookFlight.selectEmail()
        self.verify_clickable(bookFlight.choose_email)
        bookFlight.chooseEmail()
        time.sleep(3)
        self.verify_clickable(bookFlight.to_click_on_continue)
        bookFlight.clickContinue()
        self.verify_clickable(bookFlight.cnf_review_details)
        bookFlight.cnfReviewDetails()
        self.verify_clickable(bookFlight.select_seat)
        bookFlight.selectSeat()
        self.verify_clickable(bookFlight.to_click_on_continue)
        bookFlight.clickContinue()
        bookFlight.clickContinue()
        time.sleep(3)
        self.verify_clickable(bookFlight.click_continue_anyway)
        bookFlight.clickContinueAnyway()
        self.verify_clickable(bookFlight.select_proceed_to_pay)
        bookFlight.proceedToPay()

        time.sleep(10)
        # view_prices = self.find_elements(By.CSS_SELECTOR, ".ViewFareBtn")
        # view_prices([2]).click()
        # self.flight_list[2]['price'].click()
        # self.driver.find_element(By.XPATH, "//button[@id='bookbutton-RKEY:2213ffac-9d9
        # 4-44e1-9e21-9f9a5ff8c017:17_0']").click()

        # all_flight_details = self.driver.find_elements(By.XPATH, "//div[@class='makeFlex simpleow']")
        # for all_flight_detail in all_flight_details:
        #     print(all_flight_detail.text)

        # flights_name = self.driver.find_elements(By.XPATH, "//div[@class='makeFlex align-items-center gap-x-10
        # airline-info-wrapper']") for flight in flights_name: print(flight.text) flights = {} for flight in range(
        # len(flights_name)): print(flights_name[flight].text) flights['flight_%s' % flight] = flights_name[
        # flight].text

        # flight_details = self.driver.find_elements(By.XPATH, "//div[@class='timingOptionOuter']")
        # for flight_detail in flight_details:
        #     print(flight_detail.text)

        # flight_prices = self.driver.find_elements(By.CLASS_NAME, "textRight flexOne")
        # for flight_price in flight_prices:
        #     print(flight_price.text)

        # flights = {
        #     "flight_name": flights_name.text,
        #     "flight_Fare": flight_details.text
        # }
        #
        # for flight in flights:
        #     print(flight)

        # Getting all the values of a dictionary as a list
        # list_of_the_values = list(flights.values())

        # Printing the list which contains all the values of the dictionary
        # print(list_of_the_values)

        # time.sleep(3)
        # homePage.clickFrom()
        # time.sleep(3)
        # self.verify_clickable(homePage.select_departure)
        # homePage.selectDeparture()
        # time.sleep(3)
        # homePage.clickTo()
        # time.sleep(3)
        # # # homePage.selectDesignation()
        # # time.sleep(3)
        # homePage.clickOnSearch()
        # time.sleep(6)
