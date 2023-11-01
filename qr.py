import qrcode

features = qrcode.QRCode(version=1, box_size=40, border=5)
features.add_data('https://www.instagram.com/ar/261938039613412/')
features.make(fit=True)
generate_image = features.make_image(fill_color='black')
generate_image.save('Reconqr.png')