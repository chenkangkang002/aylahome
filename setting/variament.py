'''公共的变量'''

HOST = 'https://abp-test.ayla.com.cn'   #测试环境
# HOST = 'https://abp-prod.ayla.com.cn'   #正式环境
HOST_H5 = 'https://miya-h5-test.ayla.com.cn' #测试环境H5
# HOST_H5 = 'https://miya-h5.ayla.com.cn/'  #正式

HOME_URL = '/api/v1/miya/home'
DEVICE_LIST_URL = '/api/v1/miya/device/list'
PROPERTIES_URL = '/api/v1/miya/device/{}/properties'  #获取设备属性
MODEL_TEMPLATE_URL = '/api/v3/miya/spark/devicetypes/ZBSW0-A000002/modelTemplate'    #获取设备的物模板
USE_DEVICE_PROPERTY_URL = '/api/v1/miya/device/{}/property/PurposeDeviceLight'   #获取用途设备的开关属性
TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMzI2NDY1MTM3MzMwMjk4OTU4IiwidXNlck5hbWUiOiLpmYjlurciLCJsb2dpblR5cGUiOiIxIiwibG9naW5Tb3VyY2UiOiI1IiwiYXlsYUFwcGxpY2F0aW9uSWQiOiI2IiwidHlwZSI6ImF1dGhfdG9rZW4iLCJpYXQiOjE2MjgxNTMxODR9.lvVfXDUV1O8x1O9hvz7UA94d_wULv5DdfaRjarSyMcM'

HOME_NAME = 'A6语音'  #选择家庭 原始家庭
TIMEOUT = 5

H5_DEVICE = ['罗马水空调面板']   #控制遍历的设备，为[]时遍历所有设备
SWITCH_DEVICE = ['在线']  #通过状态控制遍历的设备

DOUBLE_CURTAIN_NAME = ['窗帘','窗纱']   #双路窗帘两个开关的名称