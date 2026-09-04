class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        INF = float('inf')

        dist = [INF] * n

        dist[src] = 0

        # k stops = k + 1 flights
        for _ in range(k + 1):

            # Make a copy of dist
            new_dist = dist[:]

            # Check every flight
            for from_city, to_city, price in flights:

                if dist[from_city] != INF:

                    new_dist[to_city] = min(
                        new_dist[to_city],
                        dist[from_city] + price
                    )

            dist = new_dist

        if dist[dst] == INF:
            return -1

        return dist[dst]