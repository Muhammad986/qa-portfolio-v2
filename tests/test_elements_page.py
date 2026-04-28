from pages.elements_page import AddRemoveElementsPage, BasicAuthPage, BrokenImagesPage, ChallengingDomPage, ContextMenuPage, ElementsPage

import time
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

    class TestContextMenuPage:
        def test_context_menu(self, driver):
            page = ContextMenuPage(driver, 'https://the-internet.herokuapp.com/context_menu')
            page.open()
            text_alert = page.get_alert_text()
            assert text_alert == 'You selected a context menu', (
            f"Expected alert text to be 'You selected a context menu', but got: '{text_alert}'"
            )