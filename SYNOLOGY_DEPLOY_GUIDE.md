# TradingAgents-CN 群晖NAS部署指南

## 📋 部署准备清单

### ✅ 群晖NAS要求
- **系统版本**: DSM 7.0 或以上
- **处理器**: x64架构（支持Docker）
- **内存**: 4GB RAM 以上（推荐8GB）
- **存储**: 20GB 可用空间以上

### ✅ 必需套件
1. **Docker** (从套件中心安装)
2. **文本编辑器** (推荐安装)

## 🚀 部署步骤

### 步骤1: 准备项目文件

1. 在你的Mac上，进入项目目录：
   ```bash
   cd /Users/zhangbin/TradingAgents-CN
   ```

2. 创建部署文件包：
   ```bash
   # 创建部署目录
   mkdir synology-deploy
   cp Dockerfile.synology synology-deploy/
   cp docker-compose.synology.yml synology-deploy/docker-compose.yml
   cp deploy-synology.sh synology-deploy/
   cp .env synology-deploy/
   cp -r web synology-deploy/
   cp -r components synology-deploy/
   cp -r utils synology-deploy/
   cp -r modules synology-deploy/
   ```

3. 打包部署文件：
   ```bash
   tar -czf tradingagents-cn-synology.tar.gz synology-deploy/
   ```

### 步骤2: 上传文件到群晖

#### 方法A: 使用File Station (推荐)
1. 打开群晖 **File Station**
2. 创建新文件夹 `docker` 或 `tradingagents`
3. 上传 `tradingagents-cn-synology.tar.gz` 到该文件夹
4. 在File Station中右键点击压缩包，选择"解压缩"

#### 方法B: 使用SCP/SFTP
```bash
scp tradingagents-cn-synology.tar.gz admin@你的群晖IP:/volume1/docker/
```

### 步骤3: 在群晖上部署

#### 通过SSH连接群晖
```bash
ssh admin@你的群晖IP
```

#### 运行部署脚本
```bash
cd /volume1/docker/synology-deploy
./deploy-synology.sh
```

### 步骤4: 验证部署

1. **检查容器状态**:
   ```bash
   docker ps
   ```

2. **查看日志**:
   ```bash
   docker logs tradingagents-cn
   ```

3. **访问应用**:
   - 打开浏览器访问: `http://你的群晖IP:8501`
   - 默认用户名: `admin`
   - 默认密码: `admin123`

## 🔧 配置管理

### 更新API密钥
1. 编辑 `/volume1/docker/synology-deploy/.env` 文件
2. 重启容器:
   ```bash
   docker-compose -f docker-compose.yml restart
   ```

### 备份数据
定期备份重要数据：
```bash
# 备份数据
docker cp tradingagents-cn:/app/data ./backup/
docker cp tradingagents-cn:/app/logs ./backup/
```

## 🐳 Docker管理命令

### 查看容器状态
```bash
docker ps -a
```

### 查看实时日志
```bash
docker logs -f tradingagents-cn
```

### 重启容器
```bash
docker restart tradingagents-cn
```

### 停止并删除容器
```bash
docker stop tradingagents-cn
docker rm tradingagents-cn
```

### 更新应用
```bash
cd /volume1/docker/synology-deploy
git pull  # 如果有更新
docker-compose down
docker-compose up -d --build
```

## 🌐 网络配置

### 端口转发
如果需要外网访问，在群晖路由器中设置端口转发：
- **外部端口**: 8501
- **内部IP**: 群晖IP
- **内部端口**: 8501

### 防火墙设置
1. 打开 **控制面板** → **安全性** → **防火墙**
2. 创建规则允许8501端口访问

## 🔍 故障排除

### 常见问题

1. **容器无法启动**
   ```bash
   # 检查Docker服务
   sudo systemctl status docker

   # 查看详细错误
   docker logs tradingagents-cn
   ```

2. **端口冲突**
   ```bash
   # 检查端口占用
   lsof -i :8501
   ```

3. **内存不足**
   - 在群晖控制面板中增加内存分配
   - 在docker-compose.yml中调整资源限制

4. **网络连接问题**
   ```bash
   # 检查网络连接
   docker exec -it tradingagents-cn ping google.com
   ```

## 📊 性能优化

### 调整Docker资源配置
编辑 `docker-compose.yml` 添加资源限制：
```yaml
services:
  tradingagents-cn:
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 1G
```

### 启用持久化存储
确保数据目录正确挂载：
```yaml
volumes:
  - /volume1/docker/tradingagents/data:/app/data
  - /volume1/docker/tradingagents/logs:/app/logs
```

## 🛠️ 维护建议

1. **定期更新**: 每月检查并更新镜像
2. **日志监控**: 定期清理日志文件
3. **数据备份**: 每周备份重要数据
4. **性能监控**: 监控内存和CPU使用情况

---

**🎉 恭喜！你的TradingAgents-CN应用现在运行在群晖NAS上了！**

*部署时间: $(date)*
*支持邮箱: 如有问题请查看日志或联系技术支持*