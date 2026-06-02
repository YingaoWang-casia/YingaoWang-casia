<div align="center">

# 王迎澳

### 语音信号处理 | 音频 AI | 轮次检测 | 全双工交互 | LLM 智能体工程

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

## 关于我

本科就读于北京工业大学人工智能专业，目前为中国科学院自动化研究所模式识别与智能系统方向硕士。

主要研究和工程方向包括：VAD 语音端点检测、对话轮次检测、全双工语音交互、语音交互 Benchmark、LLM Agent 与 RAG 工程落地。

我关注从算法建模到工程落地的完整链路，包括数据集构建、模型训练与评测、音频处理流水线、实时交互系统、文档智能解析系统以及开源项目工程化维护。

---

## 教育经历

| 时间 | 学校 / 机构 | 专业 / 方向 |
| --- | --- | --- |
| 2022.09 - 2026.07 | 北京工业大学 | 人工智能，工学学士 |
| 2026.09 - 至今 | 中国科学院自动化研究所 | 模式识别与智能系统，硕士|

研究方向：语音交互、大模型应用。

---

## 实习经历

### 百融云创 — 语音算法工程师

时间：2025.12 - 至今

主要从事语音交互相关算法与系统研发，方向包括 轮次检测、VAD 语音端点检测、全双工语音交互 等。

参与内容包括：

1. 三分类轮次检测模型与系统开发  
   面向真实人机语音交互场景，研究用户表达是否完整、是否仍需等待、是否属于无效输入等问题，参与三分类轮次检测模型的设计、评测与工程化落地。

2. VAD 与语音端点检测优化  
   参与语音活动检测相关策略优化，关注短句、弱语音、长停顿、噪声、非语义发声等场景下的检测稳定性。

3. 全双工语音交互探索  
   参与全双工交互链路中的语音检测、轮次判断、打断识别和响应时机控制等模块开发，提升语音系统在自然对话中的交互流畅度。

技术关键词：VAD Turn Detection Full-duplex Interaction Speech AI Benchmark 实时语音交互

---

### 博华信智有限公司 — 智能体研发工程师

时间：2025.09 - 2025.12

主要参与 LLM 智能文档 Agent 项目的设计与开发，负责从需求分析、技术方案设计到工程实现的完整流程。

参与项目包括：

1. 技术方案生成助手  
   基于大模型与知识检索技术，实现文档解析、内容拆分、模块提取与技术方案自动生成。系统支持多节点并行处理文档内容，将人工方案编写流程由数小时压缩至分钟级。

2. 招投标文件智能解析助手  
   面向招投标业务场景，构建多路径文档抽取流程，结合 DeepSeek-Chat、差异化 Prompt、GTE 向量检索与 Rerank 策略，实现招标文件参数抽取、结构化解析与临时知识库构建。

技术关键词：LLM Agent RAG GTE Rerank 文档解析 知识库构建

---

## 研究与工程方向

### Speech AI / Audio Intelligence

- VAD 语音端点检测
- 三分类轮次检测
- 多分类全双工轮次检测
- 真实语音交互场景 Benchmark 构建
- 用户打断识别与响应时机控制
- 语音数据集构建、清洗、标注与评测
- 长音频切分、对齐、推理与后处理

### LLM Agent / RAG Engineering

- LLM 智能体系统开发
- RAG 知识库搭建与检索链路优化
- 文档结构化解析
- 多节点任务编排
- Prompt Engineering
- 本地化工具链与 Codex Skill 开发
- 面向项目复盘、面试压测和证据链整理的 AI 工程系统

---

## 技术栈

| 方向 | 技术 |
| --- | --- |
| 编程与工程 | Python, Bash, Linux, Git, Docker |
| 深度学习 | PyTorch, ONNX, Anaconda |
| 音频处理 | FFmpeg, VAD, Turn Detection, Full-duplex Interaction |
| 大模型工程 | LLM Agent, RAG, Prompt Engineering, GTE, Rerank |
| 工具平台 | Dify, RAGFlow |

---

## 代表性开源项目

