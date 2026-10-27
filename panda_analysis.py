import pandas as pd
import numpy as np

salary_series=pd.Series([500000,600000,70000,80000,75000,65000,55000,70000,60000,75000,80000])
print("\nSalary Series:")
print(salary_series)

print(salary_series.index)
print(salary_series.values)
print(salary_series.dtype)

employee_data={
    "id":[1,2,3,4,5,6,7,8,9,10,11],
    "name":["Darsh","Aarushi","Mark","John","Rohit","Amit","Sakshi","Riya","Ankit","Nisha","Diksha"],
    "age":[25,28,30,35,32,29,27,31,26,33,34],
    "department":["ECE","ECE","Finance","IT","HR","Finance","IT","HR","Finance","IT","HR"],
    "salary":[500000,600000,70000,80000,75000,65000,55000,70000,60000,75000,80000]
}

employee_df=pd.DataFrame(employee_data)
print("\nEmployee DataFrame:")
print(employee_df,"\n")