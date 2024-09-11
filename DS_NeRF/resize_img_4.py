from PIL import Image
import os

# 定义你要处理的数据集名称
#datasets = ['back_chair', 'flower_fence', 'goddess', 'ladder', 'middle_pole', 'orchids']  # 添加所有数据集名称
datasets = ['back_chair', 'flower_fence']  # 添加所有数据集名称
factor = 4  # 缩放因子，原始分辨率/factor

# 定义函数来处理每个数据集
def process_dataset(dataset_name, base_dir='data'):
    images_dir = os.path.join(base_dir, dataset_name, 'images_4')
    subfolders = ['RGB_inpainted', 'label']
    
    # 获取原始图像的分辨率作为参考
    original_image_path = os.path.join(base_dir, dataset_name, 'images', 'img000.png')
    
    if not os.path.exists(original_image_path):
        print(f"Original image not found: {original_image_path}")
        return
    
    original_image = Image.open(original_image_path)
    original_width, original_height = original_image.size
    
    # 目标分辨率
    target_width = original_width // factor
    target_height = original_height // factor
    
    # 处理 images_4 文件夹中的图片
    for image_name in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_name)
        if os.path.isfile(image_path):  # 确保这是一个文件而不是文件夹
            with Image.open(image_path) as img:
                img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                img_resized.save(image_path)
    
    # 处理子文件夹中的图片
    for subfolder in subfolders:
        subfolder_dir = os.path.join(images_dir, subfolder)
        for image_name in os.listdir(subfolder_dir):
            image_path = os.path.join(subfolder_dir, image_name)
            if os.path.isfile(image_path):  # 确保这是一个文件而不是文件夹
                with Image.open(image_path) as img:
                    img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    img_resized.save(image_path)

# 遍历所有数据集并处理
for dataset in datasets:
    process_dataset(dataset)

print("处理完成！")

