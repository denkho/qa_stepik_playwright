import time
from playwright.sync_api import Page

link = "http://suninjuly.github.io/huge_form.html"

def test_lesson6_step4_first(page: Page):
    page.goto(link)
    page.on("dialog", lambda x: x.message)
    inputs = page.locator("input").all()
    for i in inputs:
        i.fill('my')
    page.get_by_role('button').click()
    time.sleep(3)
