from ultralytics import YOLO
import numpy as np
from PIL import Image

cam = 'rtsp://admin:admin@192.168.1.78:554/30'
model = YOLO("best.pt")
# img = Image.open('img.png')
# img = np.asarray(img)
# results = model.predict(img)
results = model.predict(source='0', show = True, stream= True)
maps = {1.0: 'bio', 2.0:'rov', 3.0: 'trash'}
names = ''
for r in results:
    print(list(r.boxes.shape)[1])
    if list(r.boxes.shape)[1] ==6:
        list_label = r.boxes.boxes.tolist()
        label = list_label[0][5]
        if label != None:
            if label==2.0:
                names ="trash"
            else:
                continue
        else:
            continue
        count = len(results)
        print(names,' Số lượng: ',count )
    else:
        continue


