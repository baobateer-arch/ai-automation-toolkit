# AI 文档分析助手 - 前端

Vue 3 + Vite 前端界面，用于 AI PDF 文档分析 Demo。

## 启动方法

### 1. 安装依赖

```bash
cd frontend
npm install
```

### 2. 启动开发服务器

```bash
cd frontend
npm run dev
```

开发服务器默认运行在 `http://localhost:5173`，已配置 `/api` 代理到
`http://localhost:8000`。

### 3. 启动后端

在项目根目录启动 FastAPI 后端：

```bash
python main.py
```

### 4. 使用

1. 打开浏览器访问 `http://localhost:5173`
2. 选择或拖拽 PDF 文件
3. 点击"上传并分析"
4. 查看 AI 分析结果
   - 摘要（Summary）
   - 关键要点（Key Points）
   - 潜在风险（Risks）
   - 建议（Suggestions）

## 构建生产版本

```bash
npm run build
```

构建产物在 `dist/` 目录。

## 技术栈

- Vue 3（Composition API + `<script setup>`）
- Vite 6
- DeepSeek API（通过后端代理）
