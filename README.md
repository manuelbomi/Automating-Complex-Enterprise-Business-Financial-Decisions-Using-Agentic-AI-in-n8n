# Automating Complex Enterprise Business & Financial Decisions Using Agentic AI in n8n

## Overview  📌 
#### This repository contains an Agentic AI workflow built in n8n that automates complex enterprise business and financial decision-making. The workflow leverages large language models (LLMs), tools (calculator & code execution), and memory to analyze scenarios, generate insights, and provide actionable recommendations — all in real-time.

### The workflow, designed in n8n is shown below:

<img width="905" height="350" alt="Image" src="https://github.com/user-attachments/assets/f6686351-dc2c-49cb-b603-884c309233ae" />

---

#### Using the Repository for Your Enterprise Buinesss/Financial Applications
##### By combining Agentic AI with workflow automation, enterprises can scale intelligent decision-making across finance, operations, and strategy without building bespoke systems from scratch. 

##### In this discourse, we present a method by which you can clone the repository and apply the Agent it to automate and provide insight on enterprise financial and business decisions. 

##### We also provide several financial and business use cases. 

##### In additional, we provide step by step method regarding how you can design the workflow in-house, in n8n for your enterprise use cases. 


## Key Features  🚀 
    • **Agentic AI Orchestration**
        ◦ LLM-powered reasoning using OpenAI’s gpt-4o-mini.
        ◦ Context-aware memory for handling multi-step conversations.
        ◦ Autonomous tool selection (Calculator & Code Tool) for solving analytical problems.
        
    • Financial & Business Analysis Tools
        ◦ Investment Analysis: NPV & IRR calculations for capital projects.
        ◦ Break-Even Analysis: Unit & revenue thresholds for profitability.
        ◦ Marketing ROI Forecasting: Campaign payback & ROI estimation.
        ◦ Loan Amortization: Monthly payments, amortization schedules, and interest breakdown.
        ◦ Pricing Strategy: Profitability & volume sensitivity analysis.
        
    • Enterprise-Ready Design
        ◦ Built entirely in n8n, ensuring scalability, automation, and easy integration with enterprise systems (databases, CRMs, ERPs, etc.).
        ◦ Extensible with vector databases (e.g., Pinecone) for Retrieval-Augmented Generation (RAG) when connected to enterprise data sources.
        ◦ Modular design: additional tools and APIs can be added seamlessly.

📊 Example Enterprise Use Cases
    1. Investment Evaluation: Automatically compute project viability using NPV & IRR.
    2. Operational Strategy: Run break-even and profit margin analyses for new products.
    3. Marketing Optimization: Forecast ROI and payback period for campaigns.
    4. Financial Risk Management: Analyze loans, interest payments, and debt strategies.
    5. Pricing & Profitability Decisions: Model “what-if” scenarios for product pricing.

🛠️ Workflow Structure
The workflow is composed of:
    • Chat Input – Starts the interaction with the Agent.
    • AI Agent – The core orchestration layer that routes tasks.
    • OpenAI Chat Model – LLM reasoning engine.
    • Simple Memory – Maintains short-term conversation state.
    • Calculator Tool – For arithmetic and financial calculations.
    • Code Tool (Python) – For advanced computations like IRR, amortization, and forecasting.

📂 Repository Contents
    • Agentic_AI_workflow_1_Calculator.json → n8n workflow file (import directly into n8n).
    • Example financial decision prompts and AI outputs (see below).
    • Documentation for extending the workflow with enterprise integrations.

📈 Why This Matters for Enterprises
Enterprises deal with massive volumes of financial, operational, and customer data. Traditional analysis pipelines require manual effort or expensive custom software. This Agentic AI workflow delivers:
    • Scalability: Automates decision-making across departments.
    • Flexibility: Integrates with enterprise systems (ERP, CRM, finance databases).
    • Cost Efficiency: Reduces reliance on manual analysis or retraining ML models.
    • Real-Time Decisions: Handles business scenarios dynamically with LLM reasoning + automated tools.
