# 🎬 MalwareGuard — Project Video Script & Storyboard

**Target length:** 5–7 minutes · **Format:** MP4 (1080p) · **Tools:** any screen recorder (QuickTime, OBS, Loom)

> Record the screen while running the MVP, narrate over it, then paste the final
> link into `Project_Form.md` and the form (`docs/Project_Abstract_Form.docx`).
> The poster QR code points to the GitHub repo where the video link will live.

---

## Scene 1 — Introduction (0:00–0:45)
**On screen:** poster / title slide.
**Say:**
> "Hi, I'm Shai Shotashvili. This is *Malware Classification via PE Header Analysis* —
> a defensive cybersecurity project for the *Introduction to AI-Driven Cyber Security* course,
> supervised by Yakov Damatov. Traditional antivirus relies on signatures, which packed and
> encrypted malware easily evades. Instead, MalwareGuard classifies Windows executables from
> the *structural* metadata in their PE headers — features attackers can't hide without
> breaking the file."

## Scene 2 — Goals & Data (0:45–1:45)
**On screen:** `Project_Summary.md` + `scripts/generate_data.py`.
**Say:**
> "Three goals: build an ML classifier from PE-header features, test its robustness to
> adversarial evasion, and ship a working analyst MVP. The dataset has 1,000 labeled samples
> across four features — VirtualSize, Entropy, NumberOfSections and Characteristics — with
> benign files showing low entropy and small size, and malware the opposite."

## Scene 3 — Model & Training (1:45–2:45)
**On screen:** run `python scripts/train_model.py` in the terminal.
**Say:**
> "I train a Random Forest with 100 trees on an 80/20 split. On the held-out test set it
> reaches 100% accuracy on this synthetic data — Entropy and VirtualSize are the most
> discriminative features, which matches the security intuition."
**Show:** the printed classification report (accuracy 1.00).

## Scene 4 — Live MVP Demo (2:45–4:15)
**On screen:** `streamlit run app.py`.
**Say & do:**
> "Here's the MVP. I'll enter a typical benign file — low entropy, small size — and analyze it."
- Enter benign values (e.g. VirtualSize 50000, Entropy 3.0, Sections 3, Characteristics 200) → **Benign**.
> "Now a suspicious file — high entropy, large size, more sections."
- Enter malware-like values (e.g. VirtualSize 160000, Entropy 7.2, Sections 8, Characteristics 700) → **🚨 Malware Detected**.
> "Every analysis is appended to `traffic_logs.log`, giving security teams an audit trail."
- Open `traffic_logs.log` to show the logged entries.

## Scene 5 — Security Testing (4:15–5:30)
**On screen:** run `python scripts/security_test.py` + show `docs/figures/fig_adversarial.png`.
**Say:**
> "For robustness I run an adversarial test: start from a high-confidence benign file and
> incrementally raise its Entropy and VirtualSize to mimic malware. The verdict flips from
> Benign to Malware exactly as the features cross into the malicious range — confirming the
> model decides on the intended security signals rather than noise."

## Scene 6 — Conclusions & Future Work (5:30–6:30)
**On screen:** poster Conclusions / Discussions sections.
**Say:**
> "All three goals were met: a working classifier, a robustness evaluation, and a deployable
> MVP with logging and alerting. Structural PE-header analysis is a lightweight complement to
> signature-based detection. Next steps: retrain on real corpora like EMBER and MalwareBazaar,
> add deep models over API-call and byte sequences, and integrate into a SOC triage pipeline.
> Thanks for watching — the full source code is on GitHub via the QR code on the poster."

---

## Recording checklist
- [ ] 1080p, clear audio, no background noise
- [ ] Show terminal output and the Streamlit UI at readable zoom
- [ ] Keep total length 5–7 minutes
- [ ] Export as MP4
- [ ] Upload (YouTube unlisted / Google Drive) and paste the link into `Project_Form.md` + the abstract form
