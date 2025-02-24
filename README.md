# Nikhil Choudhary - Teerthanker Mahaveer University 

This project is part of my AICTE internship on cybersecurity, focusing on steganography.

I've used - python3, OS Module, OpenCV, and NumPy library.

## Project Description:
"This project implements Image Steganography, a technique used to hide secret messages inside an image without noticeable changes. 

The project is built using Python, OpenCV, and NumPy, allowing users to embed a hidden message into an image and later extract it."

### 🔹 Key Features

✅ Embed Message in an Image

Converts the message into binary format.

Modifies the least significant bit (LSB) of each pixel in the image to store the binary data.

Saves the new "stego image" with the hidden message.

✅ Extract Message from an Image

Reads the least significant bits (LSB) of each pixel.

Converts extracted binary data back into readable text.

Stops reading when the delimiter ("#####") is found.

✅ Secure and Efficient

The message is hidden at a pixel level, making it undetectable to the human eye.

Uses a fixed delimiter ("#####") to identify the end of the message.

Ensures that the message does not exceed image capacity before embedding.

✅ Error Handling

Ensures the image file exists before processing.

Prevents embedding messages that are too large for the image.

Fixes potential integer overflow errors during pixel modifications.

🔹 Technologies Used

Python – Programming Language

OpenCV – Image Processing Library

NumPy – For handling pixel manipulation

OS Module – File handling

🔹 How It Works

📝 Embedding a Message (Encoding)

Read an image file.

Convert the input text into binary format.

Modify the Least Significant Bit (LSB) of pixel values to store the message.

Save the modified image.

🔍 Extracting a Message (Decoding)

Load the modified image.

Extract the LSB values from pixels.

Convert the extracted binary data back into text.

Display the hidden message.

🔹 Use Cases

Secure Communication – Hide messages in images for secret sharing.

Digital Watermarking – Embed invisible copyright marks in images.

Data Hiding – Conceal sensitive data within images without suspicion.

🚀 This project provides a simple yet powerful way to hide and retrieve secret messages in images! 😊


## Step 1.
 ✅ Source Code of Steganography
 
![Image](https://github.com/user-attachments/assets/1ef41f4c-926c-447d-a6a7-6462b4e2990d)

![Image](https://github.com/user-attachments/assets/8eae251d-a868-4a1c-8f6b-f8071d92c056)

![Image](https://github.com/user-attachments/assets/f746eb8c-e055-4ba3-891b-f167a9c6d095)

## Step 2.
 ✅ Compile the code of Steganography

 ![Image](https://github.com/user-attachments/assets/2f6a2be9-8857-4df5-bca7-c0d6f4f9181f)

 ## Step 3.
 
 ✅ Original image
 
![Image](https://github.com/user-attachments/assets/a27bff92-0e47-491e-9584-833d3c6e5192)

 ## Step 3.
 
 ✅ Successfully Compile the code of Steganography given encrypted image

 ![Image](https://github.com/user-attachments/assets/67068940-101e-4c1c-8f7d-3485da84e863)
