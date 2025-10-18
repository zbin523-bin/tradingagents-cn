#!/usr/bin/env python3
"""
TradingAgents-CN 紧急启动脚本 - 最简化版本
"""

import os
import sys

# 设置基础环境
os.environ.setdefault('PYTHONUNBUFFERED', '1')
os.environ.setdefault('PORT', '8501')

print("🚀 TradingAgents-CN 紧急启动")

# 简单的Streamlit应用
import streamlit as st

st.set_page_config(page_title="TradingAgents-CN", layout="center")
st.title("📈 TradingAgents-CN")
st.success("✅ 应用成功启动!")
st.info("🔧 修复版本 - 解决502错误")
st.write(f"🌐 端口: {os.environ.get('PORT', '8501')}")