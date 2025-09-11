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
    • Agentic AI Orchestration
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

## Example Enterprise Use Cases  📊
    1. Investment Evaluation: Automatically compute project viability using NPV & IRR.
    2. Operational Strategy: Run break-even and profit margin analyses for new products.
    3. Marketing Optimization: Forecast ROI and payback period for campaigns.
    4. Financial Risk Management: Analyze loans, interest payments, and debt strategies.
    5. Pricing & Profitability Decisions: Model “what-if” scenarios for product pricing.

## Workflow Structure  🛠️ 

The workflow is composed of:

    • Chat Input – Starts the interaction with the Agent.
    
    • AI Agent – The core orchestration layer that routes tasks.
    
    • OpenAI Chat Model – LLM reasoning engine.
    
    • Simple Memory – Maintains short-term conversation state.
    
    • Calculator Tool – For arithmetic and financial calculations.
    
    • Code Tool (Python) – For advanced computations like IRR, amortization, and forecasting.

## Repository Contents  📂 
    • Agentic_AI_workflow_1_Calculator.json → n8n workflow file (import directly into n8n).
    • Example financial decision prompts and AI outputs (see below).
    • Python evaluation of the examples
    • Documentation for extending the workflow with enterprise integrations.

## Why This Matters for Enterprises 📈
Enterprises deal with massive volumes of financial, operational, and customer data. Traditional analysis pipelines require manual effort or expensive custom software. This Agentic AI workflow delivers:

    • Scalability: Automates decision-making across departments.
    
    • Flexibility: Integrates with enterprise systems (ERP, CRM, finance databases).
    
    • Cost Efficiency: Reduces reliance on manual analysis or retraining ML models.
    
    • Real-Time Decisions: Handles business scenarios dynamically with LLM reasoning + automated tools.
    
When extended with vector databases, enterprises can achieve:

    • Retrieval-Augmented Generation (RAG) for domain-specific insights.
    
    • Real-time updates from structured and unstructured data.
    
    • Lower total cost of ownership by avoiding repeated retraining of models.

## Getting Started 📥
    1. Clone this repo.
    2. Import the workflow file into your n8n instance:
        ◦ Go to n8n → Workflows → Import from File.
        ◦ Select Agentic_AI_workflow_1_Calculator.json.
    3. Configure your credentials:
        ◦ OpenAI API Key.
        ◦ (Optional) Google Calendar / Pinecone for extended enterprise use.
    4. Trigger the chat input node to start interacting with the Agent.

## Future Extensions 🔮 
    • Vector Database Integration (e.g., Pinecone, Weaviate) for enterprise data access.
    • RAG-powered Finance Assistant capable of retrieving company-specific KPIs.
    • Integration with BI dashboards for automated reporting.
    • Multi-Agent Collaboration for handling cross-department workflows.





## Usage Examples  💡 
Below are some examples of how the workflow can be used to automate enterprise business and financial decisions. Each example shows the user’s prompt, how the Agent reasons, and the final output.

### 1. Investment Analysis (NPV & IRR)
   
Prompt:
Evaluate a project with an initial investment of $50,000 and cash inflows of $15,000 per year for 5 years at a discount rate of 10%.

Agent Reasoning (tools used):
    • Detects need for financial calculation.
    • Uses Code Tool to compute Net Present Value (NPV) and Internal Rate of Return (IRR).
    
Output:
    • NPV ≈ $6,137
    • IRR ≈ 14.5%
    
    • ✅ The project is financially viable since IRR > discount rate.

### Example of how the question was posed at the Agent's prompt:
    I am evaluating a business expansion project that requires an upfront investment of $800,000 and will generate annual cash flows of $150,000 for 10 years. The discount rate is 8%.
   
    Can you: 1. Calculate the Net Present Value (NPV)?
   
             2. Calculate the Internal Rate of Return (IRR)?
   
             3. Advise whether this is a financially viable project?

             4. Use all available tools including the code too
   
     ### AI Agent's Response:
     1. Net Present Value (NPV): The NPV of the investment is approximately $206,512.21.
        
     3. Internal Rate of Return (IRR): The calculated IRR for this investment is approximately 18.33%.
        
     5. Financial Viability: Since the NPV is positive and the IRR exceeds the discount rate of 8%, the project is considered financially viable.
        
    Summary:
        • NPV: $206,512.21
        • IRR: 18.33%
        
        If you have any more questions or need further assistance, feel free to ask!
    
---
> [!NOTE]
> Interested reader can compare the Agent's evaluation with the python analysis (investment_analysis_npv_irr.py); also available in the repository
---


### 2. Break Even Analysis
Prompt:
A product sells for $120, costs $45 per unit to make, and fixed costs are $250,000. How many units do we need to break even?

Agent Reasoning:
    • Identifies break-even formula: Fixed Costs ÷ (Price – Variable Cost).
    • Uses Calculator Tool to compute.
    
Output:
    • Break-even units = 3330
    
    • ✅ The business needs to sell 625 units to cover costs. 


