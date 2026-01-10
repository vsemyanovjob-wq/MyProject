import pytest
from pages.ui_components_page import UiComponents
# ==========================================
# POSITIVE SCENARIOS
# ==========================================
@pytest.mark.parametrize('element', UiComponents.DROP_DOWN_DATA)
def test_open_accordian_block(page,open_main_page,ui_page,element):
    ui_page.click_on_element_btn(element['Locator'])
    ui_page.check_found_text(element['content_locator'],element['text'])
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================