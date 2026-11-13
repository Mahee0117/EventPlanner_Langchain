<div align="center">

# 💍 Multi-Agent Event Planner

**A hands-on LangChain learning project** — exploring how to orchestrate multiple AI agents that reason, delegate, and search the web to solve a real-world problem.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1.5-green?logo=chainlink&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1.2-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.67-red?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black)
![Tavily](https://img.shields.io/badge/Tavily-Web_Search-purple)

</div>

---

## 🧠 Why Not Just Use ChatGPT or Gemini?

> **"You could just open ChatGPT and ask it to plan your wedding."**  
> You're right. But that's not the point.

This project is about **learning how to build AI systems**, not just using them.

| Just using ChatGPT / Gemini | This Project |
|---|---|
| You type, it answers | You **architect** how agents think and delegate |
| One model, one prompt | **Multiple agents** with distinct roles and tools |
| No real-time data | **Live web search** via Tavily at inference time |
| Black box | You control every layer — model, tools, memory, flow |
| Zero code | Full Python stack: LangChain, LangGraph, Streamlit |

This project is about understanding **how** modern AI assistants work under the hood — agent loops, tool use, task delegation, and multi-step reasoning — by building one yourself from scratch.

---

## ✨ What It Does

You describe your wedding. The system spins up a **team of AI agents** that:

1. 🧑‍💼 **Main Agent** understands your requirements and breaks the planning into sub-tasks
2. 🔍 **Sub-Agent 1 & 2** independently search the web (venues, caterers, photographers, decorators)
3. 🧩 The main agent **synthesises all results** into a structured wedding plan
4. 🖥️ Everything is served through a clean **Streamlit web UI** with a live activity log

---

## 🏗️ Architecture

```
User Input (Streamlit UI)
        │
        ▼
┌─────────────────────────┐
│      Main Agent         │  ← Senior Wedding Planner
│  (qwen2:7b via Ollama)  │  ← Reasons, plans, synthesises
│  Tools: delegate_task1  │
│         delegate_task2  │
└────────┬────────────────┘
         │  delegates sub-tasks
    ┌────┴────┐
    ▼         ▼
┌──────────┐ ┌──────────┐
│Sub-Agent1│ │Sub-Agent2│   ← Independent searchers
│  Tool:   │ │  Tool:   │
│search_web│ │search_web│
└────┬─────┘ └────┬─────┘
     │             │
     ▼             ▼
  Tavily API (Real-time Web Search)
```

---

## 📁 Project Structure

```
multiagentic_event_planner/
│
├── app.py          # Streamlit UI — main entry point
├── main.py         # CLI entry point (no UI)
├── agents.py       # Sub-agents + delegate tool definitions
├── models.py       # LLM setup (Ollama / qwen2:7b)
├── tools.py        # search_web tool using Tavily
├── prompts.py      # System prompt for the main agent
├── pyproject.toml  # Project dependencies (uv)
└── .env            # API keys (not committed)
```

---

## 🔑 Key Concepts Learned

| Concept | Where |
|---|---|
| **LangChain `@tool` decorator** | `tools.py` — wrapping Tavily into a callable tool |
| **ReAct Agent loop** | `agents.py` — `create_react_agent` (Reason → Act → Observe) |
| **Tool use & delegation** | `agents.py` — sub-agents exposed as tools to the main agent |
| **Multi-agent orchestration** | `main.py` / `app.py` — main agent coordinates sub-agents |
| **Streaming agent output** | `app.py` — `agent.stream()` with live UI updates |
| **Local LLM with Ollama** | `models.py` — `init_chat_model` + `qwen2:7b` |
| **Real-time web search** | `tools.py` — Tavily search API integration |

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.13+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) — fast Python package manager
- [Ollama](https://ollama.com/) — installed and running locally
- A [Tavily API key](https://tavily.com/) — free tier available

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/Multiagentic_Event_Planner.git
cd Multiagentic_Event_Planner
```

### 2. Pull the LLM model

```bash
ollama pull qwen2:7b
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5. Run the Streamlit app

```bash
uv run streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

---

## 🖥️ Demo

Describe your wedding in the text box — for example:

> *"I want an outdoor wedding in Bangalore with 100 guests and a budget of ₹10 lakhs. I prefer a floral theme with vegetarian catering."*

The agents will search the web in real-time and return a structured plan with venues, catering, decorators, photographers, and a planning timeline.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [LangChain](https://www.langchain.com/) | Agent framework, tool definitions |
| [LangGraph](https://www.langchain.com/langgraph) | ReAct agent loop orchestration |
| [Ollama](https://ollama.com/) | Running `qwen2:7b` locally — no API cost |
| [Tavily](https://tavily.com/) | Real-time web search API |
| [Streamlit](https://streamlit.io/) | Web UI |
| [uv](https://docs.astral.sh/uv/) | Fast Python package manager |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📖 Learning Resources

Built while exploring:

- [LangChain Python Docs](https://python.langchain.com/docs/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [ReAct: Synergizing Reasoning and Acting in LLMs](https://react-lm.github.io/)

---

## 📝 License

MIT — feel free to fork, learn from, and build on top of this.

---

<div align="center">
  Built with ❤️ as a LangChain learning project · Not for production use
</div>

