# IELTS Speaking Coach

一个基于 PyQt5 的 IELTS 口语练习与评测桌面应用，集成语音识别与 LLM 智能批改功能。

## 功能特性

- 🎤 **语音交互**：使用 Windows SAPI 实现语音输入与 TTS 播报
- 📚 **真题练习**：内置剑桥雅思 9/13 等官方口语题库
- 📝 **智能评测**：LLM（Deepseek/OpenAI）基于 IELTS 官方评分标准逐项分析
- 📄 **详细报告**：一键生成 PDF 批改报告，含 Fluency、Vocabulary、Grammar、Pronunciation 等维度评分
- 🔄 **进度保存**：自动保存练习进度，支持断点续练
- 📋 **自定义题目**：支持添加自定义口语题集

## 项目结构

`
IELTS-SpeakingCoach/
├── data/                  # 题库数据（剑桥9-21，45套真题）
│   ├── question_bank.py   # 官方题库（Cambridge 9/13）
│   ├── custom_questions.json  # 自定义题目
│   └── __init__.py
├── engine/                # 核心引擎
│   ├── scorer.py          # 评分引擎（IELTS 7 标准）
│   ├── speech_engine.py   # 语音引擎（TTS + 语音识别）
│   ├── session_manager.py # 会话管理
│   ├── correction_report.py   # PDF 批改报告生成
│   └── sample_answers.py      # 示范答案生成
├── sessions/              # 练习进度数据
├── corrections/           # 生成的 PDF 批改报告
├── references/            # 导出的参考文献
├── main.py                # 主程序入口
├── run.ps1                # PowerShell 启动脚本
├── run.bat                # CMD 启动脚本
├── requirements.txt       # Python 依赖
├── .env.example           # 环境变量配置模板
└── .gitignore
`

## 环境要求

- Windows 系统（需要 SAPI 语音引擎支持）
- Python 3.10+
- Deepseek 或 OpenAI 兼容的 API Key

## 快速开始

### 1. 安装依赖

`ash
pip install -r requirements.txt
`

### 2. 配置 API Key

`ash
# 复制环境变量模板
copy .env.example .env

# 编辑 .env 文件，填入你的 API Key
# DEEPSEEK_API_KEY=sk-your-key-here
`

### 3. 运行

`ash
# PowerShell
.\run.ps1

# 或 CMD
.\run.bat

# 或直接运行
python main.py
`

## 使用说明

1. **选择题目**：从 Cambridge 9/13 或自定义题集中选择练习
2. **开始录音**：点击语音按钮，朗读你的回答
3. **获取评测**：系统自动生成 Fluency、Vocabulary、Grammar、Pronunciation 等多维度评分
4. **查看报告**：生成详细 PDF 报告，包含改进建议

## 配置说明

应用通过 .env 文件加载配置：

| 变量 | 说明 | 默认值 |
|------|------|--------|
| DEEPSEEK_API_KEY | Deepseek API Key | - |
| DEEPSEEK_BASE_URL | Deepseek API 地址 | https://api.deepseek.com |
| DEEPSEEK_MODEL | Deepseek 模型 | deepseek-chat |
| OPENAI_API_KEY | OpenAI API Key（备选） | - |
| OPENAI_BASE_URL | OpenAI API 地址（备选） | https://api.openai.com/v1 |
| LLM_MODEL | 通用模型名 | deepseek-chat |

## 许可证

MIT