### Example of how the question was posed at the Agent's prompt:
      My company is launching a new product. The fixed costs are $250,000, the variable cost per unit is $45, and the selling price per unit is $120. 
      
      Can you: 1. Calculate the break-even point in units and dollars? 
      
               2. Determine how many units we need to sell to earn a profit of $100,000? 
               
               3. Use all the available tools including calculator and code tool
   
     ### AI Agent's Response:
      1. Break-Even Point:
      
        ◦ The break-even point is approximately 3,334 units.
        ◦ In terms of dollars, the break-even revenue can be calculated as: [ \text{Break-Even Revenue} = \text{Break-Even Units} \times \text{Selling Price} = 3344 \times 120 \approx $400,000 ]
        
      2. To earn a profit of $100,000, you need to sell approximately 4,667 units.
     
   Summary:
    • Break-Even Point: ≈ 3,334 units (≈ $400,000 revenue)
    
    • Units to Earn $100,000 Profit: ≈ 4,667 units
    
    
   If you need further assistance or analyses, feel free to ask!

---
> [!NOTE]
> Interested reader can compare the Agent's evaluation with the python analysis (break_even_analysis.py); also available in the repository
---


### 3. Marketing ROI Forecasting
Prompt:
If we spend $100,000 on a campaign that generates $250,000 in sales, what’s the ROI and payback period?

Agent Reasoning:

    • Uses Calculator Tool to compute ROI and payback.
    
Output:

    • ROI = 150%
    • Payback period = < 1 year
    
    • ✅ Campaign is highly profitable.


### Example of how the question was posed at the Agent's prompt:
      I am planning a $50,000 digital marketing campaign expected to increase monthly sales by $12,000 for the next 6 months. The profit margin on sales is 30%.
      Can you:
      
        1. Calculate the return on investment (ROI)?
        
        2. Estimate the payback period?
    
        3. Tell me if this campaign is profitable?
   
   ### AI Agent's Response:
   
     1. Return on Investment (ROI): The ROI for the marketing campaign is approximately -56.8%. 
     
     This indicates that the campaign is expected to result in a loss relative to the initial investment.
     
    2. Payback Period: The estimated payback period is approximately 13.89 months. 
    
    This means it would take nearly 14 months to recover the initial investment from the profits generated by the campaign.
    
    3. Profitability: Given the negative ROI, the campaign is not expected to be profitable, as the anticipated returns do not cover the initial investment.
    
    If you need further analysis or assistance, feel free to ask!


### 3. Loan Amortization

Prompt:

For a $200,000 loan at 6% interest over 20 years, calculate the monthly payment and total interest paid.
    Agent Reasoning:
        • Uses Code Tool (Python) with amortization formula.
        
    Output:
    
    • Monthly Payment ≈ $1,432
    
    • Total Interest ≈ $143,680
    
    • ✅ Useful for debt strategy planning.


### Example of how the question was posed at the Agent's prompt:

    I am taking a $300,000 business loan at a 6% annual interest rate, amortized over 5 years with monthly payments.
    
    Can you:
    
    1. Calculate the monthly payment?
    
    2. Generate an amortization schedule?
    
    3. Calculate the total interest paid over the loan period?
   
   ### AI Agent's Response:
   
    Monthly Payment: The monthly payment for the loan is approximately $5,799.84.
    
    1. Amortization Schedule:
    
        ◦ The loan amount is $300,000.
        
        ◦ The annual interest rate is 6%.
        
        ◦ The loan is amortized over 5 years (60 months).
        
        ◦ Based on this structure, here is a simplified look at the first few months of the amortization schedule:


                ◦ 
Month
Payment
Interest Paid
Principal Paid
Remaining Balance
1
$5,799.84
$1,500.00
$4,299.84
$295,700.16
2
$5,799.84
$1,478.50
$4,321.34
$291,378.82
3
$5,799.84
$1,458.99
$4,340.85
$287,037.96
4
$5,799.84
$1,435.19
$4,364.65
$282,673.31
5
$5,799.84
$1,416.24
$4,383.60
$278,289.71
...
...
...
...
...
60
$5,799.84
$28.55
$5,771.29
$0.00
       
3. Total Interest Paid: The total interest paid over the loan period is approximately $47,990.04.
   
Summary:

    • Monthly Payment: $5,799.84
    
    • Total Interest Paid: $47,990.04
    
If you need any further information or calculations, feel free to ask!











5. Pricing Strategy
Prompt:
If we price a product at $50 with costs of $30 per unit, what’s the profit at 10,000 units sold?
Agent Reasoning:
    • Simple arithmetic via Calculator Tool.
Output:
    • Profit = $200,000
    • ✅ Clear margin-based decision-making.


🎯 Why This Matters
These examples show how Agentic AI workflows in n8n can handle complex business and financial decisions without requiring specialized financial software. 

The agent autonomously selects the right tool (calculator or code), performs reasoning, and delivers clear, actionable outputs.

🚀 Quick Demo
Here’s an another example conversation with the agent in action.

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
