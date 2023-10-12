import os 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from PIL import ImageColor

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.dulux.co.uk/en/colour-details#tabId=item0")
driver.implicitly_wait(5)

try: 
    cookie = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie.click()
except:
    pass

colors_sub_dict = []

palette = driver.find_elements(By.CSS_SELECTOR, ".a20-color-box")
color = 0



for i in range(len(palette)):
    current_color = ""

    if palette[i].is_displayed:
        print(palette[i].get_attribute("data-id"))
        current_color = palette[i].get_attribute("data-id")
        palette[i].click()

    colors = driver.find_elements(By.CSS_SELECTOR, "div.color-card.js-color-card")
    color_names = driver.find_element(By.CSS_SELECTOR, "span.color-card-label.body-copy-s")

    WebDriverWait(driver, 10).until(
         EC.visibility_of((colors[i]))
    )
    while colors[i].is_displayed() and len(colors[color].text) > 0:
            hex_color = colors[color].get_attribute("data-hex")
            print(hex_color)
            RGB = ImageColor.getcolor(hex_color, "RGB")

            print(colors[color].text)
            colors_sub_dict.append([current_color, colors[color].text, colors[color].get_attribute("data-hex"), RGB[0], RGB[1], RGB[2]])
            color += 1
    print(colors_sub_dict)

    color_mixed = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/section/div[2]/div/div/div[1]/div[3]/ul/li[2]/button')
    color_mixed.click()
    color = 0

    color_long_list = driver.find_element(By.CLASS_NAME, "tab-content.js-tab-content.is-active")
    color_long_list_specific = color_long_list.find_elements(By.CLASS_NAME, "color-card.js-color-card")

    try: 
        while color_long_list_specific[i].is_displayed() and len(color_long_list_specific[color].text) > 0:
            print(color_long_list_specific[color].get_attribute("data-hex"))
            print(color_long_list_specific[color].text)
            color += 1
    except:
         pass
    
    palette = driver.find_elements(By.CSS_SELECTOR, ".a20-color-box")
    colors = driver.find_elements(By.CSS_SELECTOR, "div.color-card.js-color-card")
    color_names = driver.find_element(By.CSS_SELECTOR, "span.color-card-label.body-copy-s")
    color = 0


import pandas as pd

df = pd.DataFrame(colors_sub_dict)
df.to_csv("file2.csv", index=False, header=False)