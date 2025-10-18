#!/usr/bin/env python3
"""
简单的测试应用 - 用于验证Render部署
"""

import streamlit as st
import os
import sys
from pathlib import Path

def main():
    st.set_page_config(
        page_title="TradingAgents-CN - 测试",
        page_icon="📈",
        layout="wide"
    )

    st.title("🚀 TradingAgents-CN - 测试页面")

    st.write(f"✅ 应用启动成功！")
    st.write(f"📁 工作目录: {Path.cwd()}")
    st.write(f"🐍 Python版本: {sys.version}")
    st.write(f"🌐 端口: {os.getenv('PORT', '8501')}")

    # 检查环境变量
    st.subheader("🔧 环境变量状态")

    env_vars = {
        'DASHSCOPE_API_KEY': '✅ 已设置' if os.getenv('DASHSCOPE_API_KEY') else '❌ 未设置',
        'FINNHUB_API_KEY': '✅ 已设置' if os.getenv('FINNHUB_API_KEY') else '❌ 未设置',
        'DEEPSEEK_API_KEY': '✅ 已设置' if os.getenv('DEEPSEEK_API_KEY') else '❌ 未设置',
        'MEMORY_ENABLED': os.getenv('MEMORY_ENABLED', 'false'),
        'LLM_PROVIDER': os.getenv('LLM_PROVIDER', 'dashscope'),
    }

    for key, value in env_vars.items():
        st.write(f"**{key}**: {value}")

    # 简单测试功能
    st.subheader("🧪 功能测试")

    if st.button("测试按钮"):
        st.success("✅ 按钮功能正常！")

    # 显示系统信息
    st.subheader("📊 系统信息")

    try:
        import pandas as pd
        st.success("✅ Pandas 可用")
    except ImportError:
        st.error("❌ Pandas 不可用")

    try:
        import plotly.graph_objects as go
        st.success("✅ Plotly 可用")
    except ImportError:
        st.error("❌ Plotly 不可用")

    try:
        import requests
        st.success("✅ Requests 可用")
    except ImportError:
        st.error("❌ Requests 不可用")

    st.info("🎯 如果所有组件都显示为可用状态，说明应用部署成功！")

if __name__ == "__main__":
    main()