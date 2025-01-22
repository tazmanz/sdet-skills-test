"use strict";
// app.ts
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// Select DOM elements
const nameForm = document.getElementById("nameForm");
const nameInput = document.getElementById("nameInput");
const responseMessage = document.getElementById("responseMessage");
const errorMessage = document.getElementById("errorMessage");
// Function to handle form submission
nameForm === null || nameForm === void 0 ? void 0 : nameForm.addEventListener("submit", (event) => __awaiter(void 0, void 0, void 0, function* () {
    event.preventDefault();
    // Reset messages
    responseMessage.textContent = "";
    errorMessage.textContent = "";
    const name = nameInput.value.trim();
    if (!name) {
        errorMessage.textContent = "Name is required.";
        return;
    }
    try {
        // Make POST request to Flask API
        const response = yield fetch("http://127.0.0.1:5000/submit-name", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ "input_name":name }),
        });
        // Handle successful response
        if (response.ok) {
            const data = yield response.json();
            responseMessage.textContent = data.message;
            responseMessage.style.color = "green";
        }
        else {
            // Handle errors from the API
            const data = yield response.json();
            errorMessage.textContent = data.error || "An unexpected error occurred.";
            errorMessage.style.color = "red";
        }
    }
    catch (error) {
        // Handle network or other errors
        errorMessage.textContent = "There was an error communicating with the server.";
        errorMessage.style.color = "red";
    }
}));
