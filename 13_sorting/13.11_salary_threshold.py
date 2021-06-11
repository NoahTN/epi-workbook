# O(nlogn), O(1)

def compute_salary_threshold(salaries,target_pay):
   salaries.sort()
   raw_sum = 0.0
   for i, salary in enumerate(salaries):
      adj_sum = salary * (len(salaries)-1)
      if raw_sum + adj_sum >= target_pay:
         return (target_pay - raw_sum) / adj_sum
      raw_sum += salary
   return -1.0
