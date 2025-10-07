#!/usr/bin/env python3
"""
最小化部署脚本 - 直接上传到Render
"""
import os
import sys
import subprocess
from pathlib import Path

def create_minimal_package():
    """创建最小化部署包"""

    # 必需文件列表
    required_files = [
        'web/app.py',
        'web/components/',
        'web/utils/',
        'requirements.txt',
        'start_render.py',
        'render.yaml',
        'main.py',
        'tradingagents/'
    ]

    # 创建临时目录
    deploy_dir = Path("minimal_deploy")
    deploy_dir.mkdir(exist_ok=True)

    print("📦 创建最小化部署包...")

    # 复制必需文件
    import shutil
    for item in required_files:
        src = Path(item)
        if src.exists():
            dst = deploy_dir / item
            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            print(f"✅ 已复制: {item}")
        else:
            print(f"⚠️ 跳过不存在: {item}")

    # 创建简单的requirements.txt
    minimal_requirements = """streamlit>=1.28.0
pandas>=1.5.0
plotly>=5.15.0
requests>=2.28.0
python-dotenv>=1.0.0
"""

    with open(deploy_dir / "requirements.txt", "w") as f:
        f.write(minimal_requirements)

    print("✅ 最小化部署包已创建在 ./minimal_deploy/ 目录")
    return deploy_dir

if __name__ == "__main__":
    create_minimal_package()