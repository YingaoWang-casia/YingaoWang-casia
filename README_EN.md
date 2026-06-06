<div align="center">

# Yingao Wang

<p>
  <a href="README.md">中文</a> ·
  <a href="README_EN.md"><strong>English</strong></a>
</p>

### 🎙️ Speech Signal Processing | Audio AI | Turn Detection | Full-duplex Interaction | LLM Agent Engineering

<p>
  <strong>Listening, waiting, interrupting and responding at the right moment.</strong>
</p>

<p>
  <a href="https://github.com/YingaoWang-casia">
    <img src="https://img.shields.io/badge/GitHub-YingaoWang--casia-181717?style=for-the-badge&logo=github" alt="GitHub" />
  </a>
  <a href="mailto:2967523019@qq.com">
    <img src="https://img.shields.io/badge/Email-2967523019%40qq.com-0891b2?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Speech%20AI-0891b2?style=flat-square" />
  <img src="https://img.shields.io/badge/Turn%20Detection-14b8a6?style=flat-square" />
  <img src="https://img.shields.io/badge/VAD-0f766e?style=flat-square" />
  <img src="https://img.shields.io/badge/Full--duplex%20Interaction-2563eb?style=flat-square" />
  <img src="https://img.shields.io/badge/LLM%20Agent-7c3aed?style=flat-square" />
  <img src="https://img.shields.io/badge/RAG-c026d3?style=flat-square" />
</p>

</div>

---

## 👋 About Me

I studied Artificial Intelligence at Beijing University of Technology and am currently pursuing a master's degree in Pattern Recognition and Intelligent Systems at the Institute of Automation, Chinese Academy of Sciences.

My main research and engineering interests include VAD, conversational turn detection, full-duplex speech interaction, speech-interaction benchmarks, LLM agents, and practical RAG systems.

I care about the full path from algorithm modeling to engineering delivery: dataset construction, model training and evaluation, audio-processing pipelines, real-time interaction systems, intelligent document parsing, and open-source project maintenance.

---

## 🎓 Education

| Period | School / Institute | Major / Direction |
| --- | --- | --- |
| 2022.09 - 2026.07 | Beijing University of Technology | Artificial Intelligence, B.Eng. |
| 2026.09 - Present | Institute of Automation, Chinese Academy of Sciences | Pattern Recognition and Intelligent Systems, M.S. |

Research focus: speech-interaction foundation models, LLM applications, and LLM algorithms.

---

## 💼 Experience

### 🗣️ Bairong Cloud — Speech Algorithm Engineer

Period: 2025.12 - Present

I work on algorithms and systems for speech interaction, including turn detection, VAD, endpoint detection, and full-duplex speech interaction.

Main work:

1. Three-class turn detection model and system  
   Designed and evaluated turn-taking models for real human-machine voice interaction, deciding whether a user input is complete, still needs waiting, or should be treated as invalid.

2. VAD and endpoint detection optimization  
   Improved speech activity detection strategies for short utterances, weak speech, long pauses, noise, and non-semantic vocal sounds.

3. Full-duplex speech interaction exploration  
   Built modules for speech detection, turn judgment, interruption recognition, and response timing control to improve natural conversational fluency.

Keywords: VAD, Turn Detection, Full-duplex Interaction, Speech AI Benchmark, Real-time Speech Interaction

---

### 🧠 Bohua Xinzhi — Agent R&D Engineer

Period: 2025.09 - 2025.12

I participated in the design and development of an LLM-powered intelligent document agent, covering requirement analysis, technical solution design, and engineering implementation.

Projects:

1. Technical solution generation assistant  
   Built a document parsing, content splitting, module extraction, and technical proposal generation workflow based on LLMs and retrieval. The system supports multi-node parallel processing and reduces manual proposal writing from hours to minutes.

2. Intelligent tender-document parsing assistant  
   Designed a multi-path extraction pipeline for tender documents, combining DeepSeek-Chat, differentiated prompting, GTE vector retrieval, and reranking to extract parameters, parse structure, and build temporary knowledge bases.

Keywords: LLM Agent, RAG, GTE, Rerank, Document Parsing, Knowledge Base Construction

---

## 🧭 Research And Engineering

### 🎧 Speech AI / Audio Intelligence

- VAD and speech endpoint detection
- Three-class turn detection
- Multi-class full-duplex turn detection
- Benchmark construction for real speech-interaction scenarios
- Interruption recognition and response timing control
- Speech dataset construction, cleaning, annotation, and evaluation
- Long-audio segmentation, alignment, inference, and post-processing

### 🧩 LLM Agent / RAG Engineering

- LLM agent system development
- RAG knowledge-base construction and retrieval optimization
- Structured document parsing
- Multi-node task orchestration
- Prompt engineering
- Local AI toolchains and Codex Skill development
- AI engineering systems for project review, interview stress testing, and evidence-chain organization

---

## 🧰 Tech Stack

