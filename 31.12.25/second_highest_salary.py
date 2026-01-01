import pandas as pd
import numpy as np
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if len(employee) < 2 or not employee['id'].is_unique:
        return pd.DataFrame({"SecondHighestSalary": [np.nan]})
    unique_salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if len(unique_salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary": [np.nan]})
    return pd.DataFrame({"SecondHighestSalary": [unique_salaries.iloc[1]]})
