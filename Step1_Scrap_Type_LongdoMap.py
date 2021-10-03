#Import modules
from selenium import webdriver
import pandas as pd
import os
from datetime import date

#สร้าง Stampdate = today
date = date.today()
#date_str = str(date)
date_str = '2021-10-10'
list_date =[]
list_date.append(date_str)

#Set directory file
path = './chromedriver/' #Location Output

#Web path
A = "https://map.longdo.com/"
web_path = A

#Open webdriver 
driver = webdriver.Chrome(path+"chromedriver.exe")
# ใส่ web path
driver.get(web_path)

#Longdo_TagName
Tag = driver.find_elements_by_class_name('ldmap_tagcategory') 
Tag=[name.text for name in Tag]
print(Tag)


#สร้าง DF ให้เท่ากัน เพราะ ชื่อโรงแรมมี แค่ 1 row
count_1 = len(pricehotel)
hotelnames1=[]
for i in range(count_1):
    hotelnames1.extend(hotelnames)
print(hotelnames1)

stampdate = []
for i in range(count_1):
    stampdate.extend(list_date)
print(stampdate)

#Convert to table (DataFrame) ตั้งชื่อ Columns ว่า MovieNames และ Ratings
DF_Agoda=pd.DataFrame({'HotelName':hotelnames1 , 'RoomName':roomnames , 'PriceHotel':pricehotel, 'Stampdate': stampdate})

#Export to Excel
DF_Agoda.to_excel(hotelnames[0]+date_str+'.xlsx',index=False)