import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    """
    The `managerId` lines up with the `id` for employees who have managers.
    This lining up is a sign that we should use MERGE!

    We want to merge the employee DataFrame with ITSELF, lining up `managerID` with
    `id`.
    """
    df = employee.merge(
        # Merge with the same DataFrame
        right=employee,
        
        # Inner join to include only the intersection of `managerId` and `id`
        # If managerId is NA, then it is not included since it does not have an intersection
        how='inner',

        # For the left DataFrame (employee's manager ID), we will use the managerId
        left_on='managerId',

        # For the right DataFrame, we will use the manager's Id (id)
        right_on='id',

        # Left is employees and right is managers
        suffixes=('_employee', '_manager')
    )
    
    higher_earning_df = df[df['salary_employee'] > df['salary_manager']]
    return higher_earning_df['name_employee'].rename('Employee').to_frame()