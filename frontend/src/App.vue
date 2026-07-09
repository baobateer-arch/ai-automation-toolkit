<template>
  <div class="app">
    <header class="header">
      <div class="header-content">
        <h1>AI 文档分析助手</h1>
        <p class="subtitle">上传 PDF 文档，由 DeepSeek AI 智能分析</p>
      </div>
    </header>

    <main class="main">
      <!-- Upload Area -->
      <section class="upload-section">
        <div
          class="drop-zone"
          :class="{ 'has-file': selectedFile, 'dragover': isDragover, 'loading': uploading }"
          @dragover.prevent="isDragover = true"
          @dragleave.prevent="isDragover = false"
          @drop.prevent="onDrop"
        >
          <div v-if="!selectedFile" class="drop-placeholder">
            <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M12 16V4m0 0L8 8m4-4l4 4" />
              <path d="M20 16v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2" />
            </svg>
            <p class="drop-text">拖拽 PDF 文件到此处</p>
            <p class="drop-hint">或点击下方按钮选择文件</p>
          </div>
          <div v-else class="file-info">
            <svg class="file-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z" />
              <polyline points="14 2 14 8 20 8" />
              <line x1="9" y1="15" x2="15" y2="15" />
            </svg>
            <div class="file-details">
              <p class="file-name">{{ selectedFile.name }}</p>
              <p class="file-size">{{ formatSize(selectedFile.size) }}</p>
            </div>
          </div>
        </div>

        <div class="upload-actions">
          <input
            ref="fileInput"
            type="file"
            accept=".pdf"
            class="file-input"
            @change="onFileSelect"
          />
          <button class="btn btn-select" @click="selectFile" :disabled="uploading">
            {{ selectedFile ? '重新选择' : '选择 PDF 文件' }}
          </button>
          <button
            class="btn btn-upload"
            :class="{ 'btn-loading': uploading }"
            :disabled="!selectedFile || uploading"
            @click="uploadFile"
          >
            <span v-if="uploading" class="spinner"></span>
            <span v-else>
              <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4" />
                <polyline points="17 8 12 3 7 8" />
                <line x1="12" y1="3" x2="12" y2="15" />
              </svg>
              上传并分析
            </span>
          </button>
        </div>

        <p v-if="error" class="error-message">{{ error }}</p>
      </section>

      <!-- Current Result -->
      <section v-if="result" class="results-section">
        <h2 class="section-title">分析结果</h2>

        <div class="card card-summary">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z" />
              <polyline points="14 2 14 8 20 8" />
              <line x1="16" y1="13" x2="8" y2="13" />
              <line x1="16" y1="17" x2="8" y2="17" />
            </svg>
            摘要
          </h3>
          <p class="card-text">{{ result.summary }}</p>
        </div>

        <div class="card card-points">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10" />
              <line x1="12" y1="16" x2="12" y2="12" />
              <line x1="12" y1="8" x2="12.01" y2="8" />
            </svg>
            关键要点
          </h3>
          <ul class="card-list">
            <li v-for="(point, i) in result.key_points" :key="i" class="list-item">{{ point }}</li>
            <li v-if="!result.key_points.length" class="list-item empty">暂无</li>
          </ul>
        </div>

        <div class="card card-risks">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" />
              <line x1="12" y1="9" x2="12" y2="13" />
              <line x1="12" y1="17" x2="12.01" y2="17" />
            </svg>
            潜在风险
          </h3>
          <ul class="card-list">
            <li v-for="(risk, i) in result.risks" :key="i" class="list-item">{{ risk }}</li>
            <li v-if="!result.risks.length" class="list-item empty">未识别出明显风险</li>
          </ul>
        </div>

        <div class="card card-suggestions">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="12" y1="1" x2="12" y2="23" />
              <path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6" />
            </svg>
            建议
          </h3>
          <ul class="card-list">
            <li v-for="(suggestion, i) in result.suggestions" :key="i" class="list-item">{{ suggestion }}</li>
            <li v-if="!result.suggestions.length" class="list-item empty">暂无建议</li>
          </ul>
        </div>
      </section>

      <!-- Detail View -->
      <section v-if="detail" class="results-section">
        <h2 class="section-title">
          <button class="btn-back" @click="detail = null">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18">
              <polyline points="15 18 9 12 15 6" />
            </svg>
            返回
          </button>
          {{ detail.filename }}
          <div class="detail-actions">
            <a :href="`/api/reports/${detail.id}/export/pdf`" class="btn btn-download" download>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14">
                <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4" /><polyline points="7 10 12 15 17 10" /><line x1="12" y1="15" x2="12" y2="3" />
              </svg>
              下载 PDF
            </a>
            <a :href="`/api/reports/${detail.id}/export/docx`" class="btn btn-download" download>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14">
                <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z" /><polyline points="14 2 14 8 20 8" /><line x1="16" y1="13" x2="8" y2="13" /><line x1="16" y1="17" x2="8" y2="17" />
              </svg>
              下载 Word
            </a>
          </div>
        </h2>

        <div class="card card-summary">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z" />
              <polyline points="14 2 14 8 20 8" />
              <line x1="16" y1="13" x2="8" y2="13" />
              <line x1="16" y1="17" x2="8" y2="17" />
            </svg>
            摘要
          </h3>
          <p class="card-text">{{ detail.summary }}</p>
        </div>

        <div class="card card-points">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10" />
              <line x1="12" y1="16" x2="12" y2="12" />
              <line x1="12" y1="8" x2="12.01" y2="8" />
            </svg>
            关键要点
          </h3>
          <ul class="card-list">
            <li v-for="(point, i) in detail.key_points" :key="i" class="list-item">{{ point }}</li>
            <li v-if="!detail.key_points.length" class="list-item empty">暂无</li>
          </ul>
        </div>

        <div class="card card-risks">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" />
              <line x1="12" y1="9" x2="12" y2="13" />
              <line x1="12" y1="17" x2="12.01" y2="17" />
            </svg>
            潜在风险
          </h3>
          <ul class="card-list">
            <li v-for="(risk, i) in detail.risks" :key="i" class="list-item">{{ risk }}</li>
            <li v-if="!detail.risks.length" class="list-item empty">未识别出明显风险</li>
          </ul>
        </div>

        <div class="card card-suggestions">
          <h3 class="card-title">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="12" y1="1" x2="12" y2="23" />
              <path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6" />
            </svg>
            建议
          </h3>
          <ul class="card-list">
            <li v-for="(suggestion, i) in detail.suggestions" :key="i" class="list-item">{{ suggestion }}</li>
            <li v-if="!detail.suggestions.length" class="list-item empty">暂无建议</li>
          </ul>
        </div>
      </section>

      <!-- History List -->
      <section v-if="reports.length && !detail" class="history-section">
        <h2 class="section-title">历史报告</h2>
        <div v-for="r in reports" :key="r.id" class="history-card" @click="viewReport(r.id)">
          <div class="history-card-body">
            <svg class="history-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z" />
              <polyline points="14 2 14 8 20 8" />
            </svg>
            <div class="history-info">
              <p class="history-filename">{{ r.filename }}</p>
              <p class="history-summary">{{ r.summary }}</p>
              <p class="history-date">{{ r.created_at }}</p>
            </div>
          </div>
        </div>
      </section>

      <p v-if="!reports.length && !result && !detail" class="empty-hint">暂无分析记录，请上传 PDF 文件开始分析</p>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const API_URL = '/api/analyze-pdf'
