#!/usr/bin/env python3
"""
TradingAgents-CN Render部署启动脚本 - 修复版本
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

    print(f"🚀 TradingAgents-CN Render部署启动 (修复版)")
    print(f"📁 工作目录: {project_root}")
    print(f"🐍 Python版本: {sys.version}")

    # 设置默认环境变量（Render环境可能没有.env文件）
    env_vars = {
        'DASHSCOPE_API_KEY': os.getenv('DASHSCOPE_API_KEY', ''),
        'FINNHUB_API_KEY': os.getenv('FINNHUB_API_KEY', ''),
        'DEEPSEEK_API_KEY': os.getenv('DEEPSEEK_API_KEY', ''),
        'DEFAULT_CHINA_DATA_SOURCE': os.getenv('DEFAULT_CHINA_DATA_SOURCE', 'akshare'),
        'MEMORY_ENABLED': os.getenv('MEMORY_ENABLED', 'false'),
        'LLM_PROVIDER': os.getenv('LLM_PROVIDER', 'dashscope'),
        'DEEP_THINK_LLM': os.getenv('DEEP_THINK_LLM', 'qwen-plus'),
        'QUICK_THINK_LLM': os.getenv('QUICK_THINK_LLM', 'qwen-turbo'),
    }

    for key, value in env_vars.items():
        if value and not os.getenv(key):
            os.environ[key] = value
            print(f"✅ 设置环境变量: {key}")

    # 安装依赖
    print("📦 检查并安装依赖...")
    try:
        requirements_file = project_root / "requirements.txt"

        if requirements_file.exists():
            print("📦 使用requirements.txt文件...")
            subprocess.run([
                sys.executable, "-m", "pip", "install",
                "--no-cache-dir", "-r", str(requirements_file)
            ], check=True)
            print("✅ 依赖安装完成")
        else:
            print("⚠️ requirements文件不存在，安装基础依赖...")
            subprocess.run([
                sys.executable, "-m", "pip", "install",
                "--no-cache-dir",
                "streamlit>=1.28.0",
                "pandas>=2.3.0",
                "plotly>=5.0.0",
                "requests>=2.32.4",
                "python-dotenv>=1.0.0",
                "dashscope>=1.17.0"
            ], check=True)
            print("✅ 基础依赖安装完成")
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

    # 暂时使用简单测试应用
    cmd = [
        sys.executable, "-m", "streamlit", "run",
        "test_simple_app.py",
        "--server.port", str(port),
        "--server.address", host,
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false"
    ]

    try:
        print(f"🚀 启动命令: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 应用启动失败: {e}")
        print("🔍 尝试简单的启动方式...")

        # 简单启动
        simple_cmd = [
            sys.executable, "-m", "streamlit", "run",
            "web/app.py",
            "--server.port", str(port),
            "--server.address", host,
            "--server.headless", "true"
        ]

        try:
            subprocess.run(simple_cmd, check=True)
        except subprocess.CalledProcessError as e2:
            print(f"❌ 简单启动也失败: {e2}")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️ 应用已停止")

if __name__ == "__main__":
    main()