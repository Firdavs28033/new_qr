import segno

def qr_code_make(url):
    qrcode = segno.make_qr(f"www.kun.uz/{url}")
    qrcode.save(
        f"media/qr_codes/{url}.png",
        scale=5,
        dark="darkblue",
    )

    return qrcode


