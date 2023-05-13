from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font 
from openpyxl.styles import Alignment 
from time import sleep
import re
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.font_manager as mgr
from matplotlib.font_manager import FontProperties
import heapq

#以下爬蟲為林育萱(68-71為邱琬庭)
browser = webdriver.Chrome(ChromeDriverManager().install()) 
browser.get("https://serebii.net/pokedex/")
soup = BeautifulSoup(browser.page_source, "lxml")
browser.find_element(By.XPATH, '//*[@id="content"]/main/table/tbody/tr[2]/td[3]/a').click()
browser.find_element(By.XPATH, '//*[@id="content"]/main/div[2]/div/div[4]/table/tbody/tr/td[1]/a/img').click()
    
result1= []
result2=[]

types = ['bug', 'dark', 'dragon', 'electr', 'fight', 'fire', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
for i in range(3, 254):  #新加
    pokemon_num = browser.find_element(By.XPATH, '//*[@id="content"]/main/table[2]/tbody/tr['+ str(i) +']/td[2]').text.strip()
    hp = browser.find_element(By.XPATH, '//*[@id="content"]/main/table[2]/tbody/tr['+str(i)+']/td[6]/b').text.strip()
    attack = browser.find_element(By.XPATH, '//*[@id="content"]/main/table[2]/tbody/tr['+str(i)+']/td[7]').text.strip()
    defense = browser.find_element(By.XPATH, '//*[@id="content"]/main/table[2]/tbody/tr['+str(i)+']/td[8]').text.strip()
    special_attack = browser.find_element(By.XPATH, '//*[@id="content"]/main/table[2]/tbody/tr['+str(i)+']/td[9]').text.strip()
    special_defense = browser.find_element(By.XPATH, '//*[@id="content"]/main/table[2]/tbody/tr['+str(i)+']/td[10]').text.strip()
    speed = browser.find_element(By.XPATH, '//*[@id="content"]/main/table[2]/tbody/tr['+str(i)+']/td[11]').text.strip()
    pokemon_in = browser.find_element(By.XPATH,'//*[@id="content"]/main/table[2]/tbody/tr['+ str(i) +']/td[4]/a')
    browser.execute_script("(arguments[0]).click()", pokemon_in)
    pokemon = browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[4]/tbody/tr[2]/td[1]').text.strip()
    try:
        Female_rate = browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[4]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]').text.strip()
        Male_rate = browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[4]/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[2]').text.strip()
    except:
        Female_rate = 'genderles'
        Male_rate = 'genderless'
    Height = browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[4]/tbody/tr[4]/td[2]').text.strip().split('\n')
 
    Weight = browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[4]/tbody/tr[4]/td[3]').text.strip().split('\n')

    type_pic = browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[4]/tbody/tr[2]/td[5]/a/img').get_attribute('src')

    
    Type = []
    for t in range(0, len(types)):
        if types[t] in type_pic:
            Type.append(types[t])    
    if int(pokemon_num[1:]) <152:
        Generation = 1
    else:
        Generation = 2
    Classification = browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[4]/tbody/tr[4]/td[1]').text.strip()
    base_total = int(hp) + int(attack) + int(defense) + int(special_attack) + int(special_defense)+int(speed)
    
    try:#邱琬庭
        egg_group=browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[7]/tbody/tr[2]/td[2]').text.strip() #邱琬庭
    except:#邱琬庭
        egg_group=browser.find_element(By.XPATH, '//*[@id="content"]/main/div/div/table[7]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/a').text.strip() #邱琬庭
    
    if "cannot breed" in egg_group:
        legends = 1 
    else:
        legends = 0
    result1.append([pokemon_num[1:], pokemon, hp, attack, defense, special_attack, special_defense, speed, base_total, Female_rate, Male_rate, Height[1], Weight[1], Type[0], Generation, Classification, egg_group, legends])
    if legends == 1:
        result2.append([pokemon_num[1:], pokemon, hp, attack, defense, special_attack, special_defense, speed, base_total, Female_rate, Male_rate, Height[1], Weight[1], Type[0], Generation, Classification, egg_group, legends])
    browser.back()
    sleep(3)

