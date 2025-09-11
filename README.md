# Automating Complex Enterprise Business & Financial Decisions Using Agentic AI in n8n

## Overview  📌 
#### This repository contains an Agentic AI workflow built in n8n that automates complex enterprise business and financial decision-making. The workflow leverages large language models (LLMs), tools (calculator & code execution), and memory to analyze scenarios, generate insights, and provide actionable recommendations — all in real-time.

### The workflow, designed in n8n is shown below:

<img width="905" height="350" alt="Image" src="https://github.com/user-attachments/assets/f6686351-dc2c-49cb-b603-884c309233ae" />

---

#### How to Use this Repository for Your Enterprise Buinesss/Financial Applications
##### By combining Agentic AI with workflow automation, enterprises can scale intelligent decision-making across finance, operations, and strategy without building bespoke systems from scratch. 

##### In this discourse, we present a method by which you can clone the repository and apply the Agent to your use case(s), to automate and provide insight on financial and business decisions in ypur enterprise. 

##### We also provide several financial and business use cases and examples. 

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

#### However, if the user prefers to build the agent in n8n from ground up, users can start with the primer here: https://github.com/manuelbomi/An-Enterprise-Agentic-AI-Primer-with-n8n
#### Use the primer to build the Agent up to the calculator level shown below:

<img width="707" height="381" alt="Image" src="https://github.com/user-attachments/assets/7ccaba39-b772-4454-85b3-5f008173cbc5" />
---

#### After accomplishing the primer workflow, then do the following brief steps to complete the agent:

#### (i) Add Code Tool to the agent

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/82ebf3d3-ace4-4763-beb9-c8a1633fd8a7" />
---

#### (ii) Increase the Agent's memory length

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/6ddeab15-17b3-4a78-a976-52dda120ac95" />

---

#### Obtain the enterprise financial/business Agent as shown below:

<img width="905" height="350" alt="Image" src="https://github.com/user-attachments/assets/0bc7915d-425f-410a-9893-3c1e66e8c9aa" />

---


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
   
    Can you: 1. Calculate the Net Present Value (NPV)
   
             2. Calculate the Internal Rate of Return (IRR)
   
             3. Advise whether this is a financially viable project

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

---
---


### 4. Loan Amortization

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
        

| Monthly | Payment | Interest Paid | Principal Paid | Remaining Balance |
| :------- | :----------: | :--------: | :----------: | :----------: |
| 1   | $5,799.84       | $1500.00    | $4,299.84 | $295,700.16 |
| 2 | $5.799.84         |    $1478.50   | $4,321.34 | $291,378.82 | 
| 3 | $5.799.84         |   $1458.99     | $4,340.85 | $287,037.96 | 
| 4 | $5.799.84         |   $1435.19    | $4,364.65 | $282,673.31 | 
| 5 | $5.799.84         |   $1416.24    | $4,383.60 | $278,289.71 | 
| ... | ...        |  ...  | ... | ... | 
| 60 | $5.799.84         |   $28.55    | $5,771.29 | $0.00 |                ◦ 

       
3. Total Interest Paid: The total interest paid over the loan period is approximately $47,990.04.
   
Summary:

    • Monthly Payment: $5,799.84
    
    • Total Interest Paid: $47,990.04
    
If you need any further information or calculations, feel free to ask!

---
---


### 5. Pricing Strategy
Prompt:
If we price a product at $50 with costs of $30 per unit, what’s the profit at 10,000 units sold?

Agent Reasoning:

    • Simple arithmetic via Calculator Tool.
    
Output:
    • Profit = $200,000
    
    • ✅ Clear margin-based decision-making.


### Example of how the question was posed at the Agent's prompt:
     I am considering lowering the price of a product from $40 to $35 to boost volume. My variable cost per unit is $20 and fixed costs are $100,000. I currently sell 5,000 units per month.
     
    Can you:
    
    1. Estimate the new break-even point if we lower the price?
    
    2. Calculate how many additional units I need to sell to maintain the same profit level?

   ### AI Agent's Response:
   
    1. New Break-Even Point:
    
        ◦ New selling price = $35
        ◦ Variable cost per unit = $20
        ◦ Contribution Margin per unit = Selling Price - Variable Cost = $35 - $20 = $15
        ◦ Break-even point in units = Fixed Costs / Contribution Margin = $100,000 / $15 = 6,667 units.
        
    2. Additional Units to Maintain Profit Level:
    
        ◦ Current profit can be calculated as: [ \text{Current Profit} = (\text{Selling Price} - \text{Variable Cost}) \times \text{Current Units Sold} - \text{Fixed Costs} ]
        ◦ Current profit = ((40 - 20) \times 5,000 - 100,000 = 100,000 - 100,000 = 0) (this indicates zero profit at current pricing).
        ◦ To maintain the same profit level after reducing the price, calculate the new required volume: [ \text{New Required Volume} = ( 100,000 + \text{Fixed Costs}) / (\text{New Selling Price} - \text{Variable Cost}) ]
        ◦ Additional Units to Sell = New Required Volume - Current Volume = 6,667 - 5,000 = 1,667 additional units.

    Summary:
    • New Break-Even Point: 6,667 units
    • Additional Units to Maintain Same Profit Level: 1,667 units
    
    If you have further questions or need more assistance, feel free to ask!

---
---

### Some eaxamples of how the agent's front end display the financial/business calculations are shown below:

### Forecasting ROI

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/66edeb19-b071-41c2-a236-73dcec9210ec" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/805f042d-321a-4bf6-8219-2a0c60b1e4a1" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/f45982d5-d4b9-489d-85b4-915579571390" />
---

### Loan Amortization

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/1fbd2074-25cd-48f4-9f71-584ba2b59bf3" />

---




## Why This Matters for Enterprise Applications 🎯 

#### These examples show how Agentic AI workflows in n8n can handle complex business and financial decisions without requiring specialized financial software. 

#### The agent autonomously selects the right tool (calculator or code), performs reasoning, and delivers clear, actionable outputs.


--
Thank you for reading 
---


### **AUTHOR'S BACKGROUND**
### Author's Name:  Emmanuel Oyekanlu
```
Skillset:   I have experience spanning several years in data science, developing scalable enterprise data pipelines,
enterprise solution architecture, architecting enterprise systems data and AI applications,
software and AI solution design and deployments, data engineering, high performance computing (GPU, CUDA), machine learning,
NLP, Agentic-AI and LLM applications as well as deploying scalable solutions (apps) on-prem and in the cloud.

I can be reached through: manuelbomi@yahoo.com

Website:  http://emmanueloyekanlu.com/
Publications:  https://scholar.google.com/citations?user=S-jTMfkAAAAJ&hl=en
LinkedIn:  https://www.linkedin.com/in/emmanuel-oyekanlu-6ba98616
Github:  https://github.com/manuelbomi

```
[![Icons](https://skillicons.dev/icons?i=aws,azure,gcp,scala,mongodb,redis,cassandra,kafka,anaconda,matlab,nodejs,django,py,c,anaconda,git,github,mysql,docker,kubernetes&theme=dark)](https://skillicons.dev)


