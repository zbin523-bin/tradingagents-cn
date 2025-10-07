// TradingAgents-CN Render 自动部署脚本
// 在Chrome开发者工具控制台中运行此脚本

console.log("🚀 开始TradingAgents-CN Render自动化部署...");

// 等待页面加载
function waitForElement(selector, timeout = 10000) {
  return new Promise((resolve, reject) => {
    const element = document.querySelector(selector);
    if (element) {
      return resolve(element);
    }

    const observer = new MutationObserver(() => {
      const element = document.querySelector(selector);
      if (element) {
        observer.disconnect();
        resolve(element);
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });

    setTimeout(() => {
      observer.disconnect();
      reject(new Error(`元素 ${selector} 未找到`));
    }, timeout);
  });
}

// 等待函数
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// 主部署函数
async function deployToRender() {
  try {
    console.log("📍 第1步：导航到创建Web Service页面");

    // 等待并点击 New+ 按钮
    const newButton = await waitForElement('[data-testid="new-service-button"], 5000);
    newButton.click();
    console.log("✅ 点击了New+按钮");

    await sleep(1000);

    // 点击 Web Service
    const webServiceLink = await waitForElement('a[href*="/web/new"]', 5000);
    webServiceLink.click();
    console.log("✅ 选择了Web Service");

    await sleep(2000);

    console.log("📍 第2步：连接GitHub仓库");

    // 等待并点击GitHub标签
    const githubTab = await waitForElement('[data-testid="github-tab"]', 5000);
    githubTab.click();
    console.log("✅ 选择了GitHub选项");

    await sleep(2000);

    // 查找并选择仓库
    const repositoryList = await waitForElement('[data-testid="repository-list"]', 10000);
    const repositories = repositoryList.querySelectorAll('a');
    const targetRepo = Array.from(repositories).find(repo =>
      repo.textContent.includes('tradingagents-cn')
    );

    if (targetRepo) {
      targetRepo.click();
      console.log("✅ 找到了tradingagents-cn仓库");

      await sleep(1000);

      // 点击连接按钮
      const connectBtn = await waitForElement('button[type="submit"]', 5000);
      connectBtn.click();
      console.log("✅ 连接了仓库");

      await sleep(3000);

      console.log("📍 第3步：配置服务参数");

      // 设置服务名称
      const nameInput = await waitForElement('input[name="name"]', 5000);
      if (nameInput) {
        nameInput.value = 'tradingagents-cn';
        nameInput.dispatchEvent(new Event('input', { bubbles: true }));
        console.log("✅ 设置服务名称");
      }

      // 设置构建命令
      const buildInput = await waitForElement('input[name="buildCommand"]', 5000);
      if (buildInput) {
        buildInput.value = 'pip install -r requirements.txt';
        buildInput.dispatchEvent(new Event('input', { bubbles: true }));
        console.log("✅ 设置构建命令");
      }

      // 设置启动命令
      const startInput = await waitForElement('input[name="startCommand"]', 5000);
      if (startInput) {
        startInput.value = 'python start_render.py';
        startInput.dispatchEvent(new Event('input', { bubbles: true }));
        console.log("✅ 设置启动命令");
      }

      // 设置健康检查路径
      const healthInput = await waitForElement('input[name="healthCheckPath"]', 5000);
      if (healthInput) {
        healthInput.value = '/_stcore/health';
        healthInput.dispatchEvent(new Event('input', { bubbles: true }));
        console.log("✅ 设置健康检查路径");
      }

      await sleep(2000);

      console.log("📍 第4步：添加环境变量");

      // 切换到环境变量标签
      const envTab = await waitForElement('[data-testid="environment-tab"]', 5000);
      envTab.click();
      console.log("✅ 切换到环境变量标签");

      await sleep(1000);

      // 环境变量列表
      const envVars = [
        { key: 'PYTHONUNBUFFERED', value: '1' },
        { key: 'PORT', value: '8501' },
        { key: 'TAVILY_API_KEY', value: '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' },
        { key: 'DEEPSEEK_API_KEY', value: 'sk-43e5588b2aa547c9b977b374b45ddd37' },
        { key: 'SILICONFLOW_API_KEY', value: 'sk-goeenxldkpvuywhlgkwdqpzwzgodenvmpxprwluvgolrbzul' },
        { key: 'ALPHAVANTAGE_API_KEY', value: '5DGMRPMMEUBMX7PU' },
        { key: 'FINNHUB_API_KEY', value: 'your_finnhub_key_here' },
        { key: 'POLYGON_API_KEY', value: 'hb0TuTgFLB603Xtyg_ephpjMpVc8W18L' }
      ];

      // 添加环境变量
      for (const envVar of envVars) {
        console.log(`📝 添加环境变量: ${envVar.key}`);

        // 查找添加按钮
        const addBtn = await waitForElement('[data-testid="add-env-var"], 3000);
        addBtn.click();

        await sleep(500);

        // 填写键和值
        const keyInput = await waitForElement('input[name="key"]', 3000);
        const valueInput = await waitForElement('input[name="value"]', 3000);

        if (keyInput && valueInput) {
          keyInput.value = envVar.key;
          valueInput.value = envVar.value;

          keyInput.dispatchEvent(new Event('input', { bubbles: true }));
          valueInput.dispatchEvent(new Event('input', { bubbles: true }));

          // 保存环境变量
          const saveBtn = await waitForElement('button[aria-label*="Save"]', 3000);
          saveBtn.click();

          await sleep(1000);
        }
      }

      await sleep(2000);

      console.log("📍 第5步：创建服务");

      // 查找并点击创建按钮
      const createBtn = await waitForElement('button[type="submit"]', 5000);
      if (createBtn && !createBtn.disabled) {
        createBtn.click();
        console.log("✅ 点击了创建服务按钮");
        console.log("🚀 部署已开始！");

        // 开始监控部署状态
        monitorDeployment();
      } else {
        console.error("❌ 创建按钮未找到或被禁用");
      }

    } else {
      console.error("❌ 未找到tradingagents-cn仓库");
    }

  } catch (error) {
    console.error("❌ 部署过程中出错:", error);
  }
}

// 监控部署状态
function monitorDeployment() {
  let checkCount = 0;
  const maxChecks = 60; // 最多检查5分钟

  const interval = setInterval(() => {
    checkCount++;

    // 检查是否有部署状态信息
    const statusElement = document.querySelector('[data-testid="service-status"]') ||
                         document.querySelector('.service-status') ||
                         document.querySelector('[class*="status"]');

    if (statusElement) {
      const status = statusElement.textContent.trim();
      console.log(`📊 部署状态检查 ${checkCount}: ${status}`);

      // 如果显示成功状态，停止监控
      if (status.includes('live') || status.includes('ready') || status.includes('success')) {
        console.log("🎉 部署成功！");
        console.log("🌐 应用地址: https://tradingagents-cn.onrender.com");
        clearInterval(interval);
        return;
      }
    }

    // 检查是否有错误
    const errorElement = document.querySelector('[data-testid="error-message"]') ||
                       document.querySelector('.error-message') ||
                       document.querySelector('[class*="error"]');

    if (errorElement) {
      const error = errorElement.textContent.trim();
      console.error(`❌ 部署错误: ${error}`);
      clearInterval(interval);
      return;
    }

    // 超时检查
    if (checkCount >= maxChecks) {
      console.log("⏰ 部署监控超时，请手动检查部署状态");
      clearInterval(interval);
    }
  }, 5000);
}

// 开始部署
deployToRender().catch(error => {
  console.error("❌ 自动部署失败:", error);
  console.log("💡 请按照CHROME_AUTOMATION_GUIDE.md中的手动步骤完成部署");
});