df1 = pd.DataFrame(result1, columns=["編號","寶可夢", "hp", "攻擊", "防禦", "特攻", "特防", "速度", "base total", "母百分比", "公百分比","身高","體重","屬性", "世代","種族","蛋群", "傳說"])#W
df_pokemon=df1.sort_values(by=["編號"])
df_pokemon.to_excel("C:/Users/USER/Desktop/Pokemon.xlsx", sheet_name="data", index=False)
df2 = pd.DataFrame(result2, columns=["編號","寶可夢", "hp", "攻擊", "防禦", "特攻", "特防", "速度", "base total", "母百分比", "公百分比","身高","體重","屬性", "世代","種族","蛋群", "傳說"])#W
df_legends= df2.sort_values(by=["編號"])
df_legends.to_excel("C:/Users/USER/Desktop/Pokemon_legends.xlsx", sheet_name="data", index=False)

###以下是圖表程式
#debug為林育萱
file = pd.read_excel('C:/Users/USER/Desktop/Pokemon.xlsx')
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
f1=pd.read_excel("C:/Users/USER/Desktop/Pokemon.xlsx")
f2=pd.read_excel("C:/Users/USER/Desktop/Pokemon_legends.xlsx")
a="請輸入想呈現圖表的數字\n"\
    '1.寶可夢的屬性\n'\
    '2.寶可夢的種族\n'\
    '3.平均公母比\n'\
    '4.身高+體重\n'\
    '5.攻擊和防禦的關係\n'\
    '6.寶可夢的攻擊、防禦、特攻、特防\n'\
    '7.每代傳說寶可夢數量\n'\
    '8.傳說寶可夢的屬性\n'\
    '9.傳說寶可夢種類\n'\
    '10.傳說寶可夢的平均攻擊、防禦、特攻、特防\n'\
    '11.一般vs傳說寶可夢的平均攻擊、防禦、特攻、特防\n'\
    '12.一般vs傳說寶可夢的平均攻擊、防禦、特攻、特防\n'\
    '請輸入選擇資料的代號(輸入0結束程式):'

#林育萱debug
while True: 
    INPUT = eval(input(a))
    if INPUT ==str(INPUT):
        print("格式錯誤，請輸入數字\n")
        sleep(0.5)
        continue
    elif INPUT != int(INPUT):
        print("格式錯誤，請輸入數字\n")
        sleep(0.5)
        continue
    elif INPUT == int(INPUT):
        if INPUT == 0:
            break
        elif INPUT >12 or INPUT<0:
            print("請輸入介於0-12的整數\n")
            sleep(0.5)
            continue
    else:
        if INPUT=='0':
            break
