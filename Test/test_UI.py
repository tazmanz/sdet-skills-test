import pytest
from playwright.sync_api import Page, expect
from Test.Page.submit import SubmitPage

def test_has_form(page: Page):
    page.goto("file:///C:/Users/tazma/OneDrive/Documents2/GitHub/sdet-skills-test/simple-ts-ui/index.html")
    submit_form = page.get_by_role("form")
    # Expect a title "to contain" a substring.
    expect(submit_form).to_have_id("nameForm")

def test_submit_name(page: Page):
    submitName = SubmitPage(page)
    submitName.inputName("tazmanzm")
    expect(submitName.getResponseMessage()).to_contain_text("Name submitted successfully: tazmanzm")
