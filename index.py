import pandas as pd
from datetime import datetime, timedelta

# Read the Excel file directly into a DataFrame
bluejay_assignment_data_list = pd.read_excel(r"C:\\Users\\dd714\\OneDrive\\Desktop\\PracticesP\\Python\\Bluejay Delivery\\Assignment_Timecard.xlsx")

# Function to parse time strings and calculate the time difference
def time_difference(start_time, end_time):
    fmt = "%m/%d/%Y %I:%M %p"
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    return (end - start).seconds // 3600  # it Convert seconds to hours

# Function to analyze the DataFrame
def analyze_employee_data(data):
    # Using 'Time' and 'Time Out' columns
    # a) Employees who have worked for 7 consecutive days
    emp_7days = data[data['Time'].notna()]

    # b) Employees with less than 10 hours between shifts but greater than 1 hour
    time_bw_shift_emp = data[(data['Time'].shift(-1) - data['Time Out']).dt.seconds // 3600 < 10]
    time_bw_shift_emp = time_bw_shift_emp[(time_bw_shift_emp['Time'].shift(-1) - time_bw_shift_emp['Time Out']).dt.seconds // 3600 > 1]

    # c) Employees who have worked for more than 14 hours in a single shift
    long_shift_emp = data[(data['Time Out'] - data['Time']).dt.seconds // 3600 > 14]

    return emp_7days, time_bw_shift_emp, long_shift_emp

# Example usage
result_a, result_b, result_c = analyze_employee_data(bluejay_assignment_data_list)

# Print results
print("a) Employees who have worked for 7 consecutive days:")
print(result_a[['Employee Name', 'Position ID']])

print("\nb) Employees with less than 10 hours between shifts but greater than 1 hour:")
print(result_b[['Employee Name', 'Position ID']])

print("\nc) Employees who have worked for more than 14 hours in a single shift:")
print(result_c[['Employee Name', 'Position ID']])
