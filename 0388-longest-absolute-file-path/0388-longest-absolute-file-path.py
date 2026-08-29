class Solution:
    def lengthLongestPath(self, input):
        path_length = [0] * (len(input) + 1)

        max_length = 0

        for line in input.split('\n'):
       
            depth = line.count('\t')

            name = line.lstrip('\t')

       
            current_length = path_length[depth] + len(name)

         
            if '.' in name:
                max_length = max(max_length, current_length)

            else:
          
                path_length[depth + 1] = current_length + 1

        return max_length