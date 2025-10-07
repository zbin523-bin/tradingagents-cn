#!/bin/bash

# TradingAgents-CN Render部署脚本
# 使用方法: ./deploy_to_render.sh

echo "🚀 TradingAgents-CN Render部署准备"
echo "=================================="

# 检查git仓库状态
if [ ! -d ".git" ]; then
    echo "❌ 当前目录不是Git仓库"
    echo "正在初始化Git仓库..."
    git init
    git add .
    git commit -m "Initial commit: TradingAgents-CN stock analysis platform"
fi

# 检查是否有未提交的更改
if [ -n "$(git status --porcelain)" ]; then
    echo "📝 发现未提交的更改，正在提交..."
    git add .
    git commit -m "Update: Prepare for Render deployment - $(date)"
fi

# 检查远程仓库
if ! git remote get-url origin &>/dev/null; then
    echo "❌ 未找到GitHub远程仓库"
    echo "请手动设置GitHub远程仓库："
    echo "git remote add origin https://github.com/YOUR_USERNAME/TradingAgents-CN.git"
    echo "git push -u origin main"
    exit 1
fi

# 显示当前分支
current_branch=$(git branch --show-current)
echo "📋 当前分支: $current_branch"

# 推送到远程仓库
echo "📤 推送代码到GitHub..."
git push origin $current_branch

if [ $? -eq 0 ]; then
    echo "✅ 代码推送成功"
else
    echo "❌ 代码推送失败"
    exit 1
fi

echo ""
echo "🎯 接下来的步骤："
echo "1. 访问 https://dashboard.render.com"
echo "2. 点击 'New +' -> 'Web Service'"
echo "3. 连接GitHub仓库: TradingAgents-CN"
echo "4. 配置以下设置："
echo "   - Name: tradingagents-cn"
echo "   - Environment: Python"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: python start_render.py"
echo "   - Health Check Path: /_stcore/health"
echo "5. 在Environment中添加API密钥（参考render_deploy_package.json）"
echo "6. 点击 'Create Web Service' 开始部署"
echo ""
echo "📊 部署完成后，您的应用将在以下地址可用："
echo "https://tradingagents-cn.onrender.com"
echo ""
echo "🔧 如需配置Redis缓存，请在创建服务后添加Redis实例"