const REPORTS_URL = '/api/reports'

const fileInput = ref(null)
const selectedFile = ref(null)
const uploading = ref(false)
const error = ref('')
const result = ref(null)
const isDragover = ref(false)
const reports = ref([])
const detail = ref(null)

onMounted(() => {
  loadReports()
})

async function loadReports() {
  try {
    const resp = await fetch(REPORTS_URL)
    if (resp.ok) {
      reports.value = await resp.json()
    }
  } catch {
    // silently fail
  }
}

async function viewReport(id) {
  detail.value = null
  try {
    const resp = await fetch(`${REPORTS_URL}/${id}`)
    if (resp.ok) {
      detail.value = await resp.json()
    }
  } catch {
    error.value = '加载报告详情失败'
  }
}

function selectFile() {
  fileInput.value?.click()
}

function onFileSelect(e) {
  const file = e.target.files[0]
  if (file) validateAndSet(file)
}

function onDrop(e) {
  isDragover.value = false
  const file = e.dataTransfer.files[0]
  if (file) validateAndSet(file)
}

function validateAndSet(file) {
  error.value = ''
  result.value = null
  if (file.type !== 'application/pdf' && !file.name.toLowerCase().endsWith('.pdf')) {
    error.value = '请选择 PDF 格式的文件'
    return
  }
  if (file.size > 50 * 1024 * 1024) {
    error.value = '文件大小不能超过 50MB'
    return
  }
  selectedFile.value = file
}

