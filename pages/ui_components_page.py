from .base_page import BasePage

class UiComponents(BasePage):
    # Локаторы Accordion / Collapsible
    DROP_DOWN_DATA = [
        {'name': 'Selenium','Locator': '[onclick="toggleAccordion(\'accordion1\')"]','content_locator':'#accordion1','text': 'Selenium — это инструмент для'},
        {'name': 'Playwright', 'Locator': '[onclick="toggleAccordion(\'accordion2\')"]','content_locator':'#accordion2','text': 'Playwright — современный фреймворк'},
        {'name': 'Cypress', 'Locator': '[onclick="toggleAccordion(\'accordion3\')"]','content_locator':'#accordion3','text': 'Cypress — это fast, easy и reliable testing'},
        {'name': 'Appium', 'Locator': '[onclick="toggleAccordion(\'accordion4\')"]','content_locator':'#accordion4','text': 'Appium — это open-source инструмент'}
    ]