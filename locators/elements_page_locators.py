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

class ContextMenuPageLocators:
    CONTENT_BOX = (By.CSS_SELECTOR, 'div[id="hot-spot"]')