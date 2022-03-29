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
sheet.title = '身份证信息1'
sheet.append(["姓名","民族","住址","公民身份号码"])
sheet.append([x1["姓名"]["words"],x1["民族"]["words"],x1["住址"]["words"],x1["公民身份号码"]["words"]])
wb.save('身份证信息表1.xlsx')

