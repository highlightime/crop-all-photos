from PIL import Image
import os

# 입력 이미지 디렉토리
input_dir = "input_images"

# 크롭된 이미지를 저장할 디렉토리
output_dir = "cropped"

# 만약 "cropped" 디렉토리가 없다면 생성
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# 입력 디렉토리의 모든 이미지 파일을 가져옴
image_files = [f for f in os.listdir(input_dir) if f.endswith((".jpg", ".jpeg", ".png"))]

# 크롭할 좌표 및 크기 (left, upper, right, lower)
crop_box = (0, 110, 1530, 980)  # 예시 좌표 및 크기

# 모든 이미지를 크롭하고 저장
for image_file in image_files:
    input_path = os.path.join(input_dir, image_file)
    img = Image.open(input_path)
    cropped_img = img.crop(crop_box)
    output_path = os.path.join(output_dir, image_file)
    cropped_img.save(output_path)

print("이미지 크롭이 완료되었습니다.")

