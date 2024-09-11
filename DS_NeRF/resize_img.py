import os
from PIL import Image
from pathlib import Path

def resize_image(image_path, output_path):
    with Image.open(image_path) as img:
        # 获取原始尺寸
        original_size = img.size
        # 计算新的尺寸（宽和高都减半，即分辨率降低为1/4）
        new_size = (original_size[0] // 4, original_size[1] // 4)
        # 调整大小，使用 LANCZOS 进行抗锯齿处理
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
        # 保存图片到新的路径
        resized_img.save(output_path)

def process_images(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    for root, _, files in os.walk(input_dir):
        # 计算对应的输出文件夹路径
        relative_path = Path(root).relative_to(input_dir)
        output_folder = output_dir / relative_path
        output_folder.mkdir(parents=True, exist_ok=True)

        for file in files:
            input_file = Path(root) / file
            # 去掉文件名前缀 "mask_"
            new_file_name = file
            if new_file_name.startswith("mask_"):
                new_file_name = new_file_name[5:]

            output_file = output_folder / new_file_name
            
            # 只处理图片文件
            try:
                resize_image(input_file, output_file)
                print(f"Processed {input_file} -> {output_file}")
            except Exception as e:
                print(f"Failed to process {input_file}: {e}")

if __name__ == "__main__":
    input_directory = "/home/l.wanzhou/data/MVIP-NeRF/data/front_pole/images_4/label_mask"
    output_directory = "/home/l.wanzhou/data/MVIP-NeRF/data/front_pole/images_4/label"
    
    process_images(input_directory, output_directory)
