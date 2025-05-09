"""Default prompts used by the agent."""

SYSTEM_PROMPT = """You are a helpful AI assistant.

System time: {system_time}
"""

# OPENAI MODELS
GPT4O_PROMPT = """GPT-4o

"Excels at everyday tasks"

Brainstorming, summarizing, emails, and creative content. 

Fully multimodal: supports almost all capabilities (GPTs, data analysis, search, image generation, canvas, advanced voice) and inputs (documents, images, CSV files, audio, and video).

Example Prompts:
- Summarize meeting notes into key action items.
- Draft a follow-up email after a project kickoff.
- Proofread my report.
"""

GPT45_PROMPT = """GPT-4.5

"Ideal for creative tasks" 

Emotional intelligence, clear communication, creativity, and a more collaborative, intuitive approach to brainstorming.

Example Prompts:
- Create an engaging post about AI trends.
- Write a product description for a new feature launch.
- Develop a customer apology letter with an empathetic tone.
"""

O4MINI_PROMPT = """o4-mini

"Fast technical tasks" 

Quick STEM-related queries, programming, visual reasoning.

Example Prompts:
- Extract key data points from a CSV file.
- Provide a quick summary of a scientific article.
- Quick-fix this Python traceback for me.
"""

O4MINIHIGH_PROMPT = """o4-mini-high

"Detailed technical tasks"

Advanced coding, math, scientific explanations, thinks longer for higher accuracy.

Example Prompts:
- Solve a complex math equation and explain the steps.
- Draft SQL queries for data extraction.
- Explain a scientific concept in laymans terms.
"""

O3_PROMPT = """o3

"Complex, or multi step tasks" 

Strategic planning, detailed analyses, extensive coding, advanced math, science, coding, and visual reasoning.

Example Prompts:
- Develop a risk analysis for market expansion.
- Draft a business strategy outline based on competitive data.
- Run a multi-step analysis on this CSV, forecast next quarter and plot the trend.
"""

O1PRO_PROMPT = """o1-pro

"Complex reasoning" 

Takes a bit longer to think but delivers the accuracy you need for complex tasks.

Example Prompts:
- Draft a detailed risk-analysis memo for an EU data-privacy rollout.
- Generate a multi-page research summary on emerging technologies.
- Create an algorithm for financial forecasting using theoretical models.
"""


# ANTHROPIC MODELS
CLAUDE37SONNET_PROMPT = """Claude 3.7 Sonnet

"Our most intelligent model"

Highest level of intelligence and capability with toggleable extended thinking. Exceptional at complex reasoning and creative tasks.

Example Prompts:
- Draft a detailed strategic proposal with multiple stakeholder considerations.
- Analyze this dataset and provide insights with supporting visualizations.
- Create a comprehensive literature review on this specialized topic.
"""

CLAUDE35SONNET_PROMPT = """Claude 3.5 Sonnet

"Our previous most intelligent model"

High level of intelligence and capability. Excellent for complex tasks requiring deep understanding.

Example Prompts:
- Design a comprehensive research methodology for analyzing market trends.
- Explain the implications of a technical paper in simple terms.
- Create a detailed project plan with risk assessment.
"""

CLAUDE35HAIKU_PROMPT = """Claude 3.5 Haiku

"Our fastest model"

Intelligence at blazing speeds. Perfect for quick responses while maintaining quality.

Example Prompts:
- Summarize these meeting notes into key action items.
- Draft a quick email response to this customer inquiry.
- Provide a rapid analysis of these quarterly results.
"""

CLAUDE3OPUS_PROMPT = """Claude 3 Opus

"Powerful model for complex tasks"

Top-level intelligence, fluency, and understanding. Ideal for tasks requiring depth and nuance.

Example Prompts:
- Develop a comprehensive business strategy based on these market factors.
- Write a detailed technical specification for a new system architecture.
- Create an in-depth analysis of competing philosophical positions.
"""

CLAUDE3HAIKU_PROMPT = """Claude 3 Haiku

"Fastest and most compact model for near-instant responsiveness"

Quick and accurate targeted performance. Perfect for simple tasks requiring immediate responses.

Example Prompts:
- Generate a quick reply to this message.
- Summarize this paragraph in three bullet points.
- Draft a short product description based on these features.
"""

# GOOGLE MODELS
GEMINI25PRO_PROMPT = """Gemini 2.5 Pro

"Our most powerful thinking model with maximum response accuracy and state-of-the-art performance"

Input audio, images, video, and text, get text responses
Tackle difficult problems, analyze large databases, and more
Best for complex coding, reasoning, and multimodal understanding

Example Prompts:
- Analyze this video and provide a summary of its content.
- Given this dataset of user behavior, identify key trends and suggest product improvements.
- Write a Python script to automate a complex data processing task.
"""

GEMINI25FLASH_PROMPT = """GEMINI 2.5 Flash

"Our best model in terms of price-performance, offering well-rounded capabilities."

Input audio, images, video, and text, and get text responses
Model thinks as needed; or, you can configure a thinking budget
Best for low latency, high volume tasks that require thinking

Example Prompts:
- Extract all email addresses from this document.
- Summarize this article into three key bullet points.
- Generate a creative product description based on these features.
"""

GEMINI2FLASH_PROMPT = """2.0 Flash

"Our newest multimodal model, with next generation features and improved capabilities"

Input audio, images, video, and text, get text responses
Generate code and images, extract data, analyze files, generate graphs, and more
Low latency, enhanced performance, built to power agentic experiences

Example Prompts:
- Transcribe the audio from this meeting and identify action items.
- Generate a bar chart visualizing this sales data.
- Create an image of a futuristic cityscape.
"""


MODELS = {
    "gpt-4o": GPT4O_PROMPT,
    "gpt-4.5": GPT45_PROMPT,
    "o4-mini": O4MINI_PROMPT,
    "o4-mini-high": O4MINIHIGH_PROMPT,
    "o3": O3_PROMPT,
    "o1-pro": O1PRO_PROMPT,
    "claude-3.5-sonnet": CLAUDE35SONNET_PROMPT,
    "claude-3.7-sonnet": CLAUDE37SONNET_PROMPT,
    "claude-3.5-haiku": CLAUDE35HAIKU_PROMPT,
    "claude-3-opus": CLAUDE3OPUS_PROMPT,
    "claude-3-haiku": CLAUDE3HAIKU_PROMPT,
    "gemini-2.5-pro": GEMINI25PRO_PROMPT,
    "gemini-2.5-flash": GEMINI25FLASH_PROMPT,
    "gemini-2-flash": GEMINI2FLASH_PROMPT,
}
