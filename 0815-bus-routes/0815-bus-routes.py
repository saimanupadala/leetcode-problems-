from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Map each stop to the list of bus route indices passing through it
        stop_to_routes = defaultdict(list)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(route_idx)
        
        # Queue stores (bus_route_index, buses_taken_count)
        queue = deque()
        visited_routes = set()
        visited_stops = set([source])
        
        # Add all bus routes starting at 'source'
        for route_idx in stop_to_routes[source]:
            queue.append((route_idx, 1))
            visited_routes.add(route_idx)
            
        while queue:
            route_idx, buses_taken = queue.popleft()
            
            # Check all stops on the current bus route
            for stop in routes[route_idx]:
                if stop == target:
                    return buses_taken
                
                # Check for transfers to other bus routes from this stop
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_route_idx in stop_to_routes[stop]:
                        if next_route_idx not in visited_routes:
                            visited_routes.add(next_route_idx)
                            queue.append((next_route_idx, buses_taken + 1))
                            
        return -1