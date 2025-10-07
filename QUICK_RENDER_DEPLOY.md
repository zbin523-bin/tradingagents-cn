# 🚀 TradingAgents-CN 快速Render部署指南

## 📋 当前情况
- 您已有一个运行中的Render服务：`stock-analysis-system`
- URL: https://stock-analysis-system.onrender.com
- 服务ID: srv-d3337sndiees7397ac10
- 地区: Singapore

## 🎯 最快部署方案

### 方案1：更新现有服务（推荐）

1. **在Render控制台更新服务**：
   - 访问：https://dashboard.render.com/web/srv-d3337sndiees7397ac10
   - 点击 "Settings" 标签
   - 以下配置需要更新：

2. **更新构建配置**：
   ```
   Build Command: pip install -r requirements.txt
   Start Command: python start_render.py
   Health Check Path: /_stcore/health
   ```

3. **添加环境变量**：
   在Environment标签页添加：
   ```
   PYTHONUNBUFFERED=1
   PORT=8501
   DASHSCOPE_API_KEY=your_dashscope_key
   DEEPSEEK_API_KEY=your_deepseek_key
   SILICONFLOW_API_KEY=your_siliconflow_key
   TAVILY_API_KEY=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
   ALPHAVANTAGE_API_KEY=your_alpha_vantage_key
   TUSHARE_API_KEY=your_tushare_key
   FINNHUB_API_KEY=your_finnhub_key
   POLYGON_API_KEY=your_polygon_key
   ```

4. **触发部署**：
   - 点击 "Manual Deploy"
   - 选择 "Deploy latest commit"

### 方案2：创建新的独立服务

如果不想影响现有服务，可以创建新服务：

1. **创建新GitHub仓库**：
   - 访问GitHub并创建新仓库：`tradingagents-cn-deploy`
   - 将代码手动上传到GitHub

2. **在Render创建新服务**：
   - 访问：https://dashboard.render.com
   - 点击 "New+" → "Web Service"
   - 连接新创建的GitHub仓库
   - 使用我们准备好的配置

## 🔧 关键配置文件

项目已包含以下文件：
- `render.yaml` - Render配置
- `start_render.py` - 启动脚本
- `requirements.txt` - 依赖文件

## 📊 验证部署

部署完成后访问：
- 主应用：https://stock-analysis-system.onrender.com
- 健康检查：https://stock-analysis-system.onrender.com/_stcore/health

## 🎯 推荐步骤

1. **更新现有stock-analysis-system服务**（最快）
2. **如果成功，考虑创建独立的新服务**
3. **配置Redis缓存以提高性能**

---

**选择方案1最快，方案2更独立。您想选择哪个方案？**