#林育萱debug
        elif INPUT=='1':
            x=f1.iloc[:,13]
            x1=Counter(x)
            x1=dict(x1)
            y1=list(x1.keys())
            y2=list(x1.values())
            plt.pie(y2, radius=1.5, labels=y1,autopct = "%1.1f%%")
            plt.title('寶可夢的屬性')
            plt.show()
        elif INPUT=='2':
            x=f1.iloc[:,15]
            x1=Counter(x)
            x1=dict(x1)
            y1=list(x1.keys())
            y2=list(x1.values())
            plt.pie(y2, radius=1.5, labels=y1,autopct = "%1.1f%%")
            plt.title('寶可夢的種族')
            plt.show()
        elif INPUT=='3':
            #公母百分比散點圖 林育萱
            for i in range(0, 251):
                if file["母百分比"][i]== "genderles":
                    file["母百分比"][i] = "0%"

            file["母百分比"]=pd.to_numeric(file["母百分比"].str.replace("%", ""))

            for i in range(0, 251):
                if file["公百分比"][i]== "genderless":
                    file["公百分比"][i] = "0%"     
            file["公百分比"]=pd.to_numeric(file["公百分比"].str.replace("%", ""))

            file.plot.scatter(x="母百分比", y="公百分比")
            plt.xlabel("母百分比(%)", fontdict={'size': 16})
            plt.ylabel("公百分比(%)", fontdict={'size': 16})

            plt.title("寶可夢公母散點圖", fontdict={'size': 20})
            plt.show
        elif INPUT=='4':
         #身高+體重散點圖 林育萱
            file["身高"]=pd.to_numeric(file["身高"].str.replace("m", ""))

            file["體重"]=pd.to_numeric(file["體重"].str.replace("kg", ""))

            file.plot.scatter(x="身高", y="體重")
            plt.xlabel("身高(kg)", fontdict={'size': 16})
            plt.ylabel("體重(m)", fontdict={'size': 16})

            plt.title("寶可夢公母散點圖", fontdict={'size': 20})
            plt.show
        elif INPUT=='5':
                #攻擊和防禦的關係散點圖 林育萱
            file["攻擊"]=pd.to_numeric(file["攻擊"])

            file["防禦"]=pd.to_numeric(file["防禦"])

            file.plot.scatter(x="攻擊", y="防禦")
            plt.xlabel("攻擊", fontdict={'size': 16})
            plt.ylabel("防禦", fontdict={'size': 16})

            plt.title("寶可夢攻擊防禦散點圖", fontdict={'size': 20})
            plt.show

        elif INPUT=='6':
            x=f1.iloc[:,3]
            y=f1.iloc[:,4]
            z=f1.iloc[:,5]
            k=f1.iloc[:,6]
            plt.violinplot(x)
            plt.title('寶可夢的攻擊')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(y)
            plt.title('寶可夢的防禦')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(z)
            plt.title('寶可夢的特攻')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(k)
            plt.title('寶可夢的特防')
            plt.ylabel('數值')
            plt.show()
        elif INPUT=='7':
            x=f2.iloc[:,14]
            x1=Counter(x)
            x1=dict(x1)
            y1=list(x1.keys())
            y2=list(x1.values())
            plt.bar(y1,y2,linewidth=2, edgecolor='orange',tick_label=y1)
            plt.title('每代傳說寶可夢數量')
            plt.xlabel("世代")
            plt.ylabel("數量")
            plt.show()
        elif INPUT=='8':
            x=f2.iloc[:,13]
            x1=Counter(x)
            x1=dict(x1)
            y1=list(x1.keys())
            y2=list(x1.values())
            plt.pie(y2, radius=1.5, labels=y1,autopct = "%1.1f%%")
            plt.title('寶可夢的屬性')
            plt.show()
        elif INPUT=='9':
            x=f2.iloc[:,15]
            x1=Counter(x)
            x1=dict(x1)
            y1=list(x1.keys())
            y2=list(x1.values())
            plt.pie(y2, radius=1.5, labels=y1,autopct = "%1.1f%%")
            plt.show()
        elif INPUT=='10':
            x=f2.iloc[:,3]
            y=f2.iloc[:,4]
            z=f2.iloc[:,5]
            k=f2.iloc[:,6]
            plt.violinplot(x)
            plt.title('傳說寶可夢的攻擊')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(y)
            plt.title('傳說寶可夢的防禦')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(z)
            plt.title('傳說寶可夢的特攻')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(k)
            plt.title('傳說寶可夢的特防')
            plt.ylabel('數值')
            plt.show()
        elif INPUT=='11':
            x1=f1.iloc[:,3]
            y1=f1.iloc[:,4]
            z1=f1.iloc[:,5]
            k1=f1.iloc[:,6]
            x2=f2.iloc[:,3]
            y2=f2.iloc[:,4]
            z2=f2.iloc[:,5]
            k2=f2.iloc[:,6]
            plt.violinplot(x1)
            plt.violinplot(x1)
            plt.title('傳說v.s.一般寶可夢的攻擊')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(y1)
            plt.violinplot(y2)
            plt.title('傳說v.s.一般寶可夢的防禦')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(z1)
            plt.violinplot(z2)
            plt.title('傳說v.s.一般寶可夢的特攻')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(k1)
            plt.violinplot(k2)
            plt.title('傳說v.s.一般寶可夢的特防')
            plt.ylabel('數值')
            plt.show()
        elif INPUT== 12: #一般vs傳說寶可夢的平均攻擊、防禦、特攻、特防
            x1=f1.iloc[:,3]
            y1=f1.iloc[:,4]
            z1=f1.iloc[:,5]
            k1=f1.iloc[:,6]
            x2=f2.iloc[:,3]
            y2=f2.iloc[:,4]
            z2=f2.iloc[:,5]
            k2=f2.iloc[:,6]
            plt.violinplot(x1)
            plt.violinplot(x1)
            plt.title('傳說v.s.一般寶可夢的攻擊')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(y1)
            plt.violinplot(y2)
            plt.title('傳說v.s.一般寶可夢的防禦')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(z1)
            plt.violinplot(z2)
            plt.title('傳說v.s.一般寶可夢的特攻')
            plt.ylabel('數值')
            plt.show()
            plt.violinplot(k1)
            plt.violinplot(k2)
            plt.title('傳說v.s.一般寶可夢的特防')
            plt.ylabel('數值')
            plt.show()
        else:
            continue