async function uploadFile() {
  if (!selectedFile.value) return

  uploading.value = true
  error.value = ''
  result.value = null
  detail.value = null

  const formData = new FormData()
  formData.append('file', selectedFile.value)

  try {
    const resp = await fetch(API_URL, {
      method: 'POST',
      body: formData,
    })
    if (!resp.ok) {
      const data = await resp.json().catch(() => ({}))
      throw new Error(data.detail || `服务器错误 (${resp.status})`)
    }
    const data = await resp.json()
    result.value = data
    // Refresh history
    await loadReports()
  } catch (err) {
    if (err.message.includes('Failed to fetch') || err.message.includes('NetworkError')) {
      error.value = '无法连接到服务器，请确认后端已启动'
    } else {
      error.value = err.message
    }
  } finally {
    uploading.value = false
    isDragover.value = false
  }
}

function formatSize(bytes) {
  if (!bytes) return '0 B'
  const units = ['B', 'KB', 'MB', 'GB']
  let i = 0
  let size = bytes
  while (size >= 1024 && i < units.length - 1) { size /= 1024; i++ }
  return `${size.toFixed(1)} ${units[i]}`
}
</script>

<style>
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --bg: #f4f6f9;
  --surface: #ffffff;
  --primary: #2563eb;
  --primary-hover: #1d4ed8;
  --text: #1e293b;
  --text-secondary: #64748b;
  --border: #e2e8f0;
  --success: #059669;
  --warning: #d97706;
  --danger: #dc2626;
  --radius: 12px;
  --shadow: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans SC', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  min-height: 100vh;
}

.app {
  max-width: 720px;
  margin: 0 auto;
  padding: 0 20px 60px;
}

.header {
  text-align: center;
  padding: 48px 0 32px;
}

.header h1 {
  font-size: 28px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.5px;
}

.subtitle {
  margin-top: 8px;
  font-size: 15px;
  color: var(--text-secondary);
}

.upload-section {
  margin-bottom: 32px;
}

.drop-zone {
  border: 2px dashed var(--border);
  border-radius: var(--radius);
  padding: 40px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
  background: var(--surface);
  box-shadow: var(--shadow);
}

.drop-zone:hover,
.drop-zone.dragover {
  border-color: var(--primary);
  background: #f0f7ff;
}

.drop-zone.loading {
  opacity: 0.6;
  pointer-events: none;
}

.upload-icon {
  width: 48px;
  height: 48px;
  color: var(--primary);
  margin-bottom: 12px;
}

.drop-text {
  font-size: 16px;
  font-weight: 600;
  color: var(--text);
}

.drop-hint {
  font-size: 13px;
  color: var(--text-secondary);
  margin-top: 4px;
}

.has-file {
  border-style: solid;
  border-color: var(--primary);
}

.file-info {
  display: flex;
  align-items: center;
  gap: 16px;
  justify-content: center;
}

