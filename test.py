from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Specify the URL of the website
url = "https://fcainfoweb.nic.in/reports/report_menu_web.aspx"

# Initialize a web driver (assuming ChromeDriver is in your PATH)
driver = webdriver.Chrome()

# Open the website in the web driver
driver.get(url)

# Wait for the "Price report" button to load
price_report_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Price report']")))

# Click on the "Price report" button
price_report_button.click()

# Wait for the dropdown element to load
select_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "rptType")))

# Select the "Daily Prices" option from the dropdown
select_dropdown.click()
select_dropdown.send_keys(Keys.ARROW_DOWN)
select_dropdown.send_keys(Keys.ENTER)

# Wait for the date input field to load
date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "txtDate")))

# Select the desired date from the calendar (e.g., "01/02/2020")
selected_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@onclick,'setDate') and contains(text(),'01/02/2020')]")))
selected_date.click()

# Submit the form
driver.find_element(By.NAME, "BtnSubmit").click()

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dvData")))

# Now, you can scrape the data from the resulting page
# You can use BeautifulSoup or other techniques to parse the data

# For demonstration purposes, let's print the text content of the page
print(driver.find_element(By.ID, "dvData").to_string())

# Close the web driver
driver.quit()
