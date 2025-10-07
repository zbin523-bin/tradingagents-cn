# 🤖 使用Chrome DevTools自动化部署TradingAgents-CN到Render

## 📋 前提条件

1. **已安装Chrome浏览器**
2. **已登录GitHub账户**
3. **已登录Render账户**
4. **Chrome DevTools MCP工具已连接**

## 🚀 自动化部署步骤

### 步骤1：启动Chrome并导航到Render

1. 打开Chrome浏览器
2. 访问：https://dashboard.render.com
3. 登录您的Render账户

### 步骤2：创建新的Web Service

使用以下Chrome DevTools命令自动点击：

```javascript
// 等待页面加载完成
setTimeout(() => {
  // 查找并点击 "New+" 按钮
  const newButton = document.querySelector('[data-testid="new-service-button"]') ||
                     document.querySelector('button[aria-label*="New"]') ||
                     document.querySelector('a[href*="/new"]');

  if (newButton) {
    newButton.click();
    console.log("✅ 点击了New按钮");

    // 等待菜单加载
    setTimeout(() => {
      // 点击 "Web Service" 选项
      const webServiceOption = document.querySelector('a[href*="/web/new"]') ||
                           document.querySelector('[data-testid="web-service-option"]');

      if (webServiceOption) {
        webServiceOption.click();
        console.log("✅ 选择了Web Service");
      }
    }, 1000);
  }
}, 2000);
```

### 步骤3：连接GitHub仓库

```javascript
// 等待连接页面加载
setTimeout(() => {
  // 查找GitHub连接选项
  const githubTab = document.querySelector('[data-testid="github-tab"]') ||
                  document.querySelector('button[aria-label*="GitHub"]');

  if (githubTab) {
    githubTab.click();
    console.log("✅ 选择了GitHub选项");

    setTimeout(() => {
      // 查找您的仓库
      const仓库列表 = document.querySelectorAll('[data-testid="repository-list"] a');
      const targetRepo = Array.from(仓库列表).find(repo =>
        repo.textContent.includes('tradingagents-cn')
      );

      if (targetRepo) {
        targetRepo.click();
        console.log("✅ 选择了tradingagents-cn仓库");

        // 点击连接按钮
        setTimeout(() => {
          const connectBtn = document.querySelector('button[type="submit"]') ||
                           document.querySelector('[data-testid="connect-button"]');
          if (connectBtn) {
            connectBtn.click();
            console.log("✅ 点击了连接按钮");
          }
        }, 1000);
      }
    }, 2000);
  }
}, 3000);
```

### 步骤4：配置服务参数

```javascript
// 等待配置页面加载
setTimeout(() => {
  // 设置服务名称
  const nameInput = document.querySelector('input[name="name"]') ||
                   document.querySelector('#service-name');
  if (nameInput) {
    nameInput.value = 'tradingagents-cn';
    nameInput.dispatchEvent(new Event('input', { bubbles: true }));
    console.log("✅ 设置服务名称为 tradingagents-cn");
  }

  // 设置构建命令
  const buildInput = document.querySelector('input[name="buildCommand"]') ||
                    document.querySelector('#build-command');
  if (buildInput) {
    buildInput.value = 'pip install -r requirements.txt';
    buildInput.dispatchEvent(new Event('input', { bubbles: true }));
    console.log("✅ 设置构建命令");
  }

  // 设置启动命令
  const startInput = document.querySelector('input[name="startCommand"]') ||
                    document.querySelector('#start-command');
  if (startInput) {
    startInput.value = 'python start_render.py';
    startInput.dispatchEvent(new Event('input', { bubbles: true }));
    console.log("✅ 设置启动命令");
  }

  // 设置健康检查路径
  const healthInput = document.querySelector('input[name="healthCheckPath"]') ||
                     document.querySelector('#health-check-path');
  if (healthInput) {
    healthInput.value = '/_stcore/health';
    healthInput.dispatchEvent(new Event('input', { bubbles: true }));
    console.log("✅ 设置健康检查路径");
  }
}, 4000);
```

### 步骤5：添加环境变量

