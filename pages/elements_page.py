

import random

from locators.elements_page_locators import AddRemoveElementsPageLocators, BasicAuthPageLocators, BrokenImagesPageLocators, ChallengingDomPageLocators, ContextMenuPageLocators, ElementsPageLocators
from pages.base_page import BasePage


class ElementsPage(BasePage):
    locators = ElementsPageLocators()

    def get_text(self):
        self.find_is_visible(self.locators.TAB_AB_TEST).click()
        return len(self.find_is_visible(self.locators.CONTENT_AB_TEST).text)
    
class AddRemoveElementsPage(BasePage):
    locators = AddRemoveElementsPageLocators()

    def add_and_remove_elements(self) -> int:
        num = random.randint(1, 10)
        remove_count = random.randint(1, num)

        self.find_is_visible(self.locators.TAB_ADD_REMOVE_ELEMENT).click()
        add_button = self.find_is_clickable(self.locators.BUTTON_ADD_ELEMENT)
        for _ in range(num):
            add_button.click()

        for _ in range(remove_count):
            self.find_is_clickable(self.locators.BUTTON_REMOVE_ELEMENT).click()
        return (num - remove_count)
    
    def get_remainder_elements(self):
        return len(self.driver.find_elements(*self.locators.BUTTON_REMOVE_ELEMENT))
    
class BasicAuthPage(BasePage):
    locators = BasicAuthPageLocators()

    def auth_basic(self, username: str, password: str):
        protocol, rest = self.url.split("://")
        auth_url = f"{protocol}://{username}:{password}@{rest}"
        self.driver.get(auth_url)

    def get_success_message(self):
        return self.find_is_visible(self.locators.CONTENT_BASIC_AUTH).text
    
class BrokenImagesPage(BasePage):
    locators = BrokenImagesPageLocators()
    def get_all_image(self):
        return self.find_are_present(self.locators.ALL_IMAGES)
    
    def is_image_broken(self, image) -> bool:
        return not self.driver.execute_script(
            "return arguments[0].complete && arguments[0].naturalWidth > 0",
            image
        )
    def get_broken_images(self):
        images = self.get_all_image()
        broken_images = []

        for image in images:
            if self.is_image_broken(image):
                broken_images.append(image)
        
        return broken_images
    
class ChallengingDomPage(BasePage):
    locators = ChallengingDomPageLocators()

    def get_title_page(self):
        return self.find_is_visible(self.locators.PAGE_TITLE).text
    
    def get_buttons_count(self):
        buttons_count = len(self.find_are_visible(self.locators.BUTTONS))
        for index in range(buttons_count):
            self.find_are_visible(self.locators.BUTTONS)[index].click()
        return buttons_count
    
    def get_table_rows(self):
        return len(self.find_are_present(self.locators.TABLE_ROWS))
    
    def check_url_after_click_edit(self):
        self.find_is_visible(self.locators.FIRST_ROW_EDIT_BUTTON).click()
        current_link = self.driver.current_url
        return current_link
    def is_canvas_present(self):
        return self.find_is_visible(self.locators.CANVAS_RESULT) is not None
    
class ContextMenuPage(BasePage):
    locators = ContextMenuPageLocators()
    
    def get_alert_text(self):
        self.action_right_click(self.find_is_visible(self.locators.CONTENT_BOX))

        return self.click_and_handle_alert()
