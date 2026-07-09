<template>
  <div class="dash">
    <nav class="dash-nav"><div class="nav-inner">
      <router-link to="/" class="nav-logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Contract Risk AI</router-link>
      <div class="nav-links"><span class="user-email">{{ userEmail }}</span><button class="btn btn-sm btn-logout" @click="handleLogout">Log out</button></div>
    </div></nav>
    <main class="dash-main">
      <h2 class="section-title">Review a Contract</h2>
      <div class="upload-section">
        <div class="drop-zone" :class="{ 'has-file': selectedFile, 'dragover': isDragover, 'loading': uploading }" @dragover.prevent="isDragover = true" @dragleave.prevent="isDragover = false" @drop.prevent="onDrop">
          <div v-if="!selectedFile" class="drop-placeholder">
            <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <p class="drop-text">Drop your PDF contract here</p><p class="drop-hint">or click to browse files</p>
          </div>
          <div v-else class="file-info">
            <svg class="file-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
            <div class="file-details"><p class="file-name">{{ selectedFile.name }}</p><p class="file-size">{{ formatSize(selectedFile.size) }}</p></div>
          </div>
        </div>
        <div class="upload-actions">
          <input ref="fileInput" type="file" accept=".pdf" class="file-input" @change="onFileSelect" />
          <button class="btn btn-select" @click="selectFile" :disabled="uploading">{{ selectedFile ? 'Change file' : 'Select PDF' }}</button>
          <button class="btn btn-upload" :class="{ 'btn-loading': uploading }" :disabled="!selectedFile || uploading" @click="uploadFile"><span v-if="uploading" class="spinner"></span><span v-if="uploading" style="font-size:13px;padding-left:4px">Analyzing...</span><span v-else>Analyze Contract</span></button>
        </div>
        <p v-if="error" class="error-message">{{ error }}</p>
      </div>
      <section v-if="result" class="results-section">
        <h2 class="section-title">Analysis Result</h2>
        <div class="risk-badge" :class="'risk-' + (result.risk_level || '').toLowerCase()">Risk Level: <strong>{{ result.risk_level || 'N/A' }}</strong></div>
        <div class="card card-summary"><h3 class="card-title">Summary</h3><p class="card-text">{{ result.summary }}</p></div>
        <div class="card card-risks"><h3 class="card-title">High Risks</h3><ul class="card-list"><li v-for="(r,i) in result.high_risks" :key="i" class="list-item">{{ r }}</li><li v-if="!result.high_risks?.length" class="list-item empty">None identified</li></ul></div>
        <div class="card card-points"><h3 class="card-title">Missing Clauses</h3><ul class="card-list"><li v-for="(c,i) in result.missing_clauses" :key="i" class="list-item">{{ c }}</li><li v-if="!result.missing_clauses?.length" class="list-item empty">All key clauses present</li></ul></div>
        <div class="card card-suggestions"><h3 class="card-title">Suggestions</h3><ul class="card-list"><li v-for="(s,i) in result.suggestions" :key="i" class="list-item">{{ s }}</li><li v-if="!result.suggestions?.length" class="list-item empty">No suggestions</li></ul></div>
        <div v-if="result.id" class="export-actions">
          <button class="btn btn-download" @click="downloadPDF(result.id)">Download PDF</button>
          <button class="btn btn-download" @click="downloadDOCX(result.id)">Download DOCX</button>
        </div>
      </section>
      <section class="history-section">
        <h2 class="section-title">My Contract Reviews</h2>
        <div v-if="showDemo" class="demo-grid">
          <div v-for="d in demos" :key="d.id" class="demo-card" :class="'risk-' + d.risk_level.toLowerCase()" @click="viewDemo(d)">
            <div class="demo-badge" :class="'risk-' + d.risk_level.toLowerCase()">{{ d.risk_level }}</div><h3 class="demo-title">{{ d.title }}</h3><p class="demo-summary">{{ d.summary.slice(0, 80) }}...</p>
          </div>
        </div>
        <div v-if="detail" class="results-section">
          <h2 class="section-title"><button class="btn btn-back" @click="closeDetail">&larr; Back</button></h2>
          <div class="risk-badge" :class="'risk-' + (detail.risk_level || '').toLowerCase()">Risk Level: <strong>{{ detail.risk_level || 'N/A' }}</strong></div>
          <div class="card card-summary"><h3 class="card-title">Summary</h3><p class="card-text">{{ detail.summary }}</p></div>
          <div class="card card-risks"><h3 class="card-title">High Risks</h3><ul class="card-list"><li v-for="(r,i) in detail.high_risks" :key="i" class="list-item">{{ r }}</li><li v-if="!detail.high_risks?.length" class="list-item empty">None identified</li></ul></div>
          <div class="card card-points"><h3 class="card-title">Missing Clauses</h3><ul class="card-list"><li v-for="(c,i) in detail.missing_clauses" :key="i" class="list-item">{{ c }}</li><li v-if="!detail.missing_clauses?.length" class="list-item empty">All key clauses present</li></ul></div>
          <div class="card card-suggestions"><h3 class="card-title">Suggestions</h3><ul class="card-list"><li v-for="(s,i) in detail.suggestions" :key="i" class="list-item">{{ s }}</li><li v-if="!detail.suggestions?.length" class="list-item empty">No suggestions</li></ul></div>
        </div>
        <div v-if="reports.length && !detail" class="report-list">
          <div v-for="r in reports" :key="r.id" class="history-card" @click="viewReport(r.id)">
            <div class="history-card-body"><svg class="history-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              <div class="history-info"><p class="history-filename">{{ r.filename }}</p><p class="history-summary">{{ r.summary }}</p></div></div>
          </div>
        </div>
        <p v-if="!reports.length && !detail && !result && !uploading" class="empty-hint">No reviews yet. Upload a contract or try a demo.</p>
      </section>
    </main>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import request from '../api/request.js'
