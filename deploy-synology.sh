#!/bin/bash

# TradingAgents-CN 群晖NAS部署脚本
# 使用方法: ./deploy-synology.sh

echo "🚀 TradingAgents-CN 群晖NAS部署开始"
echo "=================================="

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker未安装，请先安装Docker套件"
    exit 1
fi

# 检查Docker是否运行
if ! docker info &> /dev/null; then
    echo "❌ Docker服务未运行，请启动Docker服务"
    exit 1
fi

echo "✅ Docker环境检查通过"

# 创建必要的目录
echo "📁 创建数据目录..."
mkdir -p data logs cache

# 停止并删除旧容器（如果存在）
echo "🔄 清理旧容器..."
docker stop tradingagents-cn 2>/dev/null || true
docker rm tradingagents-cn 2>/dev/null || true
docker network rm tradingagents-network 2>/dev/null || true

# 构建并启动新容器
echo "🐳 构建Docker镜像..."
docker build -f Dockerfile.synology -t tradingagents-cn:latest .

if [ $? -ne 0 ]; then
    echo "❌ Docker镜像构建失败"
    exit 1
fi

echo "✅ Docker镜像构建成功"

echo "🚀 启动容器..."
docker-compose -f docker-compose.synology.yml up -d

if [ $? -ne 0 ]; then
    echo "❌ 容器启动失败"
    exit 1
fi

echo "✅ 容器启动成功"

# 等待服务启动
echo "⏳ 等待服务启动..."
sleep 10

# 检查容器状态
if docker ps | grep tradingagents-cn > /dev/null; then
    echo "✅ TradingAgents-CN已成功启动"
    echo "📱 访问地址: http://你的群晖IP:8501"
    echo "🔑 默认用户名: admin, 密码: admin123"
else
    echo "❌ 容器启动失败，请检查日志"
    docker logs tradingagents-cn
fi

echo "=================================="
echo "🎉 部署完成！"