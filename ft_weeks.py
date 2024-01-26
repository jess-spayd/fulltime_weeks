# This function takes the months worked at a job and 
# the hours per week and calculates the weeks equivalent to 
# full-time work (40 hours per week).

def ft_weeks(months: float, hrs_per_week: float) -> float:

    weeks = months * 4.3452381
    total_hrs = weeks * hrs_per_week
    ft_weeks = total_hrs / 40
    return ft_weeks

# The while loop allows the user to input data for multiple
# jobs and calculate a cumulative total.

input_more = "y"
running_total_ft_weeks = 0

while input_more == "y":
    input_months = float(input("Months: "))
    input_hrs_per_week = float(input("Hours per week: "))
    ft_weeks_calc = ft_weeks(input_months, input_hrs_per_week)
    print(ft_weeks_calc)
    running_total_ft_weeks += ft_weeks_calc
    print(running_total_ft_weeks)
    input_more = input('Type "y" for more: ')