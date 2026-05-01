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
