def test_dynamic_id(open_page_fixture):
    page = open_page_fixture('/dynamicid').click('button.btn-primary')

def test_class_attr(open_page_fixture):
    open_page_fixture('/classattr').click('button.btn-primary')

def test_hidden_layers(open_page_fixture):
    page = open_page_fixture('/hiddenlayers')

def test_load_delay(open_page_fixture):
    page = open_page_fixture('/')
    page.click('a[href="/loaddelay"]')
    page.wait_for_selector('button.btn-primary')

def test_ajax(open_page_fixture):
    page = open_page_fixture('/ajax')

def test_client_delay(open_page_fixture):
    page = open_page_fixture('/clientdelay')
    page.click('#ajaxButton')
    page.wait_for_selector('p.bg-success')

def test_click(open_page_fixture):
    page = open_page_fixture('/click')
    page.click('#badButton')
    assert page.locator('#badButton').get_attribute('class') == 'btn btn-success'

def test_text_input(open_page_fixture):
    page = open_page_fixture('/textinput')
    page.fill('#newButtonName', '1234')
    page.click('#updatingButton')
    assert page.locator('#updatingButton').inner_text() == '1234'

def test_scrollbars(open_page_fixture):
    page = open_page_fixture('/scrollbars')

def test_dynamic_table(open_page_fixture):
    page = open_page_fixture('/dynamictable')

def test_verify_text(open_page_fixture):
    page = open_page_fixture('/verifytext')

def test_progressbar(open_page_fixture):
    page = open_page_fixture('/progressbar')

def test_visibility(open_page_fixture):
    page = open_page_fixture('/visibility')

def test_sample_app(open_page_fixture):
    page = open_page_fixture('/sampleapp')

def test_mouseover(open_page_fixture):
    page = open_page_fixture('/mouseover')

def test_non_breaking_space(open_page_fixture):
    page = open_page_fixture('/nbsp')

def test_overlapped(open_page_fixture):
    page = open_page_fixture('/overlapped')

def test_shadow_dom(open_page_fixture):
    page = open_page_fixture('/shadowdom')

def test_alerts(open_page_fixture):
    page = open_page_fixture('/alerts')

def test_upload(open_page_fixture):
    page = open_page_fixture('/upload')

def test_animation(open_page_fixture):
    page = open_page_fixture('/animation')

def test_disabled_input(open_page_fixture):
    page = open_page_fixture('/disabledinput')
    page.click('#enableButton')
    page.wait_for_selector('input[disables]', state='hidden')
    page.fill('input', '1234')
    page.keyboard.press("Enter")

    assert page.locator('#opstatus').inner_text() == 'Value changed to: 1234'

def test_auto_wait(open_page_fixture):
    page = open_page_fixture('/autowait')
