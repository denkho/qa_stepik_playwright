import math
import time
from playwright.sync_api import Page


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def test_lesson_2_1_step5(page: Page):
    link = 'https://suninjuly.github.io/math.html'
    page.goto(link)
    page.on("dialog", lambda x: x.message)

    x = int(page.locator('#input_value').text_content())
    page.locator('#answer').fill(calc(x))

    page.locator('#robotCheckbox').click()
    page.locator('#robotsRule').click()
    page.get_by_role('button', name='Submit').click()
    time.sleep(3)


def test_lesson_2_1_step7(page: Page):
    link = 'http://suninjuly.github.io/get_attribute.html'
    page.goto(link)
    page.on("dialog", lambda x: x.message)

    x = int(page.locator('#treasure').get_attribute('valuex'))
    page.locator('#answer').fill(calc(x))

    page.locator('#robotCheckbox').click()
    page.locator('#robotsRule').click()
    page.get_by_role('button', name='Submit').click()
    time.sleep(3)