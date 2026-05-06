from selenium.webdriver.common.by import By


class ElementsPageLocators:
    TAB_AB_TEST = (By.XPATH, "//a[text()='A/B Testing']")
    CONTENT_AB_TEST = (By.XPATH, '//div[@id="content"]//p')

class AddRemoveElementsPageLocators:
    TAB_ADD_REMOVE_ELEMENT = (By.XPATH, '//div[@id="content"]//a[@href="/add_remove_elements/"]')
    BUTTON_ADD_ELEMENT = (By.XPATH, '//div[@id="content"]//button[@onclick="addElement()"]')
    BUTTON_REMOVE_ELEMENT = (By.XPATH, '//div[@id="content"]//div[@id="elements"]//button')

class BasicAuthPageLocators:
    CONTENT_BASIC_AUTH = (By.XPATH, '//div[@id="content"]//p')

class BrokenImagesPageLocators:
    ALL_IMAGES = (By.CSS_SELECTOR, 'div[id="content"] img')

class ChallengingDomPageLocators:
    PAGE_TITLE = (By.XPATH, '//div[@id="content"]//h3')
    BUTTONS = (By.CSS_SELECTOR, 'div[class="large-2 columns"] a')
    FIRST_ROW_EDIT_BUTTON = (By.XPATH, '(//a[@href="#edit"])[1]')
    CANVAS_RESULT = (By.CSS_SELECTOR, 'canvas[id="canvas"]')
    TABLE_ROWS = (By.CSS_SELECTOR, 'div[class="large-10 columns"] tbody tr')

class CheckboxesPageLocators:
    CHECKBOXES = (By.CSS_SELECTOR, 'input[type="checkbox"]')

class ContextMenuPageLocators:
    CONTENT_BOX = (By.CSS_SELECTOR, 'div[id="hot-spot"]')

class DigestAuthPageLocators:
    CONTENT_SUCCESS = (By.CSS_SELECTOR, 'div[id="content"] p')

class DisappearingElementsPageLocators:
    MENU_ITEMS = (By.CSS_SELECTOR, 'div[id="content"] a')

class DragAndDropPageLocators:
    DRAG_AND_DROP_ELEMENTS = (By.XPATH, '//div[@id="columns"]//div')

class DropdownPageLocators:
    DROPDOWN = (By.CSS_SELECTOR, 'select[id="dropdown"]')

class DynamicContentPageLocators:
    CONTENT_TEXTS = (By.XPATH, '//div[@id="content"]//div[@class="large-10 columns"]')

class DynamicControlsPageLocators:
    CHECKBOX = (By.CSS_SELECTOR, '#checkbox')
    REMOVE_ADD_BUTTON = (By.CSS_SELECTOR, '#checkbox-example button')
    ENABLE_DISABLE_BUTTON = (By.CSS_SELECTOR, '#input-example button')
    INPUT_FIELD = (By.CSS_SELECTOR, '#input-example input[type="text"]')
    MESSAGE = (By.ID, 'message')

class DynamicLoadingPageLocators:
    LINKS = (By.XPATH, '//div[@id="content"]//a') 
    START_BUTTON = (By.XPATH, '//div[@class="example"]//button')
    LOADING = (By.XPATH, '//div[@class="example"]//div[@id="loading"]')
    FINISHED_TEXT = (By.XPATH, '//div[@id="content"]//div[@id="finish"]')

class EntryAdPageLocators:
    MODAL = (By.XPATH, '//div[@class="modal"]')
    MODAL_TITLE = (By.XPATH, '//div[@class="modal"]//h3')
    CLOSE_BUTTON = (By.XPATH, '//div[@class="modal"]//div[@class="modal-footer"]//p')
    RESTART_AD_LINK = (By.CSS_SELECTOR, '#content #restart-ad')

class ExitIntentPageLocators:
    MODAL = (By.XPATH, '//div[@class="modal"]')
    MODAL_TITLE = (By.XPATH, '//div[@class="modal"]//div[@class="modal-title"]')
    CLOSE_BUTTON = (By.XPATH, '//div[@class="modal"]//div[@class="modal-footer"]//p')
    HEADER_BODY_TEXT = (By.XPATH, '//div[@id="content"]//div[@class="example"]//h3')

class DownloadPageLocators:
    FILE_LINKS = (By.CSS_SELECTOR, ".example a")

    @staticmethod
    def file_link_by_name(file_name):
        return (By.LINK_TEXT, file_name)
    
class UploadPageLocators:
    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    SUCCESS_HEADER = (By.TAG_NAME, "h3")
    UPLOADED_FILE_NAME = (By.ID, "uploaded-files")

class FloatingMenuPageLocators:
    MENU = (By.ID, "menu")
    MENU_ITEMS = (By.CSS_SELECTOR, "#menu a")

    @staticmethod
    def menu_item_by_text(item_text):
        return (By.XPATH, f"//div[@id='menu']//a[normalize-space()='{item_text}']")
    
class ForgotPasswordPageLocators:
    TITLE = (By.TAG_NAME, "h2")
    EMAIL_INPUT = (By.ID, "email")
    RETRIEVE_PASSWORD_BUTTON = (By.ID, "form_submit")
    RESULT_HEADER = (By.TAG_NAME, "h1")

class LoginPageLocators:
    TITLE = (By.TAG_NAME, "h2")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    SECURE_AREA_TITLE = (By.TAG_NAME, "h2")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")

class FramesPageLocators:
    TITLE = (By.TAG_NAME, "h3")
    FRAME_LINKS = (By.CSS_SELECTOR, ".example a")
    NESTED_FRAMES_LINK = (By.LINK_TEXT, "Nested Frames")
    IFRAME_LINK = (By.LINK_TEXT, "iFrame")

    FRAME_TOP = (By.NAME, "frame-top")
    FRAME_LEFT = (By.NAME, "frame-left")
    FRAME_MIDDLE = (By.NAME, "frame-middle")
    FRAME_RIGHT = (By.NAME, "frame-right")
    FRAME_BOTTOM = (By.NAME, "frame-bottom")
    FRAME_BODY = (By.TAG_NAME, "body")

    IFRAME = (By.ID, "mce_0_ifr")
    EDITOR_BODY = (By.ID, "tinymce")
