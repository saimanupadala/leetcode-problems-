class Solution:
    def getImportance(self, employees, id):
        # Store employee by ID
        emp = {}

        for employee in employees:
            emp[employee.id] = employee

        # DFS to calculate total importance
        def dfs(employee_id):
            employee = emp[employee_id]

            total = employee.importance

            for sub_id in employee.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)