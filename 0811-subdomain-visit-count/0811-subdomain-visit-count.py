from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_counts = defaultdict(int)

        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)

            # Split domain into individual parts
            parts = domain.split('.')

            # Generate all parent subdomains by taking suffixes
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                subdomain_counts[subdomain] += count

        # Format output list
        return [f"{count} {subdomain}" for subdomain, count in subdomain_counts.items()]