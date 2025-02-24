# Project Description:
This project implements Image Steganography, a technique used to hide secret messages inside an image without noticeable changes. The project is built using Python, OpenCV, and NumPy, allowing users to embed a hidden message into an image and later extract it.
🔹 Key Features
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
🔹 Python – Programming Language
🔹 OpenCV – Image Processing Library
🔹 NumPy – For handling pixel manipulation
🔹 OS Module – File handling

🔹 How It Works
📝 Embedding a Message (Encoding)
1️⃣ Read an image file.
2️⃣ Convert the input text into binary format.
3️⃣ Modify the Least Significant Bit (LSB) of pixel values to store the message.
4️⃣ Save the modified image.

🔍 Extracting a Message (Decoding)
1️⃣ Load the modified image.
2️⃣ Extract the LSB values from pixels.
3️⃣ Convert the extracted binary data back into text.
4️⃣ Display the hidden message.

🔹 Use Cases
🔐 Secure Communication – Hide messages in images for secret sharing.
🎨 Digital Watermarking – Embed invisible copyright marks in images.
📁 Data Hiding – Conceal sensitive data within images without suspicion.
## Step 1.
![Screenshot 2024-12-07 140903](https://github.com/user-attachments/assets/cef5946c-131a-426f-a361-8a71201ceb73)
![Screenshot 2024-12-07 140927](https://github.com/user-attachments/assets/4eea7be3-b569-42ea-89d6-1233dbca5a35)
## Step 2.
![Screenshot 2024-12-07 140945](https://github.com/user-attachments/assets/442eed2d-8933-47d9-a54d-7a460835ffd1)
![Screenshot 2024-12-07 141012](https://github.com/user-attachments/assets/4619351b-a98c-4f57-aa6b-34a252566c2c)
## Step 3.
![Screenshot 2024-12-07 141113](https://github.com/user-attachments/assets/1f65cf84-cd18-49f2-9153-d9a3650dd776)
![Screenshot 2024-12-07 141127](https://github.com/user-attachments/assets/e7d779e2-4594-4549-a6aa-f7c03a43aca1)
