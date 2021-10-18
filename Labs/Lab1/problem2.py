def main ():
    cost_of_the_house = int (input ("how much will the house cost?"))
    annual_salary = float (input ("your annual salary amount is?"))
    percentage_saved_each_month = float (input ("the percentage you can save from salary each month?"))
    downpayment_percentage = 0.25

    salary_saved_each_month = annual_salary /12 * percentage_saved_each_month
    downpayment_needed = cost_of_the_house * downpayment_percentage 
    months_needed_to_save_downpayment = downpayment_needed // salary_saved_each_month + 1
    years = int (months_needed_to_save_downpayment // 12)
    months = int (months_needed_to_save_downpayment % 12)


    print ("If you save $" + str(salary_saved_each_month) + " per month, it will take " + str(years) + " year and " + str(months) + " months to save enough for the down payment")

if __name__ == "__main__":
    main()