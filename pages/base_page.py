from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def find_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def find_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    
    def  find_are_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    
    def find_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def find_is_invisible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    
    def go_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", locator)


    def action_right_click(self, element, timeout=10):
        ActionChains(self.driver).context_click(element).perform()

    def click_and_handle_alert(self, locator=None, timeout=10, action="accept", input_text=None):
        if locator is not None:
            self.find_is_clickable(locator).click()

        alert = wait(self.driver, timeout).until(EC.alert_is_present())
        alert_text = alert.text

        if input_text is not None:
            alert.send_keys(input_text)
    
        if action == "accept":
            alert.accept()
        elif action == "dismiss":
            alert.dismiss()
        else:
            raise ValueError(f"Unsupported alert action: {action}")
    
        return alert_text
    
    def action_drag_and_drop_to_element(self, what, where, hold_pause=0.2, move_pause=0.2):
        self.go_to_element(what)
        self.go_to_element(where)
    
        action = ActionChains(self.driver)
        action.move_to_element(what)
        action.click_and_hold(what)
        action.pause(hold_pause)
        action.move_to_element(where)
        action.pause(move_pause)
        action.release(where)
        action.perform()
       
