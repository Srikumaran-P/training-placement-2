import pandas as pd
import numpy as np
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if len(employee) < 1 or 'id' not in employee.columns or 'salary' not in employee.columns or N < 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [np.nan]})
    d = employee["salary"].drop_duplicates().sort_values(ascending=False)
    e = pd.DataFrame(d)
    if len(e["salary"]) < N:
        return pd.DataFrame({f"getNthHighestSalary({N})": [np.nan]})
    return pd.DataFrame({f"getNthHighestSalary({N})": e.iloc[N - 1]})
