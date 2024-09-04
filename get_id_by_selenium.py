from driversetup import create_driver
from bs4 import BeautifulSoup
from messagefinder import return_msg
import time
from selenium.webdriver.common.by import By



driver = create_driver()
driver.get("https://discord.com/channels/@me")
time.sleep(10)

while True:
    driver.get("https://discord.com/channels/@me")
    time.sleep(5)
    
    new_message_button = driver.find_elements(By.XPATH,'//div[@style="opacity: 1; height: 56px; transform: scale(1);"]')
    
    for icons in new_message_button:
        msg_count = icons.find_element(By.XPATH,'//div[@class="numberBadge_df8943 base_df8943 eyebrow_df8943 baseShapeRound_df8943"]')
        icons.click()
        time.sleep(0.5)
        new_message_channels_ids = driver.current_url
        
        # Get the message content
        message_content = return_msg(new_message_channels_ids.split("/")[-1], msg_count.text.strip())
        if message_content is not None:
            print(message_content)
            
            # Open a new tab if it doesn't already exist
            if len(driver.window_handles) == 1:
                driver.execute_script("window.open('');")
                time.sleep(2)
            
            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://www.google.com/search?q="+message_content)
            time.sleep(5)
            
            # Switch back to the original tab
            driver.switch_to.window(driver.window_handles[0])