.file-icon {
  width: 36px;
  height: 36px;
  color: var(--danger);
  flex-shrink: 0;
}

.file-details {
  text-align: left;
}

.file-name {
  font-weight: 600;
  font-size: 15px;
  word-break: break-all;
}

.file-size {
  font-size: 13px;
  color: var(--text-secondary);
}

.file-input {
  display: none;
}

.upload-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
  margin-top: 20px;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 24px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
  line-height: 1;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-select {
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}

.btn-select:hover:not(:disabled) {
  background: #f1f5f9;
}

.btn-upload {
  background: var(--primary);
  color: white;
  box-shadow: 0 1px 3px rgba(37, 99, 235, 0.3);
}

.btn-upload:hover:not(:disabled) {
  background: var(--primary-hover);
  box-shadow: 0 2px 6px rgba(37, 99, 235, 0.4);
}

.btn-icon {
  width: 16px;
  height: 16px;
}

.btn-loading {
  opacity: 0.85;
}

.spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-message {
  text-align: center;
  margin-top: 16px;
  padding: 12px 16px;
  background: #fef2f2;
  color: var(--danger);
  border-radius: 8px;
  font-size: 14px;
  border: 1px solid #fecaca;
}

.results-section {
  margin-top: 8px;
}

.section-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-back {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  border: 1px solid var(--border);
  cursor: pointer;
  background: var(--surface);
  color: var(--text-secondary);
  transition: all 0.2s;
}

.btn-back:hover {

.detail-actions {
  display: flex;
  gap: 8px;
  margin-left: auto;
  flex-shrink: 0;
}

.btn-download {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s;
  background: var(--surface);
  color: var(--text-secondary);
  border: 1px solid var(--border);
}

.btn-download:hover {
  background: #f1f5f9;
  color: var(--primary);
  border-color: var(--primary);
}
  background: #f1f5f9;
  color: var(--text);
}

.card {
  background: var(--surface);
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 16px;
  box-shadow: var(--shadow);
}

.card-summary { border-left: 4px solid var(--primary); }
.card-points { border-left: 4px solid var(--success); }
.card-risks { border-left: 4px solid var(--warning); }
.card-suggestions { border-left: 4px solid #8b5cf6; }

.card-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  color: var(--text);
}

.card-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.card-summary .card-icon { color: var(--primary); }
.card-points .card-icon { color: var(--success); }
.card-risks .card-icon { color: var(--warning); }
.card-suggestions .card-icon { color: #8b5cf6; }

.card-text {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text);
}

.card-list {
  list-style: none;
}

.list-item {
  position: relative;
  padding: 8px 0 8px 20px;
  font-size: 15px;
  line-height: 1.6;
  color: var(--text);
}

.list-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 16px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--text-secondary);
}

.list-item + .list-item {
  border-top: 1px solid var(--border);
}

.list-item.empty {
  color: var(--text-secondary);
  font-style: italic;
}

.list-item.empty::before {
  display: none;
}

.history-section {
  margin-top: 40px;
}

.history-card {
  background: var(--surface);
  border-radius: var(--radius);
  margin-bottom: 12px;
  box-shadow: var(--shadow);
  cursor: pointer;
  transition: all 0.2s;
}

.history-card:hover {
  box-shadow: var(--shadow-lg);
  border-color: var(--primary);
}

.history-card-body {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 18px 20px;
}

.history-icon {
  width: 28px;
  height: 28px;
  flex-shrink: 0;
  color: var(--danger);
  margin-top: 2px;
}

.history-info {
  flex: 1;
  min-width: 0;
}

.history-filename {
  font-weight: 600;
  font-size: 15px;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.history-summary {
  font-size: 13px;
  color: var(--text-secondary);
  margin-top: 4px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.history-date {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 4px;
}

.empty-hint {
  text-align: center;
  padding: 48px 20px;
  color: var(--text-secondary);
  font-size: 14px;
}
</style>
