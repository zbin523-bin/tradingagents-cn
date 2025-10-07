# TradingAgents-CN 安装部署完成指南

## 🎉 部署状态

✅ **项目已成功安装并运行！**

## 📋 已完成的配置

### 1. 项目克隆
- ✅ 从GitHub克隆TradingAgents-CN项目到本地目录

### 2. Python环境配置
- ✅ 安装Python 3.11.13 (通过Homebrew)
- ✅ 升级pip到最新版本
- ✅ 安装项目核心依赖

### 3. API密钥配置
- ✅ 创建 `.env` 环境配置文件
- ✅ 配置以下API服务：
  - **Tavily搜索API**: [已配置]
  - **DeepSeek**: [已配置]
  - **硅基流动**: [已配置]
  - **Alpha Vantage**: [已配置]
  - **TuShare Pro**: [已配置]
  - **Finnhub**: [已配置]
  - **Polygon.io**: [已配置]

### 4. MCP工具配置
- ✅ **Tavily MCP**: 搜索和内容提取功能
- ✅ **Render MCP**: 应用部署和管理功能

### 5. Web应用部署
- ✅ Streamlit Web界面已启动
- ✅ 运行在 `http://localhost:8501`

## 🚀 如何使用

### 启动Web应用
```bash
cd /Users/zhangbin/TradingAgents-CN
python3.11 start_web.py
```

### 访问界面
- 浏览器打开: `http://localhost:8501`
- 界面语言: 中文
- 支持功能: 股票分析、新闻获取、报告生成

### 主要功能
1. **多市场支持**: 美股、A股、港股
2. **智能分析**: 5级研究深度 (2-25分钟)
3. **多LLM模型**: 支持OpenAI、DeepSeek、Google AI等
4. **实时数据**: 新闻、财务数据、技术指标
5. **专业报告**: 支持Markdown/Word/PDF导出

## 🔧 高级配置

### 环境变量自定义
编辑 `.env` 文件来修改API密钥或添加新的配置

### MCP工具管理
```bash
# 查看已安装的MCP工具
claude mcp list

# 添加新的MCP工具
claude mcp add <tool-name> <config>

# 移除MCP工具
claude mcp remove <tool-name>
```

### 数据库配置
项目支持MongoDB和Redis，如需使用请：
1. 安装并启动MongoDB: `brew install mongodb-community`
2. 安装并启动Redis: `brew install redis`
3. 修改 `.env` 文件中的数据库连接配置

## 📊 支持的股票代码格式

- **🇺🇸 美股**: `AAPL`, `TSLA`, `MSFT`, `NVDA`, `GOOGL`
- **🇨🇳 A股**: `000001`, `600519`, `300750`, `002415`
- **🇭🇰 港股**: `0700.HK`, `9988.HK`, `3690.HK`, `1810.HK`

## 🎯 使用建议

1. **首次使用**: 建议从1级或2级分析开始
2. **深度分析**: 3级分析为推荐级别 (6-10分钟)
3. **模型选择**: 根据需求选择不同的LLM模型
4. **数据源**: 可配置多个数据源以提高准确性

## 🛠️ 故障排除

### 如果Web应用无法启动
1. 检查Python版本: `python3.11 --version`
2. 重新安装依赖: `pip3.11 install streamlit plotly`
3. 检查端口占用: `lsof -i :8501`

### 如果API调用失败
1. 检查 `.env` 文件中的API密钥
2. 确认网络连接正常
3. 检查API配额是否充足

### 如果MCP工具连接失败
1. 重新配置MCP工具
2. 检查API密钥有效性
3. 查看Claude Code日志

## 📚 相关资源

- **项目文档**: `/Users/zhangbin/TradingAgents-CN/docs/`
- **GitHub仓库**: https://github.com/hsliuping/TradingAgents-CN
- **原项目**: https://github.com/TauricResearch/TradingAgents

---

**🎉 恭喜！TradingAgents-CN已成功部署，可以开始使用了！**

*部署完成时间: 2025-10-05*
*部署环境: macOS + Python 3.11 + Streamlit*