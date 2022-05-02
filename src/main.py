from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://lost-ark.maxroll.gg/rapport'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\Users\Chali\Desktop\Rapport\src\drivers\chromedriver.exe", options=options)
driver.get(url)

rapport_list = driver.find_elements(By.CLASS_NAME, 'lap-npc-box')
for rapport in rapport_list:
    name = rapport.find_element(By.CLASS_NAME, 'lap-rapport-name').text
    zone = rapport.find_element(By.CLASS_NAME, 'lap-rapport-zone').text

    btn_list = rapport.find_elements(By.CLASS_NAME, 'lap-button')
    for btn in btn_list:
        if btn.text == 'Actions':
            driver.execute_script('arguments[0].click();', btn)

    action_name = rapport.find_elements(By.CLASS_NAME, 'lap-action-name')
    action_points = rapport.find_elements(By.CLASS_NAME, 'lap-action-points')

    print(name)
        
    check = False
    action_count = 0
    for emote, points in zip(action_name, action_points):
        points = points.text
        points = points[:points.find(' ')]
        emote = emote.text

        if int(points) == 450 or int(points) == 420:
            check = True

        if check == False:
            action_count = action_count + 1
        
        if check == True:
            if int(points) == 390 or int(points) == 360 or int(points) == 330:

                item = {
                    'name' : name,
                    'zone' : zone,
                    'actions' : action_count,
                }

                check = False
                break 

        print(emote, points)
    print(' ')

    btn_list = rapport.find_elements(By.CLASS_NAME, 'lap-button')
    for btn in btn_list:
        if btn.text == 'Stages':
            driver.execute_script('arguments[0].click();', btn)
    
    stage_table = rapport.find_elements(By.CLASS_NAME, 'lap-rapport-stages')
    



driver.quit()