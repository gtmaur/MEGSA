'''
This is a simple pythin script developed to create the QR code for the MEGSA events.
'''
import qrcode
from PIL import Image
from datetime import datetime

def generate_qr_code_with_background(url, background_image_path, event_name):
    # Create instance of QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QRCode instance
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QRCode instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Open the background image
    background_image = Image.open(background_image_path)

    # Resize the background image to match the QR code size
    background_image = background_image.resize(qr_image.size)

    # Paste the QR code on top of the background image
    combined_image = Image.alpha_composite(background_image.convert('RGBA'), qr_image.convert('RGBA'))

    # Get today's date
    today_date = datetime.now().strftime("%Y-%m-%d")

    # Save the combined image to the Desktop with the event name and today's date as PNG
    output_file = fr"C:\Users\aa21b.FSU\Desktop\{event_name}_{today_date}.png"
    combined_image.save(output_file, "PNG")

if __name__ == "__main__":
    url_to_encode = "https://docs.google.com/forms/d/e/1FAIpQLSfPbV6V34BAJwD36kIIDX9FGJfssa6BAsshWfGP8CvQj6mjBA/viewform"
    background_image_path = r"C:\Users\aa21b.FSU\Desktop\megsa_logo.jpg"  # Use raw string or double backslashes
    event_name = "megsa_bbq"

    # Generate and save QR code as PNG
    generate_qr_code_with_background(url_to_encode, background_image_path, event_name)
    print(f"QR code with background generated for event: {event_name}")
