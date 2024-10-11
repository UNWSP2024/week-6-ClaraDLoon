#Program #2: Monthly Tax Rate
#Clara Riley
#Luke Snell
#10/11/24


    FUNCTION CalculateSalesTax(totalSales)
        DECLARE stateTaxRate = 0.05
        DECLARE countyTaxRate = 0.025
        DECLARE stateTax = totalSales * stateTaxRate
        DECLARE countyTax = totalSales * countyTaxRate
        DECLARE totalTax = stateTax + countyTax
        RETURN stateTax, countyTax, totalTax
    END FUNCTION

    PROMPT "Enter your total sales for the month: "
    INPUT totalSales

    CALL CalculateSalesTax(totalSales) RETURNING stateTax, countyTax, totalTax

    DISPLAY "Your county sales tax: ", stateTax
    DISPLAY "Your state sales tax: ", countyTax
    DISPLAY "Your total sales tax: ", totalTax
