import os
from PIL import Image

# 处理图片：降低分辨率并保存为两个文件
def process_images(input_folder, output_lowres_folder, output_label_folder):
    if not os.path.exists(output_lowres_folder):
        os.makedirs(output_lowres_folder)
    if not os.path.exists(output_label_folder):
        os.makedirs(output_label_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # 缩小分辨率到原来的四分之一
            low_res_image = image.resize(
                (image.width // 4, image.height // 4), Image.Resampling.LANCZOS)

            # mask
            black_image = Image.new("RGB", low_res_image.size, (0, 0, 0))

            # 保存低分辨率图片
            low_res_image_path = os.path.join(output_lowres_folder, filename)
            low_res_image.save(low_res_image_path)

            # mask
            _, file_extension = os.path.splitext(filename)
            black_image_path = os.path.join(output_label_folder, filename)

            # 保存全黑图片
            black_image.save(black_image_path, format=file_extension[1:].upper())

            print(f"Processed and saved low-res: {low_res_image_path}")
            print(f"Processed and saved label: {black_image_path}")

def main():
    # 本地文件夹路径
    input_folder = '/home/l.wanzhou/data/MVIP-NeRF/data/front_pole/images'  # 替换为存放原始图片的输入文件夹路径
    output_lowres_folder = '/home/l.wanzhou/data/MVIP-NeRF/data/front_pole/images_4'  # 替换为存放低分辨率图片的输出文件夹路径
    output_label_folder = '/home/l.wanzhou/data/MVIP-NeRF/data/front_pole/images_4/label'  # 替换为存放标签图片的输出文件夹路径
    
    # 处理图片：降低分辨率并保存
    process_images(input_folder, output_lowres_folder, output_label_folder)

if __name__ == '__main__':
    main()


