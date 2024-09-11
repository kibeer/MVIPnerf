import os
import numpy as np

# 定义文件夹路径
base_path = '/home/l.wanzhou/data/MVIP-NeRF/logs_ours/front_pole/imgs_result_40'  # 替换为数据集的路径
depth_folder = os.path.join(base_path, 'depth')
pose_folder = os.path.join(base_path, 'pose')

# 初始化一个列表，用于存储所有视角的数据
colmap_depth_data = []

# 获取文件列表并排序（假设文件名按照一定规则排序）
depth_files = sorted(os.listdir(depth_folder))
pose_files = sorted(os.listdir(pose_folder))

# 遍历每个视角的数据
for depth_file, pose_file in zip(depth_files, pose_files):
    # 加载深度图和相应的相机位姿
    depth = np.load(os.path.join(depth_folder, depth_file), allow_pickle=True)  # 允许加载 "pickled" 数据
    pose = np.loadtxt(os.path.join(pose_folder, pose_file))  # 假设pose文件是普通的文本格式
    
    # 生成坐标和权重 (这里假设简单的生成方式，你可以根据需要定制)
    coord = np.column_stack(np.where(depth > 0))  # 获取非零深度的坐标
    weight = np.ones_like(depth[depth > 0])  # 假设所有点权重相同
    
    # 将数据添加到列表
    colmap_depth_data.append({'depth': depth.flatten(), 'coord': coord, 'weight': weight})

# 保存为新的 colmap_depth.npy 文件
output_path = os.path.join(base_path, 'colmap_depth.npy')
np.save(output_path, np.array(colmap_depth_data, dtype=object))

print(f"Generated and saved {output_path}")

