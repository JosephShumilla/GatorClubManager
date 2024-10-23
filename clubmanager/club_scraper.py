import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# This script is just for populating the database. If you want to update the database clear what is currently in there
# and run this again.

# Connects to the SQL Database
def connnect_database():
    database = sqlite3.connect('db.sqlite3')
    return database

# Function that inserts clubs into the database
def insert_club(database, club_name, club_desc):
    cursor = database.cursor()
    cursor.execute('INSERT INTO Club_Database (club_name, club_desc) VALUES (?, ?)', (club_name, club_desc))
    database.commit()


# setup for Selenium
service = ChromeService(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=service)

# connect database
database = connnect_database()
try:
    # Navigate to the GatorConnect organizations page
    driver.get("https://orgs.studentinvolvement.ufl.edu/Organizations")

    time.sleep(5)

    # Extract the names and descriptions
    pages = 0
    club_num = 0
    for i in range(95):
        pages += 1
        # Find the club elements
        elements = driver.find_elements(By.XPATH,'//*[@id="searchresults"]//div[contains(@ng-repeat, "org in filteredOrganizations")]')
        for club in elements:
            club_num += 1
            try:
                # debug statement: print(f"Element {index} HTML:", club.get_attribute('outerHTML'))
                # Extract the organization name
                club_name = club.find_element(By.XPATH, './/h2/a').text
                # Extract the organization description
                club_description = club.find_element(By.XPATH, './/p').text
                print(f"Club {club_num}:")
                print(f"Name: {club_name}")
                print(f"Description: {club_description}\n")
                print("-" * 20)

                insert_club(database,club_name,club_description)
            except Exception as e:
                print(f"Error extracting data for element {club_num + 1}: {e}")
        try:
            next_page_number = club_num // 10 + 1  # Adjust based on how many clubs are displayed per page
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[text()='{next_page_number}']"))
            )
            button.click()
            print("Button clicked!")
            time.sleep(1)
        except Exception as e:
            print(f"Error clicking the button by XPath: {e}")
finally:
    # Close the Database
    database.close()
    # Close the Browser
    driver.quit()