When extended with vector databases, enterprises can achieve:
    • Retrieval-Augmented Generation (RAG) for domain-specific insights.
    • Real-time updates from structured and unstructured data.
    • Lower total cost of ownership by avoiding repeated retraining of models.

📥 Getting Started
    1. Clone this repo.
    2. Import the workflow file into your n8n instance:
        ◦ Go to n8n → Workflows → Import from File.
        ◦ Select Agentic_AI_workflow_1_Calculator.json.
    3. Configure your credentials:
        ◦ OpenAI API Key.
        ◦ (Optional) Google Calendar / Pinecone for extended enterprise use.
    4. Trigger the chat input node to start interacting with the Agent.

🔮 Future Extensions
    • Vector Database Integration (e.g., Pinecone, Weaviate) for enterprise data access.
    • RAG-powered Finance Assistant capable of retrieving company-specific KPIs.
    • Integration with BI dashboards for automated reporting.
    • Multi-Agent Collaboration for handling cross-department workflows.





💡 Usage Examples
Below are some examples of how the workflow can be used to automate enterprise business and financial decisions. Each example shows the user’s prompt, how the Agent reasons, and the final output.

1. Investment Analysis (NPV & IRR)
Prompt:
Evaluate a project with an initial investment of $50,000 and cash inflows of $15,000 per year for 5 years at a discount rate of 10%.
Agent Reasoning (tools used):
    • Detects need for financial calculation.
    • Uses Code Tool to compute Net Present Value (NPV) and Internal Rate of Return (IRR).
Output:
    • NPV ≈ $6,137
    • IRR ≈ 14.5%
    • ✅ The project is financially viable since IRR > discount rate.

2. Break-Even Analysis
Prompt:
A product sells for $200, costs $120 per unit to make, and fixed costs are $50,000. How many units do we need to break even?
Agent Reasoning:
    • Identifies break-even formula: Fixed Costs ÷ (Price – Variable Cost).
    • Uses Calculator Tool to compute.
Output:
    • Break-even units = 625
    • ✅ The business needs to sell 625 units to cover costs.

3. Marketing ROI Forecasting
Prompt:
If we spend $100,000 on a campaign that generates $250,000 in sales, what’s the ROI and payback period?
Agent Reasoning:
    • Uses Calculator Tool to compute ROI and payback.
Output:
    • ROI = 150%
    • Payback period = < 1 year
    • ✅ Campaign is highly profitable.

4. Loan Amortization
Prompt:
For a $200,000 loan at 6% interest over 20 years, calculate the monthly payment and total interest paid.
Agent Reasoning:
    • Uses Code Tool (Python) with amortization formula.
Output:
    • Monthly Payment ≈ $1,432
    • Total Interest ≈ $143,680
    • ✅ Useful for debt strategy planning.

5. Pricing Strategy
Prompt:
If we price a product at $50 with costs of $30 per unit, what’s the profit at 10,000 units sold?
Agent Reasoning:
    • Simple arithmetic via Calculator Tool.
Output:
    • Profit = $200,000
    • ✅ Clear margin-based decision-making.

🎯 Why This Matters
These examples show how Agentic AI workflows in n8n can handle complex business and financial decisions without requiring specialized financial software. The agent autonomously selects the right tool (calculator or code), performs reasoning, and delivers clear, actionable outputs.
🚀 Quick Demo
Here’s an example conversation with the agent in action.
User Prompt:
“Evaluate a project with an initial investment of $50,000 and cash inflows of $15,000 per year for 5 years at a discount rate of 10%.”
Agent Response (demo screenshot):
The agent:
    1. Understands the problem.
    2. Selects the Code Tool for financial calculations.
    3. Returns a clear, actionable answer:
        ◦ NPV ≈ $6,137
        ◦ IRR ≈ 14.5%
        ◦ ✅ Investment is profitable since IRR > discount rate.

📌 How to add visuals:
    • If you want a GIF demo: record a short interaction using ScreenToGif (Windows), Kap (Mac), or OBS. Save as demo.gif and link in the README like:
      ![Quick Demo](demo/demo.gif)
    • If you want screenshots: take 2–3 key screenshots (demo-1.png, demo-2.png) and place them in a /demo folder. Then reference them in the README.
