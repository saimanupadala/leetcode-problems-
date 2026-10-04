class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                # If ty reached sy, check if remaining distance can be covered in steps of ty
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx %= ty
            else:
                # If tx reached sx, check if remaining distance can be covered in steps of tx
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty %= tx
                
        return False