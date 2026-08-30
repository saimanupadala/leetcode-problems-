class Solution:
    def reconstructQueue(self, people):

        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []

        for person in people:
            h, k = person
            queue.insert(k, person)

        return queue