from PIL import Image

def hide_message(image_path, message, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    # Chuyển message thành binary
    binary_msg = ''.join([format(ord(c), '08b') for c in message])
    binary_msg += '1111111111111110'  # Marker kết thúc
    
    if len(binary_msg) > img.width * img.height * 3:
        raise ValueError("Message quá dài cho ảnh này")
    
    data_index = 0
    for y in range(img.height):
        for x in range(img.width):
            pixel = list(pixels[x, y])
            
            for color in range(3):  # R, G, B
                if data_index < len(binary_msg):
                    # Thay bit cuối cùng bằng bit message
                    pixel[color] = pixel[color] & ~1 | int(binary_msg[data_index])
                    data_index += 1
            
            pixels[x, y] = tuple(pixel)
            
            if data_index >= len(binary_msg):
                img.save(output_path)
                return
            
    img.save(output_path)

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    binary_msg = ""
    for y in range(img.height):
        for x in range(img.width):
            pixel = pixels[x, y]
            
            for color in range(3):  # R, G, B
                binary_msg += str(pixel[color] & 1)
                
                # Kiểm tra marker kết thúc
                if binary_msg[-16:] == '1111111111111110':
                    binary_msg = binary_msg[:-16]
                    message = ""
                    for i in range(0, len(binary_msg), 8):
                        byte = binary_msg[i:i+8]
                        message += chr(int(byte, 2))
                    return message
                    
    return "Không tìm thấy message"

# Phần nhập flag từ người dùng
def main():
    print("Chương trình giấu flag vào ảnh bằng LSB")
    
    # Nhập đường dẫn ảnh gốc
    image_path = input("Nhập đường dẫn ảnh gốc (ví dụ: original.png): ")
    
    # Nhập flag cần giấu
    flag = input("Nhập flag bạn muốn giấu (ví dụ: sCTF{my_secret_flag}): ")
    
    # Nhập tên file output
    output_path = input("Nhập tên file output (ví dụ: hidden.png): ")
    
    try:
        # Giấu flag vào ảnh
        hide_message(image_path, flag, output_path)
        print(f"\nĐã giấu flag thành công vào {output_path}!")
        
        # Hỏi người dùng có muốn trích xuất không
        choice = input("\nBạn có muốn trích xuất flag để kiểm tra? (y/n): ")
        if choice.lower() == 'y':
            extracted = extract_message(output_path)
            print(f"\nFlag trích xuất được: {extracted}")
    except Exception as e:
        print(f"\nCó lỗi xảy ra: {str(e)}")

if __name__ == "__main__":
    main()