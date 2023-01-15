from selenium.webdriver.common.by import By


# from selenium.webdriver.support.select import Select


class SearchResult:

    def __init__(self, driver):
        self.driver = driver

    flight_details = (By.XPATH, "//div[@id='premEcon']")
    popup = (By.XPATH, "//button[normalize-space()='OKAY, GOT IT!']")

    def is_popup_present(self) -> bool:
        popup = self.driver.find_elements(*SearchResult.popup)
        popup_present = False
        if len(popup) >= 1:
            print("PopUp is present")
            popup_present = True
        else:
            print("Popup is not present")
        return popup_present

    def clear_popup(self):
        return self.driver.find_element(*SearchResult.popup).click()

    def get_flight_details_by_index(self, index):
        flight_details = {}
        containers = self.driver.find_elements(By.CSS_SELECTOR, ".listingCard")
        title = containers[index].find_element(By.CSS_SELECTOR, "p.airlineName")
        title_text = title.text
        departure_time_text = containers[index].find_element(By.CSS_SELECTOR, ".timeInfoLeft p.flightTimeInfo").text
        arrival_time_text = containers[index].find_element(By.CSS_SELECTOR, ".timeInfoRight p.flightTimeInfo").text
        travel_time_text = containers[index].find_element(By.XPATH, "//div[@class='stop-info flexOne']/p").text
        # view_price = containers[index].find_elements(By.CSS_SELECTOR, ".ViewFareBtn")
        # print(1)
        # containers2 = self.driver.find_elements(By.CSS_SELECTOR, ".listingCard")
        price_text = containers[index].find_element(By.CSS_SELECTOR, ".textRight").text
        f_price = price_text.replace("₹", "")
        flight_details['price'] = f_price
        flight_details['title'] = title_text
        flight_details['departure'] = departure_time_text
        flight_details["arrival"] = arrival_time_text
        flight_details["Travel Time"] = travel_time_text

        # print("Hi")
        # print(price_text)
        # print(price_text.text)
        print(f"Result is : {flight_details}")

        # def flightDetails(self):
        #     for detail in enumerate(self.flight_details):
        # self.driver.find_elements(By.XPATH, "//div/p[@class='boldFont blackText airlineName']")
        # print(detail)
        # self.flights["detail"] = detail.text
        return flight_details

    def get_total_container(self):
        containers = self.driver.find_elements(By.CSS_SELECTOR, ".listingCard")
        return len(containers)


