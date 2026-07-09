<template>
  <div class="landing">
    <nav class="nav"><div class="nav-inner">
      <router-link to="/" class="nav-logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Contract Risk AI</router-link>
      <div class="nav-links"><router-link to="/login">Sign In</router-link><router-link to="/register" class="btn btn-primary btn-sm">Try Free</router-link></div>
    </div></nav>
    <section class="hero"><div class="hero-inner">
      <h1 class="hero-title">Find hidden risks in your contracts before you sign.</h1>
      <p class="hero-sub">Upload a contract and get an AI-powered risk report in minutes.</p>
      <router-link to="/register" class="btn btn-hero"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg> Upload your contract</router-link>
      <p class="hero-foot">Free to try. No credit card required.</p>
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
        <div class="pricing-card"><h3>Starter</h3><p class="price"><span class="price-amt">$49</span> / contract</p><ul><li>Single contract review</li><li>Full AI risk report</li><li>PDF &amp; DOCX export</li></ul><router-link to="/register" class="btn btn-primary btn-full">Get started</router-link></div>
        <div class="pricing-card featured"><div class="badge">Popular</div><h3>Business</h3><p class="price"><span class="price-amt">$199</span> / 10 contracts</p><ul><li>10 contract reviews</li><li>Priority AI analysis</li><li>Bulk upload</li></ul><router-link to="/register" class="btn btn-primary btn-full">Get started</router-link></div>
      </div>
    </section>
    <footer class="footer"><p>&copy; 2026 Contract Risk AI. Built for small businesses.</p></footer>
  </div>
</template>
<script setup>
</script>
<style>
.landing{max-width:780px;margin:0 auto;padding:0 20px}
.nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.85);backdrop-filter:blur(12px);border-bottom:1px solid #e2e8f0}
.nav-inner{max-width:780px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:14px 0}
.nav-logo{display:flex;align-items:center;gap:8px;font-weight:700;font-size:16px;color:#0f172a;text-decoration:none}
.nav-logo svg{color:#2563eb}
.nav-links{display:flex;align-items:center;gap:24px}
.nav-links a{text-decoration:none;font-size:14px;font-weight:500;color:#64748b;transition:color .15s}
.nav-links a:hover{color:#0f172a}
.hero{text-align:center;padding:80px 0 60px}
.hero-title{font-size:36px;font-weight:800;line-height:1.15;letter-spacing:-1px;max-width:600px;margin:0 auto}
.hero-sub{font-size:17px;color:#64748b;margin-top:16px}
.hero-foot{font-size:13px;color:#64748b;margin-top:24px;opacity:.7}
.btn-hero{display:inline-flex;align-items:center;gap:8px;margin-top:28px;padding:14px 32px;background:#2563eb;color:#fff;border-radius:10px;font-size:15px;font-weight:600;text-decoration:none;transition:background .15s}
.btn-hero:hover{background:#1d4ed8}
.section{padding:48px 0}
.section-title{font-size:22px;font-weight:700;margin-bottom:28px}
.section-title.centered{text-align:center}
.steps{display:flex;align-items:flex-start;justify-content:center;text-align:center}
.step{flex:1;max-width:180px}
.step-num{width:40px;height:40px;border-radius:50%;background:#2563eb;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;margin:0 auto 12px}
.step h3{font-size:15px;font-weight:600;margin-bottom:4px}
.step p{font-size:13px;color:#64748b}
.step-arrow{display:flex;align-items:center;padding-top:8px;color:#e2e8f0}
.features-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.feature-card{background:#fff;border-radius:12px;padding:24px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0}
.feature-icon{width:40px;height:40px;border-radius:10px;background:#eff6ff;display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:#2563eb}
.feature-card h3{font-size:15px;font-weight:600;margin-bottom:6px}
.feature-card p{font-size:13px;color:#64748b}
.pricing-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.pricing-card{background:#fff;border-radius:12px;padding:32px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0;text-align:center;position:relative}
.pricing-card.featured{border-color:#2563eb;box-shadow:0 0 0 1px #2563eb,0 10px 15px -3px rgba(0,0,0,.08)}
.badge{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:#2563eb;color:#fff;font-size:12px;font-weight:600;padding:4px 14px;border-radius:20px}
.pricing-card h3{font-size:18px;font-weight:700;margin-bottom:8px}
.price{font-size:14px;color:#64748b;margin-bottom:20px}
.price-amt{font-size:32px;font-weight:800;color:#0f172a}
.pricing-card ul{list-style:none;margin-bottom:24px}
.pricing-card li{padding:6px 0;font-size:14px}
.pricing-card li::before{content:'✔';color:#059669;margin-right:8px;font-weight:700}
.btn-full{display:block;text-align:center;width:100%}
.btn{display:inline-flex;align-items:center;gap:8px;padding:10px 24px;border-radius:8px;font-size:14px;font-weight:600;border:none;cursor:pointer;transition:all .15s;line-height:1;text-decoration:none}
.btn-sm{padding:8px 16px;font-size:13px}
.btn-primary{background:#2563eb;color:#fff}
.btn-primary:hover{background:#1d4ed8}
.footer{text-align:center;padding:40px 0;font-size:13px;color:#64748b;border-top:1px solid #e2e8f0;margin-top:40px}
@media (max-width:640px){.hero-title{font-size:28px}.steps{flex-direction:column;align-items:center;gap:16px}.step-arrow{transform:rotate(90deg)}.features-grid{grid-template-columns:1fr}.pricing-grid{grid-template-columns:1fr}}
</style>
