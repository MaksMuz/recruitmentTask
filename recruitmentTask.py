from datetime import datetime, timedelta
import statistics 

expenses = {
  "2023-01": {
    "01": {
      "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
      "fuel": [ 210.22 ]
    },
    "09": {
      "food": [ 11.9 ],
      "fuel": [ 190.22 ]
    }
  },
  "2023-03": {
    "07": {
      "food": [ 20, 11.9, 30.20, 11.9 ]
    },
    "04": {
      "food": [ 10.20, 11.50, 2.5 ],
      "fuel": []
    }
  },
  "2023-04": {}
};

def get_first_sunday_of_month(year, month):
  first_day = datetime(year, month, 1)
  first_sunday = first_day + timedelta(days=6 - first_day.weekday())
  return first_sunday

def collect_expenses(expenses, year_month):
  year, month = map(int, year_month.split('-')) 
  first_sunday = get_first_sunday_of_month(year, month)

  selected_expenses = []
  for day_str, day_expenses in expenses.items():
    day = int(day_str)
    if datetime(year, month, day) <= first_sunday:
      for category_of_expenses in day_expenses.values():
        selected_expenses.extend(category_of_expenses)

  return selected_expenses


def solution(expenses):
    result = None
    all_expenses = []
    for year_month, month_expenses in expenses.items():
      all_expenses.extend(collect_expenses(month_expenses, year_month))

    if not all_expenses:
        return None

    result = statistics.median(all_expenses)
    return result

print(solution(expenses))
