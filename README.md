# ResearchAI — Multi-Agent Research System

ResearchAI is a multi-agent AI research system that searches for recent information, processes relevant web sources, generates a structured research report, and uses a separate AI critic to review the result.

The project combines **LangChain, Groq, Tavily, BeautifulSoup, and Streamlit** into a practical research workflow.

---

## 🚀 Live Demo

[Open ResearchAI →](https://multi-agent-research-system-burhan.streamlit.app/)

## Overview

Traditional LLM responses can be limited when a question requires recent information.

ResearchAI addresses this by combining web search, source extraction, AI generation, and independent critique into a single pipeline.

A typical research request follows this workflow:

```text
Research Question
       │
       ▼
┌─────────────────────┐
│  News Discovery     │
│      Tavily         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Article Extraction  │
│ BeautifulSoup       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Report Generation  │
│   Groq + LangChain  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    AI Critique      │
│   LangChain / LLM   │
└──────────┬──────────┘
           │
           ▼
      Final Report
```

---

## Features

- 🔎 Recent web research using Tavily
- 🌐 Article content extraction with BeautifulSoup
- 🤖 LLM-powered research and report generation
- 🧠 Separate AI critic for reviewing generated reports
- 🔗 LangChain-based AI workflow
- ⚡ Groq-powered inference
- 🖥️ Streamlit web interface
- 📚 Expandable research evidence
- 📥 Downloadable research report
- 🔐 API keys stored securely using environment variables

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM and agent orchestration |
| Groq | LLM inference |
| Tavily | Web search and research |
| BeautifulSoup | Web page content extraction |
| Requests | HTTP requests |
| Streamlit | Web interface |
| python-dotenv | Environment variable management |

---

## Project Structure

```text
Multi-agent System/
│
├── app.py
├── pipeline.py
├── agents.py
├── tools.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

> File names may vary depending on the final project structure.

---

## How It Works

### 1. News Discovery

The research agent receives the user's research question and uses **Tavily** to find relevant and recent web sources.

For example:

```text
What is the current petrol subsidy situation in Pakistan?
```

The search stage returns information such as:

- Article titles
- URLs
- Search snippets
- Relevant sources

---

### 2. Article Extraction

Relevant URLs are identified from the search results.

The system then retrieves the pages using `requests` and extracts readable text using **BeautifulSoup**.

This gives the later stages access to article content instead of relying only on search snippets.

---

### 3. Report Generation

The collected research is passed to an LLM through **LangChain + Groq**.

The model converts the research material into a structured report.

The goal is to provide a more useful research response than a simple search result list.

---

### 4. AI Critique

The generated report is passed through a separate critic chain.

The critic examines the report for issues such as:

- Missing information
- Weak explanations
- Unsupported claims
- Inconsistencies
- Areas that require further research

The critique is displayed separately from the final report.

---

## Streamlit Interface

The application provides a dashboard where users can:

1. Enter a research question
2. Start the research pipeline
3. View the generated report
4. Read the AI critique
5. Inspect discovered sources
6. Inspect extracted article content
7. Download the final report

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd "Multi-agent System"
```

Replace the repository URL with your actual GitHub repository.

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

You can use `.env.example` as a template.

**Never commit your `.env` file to GitHub.**

The `.gitignore` file already excludes it from version control.

---

## Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

If Streamlit does not open automatically, use the local URL shown in the terminal.

---

## Example Research Questions

You can try questions such as:

```text
What are the latest developments in artificial intelligence?

What is the current state of renewable energy adoption?

What are the latest developments in Pakistan's technology sector?

What are the current trends in cybersecurity?

What is the current petrol subsidy situation in Pakistan?
```

For best results, use specific research questions.

---

## Important Limitations

This project is designed as a practical AI research system, but it has several limitations.

### Web Scraping

Some websites may:

- Block automated requests
- Require JavaScript
- Use anti-bot protection
- Return incomplete content

BeautifulSoup and standard HTTP requests cannot reliably extract content from every website.

### Search Results

The quality of the final report depends partly on the sources returned by the search provider.

Search results should therefore be treated as research material rather than guaranteed truth.

### LLM Output

AI-generated reports can contain:

- Incorrect interpretations
- Missing context
- Hallucinated information
- Unsupported conclusions

The critique stage helps identify potential weaknesses but does not guarantee factual correctness.

### API Limits

The project uses external APIs with usage and rate limits.

Free API tiers may also introduce latency, so research requests can take some time to complete.

---

## Future Improvements

Possible improvements include:

- Real-time pipeline progress in the Streamlit UI
- Better article extraction
- Source ranking and filtering
- Citation-aware report generation
- Parallel article scraping
- More robust URL extraction
- Research history
- Report export to PDF
- Persistent research storage
- Source credibility analysis
- Human-in-the-loop verification
- More specialized research agents
- LangGraph-based workflow orchestration

---

## Learning Goals

This project was built to explore practical concepts in:

- Generative AI
- AI agents
- Multi-agent workflows
- LangChain
- LLM tool calling
- Web search integration
- Web scraping
- Prompt engineering
- AI-generated reports
- AI evaluation and critique
- Streamlit application development

---

## Disclaimer

ResearchAI is an educational AI research project.

The generated reports should not be treated as authoritative sources. Important information should be independently verified using the original sources, particularly for financial, medical, legal, political, or other high-impact topics.

---

## Author

**Burhan Arshad**

BS Computer Science  
University of Central Punjab

GitHub: `https://github.com/burhan-arshad`

---

## License

This project is available for educational and personal use. Add an appropriate open-source license if you decide to distribute the project publicly.
