from playwright.sync_api import Page

class SubmitPage:
    def __init__(self, page):
        self.page = page
        self.submitForm = page.get_by_role("form")
        self.inputName = page.get_by_role("input")
        self.submitButton = page.get_by_role("button")
        self.responseMessage = page.get_by_id("responseMessage")
        self.errorMessage = page.get_by_id("errorMessage")

    def inputName(self,input_name):
        self.inputName.fill(input_name)
        self.submitButton.click()

    def getErrorMessage(self):
        return self.errorMessage.text()

    def getResponseMessage(self):
        return self.responseMessage.text()