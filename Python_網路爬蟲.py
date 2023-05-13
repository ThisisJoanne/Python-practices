from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())  
browser.get("https://old.accupass.com/search/r/0/0/0/0/4/0/00010101/99991231?q=python")
 
soup = BeautifulSoup(browser.page_source, "lxml")
activities = soup.find_all("div", {"class": "apcss-activity-card ng-isolate-scope"})
 
result = []
for activity in activities:
 
    title = activity.find("h3", {"class": "apcss-activity-card-title ng-binding"}).getText().strip()
    
    view = activity.find("span", {"class": "apcss-activity-pageview ng-binding"}).getText().strip()
    
    like = activity.find("span", {"class": "apcss-activity-card-like ng-binding"}).getText().strip().replace(" 人喜歡", "")
    
    status = activity.find("a", {"class": "apcss-btn apcss-btn-block ng-binding activity-card-status-ready"})
    
    if status == None:
        status = activity.find("a", {"class": "apcss-btn apcss-btn-block ng-binding activity-card-status-hot"})
        if status == None:
            stat = "已完售"
        else:
            stat = "即將完售"
    else:
        stat = "熱銷中"

    result.append([title, int(view), int(like), stat])
 
df = pd.DataFrame(result, columns=["活動名稱", "觀看人數", "喜歡人數", "售票狀態"])
 
new_df = df[df["售票狀態"] == "熱銷中"]  #篩選資料
 
sort_df = new_df.sort_values(["觀看人數"], ascending=False)  #依據觀看人數遞減
 
sort_df.to_excel("C:/Users/USER/Desktop/accupass.xlsx", sheet_name="activities", index=False)  # 匯出Excel檔案(不寫入資料索引值)
 
browser.quit()  
