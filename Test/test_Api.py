import pytest
from typing import Generator
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:

    request_context = playwright.request.new_context(
        base_url="http://127.0.0.1:5000")
    yield request_context
    request_context.dispose()

def test_should_return_success(api_request_context: APIRequestContext) -> None:
    data = {
        {"input_name": "tazmanz"}
            }
    name_submit = api_request_context.post(
        f"/submit-name", data=data
    )
    assert name_submit.ok
    name_submit_response = name_submit.json()
    assert name_submit_response["message"] == "Name submitted successfully: tazmanzm"

def test_should_return_fail(api_request_context: APIRequestContext) -> None:
    data = {
        {"name": "tazmanz"}
            }
    name_submit = api_request_context.post(
        f"/submit-name", data=data
    )
    assert name_submit.ok
    name_submit_response = name_submit.json()
    assert name_submit_response["error"] == "Name is required"

def test_should_return_valueError(api_request_context: APIRequestContext) -> None:
    data = {
        {"name": "Waldo"}
            }
    name_submit = api_request_context.post(
        f"/submit-name", data=data
    )
    assert name_submit.ok
