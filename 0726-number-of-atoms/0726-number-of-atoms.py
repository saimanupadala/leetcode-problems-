class Solution:
    def countOfAtoms(self, formula):
        stack = [{}]
        i = 0
        n = len(formula)

        while i < n:
            # Opening bracket
            if formula[i] == '(':
                stack.append({})
                i += 1

            # Closing bracket
            elif formula[i] == ')':
                i += 1

                # Read multiplier
                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                group = stack.pop()

                # Multiply all atoms in the group
                for atom in group:
                    group[atom] *= num

                # Add group to previous level
                for atom, count in group.items():
                    stack[-1][atom] = stack[-1].get(atom, 0) + count

            # Element
            else:
                # Read element name
                atom = formula[i]
                i += 1

                while i < n and formula[i].islower():
                    atom += formula[i]
                    i += 1

                # Read count
                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                stack[-1][atom] = stack[-1].get(atom, 0) + num

        # Sort atoms alphabetically
        result = ""

        for atom in sorted(stack[0]):
            result += atom
            if stack[0][atom] > 1:
                result += str(stack[0][atom])

        return result