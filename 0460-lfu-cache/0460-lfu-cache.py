from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

  
        self.key_info = {}

        self.freq_keys = defaultdict(OrderedDict)

        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_info:
            return -1

        value, freq = self.key_info[key]

        
        del self.freq_keys[freq][key]

        if not self.freq_keys[freq]:
            del self.freq_keys[freq]

            if self.min_freq == freq:
                self.min_freq += 1

    
        freq += 1
        self.freq_keys[freq][key] = None
        self.key_info[key] = [value, freq]

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_info:
            _, freq = self.key_info[key]

        
            del self.freq_keys[freq][key]

            if not self.freq_keys[freq]:
                del self.freq_keys[freq]

                if self.min_freq == freq:
                    self.min_freq += 1

            freq += 1

            self.freq_keys[freq][key] = None
            self.key_info[key] = [value, freq]

            return

      
        if len(self.key_info) >= self.capacity:
          
            key_to_remove, _ = self.freq_keys[self.min_freq].popitem(last=False)

            del self.key_info[key_to_remove]

       
        self.key_info[key] = [value, 1]
        self.freq_keys[1][key] = None

        self.min_freq = 1