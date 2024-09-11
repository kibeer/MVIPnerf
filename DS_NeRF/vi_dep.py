import numpy as np
from PIL import Image
import os

# 设定路径
npy_folder = '/home/l.wanzhou/data/MVIP-NeRF/logs_ours/front_pole/imgs_result_40/depth/'  # 替换为包含npy文件的文件夹路径
output_folder = '/home/l.wanzhou/data/MVIP-NeRF/logs_ours/front_pole/test/'  # 替换为保存png文件的目标文件夹路径
reference_image_path = '/home/l.wanzhou/data/MVIP-NeRF/logs_ours/front_pole/imgs_result_rgb_inp/rgb/000000.png'  # 替换为目标.png文件路径

# 加载参考图片以获取目标尺寸
reference_image = Image.open(reference_image_path)
target_size = reference_image.size

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历npy文件并处理
for npy_file in os.listdir(npy_folder):
    if npy_file.endswith('.npy'):
        # 加载npy文件
        depth = np.load(os.path.join(npy_folder, npy_file))
        
        # 调整深度数据的尺寸
        depth_resized = Image.fromarray(depth).resize(target_size, Image.LANCZOS)
        
        # 转换为可视化的图像 (可选择使用颜色映射)
        depth_resized = np.array(depth_resized)
        depth_image = Image.fromarray((depth_resized / np.max(depth_resized) * 255).astype(np.uint8))
        
        # 保存为.png文件
        output_path = os.path.join(output_folder, npy_file.replace('.npy', '.png'))
        depth_image.save(output_path)

        print(f"Processed {npy_file} and saved to {output_path}")

print("Batch processing complete.")

