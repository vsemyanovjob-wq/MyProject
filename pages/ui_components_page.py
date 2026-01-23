from .base_page import BasePage

class UiComponents(BasePage):
    # Локаторы Accordion / Collapsible
    DROP_DOWN_DATA = [
        {'name': 'Selenium','Locator': '[onclick="toggleAccordion(\'accordion1\')"]','content_locator':'#accordion1','text': 'Selenium — это инструмент для'},
        {'name': 'Playwright', 'Locator': '[onclick="toggleAccordion(\'accordion2\')"]','content_locator':'#accordion2','text': 'Playwright — современный фреймворк'},
        {'name': 'Cypress', 'Locator': '[onclick="toggleAccordion(\'accordion3\')"]','content_locator':'#accordion3','text': 'Cypress — это fast, easy и reliable testing'},
        {'name': 'Appium', 'Locator': '[onclick="toggleAccordion(\'accordion4\')"]','content_locator':'#accordion4','text': 'Appium — это open-source инструмент'}
    ]

    # Локаторы Multi-step Forms / Wizard
    WIZARD_NAME = '#wizardFirstName'
    WIZARD_LAST_NAME = '#wizardLastName'
    WIZARD_EMAIL = '#wizardEmail'
    WIZARD_PHONE = '#wizardPhone'
    WIZARD_RESULT = '#wizardStep3'
    WIZARD_FORM_WITH_RESULT = '#wizardSuccess'
    BTN_NEXT_PAGE_1 = 'button[onclick="nextWizardStep(2)"]'
    BTN_BACK_PAGE_2 = 'button[onclick="prevWizardStep(1)"]'
    BTN_NEXT_PAGE_2 = 'button[onclick="nextWizardStep(3)"]'
    BTN_BACK_PAGE_3 = 'button[onclick="prevWizardStep(2)"]'
    BTN_SUBMIT = 'button[onclick="submitWizard()"]'
    EXPECTED = {
        "#confirmFirstName": "Оля",
        "#confirmLastName": "Сергеева",
        "#confirmEmail": "test121@gmail.com",
        "#confirmPhone": "8800-555-3535"
    }

    # Локаторы Shadow DOM
    SHADOW_HOST = '#shadowHost'
    SHADOW_BTN = '#shadowButton'
    CLICK_COUNTER = '#shadowClickCount'

    # Локаторы Breadcrumbs
    NAVIGATE_TO_PRODUCT_BTN = "button[onclick=\"navigateBreadcrumb('products')\"]"
    NAVIGATE_TO_CATEGORY_BTN = "button[onclick=\"navigateBreadcrumb('category')\"]"
    NAVIGATE_TO_ITEM_BTN = "button[onclick=\"navigateBreadcrumb('item')\"]"
    PAGE_CONTENT_RESULT = '#pageContent'

    # Локаторы Autocomplete / Typeahead
    RELATIVE_BTN = '#autocompleteInput'
    TEXT_IN_DROPDOWN_AUTO = '#autocompleteDropdown'

    # Локаторы Copy to Clipboard
    COPY_IN_BUFFER_BTN = '#copyButton'
    COPY_RESULT_BTN = '#copyText'
    COPY_INFO_BTN = '#copySuccess'

    # Локаторы Tabs / Tabbed Interface
    TABS_EXPECTED_DATA = [
        {'locator': '#tab-javascript', 'text': 'JavaScript для автоматизации','locator_content': '#content-javascript'},
        {'locator': '#tab-java', 'text': 'Java для автоматизации', 'locator_content': '#content-java'},
        {'locator': '#tab-csharp', 'text': 'C# для автоматизации','locator_content': '#content-csharp'},
        {'locator': '#tab-python', 'text': 'Python для автоматизации','locator_content': '#content-python'}
    ]

    # Локаторы WYSIWYG Editor
    FORMAT_TEXT_BOLT_BTN = 'button[onclick="formatText(\'bold\')"]'
    FORMAT_TEXT_ITALIC_BTN = 'button[onclick="formatText(\'italic\')"]'
    FORMAT_TEXT_UNDERLINE = 'button[onclick="formatText(\'underline\')"]'
    DELETE_TEXT_BTN = 'button[onclick="clearEditor()"]'
    FORM_WYSIWYG_EDITOR = '#wysiwygEditor'