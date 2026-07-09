<template>
  <div id="app">
    <nav class="nav"><div class="nav-inner">
      <span class="nav-logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Contract Risk AI</span>
      <div class="nav-links"><a href="#features">Features</a><a href="#pricing">Pricing</a><a href="#dashboard" class="btn btn-primary btn-sm">Upload Contract</a></div>
    </div></nav>
    <section class="hero"><div class="hero-inner">
      <h1 class="hero-title">Find hidden risks in your contracts before you sign.</h1>
      <p class="hero-sub">Upload a contract and get an AI-powered risk report in minutes.</p>
      <a href="#dashboard" class="btn btn-hero"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg> Upload your contract</a>
      <p class="hero-foot">No signup required. Your documents are private.</p>
    </div></section>

    <section class="section how-section">
      <h2 class="section-title centered">How It Works</h2>
      <div class="steps">
        <div class="step"><div class="step-num">1</div><h3>Upload</h3><p>Drop your PDF contract or agreement.</p></div>
        <div class="step-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><polyline points="9 18 15 12 9 6"/></svg></div>
        <div class="step"><div class="step-num">2</div><h3>AI Review</h3><p>DeepSeek AI analyzes clauses, risks, and gaps.</p></div>
        <div class="step-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><polyline points="9 18 15 12 9 6"/></svg></div>
        <div class="step"><div class="step-num">3</div><h3>Get Report</h3><p>Download a detailed risk report in PDF or DOCX.</p></div>
      </div>
    </section>
    <section id="features" class="section features-section">
      <h2 class="section-title centered">What You Get</h2>
      <div class="features-grid">
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3>Contract Risk Detection</h3><p>Identifies high-risk clauses that could cost you.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg></div><h3>Missing Clause Identification</h3><p>Finds important clauses that may be absent.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div><h3>Suggested Improvements</h3><p>Actionable edits to strengthen your position.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></div><h3>Key Obligation Summary</h3><p>Quick overview of what each party must do.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></div><h3>DOCX Export</h3><p>Editable Word documents.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></div><h3>PDF Export</h3><p>Professional report downloads.</p></div>
      </div>
    </section>
    <section id="pricing" class="section pricing-section">
      <h2 class="section-title centered">Simple Pricing</h2>
      <div class="pricing-grid">
        <div class="pricing-card"><h3>Starter</h3><p class="price"><span class="price-amt">$49</span> / contract</p><ul><li>Single contract review</li><li>Full AI risk report</li><li>PDF &amp; DOCX export</li><li>Email support</li></ul><a href="#dashboard" class="btn btn-primary btn-full">Upload your contract</a></div>
        <div class="pricing-card featured"><div class="badge">Popular</div><h3>Business</h3><p class="price"><span class="price-amt">$199</span> / 10 contracts</p><ul><li>10 contract reviews</li><li>Priority AI analysis</li><li>Bulk upload</li><li>Priority support</li></ul><a href="#dashboard" class="btn btn-primary btn-full">Get started</a></div>
      </div>
    </section>
    <section id="dashboard" class="section dashboard-section">
      <h2 class="section-title centered">Review Your Contract</h2>
      <div class="upload-section">
        <div class="drop-zone" :class="{ 'has-file': selectedFile, 'dragover': isDragover, 'loading': uploading }"
          @dragover.prevent="isDragover = true" @dragleave.prevent="isDragover = false" @drop.prevent="onDrop">
          <div v-if="!selectedFile" class="drop-placeholder">
            <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <p class="drop-text">Drop your PDF contract here</p>
            <p class="drop-hint">or click to browse files</p>
          </div>
          <div v-else class="file-info">
            <svg class="file-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
            <div class="file-details"><p class="file-name">{{ selectedFile.name }}</p><p class="file-size">{{ formatSize(selectedFile.size) }}</p></div>
          </div>
        </div>
        <div class="upload-actions">
          <input ref="fileInput" type="file" accept=".pdf" class="file-input" @change="onFileSelect" />
          <button class="btn btn-select" @click="selectFile" :disabled="uploading">{{ selectedFile ? 'Change file' : 'Select PDF' }}</button>
          <button class="btn btn-upload" :class="{ 'btn-loading': uploading }" :disabled="!selectedFile || uploading" @click="uploadFile">
            <span v-if="uploading" class="spinner"></span>
            <span v-else><svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg> Analyze Contract</span>
          </button>
        </div>
        <p v-if="error" class="error-message">{{ error }}</p>
      </div>
      <section v-if="result" class="results-section">
        <h2 class="section-title">Analysis Result</h2>
        <div class="risk-badge" :class="'risk-' + (result.risk_level || '').toLowerCase()">Risk Level: <strong>{{ result.risk_level || 'N/A' }}</strong></div>
        <div class="card card-summary"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>Summary</h3><p class="card-text">{{ result.summary }}</p></div>
        <div class="card card-risks"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>High Risks</h3>
          <ul class="card-list"><li v-for="(risk, i) in result.high_risks" :key="i" class="list-item">{{ risk }}</li><li v-if="!result.high_risks?.length" class="list-item empty">None identified</li></ul></div>
        <div class="card card-points"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>Missing Clauses</h3>
          <ul class="card-list"><li v-for="(c, i) in result.missing_clauses" :key="i" class="list-item">{{ c }}</li><li v-if="!result.missing_clauses?.length" class="list-item empty">All key clauses present</li></ul></div>
        <div class="card card-suggestions"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>Suggestions</h3>
          <ul class="card-list"><li v-for="(s, i) in result.suggestions" :key="i" class="list-item">{{ s }}</li><li v-if="!result.suggestions?.length" class="list-item empty">No suggestions</li></ul></div>
        <div v-if="result.id" class="export-actions">
          <a :href="'/api/reports/' + result.id + '/export/pdf'" class="btn btn-download" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download PDF</a>
          <a :href="'/api/reports/' + result.id + '/export/docx'" class="btn btn-download" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg> Download DOCX</a>
        </div>
      </section>
      <section class="history-section">
        <h2 class="section-title"><span>My Reviews</span></h2>
        <div v-if="showDemo" class="demo-grid">
          <div v-for="d in demos" :key="d.id" class="demo-card" :class="'risk-' + d.risk_level.toLowerCase()" @click="viewDemo(d)">
            <div class="demo-badge" :class="'risk-' + d.risk_level.toLowerCase()">{{ d.risk_level }}</div>
            <h3 class="demo-title">{{ d.title }}</h3>
            <p class="demo-summary">{{ d.summary.slice(0, 80) }}...</p>
          </div>
        </div>
        <div v-if="detail" class="results-section">
          <h2 class="section-title"><button class="btn btn-back" @click="closeDetail"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><polyline points="15 18 9 12 15 6"/></svg> Back</button></h2>
          <div class="risk-badge" :class="'risk-' + (detail.risk_level || '').toLowerCase()">Risk Level: <strong>{{ detail.risk_level || 'N/A' }}</strong></div>
          <div class="card card-summary"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>Summary</h3><p class="card-text">{{ detail.summary }}</p></div>
          <div class="card card-risks"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>High Risks</h3>
            <ul class="card-list"><li v-for="(r, i) in detail.high_risks" :key="i" class="list-item">{{ r }}</li><li v-if="!detail.high_risks?.length" class="list-item empty">None identified</li></ul></div>
          <div class="card card-points"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>Missing Clauses</h3>
            <ul class="card-list"><li v-for="(c, i) in detail.missing_clauses" :key="i" class="list-item">{{ c }}</li><li v-if="!detail.missing_clauses?.length" class="list-item empty">All key clauses present</li></ul></div>
          <div class="card card-suggestions"><h3 class="card-title"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>Suggestions</h3>
            <ul class="card-list"><li v-for="(s, i) in detail.suggestions" :key="i" class="list-item">{{ s }}</li><li v-if="!detail.suggestions?.length" class="list-item empty">No suggestions</li></ul></div>
        </div>
        <div v-if="reports.length && !detail" class="report-list">
          <div v-for="r in reports" :key="r.id" class="history-card" @click="viewReport(r.id)">
            <div class="history-card-body"><svg class="history-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              <div class="history-info"><p class="history-filename">{{ r.filename }}</p><p class="history-summary">{{ r.summary }}</p></div></div>
          </div>
        </div>
        <p v-if="!reports.length && !demoViewed && !detail && !result" class="empty-hint">No reviews yet. Upload a contract above or try a demo.</p>
      </section>
    </section>
    <footer class="footer"><p>&copy; 2026 Contract Risk AI. Built for small businesses.</p></footer>
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
const showDemo = ref(true)
const demoViewed = ref(false)
const demos = [
  { id: 'demo-1', title: 'NDA Agreement', risk_level: 'Medium',
    summary: 'This NDA has reasonable confidentiality terms but includes a broad non-compete clause extending 3 years post-termination, which may be unenforceable in some jurisdictions.',
    high_risks: ['Non-compete clause extends 3 years post-termination','Confidentiality definition includes "any information" without limitation','Indemnification clause heavily favors disclosing party'],
    missing_clauses: ['No mutual non-disclosure provisions','No data breach notification requirement','No governing law or jurisdiction clause'],
    suggestions: ['Limit non-compete to 1 year and specific business areas','Narrow confidentiality definition to marked written information','Add mutual indemnification with financial caps'] },
  { id: 'demo-2', title: 'Freelance Contract', risk_level: 'High',
    summary: 'This freelance agreement grants broad intellectual property transfer without clear scope. Payment terms are vague and the termination clause allows for immediate cancellation without cause.',
    high_risks: ['All IP assigned "works made for hire" without limitation','No payment schedule or late fee penalty','Client can terminate without notice or cause'],
    missing_clauses: ['No scope of work or deliverable definition','No revision or change order process','No limitation of liability clause','No dispute resolution mechanism'],
    suggestions: ['Define specific deliverables with acceptance criteria','Add milestone-based payment schedule with late penalties','Include 30-day notice requirement for termination','Cap liability at contract value'] },
  { id: 'demo-3', title: 'Software Service Agreement', risk_level: 'Low',
    summary: 'A well-structured SaaS agreement with clear SLAs and data protection provisions. Some minor areas for improvement around auto-renewal and data portability.',
    high_risks: ['Auto-renewal clause lacks opt-out reminder','Service credits as sole remedy for downtime'],
    missing_clauses: ['No data portability or export provisions','No SLA credit escalation for repeated outages'],
    suggestions: ['Add 30-day renewal notice requirement','Include customer data export mechanism on termination','Add SLA credit escalation for recurring incidents'] },
]
onMounted(() => { loadReports(); showDemo.value = reports.value.length === 0 })
async function loadReports() { try { const r = await fetch(REPORTS_URL); if (r.ok) { const d = await r.json(); reports.value = d; showDemo.value = d.length === 0 } } catch {} }
async function viewReport(id) { detail.value = null; try { const r = await fetch(REPORTS_URL + '/' + id); if (r.ok) { detail.value = await r.json(); demoViewed.value = true } } catch { error.value = 'Failed to load report details' } }
function viewDemo(demo) { detail.value = { ...demo }; demoViewed.value = true }
function closeDetail() { detail.value = null }
function selectFile() { fileInput.value?.click() }
function onFileSelect(e) { const f = e.target.files[0]; if (f) validateAndSet(f) }
function onDrop(e) { isDragover.value = false; const f = e.dataTransfer.files[0]; if (f) validateAndSet(f) }
function validateAndSet(file) { error.value = ''; result.value = null; detail.value = null; if (file.type !== 'application/pdf' && !file.name.toLowerCase().endsWith('.pdf')) { error.value = 'Please select a PDF file'; return }; if (file.size > 50 * 1024 * 1024) { error.value = 'File size must be under 50MB'; return }; selectedFile.value = file }
async function uploadFile() {
  if (!selectedFile.value) return; uploading.value = true; error.value = ''; result.value = null; detail.value = null
  const fd = new FormData(); fd.append('file', selectedFile.value)
  try { const r = await fetch(API_URL, { method: 'POST', body: fd }); if (!r.ok) { const d = await r.json().catch(() => ({})); throw new Error(d.detail || 'Server error (' + r.status + ')') }; result.value = await r.json(); showDemo.value = false; await loadReports() }
  catch (err) { if (err.message.includes('Failed to fetch') || err.message.includes('NetworkError')) { error.value = 'Cannot connect to server. Please make sure the backend is running.' } else { error.value = err.message } }
  finally { uploading.value = false; isDragover.value = false }
}
function formatSize(bytes) { if (!bytes) return '0 B'; const u = ['B','KB','MB','GB']; let i = 0; let s = bytes; while (s >= 1024 && i < u.length - 1) { s /= 1024; i++ }; return s.toFixed(1) + ' ' + u[i] }
</script>
<style>
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --bg: #f8fafc; --surface: #fff; --primary: #2563eb; --primary-hover: #1d4ed8;
  --text: #0f172a; --text-muted: #64748b; --border: #e2e8f0;
  --success: #059669; --warning: #d97706; --danger: #dc2626;
  --radius: 12px; --shadow: 0 1px 3px rgba(0,0,0,.06); --shadow-lg: 0 10px 15px -3px rgba(0,0,0,.08);
}
body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; -webkit-font-smoothing: antialiased; }
#app { max-width: 780px; margin: 0 auto; padding: 0 20px; }
.nav { position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,.85); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); }
.nav-inner { max-width: 780px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 14px 0; }
.nav-logo { display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 16px; }
.nav-logo svg { color: var(--primary); }
.nav-links { display: flex; align-items: center; gap: 24px; }
.nav-links a { text-decoration: none; font-size: 14px; font-weight: 500; color: var(--text-muted); transition: color .15s; }
.nav-links a:hover { color: var(--text); }
.hero { text-align: center; padding: 80px 0 60px; }
.hero-title { font-size: 36px; font-weight: 800; line-height: 1.15; letter-spacing: -1px; max-width: 600px; margin: 0 auto; }
.hero-sub { font-size: 17px; color: var(--text-muted); margin-top: 16px; }
.hero-foot { font-size: 13px; color: var(--text-muted); margin-top: 24px; opacity: .7; }
.btn-hero { display: inline-flex; align-items: center; gap: 8px; margin-top: 28px; padding: 14px 32px; background: var(--primary); color: #fff; border-radius: 10px; font-size: 15px; font-weight: 600; text-decoration: none; transition: background .15s; }
.btn-hero:hover { background: var(--primary-hover); }
.section { padding: 48px 0; }
.section-title { font-size: 22px; font-weight: 700; margin-bottom: 28px; }
.section-title.centered { text-align: center; }
.steps { display: flex; align-items: flex-start; justify-content: center; text-align: center; }
.step { flex: 1; max-width: 180px; }
.step-num { width: 40px; height: 40px; border-radius: 50%; background: var(--primary); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700; margin: 0 auto 12px; }
.step h3 { font-size: 15px; font-weight: 600; margin-bottom: 4px; }
.step p { font-size: 13px; color: var(--text-muted); }
.step-arrow { display: flex; align-items: center; padding-top: 8px; color: var(--border); }
.features-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.feature-card { background: var(--surface); border-radius: var(--radius); padding: 24px; box-shadow: var(--shadow); border: 1px solid var(--border); }
.feature-icon { width: 40px; height: 40px; border-radius: 10px; background: #eff6ff; display: flex; align-items: center; justify-content: center; margin-bottom: 12px; color: var(--primary); }
.feature-card h3 { font-size: 15px; font-weight: 600; margin-bottom: 6px; }
.feature-card p { font-size: 13px; color: var(--text-muted); }
.pricing-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.pricing-card { background: var(--surface); border-radius: var(--radius); padding: 32px; box-shadow: var(--shadow); border: 1px solid var(--border); text-align: center; position: relative; }
.pricing-card.featured { border-color: var(--primary); box-shadow: 0 0 0 1px var(--primary), var(--shadow-lg); }
.badge { position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: var(--primary); color: #fff; font-size: 12px; font-weight: 600; padding: 4px 14px; border-radius: 20px; }
.pricing-card h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; }
.price { font-size: 14px; color: var(--text-muted); margin-bottom: 20px; }
.price-amt { font-size: 32px; font-weight: 800; }
.pricing-card ul { list-style: none; margin-bottom: 24px; }
.pricing-card li { padding: 6px 0; font-size: 14px; }
.pricing-card li::before { content: '?'; color: var(--success); margin-right: 8px; font-weight: 700; }
.btn-full { display: block; text-align: center; width: 100%; }
.dashboard-section { border-top: 1px solid var(--border); padding-top: 48px; }
.upload-section { margin-bottom: 32px; }
.drop-zone { border: 2px dashed var(--border); border-radius: var(--radius); padding: 48px 20px; text-align: center; cursor: pointer; transition: all .2s; background: var(--surface); box-shadow: var(--shadow); }
.drop-zone:hover, .drop-zone.dragover { border-color: var(--primary); background: #f0f7ff; }
.drop-zone.loading { opacity: .6; pointer-events: none; }
.upload-icon { width: 48px; height: 48px; color: var(--primary); margin-bottom: 12px; }
.drop-text { font-size: 16px; font-weight: 600; }
.drop-hint { font-size: 13px; color: var(--text-muted); margin-top: 4px; }
.has-file { border-style: solid; border-color: var(--primary); }
.file-info { display: flex; align-items: center; gap: 16px; justify-content: center; }
.file-icon { width: 36px; height: 36px; color: var(--danger); flex-shrink: 0; }
.file-details { text-align: left; }
.file-name { font-weight: 600; font-size: 15px; word-break: break-all; }
.file-size { font-size: 13px; color: var(--text-muted); }
.file-input { display: none; }
.upload-actions { display: flex; gap: 12px; justify-content: center; margin-top: 20px; }
.btn { display: inline-flex; align-items: center; gap: 8px; padding: 10px 24px; border-radius: 8px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; transition: all .15s; line-height: 1; text-decoration: none; }
.btn:disabled { opacity: .5; cursor: not-allowed; }
.btn-sm { padding: 8px 16px; font-size: 13px; }
.btn-primary { background: var(--primary); color: #fff; }
.btn-primary:hover { background: var(--primary-hover); }
.btn-select { background: var(--surface); color: var(--text); border: 1px solid var(--border); }
.btn-select:hover:not(:disabled) { background: #f1f5f9; }
.btn-upload { background: var(--primary); color: #fff; }
.btn-upload:hover:not(:disabled) { background: var(--primary-hover); }
.btn-back { display: inline-flex; align-items: center; gap: 4px; padding: 6px 12px; border-radius: 6px; font-size: 13px; font-weight: 600; border: 1px solid var(--border); cursor: pointer; background: var(--surface); color: var(--text-muted); }
.btn-back:hover { background: #f1f5f9; color: var(--text); }
.spinner { display: inline-block; width: 16px; height: 16px; border: 2px solid rgba(255,255,255,.3); border-top-color: #fff; border-radius: 50%; animation: spin .6s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.error-message { text-align: center; margin-top: 16px; padding: 12px 16px; background: #fef2f2; color: var(--danger); border-radius: 8px; font-size: 14px; border: 1px solid #fecaca; }
.results-section { margin-top: 8px; }
.risk-badge { display: inline-flex; align-items: center; gap: 8px; padding: 8px 18px; border-radius: 20px; font-size: 14px; font-weight: 500; margin-bottom: 20px; }
.risk-low { background: #ecfdf5; color: var(--success); }
.risk-medium { background: #fffbeb; color: var(--warning); }
.risk-high { background: #fef2f2; color: var(--danger); }
.card { background: var(--surface); border-radius: var(--radius); padding: 24px; margin-bottom: 16px; box-shadow: var(--shadow); }
.card-summary { border-left: 4px solid var(--primary); }
.card-points { border-left: 4px solid var(--success); }
.card-risks { border-left: 4px solid var(--warning); }
.card-suggestions { border-left: 4px solid #8b5cf6; }
.card-title { display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600; margin-bottom: 12px; }
.card-icon { width: 20px; height: 20px; flex-shrink: 0; }
.card-summary .card-icon { color: var(--primary); }
.card-points .card-icon { color: var(--success); }
.card-risks .card-icon { color: var(--warning); }
.card-suggestions .card-icon { color: #8b5cf6; }
.card-text { font-size: 15px; line-height: 1.7; }
.card-list { list-style: none; }
.list-item { position: relative; padding: 8px 0 8px 20px; font-size: 14px; line-height: 1.6; }
.list-item::before { content: ''; position: absolute; left: 0; top: 15px; width: 6px; height: 6px; border-radius: 50%; background: var(--text-muted); }
.list-item + .list-item { border-top: 1px solid var(--border); }
.list-item.empty { color: var(--text-muted); font-style: italic; }
.list-item.empty::before { display: none; }
.export-actions { display: flex; gap: 10px; margin-top: 20px; }
.btn-download { display: inline-flex; align-items: center; gap: 6px; padding: 8px 18px; border-radius: 6px; font-size: 13px; font-weight: 600; text-decoration: none; cursor: pointer; transition: all .15s; background: var(--surface); color: var(--text-muted); border: 1px solid var(--border); }
.btn-download:hover { background: #f1f5f9; color: var(--primary); border-color: var(--primary); }
.demo-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-bottom: 28px; }
.demo-card { background: var(--surface); border-radius: var(--radius); padding: 20px; box-shadow: var(--shadow); border: 1px solid var(--border); cursor: pointer; transition: all .15s; }
.demo-card:hover { box-shadow: var(--shadow-lg); transform: translateY(-2px); }
.demo-card.risk-low { border-left: 3px solid var(--success); }
.demo-card.risk-medium { border-left: 3px solid var(--warning); }
.demo-card.risk-high { border-left: 3px solid var(--danger); }
.demo-badge { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; margin-bottom: 8px; }
.demo-badge.risk-low { background: #ecfdf5; color: var(--success); }
.demo-badge.risk-medium { background: #fffbeb; color: var(--warning); }
.demo-badge.risk-high { background: #fef2f2; color: var(--danger); }
.demo-title { font-size: 15px; font-weight: 600; margin-bottom: 6px; }
.demo-summary { font-size: 13px; color: var(--text-muted); line-height: 1.5; }
.history-section { margin-top: 8px; }
.section-title { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.report-list { margin-top: 8px; }
.history-card { background: var(--surface); border-radius: var(--radius); margin-bottom: 12px; box-shadow: var(--shadow); cursor: pointer; }
.history-card:hover { box-shadow: var(--shadow-lg); }
.history-card-body { display: flex; align-items: flex-start; gap: 14px; padding: 18px 20px; }
.history-icon { width: 28px; height: 28px; flex-shrink: 0; color: var(--danger); margin-top: 2px; }
.history-info { flex: 1; min-width: 0; }
.history-filename { font-weight: 600; font-size: 15px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.history-summary { font-size: 13px; color: var(--text-muted); margin-top: 4px; line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.empty-hint { text-align: center; padding: 48px 20px; color: var(--text-muted); font-size: 14px; }
.footer { text-align: center; padding: 40px 0; font-size: 13px; color: var(--text-muted); border-top: 1px solid var(--border); margin-top: 40px; }
@media (max-width: 640px) { .hero-title { font-size: 28px; } .steps { flex-direction: column; align-items: center; gap: 16px; } .step-arrow { transform: rotate(90deg); } .features-grid { grid-template-columns: 1fr; } .pricing-grid { grid-template-columns: 1fr; } .demo-grid { grid-template-columns: 1fr; } .nav-links a:not(.btn) { display: none; } }
</style>
