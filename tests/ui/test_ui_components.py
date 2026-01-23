import time

import pytest
from pages.ui_components_page import UiComponents
# ==========================================
# POSITIVE SCENARIOS
# ==========================================
@pytest.mark.parametrize('element', UiComponents.DROP_DOWN_DATA)
def test_open_accordian_block(open_main_page,ui_page,element):
    ui_page.click_on_element_btn(element['Locator'])
    ui_page.check_found_text(element['content_locator'],element['text'])

def test_successful_form_submission(open_main_page,ui_page):
    ui_page.fill_input(ui_page.WIZARD_NAME,'Оля')
    ui_page.fill_input(ui_page.WIZARD_LAST_NAME,'Сергеева')
    ui_page.click_on_element_btn(ui_page.BTN_NEXT_PAGE_1)
    ui_page.fill_input(ui_page.WIZARD_EMAIL,'test121@gmail.com')
    ui_page.fill_input(ui_page.WIZARD_PHONE,'8800-555-3535')
    ui_page.click_on_element_btn(ui_page.BTN_NEXT_PAGE_2)
    for locator,value in ui_page.EXPECTED.items():
        ui_page.check_exact_text(locator,value)
    ui_page.click_on_element_btn(ui_page.BTN_SUBMIT)
    ui_page.check_found_text(ui_page.WIZARD_FORM_WITH_RESULT,'Форма успешно отправлена!')

def test_click_count_increases(open_main_page,ui_page):
    ui_page.click_on_element_btn(ui_page.SHADOW_BTN)
    ui_page.click_on_element_btn(ui_page.SHADOW_BTN)
    ui_page.check_found_text(ui_page.SHADOW_HOST,'2')

def test_counter_default_value_is_zero(open_main_page,ui_page):
    ui_page.check_found_text(ui_page.SHADOW_HOST,'0')

def test_breadcrumbs_navigation_forward_finds_product(open_main_page,ui_page):
    ui_page.click_on_element_btn(ui_page.NAVIGATE_TO_PRODUCT_BTN)
    ui_page.check_found_text(ui_page.PAGE_CONTENT_RESULT, 'Каталог товаров')
    ui_page.click_on_element_btn(ui_page.NAVIGATE_TO_CATEGORY_BTN)
    ui_page.check_found_text(ui_page.PAGE_CONTENT_RESULT, 'Категория: Электроника')
    ui_page.click_on_element_btn(ui_page.NAVIGATE_TO_ITEM_BTN)
    ui_page.check_found_text(ui_page.PAGE_CONTENT_RESULT, 'Товар: Ноутбук')

def test_autocomplete_suggestions(open_main_page,ui_page):
    ui_page.fill_input(ui_page.RELATIVE_BTN,'Pl')
    ui_page.check_found_text(ui_page.TEXT_IN_DROPDOWN_AUTO,'Playwright')

def test_copy_text_in_buffer(open_main_page,ui_page):
    ui_page.click_on_element_btn(ui_page.COPY_IN_BUFFER_BTN)
    ui_page.check_found_text(ui_page.COPY_INFO_BTN,'Скопировано в буфер обмена!')
    ui_page.check_found_text(ui_page.COPY_RESULT_BTN,'Скопировано!')

@pytest.mark.parametrize('element',UiComponents.TABS_EXPECTED_DATA, ids=[e['text'] for e in UiComponents.TABS_EXPECTED_DATA] )
def test_switch_tabs(open_main_page,ui_page,element):
    ui_page.click_on_element_btn(element['locator'])
    ui_page.check_found_text(element['locator_content'],element['text'])

def test_change_format_text_on_bolt(open_main_page,ui_page):
    ui_page.select_all_text(ui_page.FORM_WYSIWYG_EDITOR)
    ui_page.click_on_element_btn(ui_page.FORMAT_TEXT_BOLT_BTN)
    ui_page.check_text_wrapped_in_tag('b', 'Начните печатать здесь... Используйте кнопки выше для форматирования текста.')

def test_change_format_text_on_italic(open_main_page,ui_page):
    ui_page.select_all_text(ui_page.FORM_WYSIWYG_EDITOR)
    ui_page.click_on_element_btn(ui_page.FORMAT_TEXT_ITALIC_BTN)
    ui_page.check_text_wrapped_in_tag('i','Начните печатать здесь... Используйте кнопки выше для форматирования текста.')

def test_change_format_text_on_underline(open_main_page,ui_page):
    ui_page.select_all_text(ui_page.FORM_WYSIWYG_EDITOR)
    ui_page.click_on_element_btn(ui_page.FORMAT_TEXT_UNDERLINE)
    ui_page.check_text_wrapped_in_tag('u','Начните печатать здесь... Используйте кнопки выше для форматирования текста.')

# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
def test_back_navigation_from_last_step(open_main_page, ui_page):
    ui_page.fill_input(ui_page.WIZARD_NAME, 'Оля')
    ui_page.fill_input(ui_page.WIZARD_LAST_NAME, 'Сергеева')
    ui_page.click_on_element_btn(ui_page.BTN_NEXT_PAGE_1)
    ui_page.fill_input(ui_page.WIZARD_EMAIL, 'test121@gmail.com')
    ui_page.fill_input(ui_page.WIZARD_PHONE, '8800-555-3535')
    ui_page.click_on_element_btn(ui_page.BTN_NEXT_PAGE_2)
    ui_page.click_on_element_btn(ui_page.BTN_BACK_PAGE_3)
    ui_page.click_on_element_btn(ui_page.BTN_BACK_PAGE_2)
    ui_page.check_input_value(ui_page.WIZARD_NAME,'Оля')

def test_check_empty_input(open_main_page,ui_page):
    ui_page.delete_all_text(ui_page.FORM_WYSIWYG_EDITOR)
    ui_page.check_editor_is_empty(ui_page.FORM_WYSIWYG_EDITOR)