| Direction | Technologies |
| --- | --- |
| Programming & Engineering | Python, Bash, Linux, Git, Docker |
| Deep Learning | PyTorch, ONNX, Anaconda |
| Audio Processing | FFmpeg, VAD, Turn Detection, Full-duplex Interaction |
| LLM Engineering | LLM Agent, RAG, Prompt Engineering, GTE, Rerank |
| Platforms | Dify, RAGFlow |

---

## 🚀 Featured Open-source Projects

### 🎙️ Speech AI / Turn-taking

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/Bairong-Xdynamics/TurnSense">
          🎧 TurnSense
        </a>
      </h3>
      <p>
        A three-class turn detection model for real human-machine speech interaction. It classifies user input as
        <code>complete</code> / <code>incomplete</code> / <code>invalid</code>
        to decide whether the system should respond immediately, keep waiting, or ignore invalid input.
      </p>
      <p>
        <code>Turn Detection</code>
        <code>Speech AI</code>
        <code>VAD</code>
        <code>ONNX</code>
      </p>
      <p>
        <a href="https://github.com/Bairong-Xdynamics/TurnSense">
          <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github" />
        </a>
        <img src="profile/badges/stars-turnsense.svg" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/YingaoWang-casia/CoDeTT.github.io">
          🧪 CoDeTT Benchmark
        </a>
      </h3>
      <p>
        A multi-class turn detection benchmark for full-duplex speech interaction, designed to evaluate Turn-Taking
        models on multi-scenario decision tasks. The project includes unified evaluation scripts for multiple models.
      </p>
      <p>
        <code>Benchmark</code>
        <code>Full-duplex</code>
        <code>Turn-taking</code>
        <code>Evaluation</code>
      </p>
      <p>
        <a href="https://github.com/YingaoWang-casia/CoDeTT.github.io">
          <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github" />
        </a>
        <img src="profile/badges/stars-codett.svg" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
  </tr>
</table>

---

### 🧩 LLM Agent / RAG / Codex Skill

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/YingaoWang-casia/shushu-ProjectProof">
          🛠️ ProjectProof for Codex
        </a>
      </h3>
      <p>
        A Codex Skill for AI / Agent / RAG / algorithm / data / frontend-backend internship projects.
        It does not fabricate experience; instead, it helps users bring real projects back to evidence chains,
        engineering boundaries, and interview follow-up questions.
      </p>
      <p>
        <code>Codex Skill</code>
        <code>Project Review</code>
        <code>Evidence Contract</code>
        <code>Interview</code>
      </p>
      <p>
        <a href="https://github.com/YingaoWang-casia/shushu-ProjectProof">
          <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github" />
        </a>
        <img src="profile/badges/stars-projectproof.svg" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/YingaoWang-casia/shushu-InterviewProof-RAG">
          📚 InterviewProof-RAG
        </a>
      </h3>
      <p>
        A Codex-first local interview-experience RAG and project stress-testing system. It turns scattered interview notes
        into traceable InterviewCards, then uses local indexing, Codex Packs, and ProjectProof Bridge to check whether
        personal projects can survive real interview follow-ups.
      </p>
      <p>
        <code>RAG</code>
        <code>Local Index</code>
        <code>InterviewCard</code>
        <code>Codex Pack</code>
      </p>
      <p>
        <a href="https://github.com/YingaoWang-casia/shushu-InterviewProof-RAG">
          <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github" />
        </a>
        <img src="profile/badges/stars-interviewproof-rag.svg" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
  </tr>
</table>

---

## 📈 Contribution Activity

<div align="center">

<a href="https://github.com/YingaoWang-casia">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=YingaoWang-casia&bg_color=ffffff&color=0f172a&line=0891b2&point=14b8a6&area=true&area_color=ccfbf1&hide_border=true&custom_title=GitHub%20Contribution%20Activity" alt="GitHub contribution activity graph" />
</a>

</div>

---

## ⭐ GitHub Stats

<div align="center">

<a href="https://github.com/YingaoWang-casia">
  <img height="168" src="profile/github-stats.svg" alt="GitHub stats" />
</a>
<a href="https://github.com/YingaoWang-casia?tab=repositories">
  <img height="168" src="profile/top-languages.svg" alt="Top languages" />
</a>

</div>

---

## 🔭 Current Focus

- Three-class / multi-class turn detection for real speech interaction
- Interruption recognition and response timing control in full-duplex speech systems
- Speech-interaction benchmark construction and multi-model evaluation
- Robust VAD and semantic endpoint detection for low-resource scenarios
- Agent + RAG engineering for document intelligence and project review
- Codex Skill and local AI toolchain development

---

## 📬 Contact

- GitHub: @YingaoWang-casia
- Email: 2967523019@qq.com

<div align="center">

> Focus on Speech AI, Turn-taking, Full-duplex Interaction and Practical LLM Agent Systems.

</div>
