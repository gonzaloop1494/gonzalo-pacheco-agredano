import qrcode

url = "https://raw.githubusercontent.com/gonzaloop1494/gonzalo-pacheco-agredano/main/certificate%20in%20advanced%20English%20C1%20.pdf"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR_English.png")

print("QR_English.png generado")
