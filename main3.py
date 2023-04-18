# Username: bob-the-builder
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from noaa_sdk import NOAA
from selenium import webdriver


# Test Functions
def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

# Using the NOAA-SDK in python
def check_weather():
    noaa_object = NOAA()
    lat = 40.7314
    lon = -73.8656
    forecasts = noaa_object.points_forecast(lat, lon, type='forecastGridData')

def scrape_webpage(link: str, wait_time) -> None:
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to webpage
    driver.get('https://www.google.com')

    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)

    # Get all visible elements on the page
    visible_elements = driver.execute_script("return Array.from(document.querySelectorAll('*')).filter(e => e.offsetWidth || e.offsetHeight || e.getClientRects().length);")

    # Save visible elements to an HTML file
    with open('visible_elements.html', 'w', encoding='utf-8') as file:
        file.write('<html><body>')
        for element in visible_elements:
            file.write(driver.execute_script("return arguments[0].outerHTML;", element))
        file.write('</body></html>')

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    # Test the is_palindrome function
    try:
        assert is_palindrome(112211) == True and is_palindrome(12345) == False
        print("Test 1 passed.")
    except AssertionError:
        print("Test case 1 failed. Please correct the is_palindrome function")

    # Test the check_weather function
    try:
        check_weather()
        print("Test case 2 passed.")
    except Exception as err:
        print("Test case 2 failed.")
        print(err)


    # Test the scrape_webpage function
    try:
        wait_time = 2
        scrape_webpage('https://www.google.com', wait_time)
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed.")
        print(err)
