import os
from PIL import Image

def rename_and_resize_images(folder_path, target_resolution):
    # 获取文件夹中所有图片文件的列表
    images = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])
    
    # 检查图片数量是否为40张
    #if len(images) != 31:
    #    raise ValueError("文件夹中必须有且仅有40张图片。")
    
    # 按顺序重命名并调整大小
    for i, filename in enumerate(images):
        new_name = f"img{i:03}.png"
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_name)
        
        # 打开图片并调整大小
        img = Image.open(old_file_path)
        img_resized = img.resize(target_resolution)
        
        # 保存重命名和调整大小后的图片
        img_resized.save(new_file_path)
        
        # 删除旧文件（可选）
        if old_file_path != new_file_path:
            os.remove(old_file_path)
        
        print(f"已处理: {filename} -> {new_name}, 分辨率: {target_resolution}")

if __name__ == "__main__":
    folder_path = "/home/l.wanzhou/data/MVIP-NeRF/data/fence2/images_4/RGB_inpainted"  # 替换为你的图片文件夹路径
    target_resolution = (480, 270)  # 替换为你需要的目标分辨率 (宽度, 高度)
    
    rename_and_resize_images(folder_path, target_resolution)


