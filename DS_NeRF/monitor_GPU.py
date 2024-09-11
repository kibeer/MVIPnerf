import os
import time
import subprocess

def get_free_memory(gpu_index):
    """
    获取指定 GPU 的空闲显存量（MB）。
    """
    result = subprocess.run(
        ['nvidia-smi', '--query-gpu=memory.free', '--format=csv,nounits,noheader'],
        stdout=subprocess.PIPE
    )
    memory_free = result.stdout.decode('utf-8').strip().split('\n')
    return int(memory_free[gpu_index])

def are_gpus_idle(gpu_indices, threshold_mb):
    """
    判断所有指定的 GPU 是否都处于空闲状态，空闲条件为显存使用小于指定阈值。
    """
    for gpu_index in gpu_indices:
        free_memory = get_free_memory(gpu_index)
        print(f"GPU {gpu_index} free memory: {free_memory} MB")
        if free_memory <= threshold_mb:
            return False
    return True

def execute_task(script_path):
    """
    需要执行的任务，运行指定的 .sh 脚本。
    """
    print("所有 GPU 空闲，开始执行任务...")
    os.system(f"bash {script_path}")

def monitor_gpus_and_run_task(gpu_indices, check_interval, threshold_mb, script_path):
    """
    监控指定的 GPU 的显存使用情况，并在所有 GPU 空闲时执行任务。
    """
    while True:
        if are_gpus_idle(gpu_indices, threshold_mb):
            execute_task(script_path)
            break  # 任务执行完毕后退出监控循环
        else:
            print(f"GPU 仍在使用中，等待 {check_interval} 秒后重试...")
            time.sleep(check_interval)

# 配置参数
gpu_indices = [0, 1]  # 监控 GPU 0 和 GPU 1
check_interval = 60  # 检查间隔时间（秒）
threshold_mb = 10000  # 空闲显存阈值（MB）
script_path = "/home/l.wanzhou/data/MVIP-NeRF/DS_NeRF/run_all.sh"  # 需要执行的 .sh 脚本路径

# 开始监控并在所有 GPU 空闲时执行任务
monitor_gpus_and_run_task(gpu_indices, check_interval, threshold_mb, script_path)
