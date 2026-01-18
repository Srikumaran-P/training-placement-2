# Write your MySQL query statement below
SELECT employee_id
FROM (
  SELECT e.employee_id
  FROM employees e
    LEFT OUTER JOIN salaries s
      ON e.employee_id = s.employee_id
  WHERE s.employee_id IS NULL
  UNION
  SELECT s.employee_id
  FROM employees e
    RIGHT OUTER JOIN salaries s
      ON e.employee_id = s.employee_id
  WHERE e.employee_id IS NULL
) t
ORDER BY employee_id
