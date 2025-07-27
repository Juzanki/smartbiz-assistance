import sys
import os

# Ruhusu import kutoka utils/
utils_path = os.path.join(os.path.dirname(__file__), "utils")
sys.path.append(utils_path)

from qr_generator import generate_product_qr

if __name__ == "__main__":
    path = generate_product_qr("https://smartbiz.co.tz/product/1009", "my_qr")
    print(f"✅ QR saved to: {path}")
