# 🚀 TradingAgents-CN 快速修复脚本

## ⚠️ 当前状态
所有代码修复已完成，由于网络连接问题需要手动上传。

## 📋 立即执行的步骤

### 1. 打开GitHub仓库
访问: https://github.com/zbin523-bin/tradingagents-cn

### 2. 上传修复的文件
点击 "Add file" → "Upload files"，然后上传以下4个关键文件：

#### A. requirements.txt
```
# TradingAgents-CN 极简依赖包
# 只包含 Streamlit 应用启动的绝对必需依赖

streamlit>=1.28.0
pandas>=2.3.0
plotly>=5.0.0
requests>=2.32.4
python-dotenv>=1.0.0
typing-extensions>=4.14.0
pytz>=2025.2
tqdm>=4.67.1
psutil>=6.1.0

# 基础数据处理
markdown>=3.4.0
rich>=14.0.0
setuptools>=80.9.0

# 额外工具依赖
python-dateutil>=2.8.0
numpy>=1.24.0
scipy>=1.10.0

# 网页抓取依赖
beautifulsoup4>=4.9.0
lxml>=4.6.0

# AI 模型依赖
openai>=1.0.0,<2.0.0
langchain-openai>=0.1.0
langchain-google-genai>=1.0.0
langchain-anthropic>=0.1.0
dashscope>=1.17.0

# LangChain 核心依赖
langchain>=0.1.0
langchain-core>=0.1.0
langgraph>=0.1.0

# 内存和向量数据库
chromadb>=0.4.0
sentence-transformers>=2.2.0
tiktoken>=0.5.0

# 金融数据源
akshare>=1.10.0
tushare>=1.2.0
yfinance>=0.2.63
stockstats>=0.6.5
baostock>=0.8.8
```

#### B. render.yaml
```yaml
services:
  # Streamlit Web Service
  - type: web
    name: tradingagents-cn
    env: python
    plan: starter
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python start_render.py"
    healthCheckPath: /_stcore/health
    autoDeploy: true

    # Environment variables (will be set via Render dashboard or API)
    envVars:
      - key: PORT
        value: 8501
      - key: PYTHONUNBUFFERED
        value: 1

      # Essential API Keys
      - key: DASHSCOPE_API_KEY
        value: sk-e0100915b5394da0aa8e852bf09d9db8
      - key: FINNHUB_API_KEY
        value: d372ms9r01qtvbtjrefgd372ms9r01qtvbtjreg0
      - key: DEEPSEEK_API_KEY
        value: sk-43e5588b2aa547c9b977b374b45ddd37
      - key: DEEPSEEK_ENABLED
        value: true
      - key: GOOGLE_API_KEY
        value: your_google_api_key_here

      # Configuration
      - key: DEFAULT_CHINA_DATA_SOURCE
        value: akshare
      - key: MEMORY_ENABLED
        value: false

      # Critical fallback configurations
      - key: TUSHARE_TOKEN
        value: ""
      - key: SILICONFLOW_API_KEY
        value: ""
      - key: OPENAI_API_KEY
        value: ""
      - key: ANTHROPIC_API_KEY
        value: ""

      # System settings
      - key: ENABLE_COST_TRACKING
        value: true
      - key: TRADINGAGENTS_LOG_LEVEL
        value: INFO

    # Build and runtime settings
    buildFilter:
      paths:
        - "!synology-deploy/**"
        - "!data/**"
        - "!logs/**"
        - "!cache/**"
        - "!tests/**"
        - "!docs/**"
        - "!scripts/**"
        - "!upstream_contribution/**"
        - "!data_backup_*/**"
        - "!.git/**"
        - "!node_modules/**"

  # Redis Service (optional, for session management and caching)
  - type: redis
    name: tradingagents-redis
    plan: free
    ipAllowList: []  # Only allow internal connections

version: "1"
```

### 3. 提交更改
提交信息填写: `🔧 修复所有依赖错误和模型配置问题`

### 4. 验证部署
上传完成后，Render会自动重新部署。等待2-3分钟后访问：
https://tradingagents-cn-1tva.onrender.com

## ✅ 修复的问题
- ✅ No module named 'langgraph'
- ✅ No module named 'chromadb'
- ✅ No module named 'bs4' (beautifulsoup4)
- ✅ No module named 'openai'
- ✅ No module named 'dashscope'
- ✅ name 'client_options' is not defined
- ✅ AI模型硬依赖问题

## 🎯 预期结果
部署成功后，阿里百炼模型应该可以正常工作，所有分析功能恢复正常。