
import requests
from requests.auth import HTTPDigestAuth
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait

import random

from locators.elements_page_locators import AddRemoveElementsPageLocators, BasicAuthPageLocators, BrokenImagesPageLocators, ChallengingDomPageLocators, CheckboxesPageLocators, ContextMenuPageLocators, DigestAuthPageLocators, DisappearingElementsPageLocators, DragAndDropPageLocators, DropdownPageLocators, DynamicContentPageLocators, DynamicControlsPageLocators, ElementsPageLocators
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
    
class CheckboxesPage(BasePage):
    locators = CheckboxesPageLocators()

    def toggle_checkboxes_and_get_states(self):
        checkboxes = self.find_are_visible(self.locators.CHECKBOXES)
        states_before = [checkbox.is_selected() for checkbox in checkboxes]
        for checkbox in checkboxes:
            checkbox.click()
        states_after = [checkbox.is_selected() for checkbox in checkboxes]
        return states_before, states_after
    

class ContextMenuPage(BasePage):
    locators = ContextMenuPageLocators()
    
    def get_alert_text(self):
        self.action_right_click(self.find_is_visible(self.locators.CONTENT_BOX))

        return self.click_and_handle_alert()

class DigestAuthPage(BasePage):
    locators = DigestAuthPageLocators()
    def digest_auth_api(self, username: str, password: str):
        response = requests.get(
            self.url,
            auth=HTTPDigestAuth(username, password),
            timeout=10,
        )
        return response
    
class DisappearingElementsPage(BasePage):
    locators = DisappearingElementsPageLocators()

    def get_menu_item_text(self):
        elements = self.find_are_visible(self.locators.MENU_ITEMS)
        return [item.text for item in elements]
    
    def disappearing_menu(self):
        first_state = self.get_menu_item_text()
        changed = False

        for _ in range(5):
            self.driver.refresh()

            current_state = self.get_menu_item_text()
            if current_state != first_state:
                changed = True
                break
        return changed
    
class DragAndDropPage(BasePage):
    locators = DragAndDropPageLocators()

    def get_column_headers(self):
        header_a_and_b = self.find_are_visible(self.locators.DRAG_AND_DROP_ELEMENTS)
        headers = [header.text for header in header_a_and_b]
        return headers

    def swap_elements(self):
        state_before = self.get_column_headers()
        colums = self.find_are_visible(self.locators.DRAG_AND_DROP_ELEMENTS)
        colum_first = colums[0]
        colums_second = colums[1]
        self.action_drag_and_drop_to_element(colum_first, colums_second)
        state_after = self.get_column_headers()
        return state_before, state_after

class DropdownPage(BasePage):
    locators = DropdownPageLocators()
    
    def get_dropdown(self):
        return Select(self.find_is_visible(self.locators.DROPDOWN))

    def select_option_by_text(self, text):
        self.get_dropdown().select_by_visible_text(text)
        return text

    def get_selected_option_text(self):
        return self.get_dropdown().first_selected_option.text
    
class DynamicContentPage(BasePage):
    locators = DynamicContentPageLocators()
    def get_content_text(self):
        elements = self.find_are_present(self.locators.CONTENT_TEXTS)
        return [element.text.strip() for element in elements]
    
    def refresh_page(self):
        self.driver.refresh()

class DynamicControlsPage(BasePage):
    locators = DynamicControlsPageLocators()

    def wait_for_message(self, expected_text, timeout=10):
        def message_text(driver):
            text = driver.find_element(*self.locators.MESSAGE).text.strip()
            return text if text == expected_text else False

        return wait(self.driver, timeout).until(message_text)

    def wait_for_input_state(self, enabled, timeout=10):
        def input_state(driver):
            input_field = driver.find_element(*self.locators.INPUT_FIELD)
            return input_field if input_field.is_enabled() == enabled else False

        return wait(self.driver, timeout).until(input_state)

    def remove_checkbox(self):
        self.find_is_clickable(self.locators.REMOVE_ADD_BUTTON).click()
        self.find_is_invisible(self.locators.CHECKBOX)
        return self.wait_for_message("It's gone!")

    def add_checkbox(self):
        self.find_is_clickable(self.locators.REMOVE_ADD_BUTTON).click()
        self.find_is_visible(self.locators.CHECKBOX)
        return self.wait_for_message("It's back!")

    def appears_disappers_checkbox(self):
        removed_message = self.remove_checkbox()
        added_message = self.add_checkbox()
        return removed_message, added_message

    def enable_input(self):
        self.find_is_clickable(self.locators.ENABLE_DISABLE_BUTTON).click()
        input_field = self.wait_for_input_state(True)
        message = self.wait_for_message("It's enabled!")
        return input_field, message

    def disable_input(self):
        self.find_is_clickable(self.locators.ENABLE_DISABLE_BUTTON).click()
        input_field = self.wait_for_input_state(False)
        message = self.wait_for_message("It's disabled!")
        return input_field, message

    def check_input(self, text="Hello world"):
        input_field, enable_message = self.enable_input()
        input_field.clear()
        input_field.send_keys(text)
        entered_text = input_field.get_attribute("value")

        input_field, disable_message = self.disable_input()
        is_disabled = not input_field.is_enabled()

        return {
            "enable_message": enable_message,
            "entered_text": entered_text,
            "disable_message": disable_message,
            "is_disabled": is_disabled,
        }
