from noaa_sdk import NOAA  # NOAA-SDK python
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# Test Functions


def check_palindrome(num):
    return str(num) == str(num)[::-1]


def check_webpage(link: str) -> None:
    # Initialize Chrome WebDriver
    driver: Chrome = Chrome()
    # Navigate to webpage
    driver.get(link)

    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    # Get all visible elements on the page
    visible_elements = driver.find_elements(
        By.CSS_SELECTOR, "*[style]:not([style*='display:none']):not([style*='display: none'])")
    # Save visible elements to an HTML file
    with open("visible_elements.html", "w", encoding="utf-8") as file:
        file.write("<html><body>")
        for element in visible_elements:
            file.write(element.get_attribute("outerHTML"))
        file.write("</body></html>")
    # Close the WebDriver
    driver.quit()

# Using the NOAA-SDK in python


def check_weather():
    n = NOAA()
    lat = 40.7314
    lon = -73.8656
    try:
        forecasts = n.get_forecasts(coordinates=(lat, lon))
    except Exception as err:
        print("Error occurred while checking weather:", err)


if __name__ == "__main__":
    link = 'https://www.google.com'
    pallin_num = 112211
    non_pallin_num = 12345
    tests_passed = 0

    try:  # Check the pallindrome function
        if not check_palindrome(pallin_num) or check_palindrome(non_pallin_num):
            raise Exception
        else:
            print("Test 1 passed.")
            tests_passed += 1
    except Exception as err:
        print("Test case 1 failed. Please correct the pallindrome function")
        print(err)

    try:  # Check the weather function
        check_weather()
        tests_passed += 1
        print("Test case 2 passed.")
    except Exception as err:
        print("Test case 2 failed.")
        print(err)

    try:  # Check the webpage function
        check_webpage(link)
        tests_passed += 1
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed.")
        print(err)

    print(f"Total {tests_passed}/3 tests passed")
