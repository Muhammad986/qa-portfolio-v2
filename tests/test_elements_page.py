from pages.elements_page import AddRemoveElementsPage, BasicAuthPage, BrokenImagesPage, ChallengingDomPage, CheckboxesPage, ContextMenuPage, DigestAuthPage, DisappearingElementsPage, DownloadPage, DragAndDropPage, DropdownPage, DynamicContentPage, DynamicControlsPage, DynamicLoadingPage, ElementsPage, EntryAdPage, ExitIntentPage, FloatingMenuPage, ForgotPasswordPage, FramesPage, LoginPage, UploadPage

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

    class TestDynamicLoadingPage:
        def test_exaple_1(self, driver):
            page = DynamicLoadingPage(driver, 'https://the-internet.herokuapp.com/dynamic_loading')
            page.open()
            result = page.start_exaples(0)
            assert result == "Hello World!", (
                f"Expected 'Hello World!', but got '{result}'"
            )

        def test_exaple_2(self, driver):
            page = DynamicLoadingPage(driver, 'https://the-internet.herokuapp.com/dynamic_loading')
            page.open()
            result = page.start_exaples(1)
            assert result == "Hello World!", (
                f"Expected 'Hello World!', but got '{result}'"
            )

    class TestEntryAdPage:
        def test_entry_ad_modal_is_displayed(self, driver):
            page = EntryAdPage(driver, "https://the-internet.herokuapp.com/entry_ad")
            page.open()

            assert page.is_modal_vivsible() is True, "Expected modal window to be visible"

        def test_entry_ad_modal_can_be_closed(self, driver):
            page = EntryAdPage(driver, "https://the-internet.herokuapp.com/entry_ad")
            page.open()
            is_closed = page.close_modal_if_visible()

            assert is_closed is True, "Expected modal window to be closed"

        def test_entry_ad_modal_content(self, driver):
            page = EntryAdPage(driver, "https://the-internet.herokuapp.com/entry_ad")
            page.open()

            modal_title = page.restart_ad()
            assert modal_title.lower() == "this is a modal window", (
            f"Expected modal title 'This is a modal window', but got '{modal_title}'"
        )
            
    class TestExitIntentPage:
        def test_exit_intent_modal_content(self, driver):
            page = ExitIntentPage(driver, 'https://the-internet.herokuapp.com/exit_intent')
            page.open()

            is_visible = page.trigger_exit_intent()
            modal_title = page.get_modal_title()

            is_invisible = page.close_modal()
            
            assert is_visible is True, "Expected exit intent modal to be visible"
            assert modal_title == "this is a modal window", (
                f"Expected modal title 'THIS IS A MODAL WINDOW', but got '{modal_title}'"
            )
            assert is_invisible is True, "Expected modal window to be invisible after clicking Close"

    class TestDownloadPage:

        def test_file_can_be_downloaded(self, driver, download_dir):
            page = DownloadPage(
                driver,
                "https://the-internet.herokuapp.com/download",
                download_dir
            )
            page.open()

            expected_file_name, file_path, downloaded_file_name, file_size = page.download_random_file()
            print(expected_file_name, file_path, downloaded_file_name, file_size)

            assert downloaded_file_name == expected_file_name, (
                f"Expected downloaded file name '{expected_file_name}', "
                f"but got '{downloaded_file_name}'"
            )

            assert file_size > 0, (
                f"Expected downloaded file '{downloaded_file_name}' to be not empty"
            )

            assert page.delete_downloaded_file(file_path) is True, (
                f"Expected downloaded file '{downloaded_file_name}' to be deleted"
            )

    class TestUploadPage:

        def test_file_can_be_uploaded(self, driver, download_dir):
            page = UploadPage(driver, "https://the-internet.herokuapp.com/upload")
            page.open()

            file_path = download_dir / "upload_test_file.txt"
            file_path.write_text("This file is used for upload testing.", encoding="utf-8")
            print(file_path)
            success_header, uploaded_file_name = page.upload_and_get_result(file_path)

            assert success_header == "File Uploaded!", (
                f"Expected success header 'File Uploaded!', but got '{success_header}'"
            )

            assert uploaded_file_name == file_path.name, (
                f"Expected uploaded file name '{file_path.name}', but got '{uploaded_file_name}'"
            )

    class TestFloatingMenuPage:

        def test_floating_menu(self, driver):
            page = FloatingMenuPage(driver, "https://the-internet.herokuapp.com/floating_menu")
            page.open()

            result = page.check_floating_menu("News")
            time.sleep(6)
            assert result["menu_items"] == ["Home", "News", "Contact", "About"], (
                f"Expected menu items ['Home', 'News', 'Contact', 'About'], "
                f"but got {result['menu_items']}"
            )

            assert result["is_visible_after_scroll"] is True, (
                "Expected floating menu to remain visible after scroll"
            )

            assert abs(result["top_after_scroll"]) < 10, (
                f"Expected menu to stay near the top of viewport after scroll, "
                f"but got top={result['top_after_scroll']}"
            )

            assert result["top_after_scroll"] < result["top_before_scroll"], (
                f"Expected menu to move closer to the top after scroll, "
                f"but before={result['top_before_scroll']}, after={result['top_after_scroll']}"
            )

            assert "#news" in result["current_url"].lower(), (
                f"Expected URL to contain '#news' after clicking News, "
                f"but got '{result['current_url']}'"
            )


    class TestForgotPasswordPage:

        def test_forgot_password(self, driver):
            page = ForgotPasswordPage(driver, "https://the-internet.herokuapp.com/forgot_password")
            page.open()

            email = "test@example.com"

            assert page.get_title() == "Forgot Password", (
                f"Expected page title 'Forgot Password', but got '{page.get_title()}'"
            )

            result = page.submit_email(email)

            assert result["entered_email"] == email, (
                f"Expected entered email '{email}', but got '{result['entered_email']}'"
            )

            assert result["result_header"] == "Internal Server Error", (
                f"Expected result header 'Internal Server Error', but got '{result['result_header']}'"
            )
            

    class TestLoginPage:

        def test_login_success(self, driver):
            page = LoginPage(driver, "https://the-internet.herokuapp.com/login")
            page.open()

            assert page.get_title() == "Login Page", (
                f"Expected page title 'Login Page', but got '{page.get_title()}'"
            )

            result = page.successful_login("tomsmith", "SuperSecretPassword!")

            assert "/secure" in result["current_url"], (
                f"Expected URL to contain '/secure', but got '{result['current_url']}'"
            )

            assert result["secure_area_title"] == "Secure Area", (
                f"Expected secure area title 'Secure Area', but got '{result['secure_area_title']}'"
            )

            assert "You logged into a secure area!" in result["flash_message"], (
                f"Expected success flash message, but got '{result['flash_message']}'"
            )

        def test_login_invalid_password(self, driver):
            page = LoginPage(driver, "https://the-internet.herokuapp.com/login")
            page.open()

            result = page.login("tomsmith", "wrong_password")

            assert "/login" in result["current_url"], (
                f"Expected to stay on login page, but got '{result['current_url']}'"
            )

            assert "Your password is invalid!" in result["flash_message"], (
                f"Expected invalid password message, but got '{result['flash_message']}'"
            )
            
    class TestFramesPage:

        def test_nested_frames(self, driver):
            page = FramesPage(driver, "https://the-internet.herokuapp.com/frames")
            page.open()

            assert page.get_title() == "Frames", (
                f"Expected page title 'Frames', but got '{page.get_title()}'"
            )

            assert page.get_frame_links_text() == ["Nested Frames", "iFrame"], (
                f"Expected links ['Nested Frames', 'iFrame'], but got {page.get_frame_links_text()}"
            )

            result = page.get_nested_frames_text()

            assert result == {
                "left": "LEFT",
                "middle": "MIDDLE",
                "right": "RIGHT",
                "bottom": "BOTTOM",
            }, f"Expected nested frame texts to match, but got {result}"

        def test_iframe_editor(self, driver):
            page = FramesPage(driver, "https://the-internet.herokuapp.com/frames")
            page.open()

            text = "Hello from Selenium"
            entered_text = page.edit_iframe_text(text)
            assert entered_text == text, (
                f"Expected iframe text '{text}', but got '{entered_text}'"
            )

