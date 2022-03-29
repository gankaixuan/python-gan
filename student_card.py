from aip import AipOcr

APP_ID = '25681540'
API_KEY = 'T7nO4P5IqW9TfrGpOl5uR6I3'
SECRET_KEY = 'qvMDn0PgGRtLDfYBpwsQX606qG2hG1pw '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('student_card.jpg')
print(client.basicGeneral(image))

