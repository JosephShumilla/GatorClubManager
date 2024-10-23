from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

service = ChromeService(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=service)

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
            #print(f"Element {index} HTML:", club.get_attribute('outerHTML'))
            # Extract the organization name
            club_name = club.find_element(By.XPATH, './/h2/a').text
            # Extract the organization description
            club_description = club.find_element(By.XPATH, './/p').text
            print(f"Club {club_num}:")
            print(f"Name: {club_name}")
            print(f"Description: {club_description}\n")
            print("-" * 20)
        except Exception as e:
            print(f"Error extracting data for element {club_num + 1}: {e}")

    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[text()='{pages + 1}']"))
        )
        button.click()
        print("Button clicked!")
        time.sleep(1)  # Optional: wait for the new content to load
    except Exception as e:
        print(f"Error clicking the button by XPath: {e}")


# Close the browser
driver.quit()