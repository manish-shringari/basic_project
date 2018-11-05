from pyzbar import pyzbar
import cv2
import glob, os

def get_data():
    #img_path = "C:/Users/SHRIM006/Downloads/bkup/basic_project/buyers/basic_app/vin.jpg"
    li = glob.glob('*.jpg')
    print li

    #img = cv2.imread(img_path)
    img = cv2.imread(li[0])
    barcode = pyzbar.decode(img)
    # print type(barcode),barcode[0][0]
    # print ('========Barcode==========')
    # (x, y, w, h) = barcode.rect
    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # barcodeData = barcode.data.decode("utf-8")
    # barcodeType = barcode.type
    # text = "{} ({})".format(barcodeData, barcodeType)
    # cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # print("[INFO] found {} barcode {}".format(barcodeType, barcodeData))
    cmd = 'del *.jpg'
    os.system(cmd)
    return barcode[0][0]
# res = get_data()
# print res
