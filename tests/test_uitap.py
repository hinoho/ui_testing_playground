#запустить 15 раз
from playwright.sync_api import expect


def test_dynamic_id(open_page_fixture):
    page = open_page_fixture('/dynamicid').click('button.btn-primary')

def test_class_attr(open_page_fixture):
    open_page_fixture('/classattr').click('button.btn-primary')

def test_hidden_layers(open_page_fixture):
    page = open_page_fixture('/hiddenlayers')
    page.click('#greenButton')
    page.click('#blueButton')
    expect(page.locator('#greenButton')).not_to_be_focused()

def test_load_delay(open_page_fixture):
    page = open_page_fixture('/')
    page.click('a[href="/loaddelay"]')
    page.wait_for_selector('button.btn-primary')

def test_ajax(open_page_fixture):
    page = open_page_fixture('/ajax')
    page.click('#ajaxButton')
    page.expect_request_finished(lambda request: request.url == 'http://www.uitestingplayground.com/ajaxdata')
    assert page.locator('.bg-success').inner_text() == 'Data loaded with AJAX get request.'

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
    button = page.locator("#hidingButton")
    button.scroll_into_view_if_needed()
    button.click()

def test_dynamic_table(open_page_fixture):
    page = open_page_fixture('/dynamictable')
    column_id = 0
    page.screenshot(path='1.png')
    for column in page.locator('[role="columnheader"]').all():
        if column.inner_text() == 'CPU':
            break
        column_id += 1
    for row in page.locator('[role="row"]').all():
        if row.locator(':first-child').inner_text() == 'Chrome':
            result = row.locator(f':nth-child({column_id+1})').inner_text()
    assert page.locator('.bg-warning').inner_text() == f'Chrome CPU: {result}'

def test_verify_text(open_page_fixture):
    page = open_page_fixture('/verifytext')
    assert page.locator('//span[normalize-space()="Welcome UserName!"]').is_visible()

def test_progressbar(open_page_fixture):
    page = open_page_fixture('/progressbar')
    page.click('#startButton')
    page.wait_for_selector('#progressBar[aria-valuenow="75"]')
    page.click('#stopButton')
    assert 'Result: 0' in  page.locator('#result').inner_text()

def test_visibility(open_page_fixture):
    page = open_page_fixture('/visibility')
    # ???
    page.click('#hideButton')
    assert not page.locator('#removedButton').is_visible()
    assert not page.locator('#zeroWidthButton').is_visible()
    assert not page.locator('#overlappedButton').is_visible()

def test_sample_app(open_page_fixture):
    page = open_page_fixture('/sampleapp')
    page.fill('input[name="UserName"]', 'User')
    page.fill('input[name="Password"]', 'pwd')
    page.click('button.btn-primary')
    assert page.locator('#loginstatus').inner_text() == 'Welcome, User!'

def test_mouseover(open_page_fixture):
    page = open_page_fixture('/mouseover')
    link_locator = page.get_by_text('Click me')
    link_locator.click()
    link_locator.click()
    assert page.locator('#clickCount').inner_text() == '2'

def test_non_breaking_space(open_page_fixture):
    page = open_page_fixture('/nbsp')
    page.click("button:text('My\xa0Button')")

def test_overlapped(open_page_fixture):
    page = open_page_fixture('/overlapped')
    page.fill('#name', 'Name')

def test_shadow_dom(open_page_fixture):
    #???
    page = open_page_fixture('/shadowdom')
    page.context.grant_permissions(['clipboard-read'])
    page.click('#buttonGenerate')
    page.click('#buttonCopy')
    clipboard_text = page.evaluate("navigator.clipboard.readText()")
    input_text = page.locator('#editField').inner_text()
    assert clipboard_text == input_text

def test_alerts(open_page_fixture):
    page = open_page_fixture('/alerts')
    page.once("dialog", alert_dialog)
    page.click('#alertButton')

    page.once("dialog", confirm_dialog)
    page.click('#confirmButton')

    page.once("dialog", prompt_dialog)
    page.click('#promptButton')

def alert_dialog(dialog):
    assert dialog.message == 'Today is a working day.\nOr less likely a holiday.'
    dialog.accept()

def confirm_dialog(dialog):
    assert dialog.message == 'Today is Friday.\nDo you agree?'
    dialog.accept()

def prompt_dialog(dialog):
    assert dialog.message == 'Choose "cats" or \'dogs\'.\nEnter your value:'
    dialog.accept('dogs')

def test_animation(open_page_fixture):
    page = open_page_fixture('/animation')
    page.click('#animationButton')
    page.wait_for_selector('#movingTarget.spin', state='hidden')
    page.click('#movingTarget')
    assert page.locator('#opstatus').inner_text() == "Moving Target clicked. It's class name is 'btn btn-primary'"

def test_disabled_input(open_page_fixture):
    page = open_page_fixture('/disabledinput')
    page.click('#enableButton')
    page.wait_for_selector('input[disables]', state='hidden')
    page.fill('input', '1234')
    page.keyboard.press("Enter")

    assert page.locator('#opstatus').inner_text() == 'Value changed to: 1234'

def test_auto_wait(open_page_fixture):
    page = open_page_fixture('/autowait')
