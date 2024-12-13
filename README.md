# Overview

We have a simple web application that consists of two primary components:

    A Front-End UI: A web page where a user can input their name and submit it.
        When the user enters a name and clicks the submit button, the name is sent to a Python-based REST API.
        The page then displays a confirmation message with the submitted name.

    A Python REST API: A simple backend built using Flask that accepts POST requests at the endpoint /submit-name. This API accepts a JSON payload with a name field, processes it, and responds with a confirmation message, e.g., { "message": "Name submitted successfully: <name>" }.

Your task is to demonstrate how you would go about testing both the UI and the API. Please walk us through your approach for the following:
1. Testing the UI

    What type of tests would you write to ensure the user can interact with the form correctly?
    How would you handle validation of the form submission (e.g., ensuring the name field is not empty)?
    How would you validate the proper display of the confirmation message after submitting the form?

2. Testing the Python REST API

    What kind of unit or integration tests would you write for the /submit-name endpoint?
    How would you handle edge cases such as missing or invalid data (e.g., submitting an empty name or non-string values)?
    How would you simulate the interaction between the UI and the API in your tests?

Expected Skills to Assess:

    UI Testing: Familiarity with tools like Selenium, Cypress, or Playwright for testing the web page, form validation, and dynamic content rendering.
    API Testing: Understanding of API testing frameworks such as pytest, requests, or Postman, and experience writing tests for REST endpoints.
    End-to-End Testing: Knowledge of how to combine both UI and API testing to simulate real-world scenarios, such as testing form submissions that hit the API.

This prompt is designed to assess the candidate’s experience and understanding of testing methodologies for both front-end and back-end components, as well as their ability to think critically about edge cases and end-to-end workflows.
