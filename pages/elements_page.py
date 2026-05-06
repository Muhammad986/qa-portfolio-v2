
import os
from pathlib import Path

import requests
from requests.auth import HTTPDigestAuth
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import random

from locators.elements_page_locators import AddRemoveElementsPageLocators, BasicAuthPageLocators, BrokenImagesPageLocators, ChallengingDomPageLocators, CheckboxesPageLocators, ContextMenuPageLocators, DigestAuthPageLocators, DisappearingElementsPageLocators, DownloadPageLocators, DragAndDropPageLocators, DropdownPageLocators, DynamicContentPageLocators, DynamicControlsPageLocators, DynamicLoadingPageLocators, ElementsPageLocators, EntryAdPageLocators, ExitIntentPageLocators, FloatingMenuPageLocators, ForgotPasswordPageLocators, FramesPageLocators, LoginPageLocators, UploadPageLocators
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

class DynamicLoadingPage(BasePage):
    locators = DynamicLoadingPageLocators()

    def start_exaples(self, example_num):
        if example_num not in [0, 1]:
            raise ValueError("Example number should be 1 or 2")
        self.find_are_visible(self.locators.LINKS)[example_num].click()
        self.find_is_clickable(self.locators.START_BUTTON).click()
        self.find_is_invisible(self.locators.LOADING)
        return self.find_is_visible(self.locators.FINISHED_TEXT).text.strip()
    
class EntryAdPage(BasePage):
    locators = EntryAdPageLocators()
    def is_modal_vivsible(self):
        try:
            self.find_is_visible(self.locators.MODAL)
            return True
        except TimeoutException:
            return False
        
    def close_modal(self):
        self.find_is_visible(self.locators.CLOSE_BUTTON).click()
        return self.find_is_invisible(self.locators.MODAL)
    
    def close_modal_if_visible(self):
        try:
            self.find_is_visible(self.locators.MODAL)
            self.close_modal()
            return True
        except TimeoutException:
            return False
    
    def wait_for_modal_viisible(self):
        return self.find_is_visible(self.locators.MODAL)
        
    def restart_ad(self):

        self.close_modal_if_visible()
        self.find_is_visible(self.locators.RESTART_AD_LINK).click()
        self.wait_for_modal_viisible()
        return self.find_is_visible(self.locators.MODAL_TITLE).text.strip()
    
class ExitIntentPage(BasePage):
    locators = ExitIntentPageLocators()

    def trigger_exit_intent(self):
        try:
            self.find_is_present(self.locators.MODAL)
            #Имитируем уход мышки за верхнюю границу viewport.
            self.driver.execute_script("""
                const event = new MouseEvent('mouseleave', {
                    bubbles: true,
                    cancelable: true,
                    view: window,
                    clientY: 0,
                    screenY: 0,
                    relatedTarget: null
                });
                document.documentElement.dispatchEvent(event);
            """)
            self.find_is_visible(self.locators.MODAL)
            return True
        except TimeoutException:
            return False
    
    def get_modal_title(self):
        return self.find_is_visible(self.locators.MODAL_TITLE).text.lower()
    
    def close_modal(self):
        try:
            self.find_is_visible(self.locators.CLOSE_BUTTON).click()
            self.find_is_invisible(self.locators.MODAL)
            return True
        except TimeoutException:
            return False
    
    def get_body_header(self):
        return self.find_is_visible(self.locators.HEADER_BODY_TEXT).text.strip()
    
class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    def __init__(self, driver, url, download_dir="file_for_tests"):
        super().__init__(driver, url)
        self.download_dir = Path(download_dir).resolve()
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def get_files_names(self):
        files = self.find_are_visible(self.locators.FILE_LINKS)
        return [file.text.strip() for file in files if file.text.strip()]

    def get_random_file_name(self):
        files = self.get_files_names()
        if not files:
            raise ValueError("No files available for download")
        return random.choice(files)

    def wait_for_downloaded_file(self, file_name, timeout=10):
        expected_file = self.download_dir / file_name
        temp_file = self.download_dir / f"{file_name}.crdownload"

        def download_completed(_):
            if temp_file.exists():
                return False

            if expected_file.exists() and expected_file.is_file() and expected_file.stat().st_size > 0:
                return expected_file

            return False

        return wait(
            self.driver,
            timeout,
            poll_frequency=0.5
        ).until(
            download_completed,
            message=f"File '{file_name}' was not downloaded during {timeout} seconds"
        )

    def download_file(self, file_name, timeout=10):
        self.find_is_clickable(self.locators.file_link_by_name(file_name)).click()

        file_path = self.wait_for_downloaded_file(file_name, timeout)
        file_size = file_path.stat().st_size

        return file_path, file_path.name, file_size

    def download_random_file(self, timeout=10):
        file_name = self.get_random_file_name()
        file_path, downloaded_file_name, file_size = self.download_file(file_name, timeout)

        return file_name, file_path, downloaded_file_name, file_size

    def delete_downloaded_file(self, file_path):
        file_path = Path(file_path)

        if file_path.exists():
            file_path.unlink()
            return not file_path.exists()

        return False

class UploadPage(BasePage):
    locators = UploadPageLocators()

    def upload_file(self, file_path):
        file_path = Path(file_path).resolve()

        if not file_path.exists():
            raise FileNotFoundError(f"File was not found: {file_path}")

        self.find_is_present(self.locators.FILE_INPUT).send_keys(str(file_path))
        self.find_is_clickable(self.locators.UPLOAD_BUTTON).click()

    def get_success_header(self):
        return self.find_is_visible(self.locators.SUCCESS_HEADER).text.strip()

    def get_uploaded_file_name(self):
        return self.find_is_visible(self.locators.UPLOADED_FILE_NAME).text.strip()

    def upload_and_get_result(self, file_path):
        self.upload_file(file_path)
        return self.get_success_header(), self.get_uploaded_file_name()

