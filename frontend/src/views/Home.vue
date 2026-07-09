<template>
  <div class="landing">
    <nav class="nav"><div class="nav-inner">
      <router-link to="/" class="nav-logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Contract Risk AI</router-link>
      <div class="nav-links"><router-link to="/login">Login</router-link><router-link to="/register" class="btn btn-primary btn-sm">Get Free Review</router-link></div>
    </div></nav>
    <section class="hero"><div class="hero-inner">
      <h1 class="hero-title">Find hidden risks in your contracts before you sign.</h1>
      <p class="hero-sub">AI-powered contract review for freelancers, startups and small businesses.</p>
      <div class="hero-actions"><router-link to="/register" class="btn btn-hero">Get Free Contract Review</router-link><router-link to="/login" class="btn btn-hero-outline">Login</router-link></div>
    </div></section>
    <section id="features" class="section">
      <h2 class="section-title centered">Why Contract Risk AI?</h2>
      <div class="features-grid">
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3>Find hidden contract risks</h3><p>Detect unfavorable clauses and potential liabilities before signing.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg></div><h3>Identify missing clauses</h3><p>Find important protections that may be absent from your agreement.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div><h3>Summarize key obligations</h3><p>Get a clear overview of what each party is required to do.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div><h3>Suggest improvements</h3><p>Receive actionable recommendations to strengthen your position.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></div><h3>Generate professional reports</h3><p>Download detailed risk reports in PDF or DOCX format.</p></div>
      </div>
    </section>
    <section class="section how-section">
      <h2 class="section-title centered">How It Works</h2>
      <div class="steps">
        <div class="step"><div class="step-num">1</div><h3>Upload your contract</h3><p>Upload your PDF contract or agreement.</p></div>
        <div class="step-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><polyline points="9 18 15 12 9 6"/></svg></div>
        <div class="step"><div class="step-num">2</div><h3>AI reviews risks</h3><p>DeepSeek AI analyzes clauses, risks, and gaps.</p></div>
        <div class="step-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><polyline points="9 18 15 12 9 6"/></svg></div>
        <div class="step"><div class="step-num">3</div><h3>Get your report</h3><p>Download a detailed risk report in PDF or DOCX.</p></div>
      </div>
    </section>
    <section id="pricing" class="section pricing-section">
      <h2 class="section-title centered">Simple Pricing</h2>
      <div class="pricing-grid">
        <div class="pricing-card"><h3>Starter</h3><p class="price"><span class="price-amt">$49</span> / contract</p><ul><li>Single contract review</li><li>Full AI risk report</li><li>PDF &amp; DOCX export</li></ul><router-link to="/register" class="btn btn-primary btn-full">Get started</router-link></div>
        <div class="pricing-card featured"><div class="badge">Popular</div><h3>Business</h3><p class="price"><span class="price-amt">$199</span> / 10 contracts</p><ul><li>10 contract reviews</li><li>Priority AI analysis</li><li>Bulk upload</li></ul><router-link to="/register" class="btn btn-primary btn-full">Get started</router-link></div>
        <div class="pricing-card"><h3>Enterprise</h3><p class="price"><span class="price-amt">Custom</span></p><ul><li>Unlimited reviews</li><li>Custom AI model tuning</li><li>Dedicated support</li><li>API access</li></ul><a href="mailto:sales@contractriskai.com" class="btn btn-primary btn-full">Contact us</a></div>
      </div>
    </section>
    <section class="section cta-section">
      <h2 class="section-title centered">Ready to review your contract?</h2>
      <p class="cta-sub">Upload your first contract free and see what Contract Risk AI can do.</p>
      <router-link to="/register" class="btn btn-hero">Start Free Review</router-link>
    </section>
    <footer class="footer"><p>&copy; 2026 Contract Risk AI. Built for small businesses.</p></footer>
  </div>
</template>
<script setup></script>
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
.hero-sub{font-size:17px;color:#64748b;margin-top:16px;max-width:500px;margin-left:auto;margin-right:auto}
.hero-actions{display:flex;align-items:center;justify-content:center;gap:16px;margin-top:28px}
.btn-hero{display:inline-flex;align-items:center;padding:14px 32px;background:#2563eb;color:#fff;border-radius:10px;font-size:15px;font-weight:600;text-decoration:none;transition:background .15s}
.btn-hero:hover{background:#1d4ed8}
.btn-hero-outline{display:inline-flex;align-items:center;padding:14px 28px;border:1px solid #e2e8f0;border-radius:10px;font-size:15px;font-weight:600;text-decoration:none;color:#0f172a;transition:all .15s}
.btn-hero-outline:hover{background:#f1f5f9;border-color:#2563eb}
.section{padding:48px 0}
.section-title{font-size:22px;font-weight:700;margin-bottom:28px}
.section-title.centered{text-align:center}
.features-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.feature-card{background:#fff;border-radius:12px;padding:24px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0}
.feature-icon{width:40px;height:40px;border-radius:10px;background:#eff6ff;display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:#2563eb}
.feature-card h3{font-size:15px;font-weight:600;margin-bottom:6px}
.feature-card p{font-size:13px;color:#64748b}
.steps{display:flex;align-items:flex-start;justify-content:center;text-align:center}
.step{flex:1;max-width:180px}
.step-num{width:40px;height:40px;border-radius:50%;background:#2563eb;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;margin:0 auto 12px}
.step h3{font-size:15px;font-weight:600;margin-bottom:4px}
.step p{font-size:13px;color:#64748b}
.step-arrow{display:flex;align-items:center;padding-top:8px;color:#e2e8f0}
.pricing-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
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
.cta-section{text-align:center;padding:64px 0}
.cta-sub{font-size:17px;color:#64748b;margin-top:12px}
.footer{text-align:center;padding:40px 0;font-size:13px;color:#64748b;border-top:1px solid #e2e8f0;margin-top:40px}
@media (max-width:768px){.features-grid{grid-template-columns:1fr 1fr}.pricing-grid{grid-template-columns:1fr}.steps{flex-direction:column;align-items:center;gap:16px}.step-arrow{transform:rotate(90deg)}}
@media (max-width:640px){.hero-title{font-size:28px}.features-grid{grid-template-columns:1fr}.hero-actions{flex-direction:column}.pricing-grid{grid-template-columns:1fr}}
</style>
