import qrcode
import cv2
# qr=qrcode.make(" creating mrv technology")
# data="https://mrvtechnology.com/ "
# qr=qrcode.make(data)
# qr.save(" mrvqr1.png")


qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=3
)
Name=input("enter ur name:")
age=input("enter ur age:")
email=input("enter ur email:")
phone_number=input("enter ur Phone_number:")
Data={"Name":Name,"Age": age,"Email":email,"Phone_number":phone_number}
qr.add_data(Data)
qr.make(fit=True)
img=qr.make_image()
img.save("Store_details_in_qr3.png")
print("QR code generated and saved as 'Store_details_in_qr3.png'")
def decode_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
                                                                   
    if vertices_array is not None:
        print("QR code detected and decoded:")
        print(data)
    else:
        print("QR code not detected")
        decode_qr_code("Store_details_in_qr3.png")








