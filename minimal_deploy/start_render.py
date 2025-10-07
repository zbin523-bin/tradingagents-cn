#!/usr/bin/env python3
"""
TradingAgents-CN Render部署启动脚本
适用于Render.com平台的Web应用启动
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """主启动函数"""

    # 设置环境变量
    os.environ.setdefault('PYTHONUNBUFFERED', '1')

    # 确保在正确的目录中
    project_root = Path(__file__).parent
    os.chdir(project_root)

    print(f"🚀 TradingAgents-CN Render部署启动")
    print(f"📁 工作目录: {project_root}")
    print(f"🐍 Python版本: {sys.version}")

    # 安装依赖
    print("📦 检查并安装依赖...")
    try:
        # 检查requirements.txt是否存在
        requirements_file = project_root / "requirements.txt"
        if requirements_file.exists():
            subprocess.run([
                sys.executable, "-m", "pip", "install",
                "--no-cache-dir", "-r", str(requirements_file)
            ], check=True)
            print("✅ 依赖安装完成")
        else:
            print("⚠️ requirements.txt文件不存在")
    except subprocess.CalledProcessError as e:
        print(f"❌ 依赖安装失败: {e}")
        sys.exit(1)

    # 创建必要的目录
    directories = [
        "data",
        "logs",
        "cache",
        "web/data",
        "web/config"
    ]

    for directory in directories:
        dir_path = project_root / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 创建目录: {directory}")

    # 启动Streamlit应用
    port = int(os.environ.get('PORT', 8501))
    host = os.environ.get('HOST', '0.0.0.0')

    print(f"🌐 启动Web应用...")
    print(f"🔗 地址: http://{host}:{port}")

    # Streamlit启动命令
    cmd = [
        sys.executable, "-m", "streamlit", "run",
        "web/app.py",
        "--server.port", str(port),
        "--server.address", host,
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 应用启动失败: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️ 应用已停止")

if __name__ == "__main__":
    main()