import serial # 导入模块

ser = serial.Serial('COM3', 9600, timeout=1)
# serial.Serial  的三个形参 分别对应 Arduino的串口  波特率 连接超时时间
print(ser)
while 1:
    val = ser.readline().decode('utf-8')
    # ser.readline() 读取窗串口中的数据以二进制的形式展示需要使用.decode('utf-8')进行解码
    print(val)

    # parsed = val.split(',')
    # parsed = [x.strip() for x in parsed]
    # print(parsed)