```javascript
// 添加环境变量的JavaScript代码
setTimeout(() => {
  const envTab = document.querySelector('[data-testid="environment-tab"]') ||
                 document.querySelector('button[aria-label*="Environment"]');

  if (envTab) {
    envTab.click();
    console.log("✅ 切换到环境变量标签");

    setTimeout(() => {
      // 添加必需的环境变量
      const envVars = [
        { key: 'PYTHONUNBUFFERED', value: '1' },
        { key: 'PORT', value: '8501' },
        { key: 'TAVILY_API_KEY', value: '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' },
        { key: 'DEEPSEEK_API_KEY', value: 'sk-43e5588b2aa547c9b977b374b45ddd37' },
        { key: 'SILICONFLOW_API_KEY', value: 'sk-goeenxldkpvuywhlgkwdqpzwzgodenvmpxprwluvgolrbzul' },
        { key: 'ALPHAVANTAGE_API_KEY', value: '5DGMRPMMEUBMX7PU' },
        key: 'FINNHUB_API_KEY', value: 'your_finnhub_key_here',
        key: 'POLYGON_API_KEY', value: 'hb0TuTgFLB603Xtyg_ephpjMpVc8W18L'
      ];

      envVars.forEach((envVar, index) => {
        setTimeout(() => {
          const addBtn = document.querySelector('[data-testid="add-env-var"]') ||
                        document.querySelector('button[aria-label*="Add environment variable"]');

          if (addBtn) {
            addBtn.click();

            setTimeout(() => {
              const keyInput = document.querySelector('input[name="key"]') ||
                           document.querySelector('#env-key');
              const valueInput = document.querySelector('input[name="value"]') ||
                             document.querySelector('#env-value');

              if (keyInput && valueInput) {
                keyInput.value = envVar.key;
                valueInput.value = envVar.value;

                keyInput.dispatchEvent(new Event('input', { bubbles: true }));
                valueInput.dispatchEvent(new Event('input', { bubbles: true }));

                console.log(`✅ 添加环境变量: ${envVar.key}`);

                // 点击保存按钮
                setTimeout(() => {
                  const saveBtn = document.querySelector('button[aria-label*="Save"]') ||
                                document.querySelector('[data-testid="save-env-var"]');
                  if (saveBtn) {
                    saveBtn.click();
                  }
                }, 500);
              }
            }, 500);
          }
        }, index * 1000);
      });
    }, 1000);
  }
}, 5000);
```

### 步骤6：创建服务

```javascript
// 最后创建服务
setTimeout(() => {
  const createBtn = document.querySelector('button[type="submit"]') ||
                   document.querySelector('[data-testid="create-service"]') ||
                   document.querySelector('button:has([data-testid="create-service"])');

  if (createBtn && !createBtn.disabled) {
    createBtn.click();
    console.log("✅ 点击创建服务按钮");
    console.log("🚀 部署已开始！");
  } else {
    console.log("⚠️ 创建按钮未找到或被禁用");
  }
}, 10000);
```

## 📊 监控部署进度

```javascript
// 监控部署状态
setInterval(() => {
  const statusElement = document.querySelector('[data-testid="service-status"]') ||
                       document.querySelector('.service-status') ||
                       document.querySelector('[class*="status"]');

  if (statusElement) {
    const status = statusElement.textContent;
    console.log(`📊 部署状态: ${status}`);
  }

  // 检查是否有错误
  const errorElement = document.querySelector('[data-testid="error-message"]') ||
                     document.querySelector('.error-message');
  if (errorElement) {
    console.error(`❌ 部署错误: ${errorElement.textContent}`);
  }
}, 5000);
```

## 🔧 使用方法

1. **打开Chrome开发者工具**
   - 按 F12 或右键选择"检查"
   - 切换到 "Console" 标签

2. **复制粘贴脚本**
   - 将上述JavaScript代码逐段复制到控制台
   - 每段代码之间等待执行完成

3. **监控进度**
   - 观察控制台输出的日志信息
   - 等待部署完成

4. **验证部署**
   - 部署完成后访问：https://tradingagents-cn.onrender.com
   - 测试基本功能

## ⚠️ 注意事项

1. **手动干预**：如果自动化脚本遇到问题，请手动完成剩余步骤
2. **网络连接**：确保网络连接稳定
3. **权限验证**：确保有足够的权限创建服务
4. **API密钥**：确保所有API密钥都正确配置

## 🎯 预期结果

自动化完成后，您将拥有：
- ✅ 在Render.com上运行的TradingAgents-CN应用
- ✅ 自动配置的环境变量
- ✅ 健康检查端点
- ✅ 可通过 https://tradingagents-cn.onrender.com 访问

---

**🚀 现在您可以开始使用Chrome自动化部署了！**