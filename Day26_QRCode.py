import qrcode

def generate_qr_code(data, filename='qrcode.png'):
    """
    Generate a QR code with the given data and save it as an image.
    
    Parameters:
    - data (str): The data to encode in the QR code.
    - filename (str): The filename to save the QR code image as.
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code: 1 (21x21) to 40 (177x177)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border (in boxes)
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"✅ QR Code saved as: {filename}")

# Example usage
if __name__ == "__main__":
    input_data = "https://example.com"
    generate_qr_code(input_data)