const router = useRouter()
const fileInput = ref(null); const selectedFile = ref(null); const uploading = ref(false)
const error = ref(''); const result = ref(null); const isDragover = ref(false)
const reports = ref([]); const detail = ref(null); const showDemo = ref(true)
const userEmail = ref(localStorage.getItem('user_email') || 'User')
const demos = [
  { id:'demo-1',title:'Freelance Agreement',risk_level:'Medium',
    summary:'Standard freelance contract with reasonable terms but some unclear areas.',
    high_risks:['Payment terms unclear','Scope of work undefined'],
    missing_clauses:['No late payment penalty','No change order process'],
    suggestions:['Add clear payment schedule with milestones','Define specific deliverables and acceptance criteria'] },
  { id:'demo-2',title:'NDA Agreement',risk_level:'Low',
    summary:'Standard mutual NDA with reasonable confidentiality terms.',
    high_risks:['Confidentiality period not specified'],
    missing_clauses:['No data breach notification requirement','No jurisdiction clause'],
    suggestions:['Define confidentiality period explicitly','Add governing law provision'] },
  { id:'demo-3',title:'Software Service Agreement',risk_level:'High',
    summary:'SaaS agreement with significant liability exposure for the customer.',
    high_risks:['Unlimited liability clause','Missing termination clause','No SLA guarantees'],
    missing_clauses:['No data portability provisions','No service level commitments','No limitation of liability'],
    suggestions:['Add liability cap at contract value','Include 30-day termination notice','Define specific SLA metrics and remedies'] },
]
onMounted(() => { loadReports() })
async function loadReports() { try { const r = await request.get('/reports'); reports.value = r.data; showDemo.value = r.data.length === 0 } catch {} }
async function viewReport(id) { detail.value = null; try { detail.value = (await request.get('/reports/' + id)).data } catch { error.value = 'Failed to load report' } }
function viewDemo(d) { detail.value = { ...d } }
function closeDetail() { detail.value = null }
function handleLogout() { localStorage.removeItem('token'); localStorage.removeItem('user_email'); router.push('/') }
function selectFile() { fileInput.value?.click() }
function onFileSelect(e) { const f = e.target.files[0]; if (f) validateAndSet(f) }
function onDrop(e) { isDragover.value = false; const f = e.dataTransfer.files[0]; if (f) validateAndSet(f) }
function validateAndSet(file) { error.value='';result.value=null;detail.value=null;if(file.type!=='application/pdf'&&!file.name.endsWith('.pdf')){error.value='Please select a PDF file';return};if(file.size>50*1024*1024){error.value='File must be under 50MB';return};selectedFile.value=file }
async function uploadFile() {
  if (!selectedFile.value) return; uploading.value=true;error.value='';result.value=null;detail.value=null
  const fd=new FormData();fd.append('file',selectedFile.value)
  try { const r=await request.post('/analyze-pdf',fd,{headers:{'Content-Type':'multipart/form-data'}});result.value=r.data;showDemo.value=false;await loadReports() }
  catch(err){if(err.response){error.value=err.response.data?.detail||'Server error'}else if(err.request){error.value='Cannot connect to server'}else{error.value='Upload failed'}}
  finally{uploading.value=false;isDragover.value=false}
}
async function downloadPDF(id){try{const r=await request.get('/reports/'+id+'/export/pdf',{responseType:'blob'});const u=window.URL.createObjectURL(new Blob([r.data]));const a=document.createElement('a');a.href=u;a.download='report_'+id+'.pdf';document.body.appendChild(a);a.click();a.remove();window.URL.revokeObjectURL(u)}catch{error.value='Download failed'}}
async function downloadDOCX(id){try{const r=await request.get('/reports/'+id+'/export/docx',{responseType:'blob'});const u=window.URL.createObjectURL(new Blob([r.data]));const a=document.createElement('a');a.href=u;a.download='report_'+id+'.docx';document.body.appendChild(a);a.click();a.remove();window.URL.revokeObjectURL(u)}catch{error.value='Download failed'}}
function formatSize(bytes){if(!bytes)return'0 B';const u=['B','KB','MB','GB'];let i=0;let s=bytes;while(s>=1024&&i<u.length-1){s/=1024;i++}return s.toFixed(1)+' '+u[i]}
</script>
<style>
.dash{max-width:780px;margin:0 auto;padding:0 20px 60px}
.dash-nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.85);backdrop-filter:blur(12px);border-bottom:1px solid #e2e8f0}
.dash-nav .nav-inner{max-width:780px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:14px 0}
.dash-nav .nav-logo{display:flex;align-items:center;gap:8px;font-weight:700;font-size:16px;color:#0f172a;text-decoration:none}
.dash-nav .nav-logo svg{color:#2563eb}
.dash-nav .nav-links{display:flex;align-items:center;gap:16px}
.user-email{font-size:13px;color:#64748b}
.btn-logout{padding:6px 14px;font-size:13px;border-radius:6px;background:transparent;color:#64748b;border:1px solid #e2e8f0;cursor:pointer;transition:all .15s}
.btn-logout:hover{background:#f1f5f9;color:#dc2626;border-color:#dc2626}
.dash-main{padding:32px 0}
.section-title{font-size:22px;font-weight:700;margin-bottom:24px;color:#0f172a}
.upload-section{margin-bottom:32px}
.drop-zone{border:2px dashed #e2e8f0;border-radius:12px;padding:48px 20px;text-align:center;cursor:pointer;transition:all .2s;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.drop-zone:hover,.drop-zone.dragover{border-color:#2563eb;background:#f0f7ff}
.drop-zone.loading{opacity:.6;pointer-events:none}
.upload-icon{width:48px;height:48px;color:#2563eb;margin-bottom:12px}
.drop-text{font-size:16px;font-weight:600;color:#0f172a}
.drop-hint{font-size:13px;color:#64748b;margin-top:4px}
.has-file{border-style:solid;border-color:#2563eb}
.file-info{display:flex;align-items:center;gap:16px;justify-content:center}
.file-icon{width:36px;height:36px;color:#dc2626;flex-shrink:0}
.file-details{text-align:left}
.file-name{font-weight:600;font-size:15px;word-break:break-all;color:#0f172a}
.file-size{font-size:13px;color:#64748b}
.file-input{display:none}
.upload-actions{display:flex;gap:12px;justify-content:center;margin-top:20px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:10px 24px;border-radius:8px;font-size:14px;font-weight:600;border:none;cursor:pointer;transition:all .15s;line-height:1;text-decoration:none;color:#fff}
.btn:disabled{opacity:.5;cursor:not-allowed}
.btn-select{background:#fff;color:#0f172a;border:1px solid #e2e8f0;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.btn-select:hover:not(:disabled){background:#f1f5f9}
.btn-upload{background:#2563eb;box-shadow:0 1px 3px rgba(37,99,235,.3)}
.btn-upload:hover:not(:disabled){background:#1d4ed8}
.btn-back{padding:6px 12px;border-radius:6px;font-size:13px;font-weight:600;border:1px solid #e2e8f0;cursor:pointer;background:#fff;color:#64748b}
.btn-back:hover{background:#f1f5f9;color:#0f172a}
.spinner{display:inline-block;width:16px;height:16px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.error-message{text-align:center;margin-top:16px;padding:12px 16px;background:#fef2f2;color:#dc2626;border-radius:8px;font-size:14px;border:1px solid #fecaca}
.results-section{margin-top:8px}
.risk-badge{display:inline-flex;align-items:center;gap:8px;padding:8px 18px;border-radius:20px;font-size:14px;font-weight:500;margin-bottom:20px}
.risk-low{background:#ecfdf5;color:#059669}
.risk-medium{background:#fffbeb;color:#d97706}
.risk-high{background:#fef2f2;color:#dc2626}
.card{background:#fff;border-radius:12px;padding:24px;margin-bottom:16px;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.card-summary{border-left:4px solid #2563eb}
.card-points{border-left:4px solid #059669}
.card-risks{border-left:4px solid #d97706}
.card-suggestions{border-left:4px solid #8b5cf6}
.card-title{font-size:15px;font-weight:600;margin-bottom:12px;color:#0f172a}
.card-text{font-size:15px;line-height:1.7;color:#0f172a}
.card-list{list-style:none}
.list-item{position:relative;padding:8px 0 8px 20px;font-size:14px;line-height:1.6;color:#0f172a}
.list-item::before{content:'';position:absolute;left:0;top:15px;width:6px;height:6px;border-radius:50%;background:#64748b}
.list-item+.list-item{border-top:1px solid #e2e8f0}
.list-item.empty{color:#64748b;font-style:italic}
.list-item.empty::before{display:none}
.export-actions{display:flex;gap:10px;margin-top:20px}
.btn-download{padding:8px 18px;border-radius:6px;font-size:13px;font-weight:600;cursor:pointer;background:#fff;color:#64748b;border:1px solid #e2e8f0;transition:all .15s;text-decoration:none}
.btn-download:hover{background:#f1f5f9;color:#2563eb;border-color:#2563eb}
.demo-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:28px}
.demo-card{background:#fff;border-radius:12px;padding:20px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0;cursor:pointer;transition:all .15s}
.demo-card:hover{box-shadow:0 10px 15px -3px rgba(0,0,0,.08);transform:translateY(-2px)}
.demo-card.risk-low{border-left:3px solid #059669}
.demo-card.risk-medium{border-left:3px solid #d97706}
.demo-card.risk-high{border-left:3px solid #dc2626}
.demo-badge{display:inline-block;padding:2px 10px;border-radius:12px;font-size:11px;font-weight:600;margin-bottom:8px;color:#fff}
.demo-badge.risk-low{background:#059669;color:#059669!important;background:#ecfdf5}
.demo-badge.risk-medium{background:#d97706;color:#d97706!important;background:#fffbeb}
.demo-badge.risk-high{background:#dc2626;color:#dc2626!important;background:#fef2f2}
.demo-title{font-size:15px;font-weight:600;margin-bottom:6px;color:#0f172a}
.demo-summary{font-size:13px;color:#64748b;line-height:1.5}
.history-section{margin-top:8px}
.section-title{display:flex;align-items:center;justify-content:space-between;gap:12px}
.report-list{margin-top:8px}
.history-card{background:#fff;border-radius:12px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,.06);cursor:pointer}
.history-card:hover{box-shadow:0 10px 15px -3px rgba(0,0,0,.08)}
.history-card-body{display:flex;align-items:flex-start;gap:14px;padding:18px 20px}
.history-icon{width:28px;height:28px;flex-shrink:0;color:#dc2626;margin-top:2px}
.history-info{flex:1;min-width:0}
.history-filename{font-weight:600;font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#0f172a}
.history-summary{font-size:13px;color:#64748b;margin-top:4px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.empty-hint{text-align:center;padding:48px 20px;color:#64748b;font-size:14px}
</style>
