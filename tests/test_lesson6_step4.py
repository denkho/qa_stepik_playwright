import time
from playwright.sync_api import Page

link = "http://suninjuly.github.io/simple_form_find_task.html"

def test_lesson6_step4_first(page: Page):
    page.goto(link)
    page.on("dialog", lambda x: x.message)
    input1 = page.locator('input[name="first_name"]')
    input1.fill("Ivan")
    input2 = page.locator('input[name="last_name"]')
    input2.fill("Petrov")
    input3 = page.locator('.city')
    input3.fill("Smolensk")
    input4 = page.locator("#country")
    input4.fill("Russia")
    button = page.locator("button")
    button.click()
    time.sleep(3)
