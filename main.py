import cv2
import os
import pandas as pd
from Detectron2.demo import demo
import serial

# sets up serial connection (make sure baud rate is correct - matches Arduino)
ser = serial.Serial('com3', 9600)


### df Part
json_path = 'D:/Coding/ADI/HF/Final/FestivalMachine/interactive_screen/public/data/df.json'
if os.path.exists(json_path):
    df = pd.read_json(json_path)
else:
    df = pd.DataFrame(columns=['label', 'path', 'comment'])
# get how many lines in df
num_df = len(df)


# ### camera Part
print('Loading...')
cap = cv2.VideoCapture(0)  # open the camera
print('Ready for screenshot')
ss_path = "D:/Coding/ADI/HF/Final/img/screenshot/ss.png"
rembg_path_root = "D:/Coding/ADI/HF/Final/FestivalMachine/interactive_screen/public"

while (1):
    data = ser.readline()  # 按行读取串口数据进来
    data = data.decode()  # 读进来的数据是bytes形式，需要转化为字符串格式
    data = data.strip()
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)  # create the window of camera

    # if cv2.waitKey(1) & 0xFF == ord('q'):  # if click q, then take a screenshot and quit
    if data == 'q':
        cv2.imwrite(ss_path, frame)  # save_path
        print('Finished.')
        break
cap.release()
cv2.destroyAllWindows()


### remove background Part
relative_path = '/pictures/{}.png'.format(num_df)
rembg_path = rembg_path_root + relative_path
f = os.popen('rembg i {} {}'.format(ss_path, rembg_path))
# print(f.read())


# ### classification Part
label = demo.run_pre_set(ss_path)


### record the result
df.loc[num_df] = [label, relative_path, '']
df.to_json(json_path)
