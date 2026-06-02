<div align="center">

# 王迎澳

### 语音信号处理 | 音频 AI | 轮次检测 | 全双工交互 | LLM 智能体工程

<p>
  <a href="https://github.com/YingaoWang-casia">
    <img src="https://img.shields.io/github/followers/YingaoWang-casia?label=Followers&style=for-the-badge&color=0891b2" alt="GitHub followers" />
  </a>
  <img src="https://komarev.com/ghpvc/?username=YingaoWang-casia&style=for-the-badge&color=0f766e" alt="Profile views" />
</p>

Python PyTorch Speech AI Turn Detection VAD Full-duplex Interaction LLM Agent RAG

</div>

---

## 关于我

本科就读于北京工业大学人工智能专业，目前为中国科学院自动化研究所 / 中国科学院大学模式识别与智能系统方向硕士研 0。

主要研究和工程方向包括：语音信号处理、VAD 语音端点检测、对话轮次检测、全双工语音交互、语音交互 Benchmark、LLM Agent 与 RAG 工程落地。

我关注从算法建模到工程落地的完整链路，包括数据集构建、模型训练与评测、音频处理流水线、实时交互系统、文档智能解析系统以及开源项目工程化维护。

---

## 教育经历

<p align="left">
  <strong>北京工业大学 | 人工智能 | 工学学士</strong><br/>
  2022.09 - 2026.07
</p>

<p align="left">
  <strong>中国科学院自动化研究所 / 中国科学院大学 | 模式识别与智能系统 | 硕士（研 0）</strong><br/>
  2026.09 - 至今<br/>
  研究方向：语音信号处理、声学建模、语音交互系统、大模型应用工程
</p>

---

## 实习经历

### 百融云创 — 语音算法 / 音频 AI 实习生

时间：2025.12 - 至今

主要从事语音交互相关算法与系统研发，方向包括 轮次检测、VAD 语音端点检测、全双工语音交互 等。

参与内容包括：

1. 三分类轮次检测模型与系统开发  
   面向真实人机语音交互场景，研究用户表达是否完整、是否仍需等待、是否属于无效输入等问题，参与三分类轮次检测模型的设计、评测与工程化落地。

2. VAD 与语音端点检测优化  
   参与语音活动检测相关策略优化，关注短句、弱语音、长停顿、噪声、非语义发声等场景下的检测稳定性。

3. 全双工语音交互探索  
   参与全双工交互链路中的语音检测、轮次判断、打断识别和响应时机控制等模块开发，提升语音系统在自然对话中的交互流畅度。

技术关键词：VAD Turn Detection Full-duplex Interaction Speech AI ONNX Benchmark 实时语音交互

---

### 博华信智有限公司 — 智能体研发工程师

时间：2025.09 - 2025.12

主要参与 LLM 智能文档 Agent 项目的设计与开发，负责从需求分析、技术方案设计到工程实现的完整流程。

参与项目包括：

1. 技术方案生成助手  
   基于大模型与知识检索技术，实现文档解析、内容拆分、模块提取与技术方案自动生成。系统支持多节点并行处理文档内容，将人工方案编写流程由数小时压缩至分钟级。

2. 招投标文件智能解析助手  
   面向招投标业务场景，构建多路径文档抽取流程，结合 DeepSeek-Chat、差异化 Prompt、GTE 向量检索与 Rerank 策略，实现招标文件参数抽取、结构化解析与临时知识库构建。

技术关键词：LLM Agent RAG DeepSeek GTE Rerank 文档解析 知识库构建

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

<p>
  <img src="https://skillicons.dev/icons?i=python,linux,bash,git,docker,pytorch,anaconda,ffmpeg&perline=8" alt="Tech stack" />
</p>

常用工具与框架：

Python PyTorch Linux Docker FFmpeg ONNX Anaconda Git FastAPI LangChain Dify RAGFlow Coze

---

## 代表性开源项目

### Speech AI / Turn-taking

<table>
  <tr>
    <td width="50%">
      <a href="https://github.com/Bairong-Xdynamics/TurnSense">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=Bairong-Xdynamics&repo=TurnSense&hide_border=true&bg_color=ffffff&title_color=0891b2&text_color=0f172a" />
      </a>
    </td>
    <td width="50%">
      <a href="https://github.com/YingaoWang-casia/CoDeTT.github.io">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=YingaoWang-casia&repo=CoDeTT.github.io&hide_border=true&bg_color=ffffff&title_color=0891b2&text_color=0f172a" />
      </a>
    </td>
  </tr>
</table>

