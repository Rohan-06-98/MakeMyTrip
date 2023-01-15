from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    pop_up = (By.CSS_SELECTOR, ".loginModal.displayBlock.modalLogin.dynHeight.personal")
    to_click_on_from = (By.CSS_SELECTOR, "label[for='fromCity']")
    from_city = (By.CSS_SELECTOR, "input[placeholder='From']")
    select_departure = (By.CSS_SELECTOR, "#react-autowhatever-1-section-0-item-0")
    to_click_on_to = (By.XPATH, "//span[normalize-space()='To']")
    to_city = (By.CSS_SELECTOR, "input[placeholder='To']")
    select_designation = (
        By.CSS_SELECTOR, "li[id='react-autowhatever-1-section-0-item-0'] p[class='font14 appendBottom5 "
                         "blackText']")
    to_click_on_date = (By.CSS_SELECTOR, "div[aria-label='Thu Jan 05 2023'] div[class='dateInnerCell']")
    to_click_on_search = (By.CSS_SELECTOR, ".primaryBtn.font24.latoBold.widgetSearchBtn")

    def get_pop_up(self):
        return self.driver.find_element(*HomePage.pop_up).click()

    def toClickOnFrom(self):
        return self.driver.find_element(*HomePage.to_click_on_from).click()

    def fromCity(self):
        return self.driver.find_element(*HomePage.from_city).send_keys("Kolkata")

    def selectDeparture(self):
        return self.driver.find_element(*HomePage.select_departure).click()

    def toClickOnTo(self):
        return self.driver.find_element(*HomePage.to_click_on_to).click()

    def toCity(self):
        return self.driver.find_element(*HomePage.to_city).send_keys("Pune")

    def selectDesignation(self):
        return self.driver.find_element(*HomePage.select_designation).click()

    def toClickOnDate(self):
        return self.driver.find_element(*HomePage.to_click_on_date).click()

    def clickOnSearch(self):
        return self.driver.find_element(*HomePage.to_click_on_search).click()

# from selenium.webdriver.common.by import By
#
#
# # from selenium.webdriver.support.select import Select
#
#
# class HomePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     click_from = (By.XPATH, "//input[@id='fromCity']")
#     select_departure = (By.XPATH, "//p[normalize-space()='Kolkata, India']")
#     search_list = (By.XPATH, "//ul[@class='react-autosuggest__suggestions-list']/li")
#     click_to = (By.XPATH, "//input[@id='toCity']")
#     # select_designation = (By.XPATH, "//p[normalize-space()='Patna, India']")
#     # click_out_side = (By.XPATH, "//div[@class='fsw ']")
#     click_on_search = (By.XPATH, "//a[normalize-space()='Search']")
#
#     def clickFrom(self):
#         self.driver.find_element(*HomePage.click_from).send_keys("Kolkata")
#
#     def selectDeparture(self):
#         self.driver.find_element(*HomePage.select_departure).click()
#         # print(select)
#         # select.select_by_index([0]).click()
#
#     def clickTo(self):
#         self.driver.find_element(*HomePage.click_to).send_keys("Patna")
#
#     # def selectDesignation(self):
#     #     self.driver.find_element(*HomePage.select_designation).click()
#
#     def clickOnSearch(self):
#         self.driver.find_element(*HomePage.click_on_search).click()
#
