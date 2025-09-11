def break_even_analysis(fixed_costs, variable_cost_per_unit, selling_price_per_unit, target_profit=0):
    # Contribution margin per unit
    contribution_margin = selling_price_per_unit - variable_cost_per_unit

    if contribution_margin <= 0:
        raise ValueError("Selling price must be greater than variable cost to make a profit.")

    # Break-even units
    break_even_units = fixed_costs / contribution_margin

    # Break-even revenue
    break_even_revenue = break_even_units * selling_price_per_unit

    # Units needed for target profit
    required_units_for_profit = (fixed_costs + target_profit) / contribution_margin

    # Round up units since you can't sell partial units
    break_even_units_rounded = int(-(-break_even_units // 1))  # Ceiling
    required_units_rounded = int(-(-required_units_for_profit // 1))  # Ceiling

    return {
        "break_even_units": break_even_units_rounded,
        "break_even_revenue": break_even_units_rounded * selling_price_per_unit,
        "units_for_target_profit": required_units_rounded,
        "target_profit": target_profit
    }

# Example usage
fixed_costs = 250000
variable_cost_per_unit = 45
selling_price_per_unit = 120
target_profit = 100000

results = break_even_analysis(fixed_costs, variable_cost_per_unit, selling_price_per_unit, target_profit)

print("Break-Even Analysis Results:")
print(f"Break-even units: {results['break_even_units']}")
print(f"Break-even revenue: ${results['break_even_revenue']:.2f}")
print(f"Units needed for ${target_profit} profit: {results['units_for_target_profit']}")

Code Output
Break-Even Analysis Results:
Break-even units: 3334
Break-even revenue: $400080.00
Units needed for $100000 profit: 4667
