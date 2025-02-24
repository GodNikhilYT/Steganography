import cv2
import os
import numpy as np  

def embed_message(img_path, message, output_path):
    if not os.path.exists(img_path):
        print(f"❌ Error: Image not found at {img_path}")
        return

    img = cv2.imread(img_path)
    if img is None:
        print("❌ Error: Unable to read the image!")
        return

    print("✅ Image successfully loaded!")

    message += "#####"
    binary_msg = ''.join(format(ord(c), '08b') for c in message)
    
    data_index = 0
    total_bytes = img.shape[0] * img.shape[1] * 3  

    if len(binary_msg) > total_bytes:
        print("❌ Message too long to fit in the image!")
        return

    for row in img:
        for pixel in row:
            for channel in range(3): 
                if data_index < len(binary_msg):
                    original_value = int(pixel[channel]) 
                    modified_value = np.uint8((original_value & ~1) | int(binary_msg[data_index]))  
                    
                    # Debugging print to check value changes
                    #print(f"Original: {original_value}, Modified: {modified_value}")

                    pixel[channel] = modified_value  
                    data_index += 1
                else:
                    break

    cv2.imwrite(output_path, img)
    print(f"✅ Message successfully embedded in {output_path}")

def extract_message(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print("❌ Error: Image not found!")
        return

    binary_msg = ""
    for row in img:
        for pixel in row:
            for channel in range(3):  
                binary_msg += str(pixel[channel] & 1)


    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ''.join(chr(int(char, 2)) for char in chars)

    if "#####" in message:
        message = message[:message.index("#####")]
        print("🔓 Decrypted Message:", message)
    else:
        print("❌ No hidden message found!")

image_path = r"d:\Steganography\encrypted_img.jpg"  
output_image = r"D:\Steganography\stego_image.jpg"  

message = input("🔑 Enter message to hide: ")
embed_message(image_path, message, output_image)

print("\n🔍 Extracting hidden message...")
extract_message(output_image)
