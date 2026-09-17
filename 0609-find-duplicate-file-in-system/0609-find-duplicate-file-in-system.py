from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        files = defaultdict(list)

        for path in paths:
            parts = path.split()

            directory = parts[0]

            for file in parts[1:]:
                name, content = file.split('(')
                content = content[:-1]

                full_path = directory + "/" + name
                files[content].append(full_path)

        return [group for group in files.values() if len(group) > 1]