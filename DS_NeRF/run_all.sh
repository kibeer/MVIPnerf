#!/bin/bash

# 脚本和参数列表
declare -a scripts=(
    "python DS_NeRF/run.py --config DS_NeRF/config/config_goddess.txt"
    "python DS_NeRF/run.py --config DS_NeRF/config/config_fence2.txt"
    #"python DS_NeRF/run.py --config DS_NeRF/config/config_back_chair.txt"
    #"python DS_NeRF/run.py --config DS_NeRF/config/config_flower_fence.txt"
    #"python DS_NeRF/run.py --config DS_NeRF/config/config_orchids.txt"
    #"python DS_NeRF/run.py --config DS_NeRF/config/config_middle_pole.txt"
    #"python DS_NeRF/run.py --config DS_NeRF/config/config_ladder.txt"
)

# 遍历并执行每个脚本
for script in "${scripts[@]}"; do
    echo "Running: $script"
    $PYTHON_EXEC $script
    if [ $? -ne 0 ]; then
        echo "Error occurred while executing $script"
        exit 1
    fi
done

echo "All scripts executed successfully."
