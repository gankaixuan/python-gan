from aip import AipOcr
from openpyxl import Workbook

APP_ID = '25681540'
API_KEY = 'T7nO4P5IqW9TfrGpOl5uR6I3'
SECRET_KEY = 'qvMDn0PgGRtLDfYBpwsQX606qG2hG1pw '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('id_card.jpg')
idCardSide = "back"
options = {}
options["detect_direction"] = "true"
options["detect_risk"] = "false"
result = client.idcard(image, idCardSide, options)
print(result)
x1 = result["words_result"]

wb = Workbook()
sheet = wb.active
sheet.title = '身份证信息2'
list1 = []
list2 = []
for i in x1.keys():
    list1.append(i)
for j in x1.values():
    list2.append(j["words"])
sheet.append(list1)
sheet.append(list2)
wb.save('身份证信息表2.xlsx')