from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        email_to_name = {}

        # Build graph
        for account in accounts:
            name = account[0]
            first = account[1]

            for email in account[1:]:
                graph[first].append(email)
                graph[email].append(first)
                email_to_name[email] = name

        visited = set()
        result = []

        # Find all connected emails
        for email in email_to_name:
            if email in visited:
                continue

            stack = [email]
            visited.add(email)
            emails = []

            while stack:
                current = stack.pop()
                emails.append(current)

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            emails.sort()
            result.append([email_to_name[email]] + emails)

        return result