import streamlit as st
import requests
import json
import time

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Presentation LLM",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Hugging Face Space URL ────────────────────────────────────
HF_SPACE_URL = "https://honey2706-presentation-llm.hf.space"
API_SUBMIT   = f"{HF_SPACE_URL}/gradio_api/call/chat"

# ── CSS ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');
:root {
    --bg:#0a0a0f; --surface:#12121a; --card:#1a1a28;
    --border:#2a2a40; --accent:#7c3aed; --accent2:#06b6d4;
    --text:#e2e8f0; --muted:#64748b;
}
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2rem 0 2rem !important; max-width: 100% !important; }

/* hero */
.hero {
    background: linear-gradient(135deg,#0a0a0f 0%,#1a0a2e 50%,#0a1628 100%);
    padding: 2.5rem 3rem 1.5rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    border: 1px solid var(--border);
}
.hero-badge {
    display:inline-block; background:rgba(124,58,237,0.2);
    border:1px solid rgba(124,58,237,0.4); color:#a78bfa;
    padding:0.2rem 0.8rem; border-radius:999px;
    font-size:0.7rem; font-family:'Space Mono',monospace;
    letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.75rem;
}
.hero-title {
    font-size:2.8rem; font-weight:800; line-height:1.1;
    background:linear-gradient(135deg,#ffffff 30%,#a78bfa 70%,#06b6d4 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    background-clip:text; margin:0 0 0.4rem 0;
}
.hero-sub { color:var(--muted); font-size:0.95rem; font-family:'Space Mono',monospace; }

/* section label */
.lbl {
    font-family:'Space Mono',monospace; font-size:0.65rem;
    letter-spacing:0.15em; text-transform:uppercase;
    color:var(--muted); margin-bottom:0.6rem;
    display:flex; align-items:center; gap:0.5rem;
}
.lbl::before { content:''; display:inline-block; width:16px; height:2px; background:var(--accent); }

/* textarea */
.stTextArea textarea {
    background:var(--card) !important; border:1px solid var(--border) !important;
    border-radius:10px !important; color:var(--text) !important;
    font-family:'Space Mono',monospace !important; font-size:0.88rem !important;
    padding:0.9rem !important;
}
.stTextArea textarea:focus {
    border-color:var(--accent) !important;
    box-shadow:0 0 0 3px rgba(124,58,237,0.15) !important;
}

/* buttons */
.stButton > button {
    width:100%; background:linear-gradient(135deg,var(--accent),#9333ea) !important;
    color:white !important; border:none !important; border-radius:10px !important;
    padding:0.75rem 1.5rem !important; font-family:'Syne',sans-serif !important;
    font-weight:700 !important; font-size:0.95rem !important;
    transition:all 0.2s !important; margin-top:0.4rem !important;
}
.stButton > button:hover {
    transform:translateY(-2px) !important;
    box-shadow:0 8px 25px rgba(124,58,237,0.4) !important;
}

/* selectbox */
.stSelectbox > div > div {
    background:var(--card) !important; border:1px solid var(--border) !important;
    border-radius:10px !important; color:var(--text) !important;
}

/* response box */
.rbox {
    background:var(--card); border:1px solid var(--border);
    border-radius:12px; padding:1.2rem 1.4rem;
    font-family:'Space Mono',monospace; font-size:0.8rem;
    line-height:1.9; color:var(--text); min-height:180px;
}
.rbox.ok  { border-color:rgba(16,185,129,0.4); background:rgba(16,185,129,0.04); }
.rbox.err { border-color:rgba(239,68,68,0.4);  background:rgba(239,68,68,0.04); }
.step { display:flex; gap:0.6rem; padding:0.3rem 0; border-bottom:1px solid rgba(255,255,255,0.03); }
.si { flex-shrink:0; }
.st2 { color:var(--text); line-height:1.5; }

/* download btn */
.stDownloadButton > button {
    width:100%; background:transparent !important;
    border:1px solid var(--accent2) !important; color:var(--accent2) !important;
    border-radius:10px !important; padding:0.7rem 1.5rem !important;
    font-family:'Syne',sans-serif !important; font-weight:600 !important;
    font-size:0.92rem !important; transition:all 0.2s !important; margin-top:0.8rem !important;
}
.stDownloadButton > button:hover {
    background:rgba(6,182,212,0.1) !important;
    transform:translateY(-1px) !important;
}

/* stats */
.stats { display:flex; gap:2rem; margin-top:1.2rem; padding-top:1.2rem; border-top:1px solid var(--border); }
.stat-v {
    font-size:1.5rem; font-weight:800;
    background:linear-gradient(135deg,var(--accent),var(--accent2));
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.stat-l { font-size:0.65rem; color:var(--muted); font-family:'Space Mono',monospace; text-transform:uppercase; }

/* info card */
.icard {
    background:rgba(124,58,237,0.08); border:1px solid rgba(124,58,237,0.2);
    border-radius:10px; padding:0.85rem 1rem; margin-top:0.8rem;
    font-size:0.78rem; color:#c4b5fd; font-family:'Space Mono',monospace; line-height:1.6;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────
for k, v in [("response_text",""), ("pptx_bytes",None),
              ("slide_count",0), ("total_created",0), ("prompt","")]:
    if k not in st.session_state:
        st.session_state[k] = v

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Powered by Qwen + MCP Tools</div>
    <h1 class="hero-title">Presentation LLM</h1>
    <p class="hero-sub">Type any topic → Get a beautiful colorful PowerPoint instantly</p>
</div>
""", unsafe_allow_html=True)


# ── API helpers ───────────────────────────────────────────────
def call_hf_space(message: str):
    """Submit to Gradio API and poll for result."""
    try:
        # Step 1 — submit
        r = requests.post(
            API_SUBMIT,
            json={"data": [message]},
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        r.raise_for_status()
        event_id = r.json().get("event_id")
        if not event_id:
            return "⚠️ No event_id from Space.", None

        # Step 2 — poll result
        poll_url = f"{HF_SPACE_URL}/gradio_api/call/chat/{event_id}"
        for _ in range(120):
            time.sleep(2)
            pr = requests.get(poll_url, timeout=30)
            raw = pr.text.strip()
            if not raw:
                continue
            for line in raw.split("\n"):
                line = line.strip()
                if line.startswith("data:"):
                    payload = line[5:].strip()
                    if not payload or payload == "null":
                        continue
                    try:
                        data = json.loads(payload)
                        text_resp = data[0] if len(data) > 0 else "Done"
                        file_ref  = data[1] if len(data) > 1 else None
                        return text_resp, file_ref
                    except Exception:
                        continue

        return "⚠️ Timed out. Try again.", None

    except requests.exceptions.ConnectionError:
        return "⚠️ Cannot connect to Space. Make sure it is Running.", None
    except Exception as e:
        return f"⚠️ Error: {str(e)}", None


def fetch_pptx(file_ref):
    """Download .pptx bytes from the Gradio file reference."""
    try:
        if not file_ref:
            return None

        # Gradio returns file_ref as dict {"path":..., "url":..., "orig_name":...}
        if isinstance(file_ref, dict):
            # Try 'url' first, then build from 'path'
            url = file_ref.get("url") or file_ref.get("path") or ""
        else:
            url = str(file_ref)

        if not url:
            return None

        # Build full URL if relative
        if url.startswith("/"):
            url = HF_SPACE_URL + url
        elif not url.startswith("http"):
            url = HF_SPACE_URL + "/" + url.lstrip("/")

        r = requests.get(url, timeout=60)
        r.raise_for_status()

        # Validate it's a real PPTX (starts with PK zip header)
        if r.content[:2] == b'PK':
            return r.content
        return None

    except Exception:
        return None


# ── Layout ────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1], gap="large")

# ════════════════════════════════════
#  LEFT — Input
# ════════════════════════════════════
with col_left:
    st.markdown('<div class="lbl">Your Prompt</div>', unsafe_allow_html=True)

    prompt = st.text_area(
        label="prompt",
        value=st.session_state.prompt,
        placeholder="e.g. Create a presentation about Artificial Intelligence",
        height=130,
        label_visibility="collapsed",
        key="prompt_input"
    )

    c1, c2 = st.columns(2)
    with c1:
        slide_count = st.selectbox("Slides", ["6 slides","8 slides","10 slides","12 slides"], index=1)
    with c2:
        style = st.selectbox("Style", ["Professional","Creative","Minimal","Bold"], index=1)

    generate = st.button("⚡  Generate Presentation", use_container_width=True)

    st.markdown('<div class="lbl" style="margin-top:1.2rem">Quick Examples</div>', unsafe_allow_html=True)

    examples = [
        ("Artificial Intelligence", "Create a presentation about Artificial Intelligence"),
        ("Climate Change",          "Create a presentation about Climate Change"),
        ("Machine Learning",        "Create a presentation about Machine Learning"),
        ("Blockchain",              "Create a presentation about Blockchain"),
        ("Cybersecurity",           "Create a presentation about Cybersecurity"),
        ("Cloud Computing",         "Create a presentation about Cloud Computing"),
        ("Space Exploration",       "Create a presentation about Space Exploration"),
        ("Renewable Energy",        "Create a presentation about Renewable Energy"),
    ]

    ecols = st.columns(2)
    for i, (label, full_prompt) in enumerate(examples):
        if ecols[i % 2].button(f"✦ {label}", key=f"ex_{i}", use_container_width=True):
            st.session_state.prompt = full_prompt
            st.rerun()

    st.markdown(f"""
    <div class="stats">
        <div><div class="stat-v">{st.session_state.total_created}</div><div class="stat-l">Created</div></div>
        <div><div class="stat-v">{st.session_state.slide_count}</div><div class="stat-l">Last Slides</div></div>
        <div><div class="stat-v">8</div><div class="stat-l">Themes</div></div>
        <div><div class="stat-v">AI</div><div class="stat-l">Powered</div></div>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════
#  RIGHT — Output
# ════════════════════════════════════
with col_right:
    st.markdown('<div class="lbl">Response</div>', unsafe_allow_html=True)

    # ── Trigger generation ──
    if generate and prompt.strip():
        n      = slide_count.split()[0]
        topic  = prompt.strip().lstrip(">• \t")
        # Remove leading phrases
        for ph in ["create a presentation about","make a presentation about","presentation about"]:
            if topic.lower().startswith(ph):
                topic = topic[len(ph):].strip()
                break
        full_msg = f"Create a presentation about {topic} with {n} slides"

        with st.spinner("Generating your presentation..."):
            text_resp, file_ref = call_hf_space(full_msg)
            st.session_state.response_text = text_resp

            # Fetch the PPTX file
            pptx_data = fetch_pptx(file_ref)
            st.session_state.pptx_bytes = pptx_data

            # Count slides
            slide_lines = [l for l in text_resp.split("\n")
                           if "slide" in l.lower() and any(w in l.lower() for w in ["added","written","created"])]
            st.session_state.slide_count   = max(len(slide_lines), 0)
            st.session_state.total_created += 1

        st.rerun()

    # ── Show response ──
    if st.session_state.response_text:
        txt   = st.session_state.response_text
        cls   = "ok"  if ("✅" in txt or "🎉" in txt) else \
                "err" if ("⚠️" in txt or "❌" in txt) else ""

        rows = ""
        for line in txt.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            if   line.startswith("✅"): ic = "✅"; ln = line[1:].strip()
            elif line.startswith("📄"): ic = "📄"; ln = line[1:].strip()
            elif line.startswith("🎉"): ic = "🎉"; ln = line[1:].strip()
            elif line.startswith("⚠️"): ic = "⚠️"; ln = line[2:].strip()
            elif line.startswith("❌"): ic = "❌"; ln = line[1:].strip()
            else:                       ic = "›";  ln = line
            rows += f'<div class="step"><span class="si">{ic}</span><span class="st2">{ln}</span></div>'

        st.markdown(f'<div class="rbox {cls}">{rows}</div>', unsafe_allow_html=True)

        # ── Download ──
        if st.session_state.pptx_bytes:
            st.download_button(
                label="⬇️  Download PowerPoint (.pptx)",
                data=st.session_state.pptx_bytes,
                file_name="presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                use_container_width=True
            )
        else:
            st.markdown("""
            <div class="icard">
                ⚠️ File could not be fetched automatically.<br>
                Go to your <a href="https://honey2706-presentation-llm.hf.space" target="_blank"
                style="color:#a78bfa">Hugging Face Space</a> and download output.pptx directly.
            </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="rbox">
            <span style="color:#2a2a40; font-size:0.82rem;">
            ✦ Enter a topic and click Generate...<br><br>
            › Create a presentation about AI<br>
            › Create a presentation about Climate Change<br>
            › Create a presentation about Blockchain
            </span>
        </div>
        """, unsafe_allow_html=True)

    # ── How it works ──
    st.markdown('<div class="lbl" style="margin-top:1.5rem">How It Works</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex;flex-direction:column;gap:0.5rem;margin-top:0.4rem;">
        <div class="step"><span class="si">①</span><span class="st2" style="color:#64748b">Prompt sent to <b style="color:#a78bfa">Qwen LLM</b> on Hugging Face</span></div>
        <div class="step"><span class="si">②</span><span class="st2" style="color:#64748b">LLM generates slide content via <b style="color:#a78bfa">MCP Tools</b></span></div>
        <div class="step"><span class="si">③</span><span class="st2" style="color:#64748b"><b style="color:#a78bfa">python-pptx</b> builds a colorful .pptx file</span></div>
        <div class="step"><span class="si">④</span><span class="st2" style="color:#64748b">Download your <b style="color:#06b6d4">presentation</b> instantly</span></div>
    </div>
    """, unsafe_allow_html=True)