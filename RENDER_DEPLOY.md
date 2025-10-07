# TradingAgents-CN Render.com 部署指南

## 📋 部署准备

### 1. 环境要求
- **Python**: 3.11+
- **平台**: Render.com账号
- **代码仓库**: GitHub仓库（推荐）

### 2. 必需API密钥
在部署前，请在Render的环境变量中配置以下API密钥：

```bash
# AI模型API
DASHSCOPE_API_KEY=your_dashscope_key
DEEPSEEK_API_KEY=your_deepseek_key
SILICONFLOW_API_KEY=your_siliconflow_key

# 金融数据API
TAVILY_API_KEY=your_tavily_key
ALPHAVANTAGE_API_KEY=your_alpha_vantage_key
TUSHARE_API_KEY=your_tushare_key
FINNHUB_API_KEY=your_finnhub_key
POLYGON_API_KEY=your_polygon_key

# 其他配置
PYTHONUNBUFFERED=1
PORT=8501
```

## 🚀 部署步骤

### 方法1: 通过Render MCP工具部署（推荐）

1. **确保已配置Render MCP工具**
2. **使用MCP工具自动部署**：
   - MCP工具将自动创建Web服务
   - 自动配置环境变量
   - 自动部署应用

### 方法2: 手动部署

1. **连接GitHub仓库**
   - 在Render.com控制台中创建新的Web Service
   - 连接到包含TradingAgents-CN代码的GitHub仓库

2. **配置部署设置**
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python start_render.py`
   - Health Check Path: `/_stcore/health`

3. **设置环境变量**
   在Render控制台的Environment标签页中添加所有必需的API密钥

4. **部署应用**
   - 点击"Create Web Service"开始部署
   - 等待构建和部署完成

## 🔧 配置说明

### render.yaml配置文件
项目根目录的`render.yaml`文件包含了完整的部署配置：
- Web服务配置
- Redis缓存服务（可选）
- 自动部署设置
- 构建过滤器（排除不必要的文件）

### 启动脚本
`start_render.py`是专门为Render优化的启动脚本：
- 自动安装依赖
- 创建必要目录
- 配置Streamlit参数
- 错误处理和日志输出

## 📊 功能特性

### 支持的功能
- ✅ 股票分析（美股、A股、港股）
- ✅ 多AI模型支持
- ✅ 实时数据获取
- ✅ 报告生成和导出
- ✅ 用户认证系统
- ✅ 分析历史记录

### 优化特性
- 🚀 自动构建和部署
- 📈 Redis缓存支持
- 🔒 安全的环境变量管理
- 📋 健康检查
- 🛠️ 错误日志和监控

## 🔍 验证部署

### 1. 检查部署状态
访问Render控制台查看服务状态：
- ✅ 绿色状态表示运行正常
- 📊 查看构建日志排查问题
- 🔍 访问应用URL测试功能

### 2. 功能测试
1. **访问应用**: 使用Render提供的URL
2. **用户登录**: 使用默认账号（admin/admin123）
3. **股票分析**: 测试股票代码分析功能
4. **报告生成**: 验证分析报告生成

## 🐛 故障排除

### 常见问题

1. **构建失败**
   - 检查requirements.txt是否完整
   - 确认Python版本兼容性
   - 查看构建日志中的错误信息

2. **应用启动失败**
   - 检查环境变量配置
   - 确认启动命令正确
   - 查看运行时日志

3. **API调用失败**
   - 验证API密钥有效性
   - 检查网络连接
   - 确认API配额充足

4. **内存不足**
   - 升级Render服务计划
   - 优化代码内存使用
   - 配置Redis缓存

### 日志查看
- **构建日志**: Render控制台的Build Logs标签页
- **运行日志**: Render控制台的Logs标签页
- **应用日志**: 应用内部的日志系统

## 📈 性能优化

### 建议配置
- **服务计划**: Starter（小型）或Standard（中型）
- **Redis**: 启用Redis缓存提高性能
- **CDN**: 使用Render的全球CDN加速

### 监控指标
- 响应时间
- 内存使用率
- CPU使用率
- 错误率

## 🔄 更新部署

### 自动部署
- 启用Auto Deploy功能
- 推送到GitHub自动触发部署

### 手动部署
- 在Render控制台点击"Manual Deploy"
- 选择最新的commit进行部署

## 💡 最佳实践

1. **环境管理**
   - 使用不同的分支进行开发和测试
   - 配置独立的测试和生产环境

2. **安全考虑**
   - 定期更新API密钥
   - 监控应用访问日志
   - 配置适当的访问权限

3. **备份策略**
   - 定期备份分析数据
   - 使用GitHub进行代码版本管理
   - 导出重要的配置和数据

---

**🎉 部署完成后，您的TradingAgents-CN应用将在Render.com上运行！**

*最后更新: 2025-10-07*