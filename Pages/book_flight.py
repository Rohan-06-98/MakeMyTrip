from selenium.webdriver.common.by import By


class BookFlight:
    def __init__(self, driver):
        self.driver = driver

    view_Price = (By.CSS_SELECTOR, ".appendRight8")
    select_minimum_price = (By.XPATH, "//div[contains(@class,'viewFareBtnCol')]//button[contains(@class,'button corp-btn latoBlack buttonPrimary fontSize13')]")
    select_promocode = (By.XPATH, "//div/span/span[@class='block radio customRadioBtn']")
    click_on_secure_trip = (By.XPATH, "//div/label/span[@class='customRadioBtn']")
    click_on_add_new_adult = (By.CSS_SELECTOR, ".addTravellerBtn")
    first_name = (By.XPATH, "//input[@placeholder='First & Middle Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    select_gender = (By.XPATH, "//div[@class='selectTab ']//label")
    to_click_on_wheelchair = (By.XPATH, "//div[@class='dropdown__value-container css-1hwfws3']")
    select_wheelchair_not_required = (By.CSS_SELECTOR, ".dropdown__menu")
    select_mob_no = (By.XPATH, "//input[@placeholder='Mobile No']")
    select_email = (By.XPATH, "//input[@placeholder='Email']")
    choose_email = (By.XPATH, "//div[@class='emailId']")
    to_click_on_continue = (By.XPATH, "//button[normalize-space()='Continue']")
    cnf_review_details = (By.XPATH, "//button[normalize-space()='CONFIRM']")
    select_seat = (By.XPATH, "//button[normalize-space()='Yes, Please']")
    click_continue_anyway = (By.CSS_SELECTOR, ".reviewAddonsBtn")
    select_proceed_to_pay = (By.XPATH, "//button[normalize-space()='Proceed to pay']")


    def viewPriceFair(self):
        return self.driver.find_elements(*BookFlight.view_Price)[1].click()

    def selectMinimumPrice(self):
        return self.driver.find_elements(*BookFlight.select_minimum_price)[0].click()

    def selectPromoCode(self):
        return self.driver.find_element(*BookFlight.select_promocode).click()

    def clickOnSecureTrip(self):
        return self.driver.find_elements(*BookFlight.click_on_secure_trip)[0].click()

    def clickOnAddNewAdult(self):
        return self.driver.find_element(*BookFlight.click_on_add_new_adult).click()

    def firstName(self):
        return self.driver.find_element(*BookFlight.first_name).send_keys("Rohan")

    def lastName(self):
        return self.driver.find_element(*BookFlight.last_name).send_keys("Kumar")

    def selectGender(self):
        return self.driver.find_elements(*BookFlight.select_gender)[0].click()

    def clickOnWheelchair(self):
        return self.driver.find_element(*BookFlight.to_click_on_wheelchair).click()

    def selectWheelchairNotReq(self):
        return self.driver.find_elements(*BookFlight.select_wheelchair_not_required)[1].click()

    def selectMobNo(self):
        return self.driver.find_element(*BookFlight.select_mob_no).send_keys("7091688769")

    def selectEmail(self):
        return self.driver.find_element(*BookFlight.select_email).send_keys("rohankumarbela@gmail.com")

    def chooseEmail(self):
        return self.driver.find_element(*BookFlight.choose_email).click()

    def clickContinue(self):
        return self.driver.find_element(*BookFlight.to_click_on_continue).click()

    def cnfReviewDetails(self):
        return self.driver.find_element(*BookFlight.cnf_review_details).click()

    def selectSeat(self):
        return self.driver.find_element(*BookFlight.select_seat).click()

    def clickContinueAnyway(self):
        return self.driver.find_element(*BookFlight.click_continue_anyway).click()

    def proceedToPay(self):
        return self.driver.find_element(*BookFlight.select_proceed_to_pay).click()

