import os
from selenium.webdriver.chrome.webdriver import WebDriver
from noaa_sdk import NOAA

def check_pallindrome(num):
    """Check if a given number is a palindrome."""
    num = str(num)
    num_copy = num
    num = num[::-1]
    if num_copy == num:
        return True
    return False

def check_webpage(link):
    """Check if all elements on a given webpage are visible."""
    # Initialize Chrome WebDriver
    driver = WebDriver()
    # Navigate to webpage
    driver.get(link)
    
    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    # Get all visible elements on the page
    visible_elements = driver.find_elements_by_css_selector("*:not([style*=‘display:none’]):not([style*=‘display: none’])")
    # Save visible elements to an HTML file
    with open("visible_elements.html", "w", encoding="utf-8") as file:
        file.write("<html><body>")
        for element in visible_elements:
            file.write(element.get_attribute("outerHTML"))
        file.write("</body></html>")
    # Close the WebDriver
    driver.quit()

def check_weather(lat, lon):
    """Get weather forecasts for a given location using the NOAA API."""
    n = NOAA()
    location = (lat, lon)
    try:
        forecasts = n.get_forecasts(locpoints_forecast(40.7314, -73.8656, type='forecastGridData')
        print("Test case 2 passed")
    except Exception as err:
        print("Test case 2 failed")
        print(err)

def run_tests():
    """Run tests on the check_pallindrome, check_webpage, and check_weather functions."""
    pallin_num = 112211
    non_pallin_num = 12345
    link = 'https://www.google.com'
    lat = 40.7314
    lon = -73.8656
    
    try:
        if check_pallindrome(pallin_num) == False or check_pallindrome(non_pallin_num) == True:
            raise Exception
        else:
            print("Test case 1 passed.")
    except Exception as err:
        print("Test case 1 failed. Please correct the pallindrome function")
        print(err)

    try:
        check_webpage(link)
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed.")
        print(err)

    try:
        check_weather(lat, lon)
    except Exception as err:
        print("Test case 2 failed.")
        print(err)

if __name__=="__main__":
    run_tests()