### Speech AI / Turn-taking

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/Bairong-Xdynamics/TurnSense">
          TurnSense
        </a>
      </h3>
      <p>
        面向真实人机语音交互场景的三分类轮次检测模型。项目将用户输入划分为
        <code>complete</code> / <code>incomplete</code> / <code>invalid</code>
        三类，用于判断系统应当立即响应、继续等待，还是忽略无效输入。
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
        <img src="https://img.shields.io/github/stars/Bairong-Xdynamics/TurnSense?style=flat-square&color=0891b2" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/YingaoWang-casia/CoDeTT.github.io">
          CoDeTT Benchmark
        </a>
      </h3>
      <p>
        面向全双工语音交互的多分类轮次检测 Benchmark，用于评测 Turn-Taking
        模型在多场景决策任务中的表现。项目包含多模型统一评测脚本，
        论文已投稿至 Interspeech。
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
        <img src="https://img.shields.io/github/stars/YingaoWang-casia/CoDeTT.github.io?style=flat-square&color=0891b2" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
  </tr>
</table>

---

### LLM Agent / RAG / Codex Skill

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/YingaoWang-casia/shushu-ProjectProof">
          ProjectProof for Codex
        </a>
      </h3>
      <p>
        面向 AI / Agent / RAG / 算法 / 数据 / 前后端实习项目的 Codex Skill。
        项目目标不是编造经历，而是帮助用户把真实项目重新放回证据链、
        工程边界和面试追问中，降低“小厂项目 / 内部项目 / Agent Demo”
        在简历和面试中显得 toy 的问题。
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
        <img src="https://img.shields.io/github/stars/YingaoWang-casia/shushu-ProjectProof?style=flat-square&color=0891b2" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>
        <a href="https://github.com/YingaoWang-casia/shushu-InterviewProof-RAG">
          InterviewProof-RAG
        </a>
      </h3>
      <p>
        Codex-first 的本地面经 RAG 与项目压测系统。项目用于将零散面经
        整理为可追溯的 InterviewCard，并通过本地索引、Codex Pack 和
        ProjectProof Bridge 反向检查个人项目能否扛住真实面试追问。
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
        <img src="https://img.shields.io/github/stars/YingaoWang-casia/shushu-InterviewProof-RAG?style=flat-square&color=0891b2" />
        <img src="https://img.shields.io/badge/status-active-14b8a6?style=flat-square" />
      </p>
    </td>
  </tr>
</table>

---

## Contribution Activity

<div align="center">

<a href="https://github.com/YingaoWang-casia">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=YingaoWang-casia&bg_color=ffffff&color=0f172a&line=0891b2&point=14b8a6&area=true&area_color=ccfbf1&hide_border=true&custom_title=GitHub%20Contribution%20Activity" alt="GitHub contribution activity graph" />
</a>

</div>

---

## GitHub Stats

<div align="center">

<a href="https://github.com/YingaoWang-casia">
  <img height="168" src="https://github-readme-stats.vercel.app/api?username=YingaoWang-casia&show_icons=true&theme=default&bg_color=ffffff&hide_border=true" alt="GitHub stats" />
</a>
<a href="https://github.com/YingaoWang-casia?tab=repositories">
  <img height="168" src="https://github-readme-stats.vercel.app/api/top-langs/?username=YingaoWang-casia&layout=compact&theme=default&bg_color=ffffff&hide_border=true" alt="Top languages" />
</a>

</div>

---

## 当前关注

- 面向真实语音交互的三分类 / 多分类轮次检测
- 全双工语音交互中的打断识别与响应时机控制
- 语音交互 Benchmark 构建与多模型评测
- 低资源场景下鲁棒 VAD 与语义端点检测
- Agent + RAG 在文档智能解析和项目复盘中的工程落地
- Codex Skill 与本地 AI 工具链开发

---

## 联系方式

- GitHub: @YingaoWang-casia
- Email: 2967523019@qq.com

<div align="center">

> Focus on Speech AI, Turn-taking, Full-duplex Interaction and Practical LLM Agent Systems.

</div>