class FloatingMenuPage(BasePage):
    locators = FloatingMenuPageLocators()

    def get_menu_items_text(self):
        menu_items = self.find_are_visible(self.locators.MENU_ITEMS)
        return [item.text.strip() for item in menu_items if item.text.strip()]

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_menu_top_offset(self):
        menu = self.find_is_visible(self.locators.MENU)
        return self.driver.execute_script(
            "return arguments[0].getBoundingClientRect().top;",
            menu
        )

    def click_menu_item(self, item_text):
        self.find_is_clickable(
            self.locators.menu_item_by_text(item_text)
        ).click()

    def get_current_url(self):
        return self.driver.current_url

    def check_floating_menu(self, item_text="News"):
        menu_items = self.get_menu_items_text()
        top_before_scroll = self.get_menu_top_offset()

        self.scroll_to_bottom()

        top_after_scroll = self.get_menu_top_offset()
        is_visible_after_scroll = self.find_is_visible(self.locators.MENU).is_displayed()

        self.click_menu_item(item_text)
        current_url = self.get_current_url()

        return {
            "menu_items": menu_items,
            "top_before_scroll": top_before_scroll,
            "top_after_scroll": top_after_scroll,
            "is_visible_after_scroll": is_visible_after_scroll,
            "current_url": current_url,
        }

class ForgotPasswordPage(BasePage):
    locators = ForgotPasswordPageLocators()

    def get_title(self):
        return self.find_is_visible(self.locators.TITLE).text.strip()

    def enter_email(self, email):
        email_input = self.find_is_visible(self.locators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def get_entered_email(self):
        return self.find_is_visible(
            self.locators.EMAIL_INPUT
        ).get_attribute("value")

    def click_retrieve_password_button(self):
        self.find_is_clickable(
            self.locators.RETRIEVE_PASSWORD_BUTTON
        ).click()

    def get_result_header(self):
        return self.find_is_visible(
            self.locators.RESULT_HEADER
        ).text.strip()

    def submit_email(self, email):
        self.enter_email(email)
        entered_email = self.get_entered_email()
        self.click_retrieve_password_button()

        result_header = self.get_result_header()

        return {
            "entered_email": entered_email,
            "result_header": result_header
        }

class LoginPage(BasePage):
    locators = LoginPageLocators()

    def get_title(self):
        return self.find_is_visible(self.locators.TITLE).text.strip()


    def enter_form(self, username, password):
        password_input = self.find_is_visible(self.locators.PASSWORD_INPUT)
        username_input = self.find_is_visible(self.locators.USERNAME_INPUT)
        password_input.clear()
        username_input.clear()
        password_input.send_keys(password)
        username_input.send_keys(username)

    def get_flash_message(self):
        raw_text = self.find_is_visible(self.locators.FLASH_MESSAGE).text
        return raw_text.replace("×", "").strip()

    def get_current_url(self):
        return self.driver.current_url

    def get_secure_area_title(self):
        return self.find_is_visible(self.locators.SECURE_AREA_TITLE).text.strip()

    def login(self, username, password):
        self.enter_form(username, password)
        self.find_is_clickable(self.locators.LOGIN_BUTTON).click()

        return {
            "current_url": self.get_current_url(),
            "flash_message": self.get_flash_message(),
        }

    def successful_login(self, username, password):
        result = self.login(username, password)
        result["secure_area_title"] = self.get_secure_area_title()
        return result

    def logout(self):
        self.find_is_clickable(self.locators.LOGOUT_BUTTON).click()
        return self.get_flash_message()

class FramesPage(BasePage):
    locators = FramesPageLocators()

    def get_title(self):
        return self.find_is_visible(self.locators.TITLE).text.strip()

    def get_frame_links_text(self):
        links = self.find_are_visible(self.locators.FRAME_LINKS)
        return [link.text.strip() for link in links if link.text.strip()]

    def switch_to_frame(self, locator):
        wait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def get_frame_text(self, *frame_locators):
        self.driver.switch_to.default_content()

        for locator in frame_locators:
            self.switch_to_frame(locator)

        text = self.find_is_visible(self.locators.FRAME_BODY).text.strip()
        self.driver.switch_to.default_content()
        return text

    def get_nested_frames_text(self):
        self.find_is_clickable(self.locators.NESTED_FRAMES_LINK).click()

        return {
            "left": self.get_frame_text(self.locators.FRAME_TOP, self.locators.FRAME_LEFT),
            "middle": self.get_frame_text(self.locators.FRAME_TOP, self.locators.FRAME_MIDDLE),
            "right": self.get_frame_text(self.locators.FRAME_TOP, self.locators.FRAME_RIGHT),
            "bottom": self.get_frame_text(self.locators.FRAME_BOTTOM),
        }

    def edit_iframe_text(self, text):
        self.find_is_clickable(self.locators.IFRAME_LINK).click()
        self.driver.switch_to.default_content()
        self.switch_to_frame(self.locators.IFRAME)

        editor = self.find_is_visible(self.locators.EDITOR_BODY)

        self.driver.execute_script(
            "arguments[0].textContent = arguments[1];",
            editor,
            text
        )

        entered_text = self.driver.execute_script(
            "return arguments[0].textContent.trim();",
            editor
        )

        self.driver.switch_to.default_content()
        return entered_text
