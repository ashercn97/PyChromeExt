// Utility functions for content script
function readFromElement(selector) {
    return document.querySelector(selector).innerText;
}

function writeToElement(selector, text) {
    document.querySelector(selector).innerText = text;
}

function clickElement(selector) {
    document.querySelector(selector).click();
}

function setElementValue(selector, value) {
    document.querySelector(selector).value = value;
}

function fetchAndProcessData(url, processData) {
    fetch(url)
        .then(response => response.json())
        .then(data => processData(data));
}

function console_log(message) {
    console.log(message);
}