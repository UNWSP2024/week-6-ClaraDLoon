#Program #2: Tax Rate
#Clara Riley
#Luke Snell
#10/11/24

def calculate_taxes(total_sales):
    state_tax_rate = 0.05
    county_tax_rate = 0.025

    state_tax = total_sales * state_tax_rate
    county_tax = total_sales * county_tax_rate
    total_tax = state_tax + county_tax

    return state_tax, county_tax, total_tax


def main():
    total_sales = float(input("Enter your total sales for the month: $"))

    state_tax, county_tax, total_tax = calculate_taxes(total_sales)

    print(f"Your county sales tax: ${county_tax:.2f}")
    print(f"Your state sales tax: ${state_tax:.2f}")
    print(f"Your total sales tax: ${total_tax:.2f}")


if __name__ == "__main__":
    main()
