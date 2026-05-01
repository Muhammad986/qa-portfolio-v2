from pages.elements_page import AddRemoveElementsPage, BasicAuthPage, BrokenImagesPage, ChallengingDomPage, CheckboxesPage, ContextMenuPage, DigestAuthPage, DisappearingElementsPage, DragAndDropPage, DropdownPage, DynamicContentPage, DynamicControlsPage, ElementsPage

import time

import random
import requests
from requests.auth import HTTPDigestAuth
class TestElementsPage:
    class TestABTest:

        def test_ab_test(self, driver):
            page = ElementsPage(driver, 'https://the-internet.herokuapp.com/')
            page.open()
            content_text = page.get_text()
            assert content_text > 0

    class TestAddRemoveElementsPage:

        def test_add_remove_elements(self, driver):
            page = AddRemoveElementsPage(driver, 'https://the-internet.herokuapp.com/')
            page.open()
            expected_remainder = page.add_and_remove_elements()
            actual_remainder = page.get_remainder_elements()
            assert expected_remainder == actual_remainder, (
                f"Expected {expected_remainder} remaining elements, but got {actual_remainder}")
            
    class TestBasicAuthPage:
        def test_basic_auth(self, driver):
            page = BasicAuthPage(driver, 'https://the-internet.herokuapp.com/basic_auth')
            page.auth_basic(username='admin', password='admin')
            message = page.get_success_message()
            assert "Congratulations" in message, (
            f"Expected success auth message, but got: '{message}'"
            )

    class TestBrokenImagesPage:
        def test_broken_image(self, driver):
            page = BrokenImagesPage(driver, 'https://the-internet.herokuapp.com/broken_images')
            page.open()
            broken_images = page.get_broken_images()
            assert len(broken_images) > 0, "Expected to find broken images on the page, but none were found"

    class TestChallengingDomPage:

        def test_challenging_dom(self, driver):
            page = ChallengingDomPage(driver, 'https://the-internet.herokuapp.com/challenging_dom')
            page.open()
            assert page.get_title_page() == "Challenging DOM", (
                f"Expected page title to be 'Challenging DOM', but got '{page.get_page_title()}'"
            )
            assert page.get_buttons_count() == 3, (
                f"Expected 3 buttons, but got {page.get_buttons_count()}"
            )
            assert page.get_table_rows() == 10, "Expected table to contain rows, but it was empty"

            current_url = page.check_url_after_click_edit()

            assert 'edit' in current_url, (
                f"Expected URL to contain 'edit' after clicking the Edit button, but got: '{current_url}'"
            )
            assert page.is_canvas_present(), "Expected canvas element to be present on the page"

    class TestCheckboxesPage:
        def test_checkboxes(self, driver):
            page = CheckboxesPage(driver, 'https://the-internet.herokuapp.com/checkboxes')
            page.open()
            before, after = page.toggle_checkboxes_and_get_states()
            assert before != after, (
                f"Expected checkbox states to change after toggle, but before={before}, after={after}"
            )

    class TestContextMenuPage:
        def test_context_menu(self, driver):
            page = ContextMenuPage(driver, 'https://the-internet.herokuapp.com/context_menu')
            page.open()
            text_alert = page.get_alert_text()
            assert text_alert == 'You selected a context menu', (
            f"Expected alert text to be 'You selected a context menu', but got: '{text_alert}'"
            )

    class TestDigestAuthPage:
        def test_digest_auth_api(self, driver):
            page = DigestAuthPage(driver, 'https://the-internet.herokuapp.com/digest_auth')
            response = page.digest_auth_api(username='admin', password='admin')

            assert response.status_code == 200, (
                f"Expected status code 200, but got {response.status_code}"
            )
            assert "Congratulations" in response.text, (
                "Expected success message after digest authentication"
            )

    class TestDisappearingElementsPage:
        def test_menu_items_may_change_after_refresh(self, driver):
            page = DisappearingElementsPage(driver, 'https://the-internet.herokuapp.com/disappearing_elements')
            page.open()

            state = page.disappearing_menu()
            assert state, 'The menu items will not change after the page is refreshed'

    class TestDragAndDropPage:
        def test_drag_and_drop(self, driver):
            page = DragAndDropPage(driver, 'https://the-internet.herokuapp.com/drag_and_drop')
            page.open()
            before, after = page.swap_elements()

            assert before != after, (
                f"Expected columns order to change after drag and drop, "
                f"but before={before}, after={after}"
            )
    
    class TestDropdownPage:
        
        def test_select_option(self, driver):
            page = DropdownPage(driver, "https://the-internet.herokuapp.com/dropdown")
            page.open()
            text = ['Option 1', 'Option 2']
            choice_option = page.select_option_by_text(random.choice(text))
            selected_option = page.get_selected_option_text()
            assert selected_option == choice_option, (
                f"Expected selected option to be 'Option 1', but got '{selected_option}'"
            )
    
    class TestDynamicContentPage:
        def test_dynamic_content_changes_after_refresh(self, driver):
            page = DynamicContentPage(driver, 'https://the-internet.herokuapp.com/dynamic_content')
            page.open()
            before_content = page.get_content_text()
            page.refresh_page()
            after_content = page.get_content_text()

            assert before_content != after_content, (
                f"Expected dynamic content to change after refresh, but before={before_content}, after={after_content}"
            )
        
        def test_static_content_does_not_change_after_refresh(self, driver):
            page = DynamicContentPage(driver, 'https://the-internet.herokuapp.com/dynamic_content?with_content=static')
            page.open()
            before_content = page.get_content_text()
            page.refresh_page()
            after_content = page.get_content_text()

            some_blocks = sum(
                1 for before, after in zip(before_content, after_content) if before == after
            )
            assert some_blocks >= 1, (
                f"Expected at least one content block to remain static after refresh, "
                f"but before={before_content}, after={after_content}"
            )

    class TestDynamicControlsPage:
        def test_checkbox(self, driver):
            page = DynamicControlsPage(driver, 'https://the-internet.herokuapp.com/dynamic_controls')
            page.open()
    
            removed_message, added_message = page.appears_disappers_checkbox()
    
            assert removed_message == "It's gone!", (
                f"Expected message \"It's gone!\", but got '{removed_message}'"
            )
            assert added_message == "It's back!", (
                f"Expected message \"It's back!\", but got '{added_message}'"
            )
    
        def test_input(self, driver):
            page = DynamicControlsPage(driver, 'https://the-internet.herokuapp.com/dynamic_controls')
            page.open()
    
            result = page.check_input("Selenium")
    
            assert result["enable_message"] == "It's enabled!", (
                f"Expected enable message, but got '{result['enable_message']}'"
            )
            assert result["entered_text"] == "Selenium", (
                f"Expected input value 'Selenium', but got '{result['entered_text']}'"
            )
            assert result["disable_message"] == "It's disabled!", (
                f"Expected disable message, but got '{result['disable_message']}'"
            )
            assert result["is_disabled"] is True, "Expected input to be disabled after clicking Disable"
    