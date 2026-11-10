# -*- coding: utf-8 -*-
"""YOLO 汽车检测 —— 训练脚本
用法: 在终端激活环境后执行  python train_car.py
"""
from ultralytics import YOLO

# ========== 按自己的电脑修改这两处 ==========
DATA_YAML = r"/kaggle/input/datasets/huansir/mydatas/data.yaml"
# ==========================================

# 课堂演示参数（GPU 推荐）
# CPU 同学改成: EPOCHS, BATCH, IMGSZ = 1, 8, 320
EPOCHS, BATCH, IMGSZ = 3, 16, 640

def main():
    model = YOLO("yolo11n.pt")   # 加载 nano 版预训练模型（首次自动下载）
    model.train(
        data=DATA_YAML,
        epochs=EPOCHS,
        imgsz=IMGSZ,
        batch=BATCH,
        name="car_demo",          # 结果保存在 runs/detect/car_demo
        exist_ok=True,            # 重名时覆盖，方便反复练习
    )
    print("\n训练完成！模型在 runs/detect/car_demo/weights/best.pt")

if __name__ == "__main__":
    main()
