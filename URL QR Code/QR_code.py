"""
QR code tool with Python , with : qrcode , Image .
"""

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcodeimg.png")

print("Hi You Want to Create QR code ?")
url = str(input("Enter Your URL: "))
generate_qrcode(url)
