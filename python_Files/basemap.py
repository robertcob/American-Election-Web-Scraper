#various imports from modules and other files
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from raw_Data_Edit import *
from database_Design import *

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

total_States = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
                "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
                "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
                "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
                "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

unavailable_States = []


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


# function will take a list of states and search real clear politics for polling data, and record any polling data in a text file to be processed
def Collect_Data(state_List):
    poll_Unavailable_Xpath = '//*[@id="container"]/div[3]/div/div[2]/div[1]/div[3]/div[3]/span[2]/div/div/div'
    for state in state_List:
        driver.get("https://www.realclearpolitics.com/epolls/latest_polls/")
        search_String = "%s: Trump vs. Biden" % state
        searchbox = driver.find_element_by_id("find_a_poll")

        searchbox.send_keys(search_String)
        searchbox.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        if check_exists_by_xpath(poll_Unavailable_Xpath) == True:
            unavailable_States.append(state)
            print("No available polls on the state of %s for this resource" % state)
            continue
        time.sleep(2)

        print("Collecting election Polling data on the state of %s" % state)

        if check_exists_by_xpath('//*[@id="polling-data-rcp"]/table') == False:
            print("No recent polling data on this State, searching for older data....")
            table2 = driver.find_element_by_xpath('//*[@id="polling-data-full"]')
            data_Writing(table2)

        else:
            table1 = driver.find_element_by_xpath('//*[@id="polling-data-rcp"]/table')
            table2 = driver.find_element_by_xpath('//*[@id="polling-data-full"]')
            data_Writing(table1)
            data_Writing(table2)
        print("\n")

#writes scraped data to text file
def data_Writing(table_Object):
    infile = open("polling_Data.txt", "a")
    for row in table_Object.find_elements_by_tag_name("tr"):
        for cell in row.find_elements_by_tag_name("td"):
            if cell.text == "RCP Average":
                break
            infile.write(cell.text + "\n")
    infile.close()


#calling functions from other files.
Collect_Data(total_States)
Sort_Data()
data_To_Be_Exported = export_Data("new_polling_data.txt")
print(data_To_Be_Exported)
database_Insertions(data_To_Be_Exported)

./mnt/c/Users/rober/PycharmProjects/Election_Scraper/basemap.py