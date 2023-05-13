import pandas as pd
from pandas import ExcelWriter
df1=pd.read_csv(r'C:\Users\USER\Desktop\preview (1).csv', encoding='Big5', skiprows=0,header=1,index_col=0,usecols=[0,1,2,3,4])
data=df1.values
df2=df1.describe()

writer = ExcelWriter(r'C:\Users\USER\Desktop\NTCappealcases.xlsx')
df1.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2') 
workbook = writer.book
worksheet1 = writer.sheets['Sheet1']
worksheet1.conditional_format('A1:E12', {'type': '3_color_scale'})
worksheet2 = writer.sheets['Sheet2']
chart = workbook.add_chart({'type': 'column'})
chart.add_series({'name': '=Sheet2!$B$1','categories': '=Sheet2!$A$2:$A$9', 'values': '=Sheet2!$B$2:$B$9'})
chart.add_series({'name': '=Sheet2!$C$1','categories': '=Sheet2!$A$2:$A$9', 'values': '=Sheet2!$C$2:$C$9'})
chart.add_series({'name': '=Sheet2!$D$1','categories': '=Sheet2!$A$2:$A$9', 'values': '=Sheet2!$D$2:$D$9'})
chart.add_series({'name': '=Sheet2!$E$1','categories': '=Sheet2!$A$2:$A$9', 'values': '=Sheet2!$E$2:$E$9'})
chart.set_x_axis({'name': 'Index'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})
chart.set_legend({'position': 'top'}) 
worksheet2.insert_chart('F2: W10', chart)
writer.save()