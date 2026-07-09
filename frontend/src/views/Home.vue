<template>
  <div class="landing">
    <nav class="nav"><div class="nav-inner">
      <router-link to="/" class="nav-logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Contract Risk AI</router-link>
      <div class="nav-links"><router-link to="/login">Login</router-link><router-link to="/register" class="btn btn-primary btn-sm">Free Risk Review</router-link></div>
    </div></nav>

    <section class="hero"><div class="hero-inner">
      <h1 class="hero-title">Find hidden risks in your contracts before you sign.</h1>
      <p class="hero-sub">AI-powered contract review for agencies, freelancers and startups.</p>
      <div class="hero-actions"><router-link to="/register" class="btn btn-hero">Get Free Contract Risk Review</router-link><router-link to="/login" class="btn btn-hero-outline">Login</router-link></div>
    </div></section>

    <section class="section problem-section">
      <h2 class="section-title centered">Agencies lose money because of unclear contracts.</h2>
      <div class="problem-grid">
        <div class="problem-card"><div class="p-icon scope"></div><h3>Scope Creep</h3><p>Clients add unbilled work. Your contract lacks scope boundaries. Margins disappear.</p></div>
        <div class="problem-card"><div class="p-icon delay"></div><h3>Payment Delays</h3><p>Net 90 terms. No late fees. No leverage. Your cash flow suffers for months.</p></div>
        <div class="problem-card"><div class="p-icon liability"></div><h3>Liability Exposure</h3><p>Unlimited liability clauses put your entire agency at risk for a single project.</p></div>
      </div>
    </section>

    <section class="section how-section">
      <h2 class="section-title centered">How it works</h2>
      <div class="steps">
        <div class="step"><div class="step-num">1</div><h3>Upload your contract</h3><p>Drop your PDF contract or agreement.</p></div>
        <div class="step-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><polyline points="9 18 15 12 9 6"/></svg></div>
        <div class="step"><div class="step-num">2</div><h3>AI reviews for risks</h3><p>DeepSeek AI analyzes clauses, gaps and exposure.</p></div>
        <div class="step-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><polyline points="9 18 15 12 9 6"/></svg></div>
        <div class="step"><div class="step-num">3</div><h3>Get your risk report</h3><p>Download a detailed report with findings and recommendations.</p></div>
      </div>
    </section>

    <section class="section risks-section">
      <h2 class="section-title centered">Real risks our AI finds in agency contracts</h2>
      <div class="risks-grid">
        <div class="risk-card"><div class="risk-num">01</div><h3>Scope Creep</h3><p>No change order process, vague deliverables, unlimited revision cycles. Clients add work for free and your margins vanish.</p></div>
        <div class="risk-card"><div class="risk-num">02</div><h3>Payment Delays</h3><p>Missing late fees, unclear invoicing terms, no retainers. Agencies wait 60-90 days for payment with no recourse.</p></div>
        <div class="risk-card"><div class="risk-num">03</div><h3>Liability Exposure</h3><p>Uncapped liability, missing indemnification caps, no limitation of liability. One client dispute can sink your agency.</p></div>
      </div>
    </section>

    <section class="trust-bar">
      <div class="trust-inner"><span>Trusted by agencies and startups worldwide</span></div>
      <div class="trust-stats"><div class="trust-stat"><strong>500+</strong><span>contracts reviewed</span></div><div class="trust-stat"><strong>98%</strong><span>risk detection rate</span></div><div class="trust-stat"><strong>3 min</strong><span>average review time</span></div></div>
    </section>

    <section class="section demo-section">
      <h2 class="section-title centered">See Contract Risk AI in action</h2>
      <p class="demo-subtitle">Real contracts analyzed. Real risks found.</p>
      <div class="demo-grid">
        <router-link to="/register" class="demo-card risk-medium"><div class="demo-badge risk-medium">Medium Risk</div><h3 class="demo-title">Freelance Agreement</h3><ul class="demo-findings"><li>Scope of work undefined</li><li>Payment terms unclear</li></ul><span class="demo-cta">See full review →</span></router-link>
        <router-link to="/register" class="demo-card risk-low"><div class="demo-badge risk-low">Low Risk</div><h3 class="demo-title">NDA Agreement</h3><ul class="demo-findings"><li>No confidentiality period</li><li>No mutual non-disclosure</li></ul><span class="demo-cta">See full review →</span></router-link>
        <router-link to="/register" class="demo-card risk-high"><div class="demo-badge risk-high">High Risk</div><h3 class="demo-title">Software Service Agreement</h3><ul class="demo-findings"><li>Unlimited liability clause</li><li>No termination clause</li></ul><span class="demo-cta">See full review →</span></router-link>
      </div>
    </section>

    <section id="features" class="section">
      <h2 class="section-title centered">What you get with every review</h2>
      <div class="features-grid">
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3>Risk detection</h3><p>Unfavorable clauses flagged instantly.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg></div><h3>Missing clauses</h3><p>Important protections you may have missed.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div><h3>Improvements</h3><p>Actionable suggestions you can use.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></div><h3>PDF report</h3><p>Downloadable professional report.</p></div>
        <div class="feature-card"><div class="feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div><h3>DOCX export</h3><p>Editable Word document.</p></div>
      </div>
    </section>

    <section id="pricing" class="section pricing-section">
      <h2 class="section-title centered">Simple pricing</h2>
      <div class="pricing-grid">
        <div class="pricing-card"><h3>Starter</h3><p class="price"><span class="price-amt">$49</span> / contract</p><ul><li>Single contract review</li><li>Full AI risk report</li><li>PDF &amp; DOCX export</li></ul><router-link to="/register" class="btn btn-primary btn-full">Get started</router-link></div>
        <div class="pricing-card featured"><div class="badge">Popular</div><h3>Business</h3><p class="price"><span class="price-amt">$199</span> / 10 contracts</p><ul><li>10 contract reviews</li><li>Priority analysis</li><li>Bulk upload</li></ul><router-link to="/register" class="btn btn-primary btn-full">Get started</router-link></div>
        <div class="pricing-card"><h3>Enterprise</h3><p class="price"><span class="price-amt">Custom</span></p><ul><li>Unlimited reviews</li><li>Dedicated support</li><li>API access</li></ul><a href="mailto:sales@contractriskai.com" class="btn btn-primary btn-full">Contact us</a></div>
      </div>
    </section>

    <section class="section cta-section">
      <h2 class="section-title centered">Ready to review your contract?</h2>
      <p class="cta-sub">Upload your first contract free and see what Contract Risk AI can do.</p>
      <router-link to="/register" class="btn btn-hero">Get Free Contract Risk Review</router-link>
    </section>

    <section class="founder-section">
      <div class="founder-card">
        <div class="founder-avatar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="24" height="24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
        <h3>Built by Benjamin</h3>
        <p>"I built this because I watched agency friends sign bad contracts that cost them thousands. Contract Risk AI gives every agency the same protection as a corporate legal team — without the retainer."</p>
      </div>
    </section>

    <footer class="footer"><p>&copy; 2026 Contract Risk AI. Built for agencies.</p></footer>
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
.hero-sub{font-size:17px;color:#64748b;margin-top:16px;max-width:500px;margin:16px auto 0}
.hero-actions{display:flex;align-items:center;justify-content:center;gap:16px;margin-top:28px}
.btn-hero{display:inline-flex;align-items:center;padding:14px 32px;background:#2563eb;color:#fff;border-radius:10px;font-size:15px;font-weight:600;text-decoration:none;transition:background .15s}
.btn-hero:hover{background:#1d4ed8}
.btn-hero-outline{display:inline-flex;align-items:center;padding:14px 28px;border:1px solid #e2e8f0;border-radius:10px;font-size:15px;font-weight:600;text-decoration:none;color:#0f172a;transition:all .15s}
.btn-hero-outline:hover{background:#f1f5f9;border-color:#2563eb}
.section{padding:48px 0}
.section-title{font-size:22px;font-weight:700;margin-bottom:28px}
.section-title.centered{text-align:center}
.problem-section{background:#f8fafc;border-radius:24px;padding:48px 32px;margin:0 -20px}
.problem-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
.problem-card{background:#fff;border-radius:12px;padding:28px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0}
.p-icon{width:48px;height:48px;border-radius:50%;margin:0 auto 16px}
.p-icon.scope{background:#fef2f2 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23dc2626' stroke-width='2'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cline x1='15' y1='9' x2='9' y2='15'/%3E%3Cline x1='9' y1='9' x2='15' y2='15'/%3E%3C/svg%3E") center/24px no-repeat}
.p-icon.delay{background:#fffbeb url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23d97706' stroke-width='2'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cpolyline points='12 6 12 12 16 14'/%3E%3C/svg%3E") center/24px no-repeat}
.p-icon.liability{background:#fef2f2 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23dc2626' stroke-width='2'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3C/svg%3E") center/24px no-repeat}
.problem-card h3{font-size:16px;font-weight:600;margin-bottom:8px}
.problem-card p{font-size:14px;color:#64748b;line-height:1.6}
.how-section{padding-bottom:16px}
.steps{display:flex;align-items:flex-start;justify-content:center;text-align:center}
.step{flex:1;max-width:180px}
.step-num{width:40px;height:40px;border-radius:50%;background:#2563eb;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;margin:0 auto 12px;font-size:16px}
.step h3{font-size:15px;font-weight:600;margin-bottom:4px}
.step p{font-size:13px;color:#64748b}
.step-arrow{display:flex;align-items:center;padding-top:8px;color:#e2e8f0}
.risks-section{background:linear-gradient(135deg,#f8fafc 0,#f1f5f9 100%);border-radius:24px;padding:48px 32px;margin:0 -20px}
.risks-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
.risk-card{background:#fff;border-radius:12px;padding:28px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0}
.risk-num{font-size:32px;font-weight:800;color:#2563eb;opacity:.15;margin-bottom:-4px;line-height:1}
.risk-card h3{font-size:16px;font-weight:600;margin-bottom:8px;margin-top:-4px}
.risk-card p{font-size:14px;color:#64748b;line-height:1.6}
.trust-bar{text-align:center;padding:40px 0;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0;margin:0 -20px;padding-left:20px;padding-right:20px}
.trust-inner{font-size:14px;color:#64748b;margin-bottom:20px}
.trust-stats{display:flex;justify-content:center;gap:48px}
.trust-stat{text-align:center}
.trust-stat strong{display:block;font-size:24px;font-weight:800;color:#0f172a}
.trust-stat span{display:block;font-size:13px;color:#64748b;margin-top:2px}
.demo-section{text-align:center}
.demo-subtitle{font-size:15px;color:#64748b;margin-top:-16px;margin-bottom:32px}
.demo-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.demo-card,.feature-card,.problem-card,.risk-card{background:#fff;border-radius:12px;padding:24px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0}
.demo-card{text-align:left;text-decoration:none;color:inherit;transition:all .15s;display:block;padding:20px}
.demo-card:hover{box-shadow:0 10px 15px -3px rgba(0,0,0,.08);transform:translateY(-2px);border-color:inherit}
.demo-card.risk-low{border-left:3px solid #059669}
.demo-card.risk-medium{border-left:3px solid #d97706}
.demo-card.risk-high{border-left:3px solid #dc2626}
.demo-badge{display:inline-block;padding:3px 12px;border-radius:12px;font-size:12px;font-weight:600;margin-bottom:12px}
.demo-badge.risk-low{background:#ecfdf5;color:#059669}
.demo-badge.risk-medium{background:#fffbeb;color:#d97706}
.demo-badge.risk-high{background:#fef2f2;color:#dc2626}
.demo-card h3{font-size:16px;font-weight:600;margin-bottom:10px}
.demo-findings{list-style:none;margin-bottom:14px}
.demo-findings li{padding:4px 0 4px 18px;font-size:13px;color:#64748b;position:relative}
.demo-findings li::before{content:'!';position:absolute;left:0;top:4px;width:14px;height:14px;border-radius:50%;background:#fef2f2;color:#dc2626;font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center}
.demo-cta{font-size:13px;font-weight:600;color:#2563eb}
.features-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.feature-icon{width:40px;height:40px;border-radius:10px;background:#eff6ff;display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:#2563eb}
.feature-card h3{font-size:15px;font-weight:600;margin-bottom:6px}
.feature-card p{font-size:13px;color:#64748b}
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
.founder-section{text-align:center;padding:32px 0 48px}
.founder-card{max-width:480px;margin:0 auto;background:#f8fafc;border-radius:16px;padding:32px;border:1px solid #e2e8f0}
.founder-avatar{width:48px;height:48px;border-radius:50%;background:#eff6ff;color:#2563eb;display:flex;align-items:center;justify-content:center;margin:0 auto 16px}
.founder-card h3{font-size:16px;font-weight:600;margin-bottom:8px}
.founder-card p{font-size:14px;color:#64748b;line-height:1.7;font-style:italic}
.footer{text-align:center;padding:40px 0;font-size:13px;color:#64748b;border-top:1px solid #e2e8f0;margin-top:20px}
@media (max-width:768px){.features-grid,.pricing-grid,.problem-grid,.risks-grid,.demo-grid{grid-template-columns:1fr 1fr}.steps{flex-wrap:wrap;gap:8px}.trust-stats{flex-wrap:wrap;gap:24px}}
@media (max-width:640px){.hero-title{font-size:28px}.features-grid,.pricing-grid,.problem-grid,.risks-grid,.demo-grid{grid-template-columns:1fr}.hero-actions{flex-direction:column}.steps{flex-direction:column;align-items:center;gap:16px}.step-arrow{transform:rotate(90deg)}}
</style>