#### TurnSense

面向真实人机语音交互场景的三分类轮次检测模型。项目将用户输入划分为 complete / incomplete / invalid 三类，用于判断系统应当立即响应、继续等待，还是忽略无效输入。

主要特点：

- 支持三分类语义轮次检测
- 面向语音助手、智能客服、实时通话等场景
- 关注误打断、抢话、无效触发等真实交互问题
- 提供模型、评测与工程化部署相关能力
- 当前持续维护

#### CoDeTT Benchmark

面向全双工语音交互的多分类轮次检测 Benchmark，用于评测 Turn-Taking 模型在多场景决策任务中的表现。

项目包含：

- 多分类全双工轮次检测评测任务
- 多模型统一评测脚本
- Qwen3-Omni、MiniCPM、KE-SemanticVAD 等模型评测入口
- 论文已投稿至 Interspeech
- 数据集已发布至 Hugging Face 和 ModelScope
- 当前持续维护

---

### LLM Agent / RAG / Codex Skill

<table>
  <tr>
    <td width="50%">
      <a href="https://github.com/YingaoWang-casia/shushu-ProjectProof">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=YingaoWang-casia&repo=shushu-ProjectProof&hide_border=true&bg_color=ffffff&title_color=0891b2&text_color=0f172a" />
      </a>
    </td>
    <td width="50%">
      <a href="https://github.com/YingaoWang-casia/shushu-InterviewProof-RAG">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=YingaoWang-casia&repo=shushu-InterviewProof-RAG&hide_border=true&bg_color=ffffff&title_color=0891b2&text_color=0f172a" />
      </a>
    </td>
  </tr>
</table>

#### ProjectProof for Codex

面向 AI / Agent / RAG / 算法 / 数据 / 前后端实习项目的 Codex Skill。项目目标不是编造经历，而是帮助用户把真实项目重新放回证据链、工程边界和面试追问中，降低“小厂项目 / 内部项目 / Agent Demo”在简历和面试中显得 toy 的问题。

核心能力：

- Truth Boundary：区分做过、参与过、了解过、补做后可写、当前不能写
- Evidence Contract：为每条强表达绑定代码、日志、截图、指标或 bad case
- Production Gap：分析 demo 与生产级项目之间的工程差距
- Question Tree：生成面试追问树
- SP / SSP Scorecard：评估项目竞争力和补强优先级
- 当前持续维护

#### InterviewProof-RAG

Codex-first 的本地面经 RAG 与项目压测系统。项目用于将零散面经整理为可追溯的 InterviewCard，并通过本地索引、Codex Pack 和 ProjectProof Bridge 反向检查个人项目能否扛住真实面试追问。

核心能力：

- 面经资料结构化整理
- 本地 lexical / vector index
- InterviewCard 抽取、去重、审核与检索
- Codex Pack 导出
- ProjectProof input 导出
- 面向项目深挖的模拟面试与证据补强
- 当前持续维护

---

## GitHub 数据统计

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=YingaoWang-casia&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=ffffff&title_color=0891b2&text_color=0f172a&icon_color=14b8a6&custom_title=GitHub%20Stats" height="170" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YingaoWang-casia&layout=compact&hide_border=true&bg_color=ffffff&title_color=0891b2&text_color=0f172a" height="170" />

</div>

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=YingaoWang-casia&theme=github" alt="GitHub Profile Summary" />

</div>

---

## Stars & Open Source Activity

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=YingaoWang-casia&hide_border=true&background=ffffff&stroke=0891b2&ring=14b8a6&fire=0891b2&currStreakLabel=0f172a&sideLabels=0f172a&currStreakNum=0f172a&sideNums=0f172a&dates=64748b" alt="GitHub Streak" />

</div>

<div align="center">

<a href="https://github.com/YingaoWang-casia?tab=repositories">
  <img src="https://img.shields.io/badge/Open%20Source-Active-14b8a6?style=for-the-badge&logo=github" />
</a>
<a href="https://github.com/YingaoWang-casia">
  <img src="https://img.shields.io/badge/Projects-Speech%20AI%20%7C%20RAG%20%7C%20Agent-0891b2?style=for-the-badge" />
</a>

</div>

---

## 贡献动态

<div align="center">
  <a href="https://github.com/YingaoWang-casia">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=YingaoWang-casia&bg_color=ffffff&color=0f172a&line=0891b2&point=14b8a6&area=true&area_color=ccfbf1&hide_border=true&custom_title=GitHub%20Contribution%20Graph" alt="GitHub Contribution Graph" />
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
