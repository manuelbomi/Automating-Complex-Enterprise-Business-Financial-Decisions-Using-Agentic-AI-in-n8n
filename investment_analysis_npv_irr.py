import numpy_financial as npf

# Inputs
initial_investment = 800000
annual_cash_flow = 150000
years = 10
discount_rate = 0.08

# Cash flows: initial investment (negative), then annual returns
cash_flows = [-initial_investment] + [annual_cash_flow] * years

# 1. Net Present Value (NPV)
npv = npf.npv(discount_rate, cash_flows)

# 2. Internal Rate of Return (IRR)
irr = npf.irr(cash_flows)

# Output results
print(f"NPV: ${npv:,.2f}")
print(f"IRR: {irr * 100:.2f}%")

Output
NPV: $206,512.21
IRR: 13.43%