# This code needs your help in removing code smells and fixing the code functionalities such that all test cases pass. 
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from noaa_sdk import NOAA # NOAA-SDK python

# Global Variables
n = NOAA()
link = 'https://www.google.com'
pallin_num = 112211
non_pallin_num = 12345
c = 0

