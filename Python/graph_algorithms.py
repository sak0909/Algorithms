class UnionFind:
    """An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.
    """

    def __init__(self, N):
        """Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        """

        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N

    def find(self, p):
        """Find the set identifier for the item p."""

        id = self._id
        while p != id[p]:
            p = id[p] = id[id[p]]   # Path compression using halving.
        return p

    def count(self):
        """Return the number of items."""

        return self._count

    def connected(self, p, q):
        """Check if the items p and q are on the same set or not."""

        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Combine sets containing p and q into a single set."""

        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def __str__(self):
        """String representation of the union find object."""
        return " ".join([str(x) for x in self._id])

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"


# Python program to find articulation points in an undirected graph

from collections import defaultdict


# This class represents an undirected graph
# using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0
        self.L = []
        self.Visited = []

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    '''A recursive function that find articulation points 
    using DFS traversal
    u --> The vertex to be visited next
    visited[] --> keeps tract of visited vertices
    disc[] --> Stores discovery times of visited vertices
    parent[] --> Stores parent vertices in DFS tree
    ap[] --> Store articulation points'''

    def APUtil(self, u, visited, ap, parent, low, disc):

        # Count of children in current node
        children = 0

        # Mark the current node as visited and print it
        visited[u] = True

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])

                # u is an articulation point in following cases
                # (1) u is root of DFS tree and has two or more chilren.
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                # (2) If u is not root and low value of one of its child is more
                # than discovery value of u.
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

                    # Update low value of u for parent function calls
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    # The function to do DFS traversal. It uses recursive APUtil()
    def AP(self):
        self.L.clear()
        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)  # To store articulation points

        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)

        for index, value in enumerate(ap):
            if value == True:
                self.L.append(index)

    def getAP(self):
        return self.L

    def solve(self, u, v, w):
        for node in self.L:
            if node != w:
                if not self.checkConnectionAvoidingNode(u, w, node):
                    if not self.checkConnectionAvoidingNode(v, w, node):
                        print("NO")
                        return
                if u == node:
                    if not self.checkConnectionAvoidingNode(v, w, node):
                        print("NO")
                        return
                if v == node:
                    if not self.checkConnectionAvoidingNode(u, w, node):
                        print("NO")
                        return
        print("YES")

    def checkConnectionAvoidingNode(self, start, end, block):
        self.Visited = [False] * len(self.graph)
        self.Visited[block] = True

        self.DFSUtil(start, end)

        return self.Visited[end]


    def DFSUtil(self, v, end):

        # Mark the current node as visited and print it
        self.Visited[v] = True

        if self.Visited[end]:
            return

        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if self.Visited[i] == False:
                self.DFSUtil(i, end)


class OfflineLCA(defaultdict):
    """Find LCAs of all pairs in a given sequence, using Union-Find."""

    def __init__(self,parent,pairs):
        """Set up to find LCAs of pairs in tree defined by parent.
        LCA of any given pair x,y can then be found by self[x][y].
        However unlike the online LCA structure we can not find LCAs
        of pairs that are not supplied to us at startup time.
        """

        # set up dictionary where answers get stored
        defaultdict.__init__(self,dict)
        for u,v in pairs:
            self[u][v] = self[v][u] = None

        # set up data structure for finding node ancestor on search path
        # self.descendants forms a collection of disjoint sets,
        #    one set for the descendants of each search path node.
        # self.ancestors maps disjoint set ids to the ancestors themselves.
        self.descendants = UnionFind()
        self.ancestors = {}

        # invert the parent relationship so we can traverse the tree
        self.children = defaultdict(list)
        for x,px in parent.items():
            self.children[px].append(x)
        root = [x for x in self.children if x not in parent]
        if len(root) != 1:
            raise ValueError("LCA input is not a tree")

        # initiate depth first traversal
        self.visited = set()
        self.traverse(root[0])

    def traverse(self,node):
        """Perform depth first traversal of tree."""
        self.ancestors[self.descendants[node]] = node
        for child in self.children[node]:
            self.traverse(child)
            self.descendants.union(child,node)
            self.ancestors[self.descendants[node]] = node
        self.visited.add(node)
        for query in self[node]:
            if query in self.visited:
                lca = self.ancestors[self.descendants[query]]
                self[node][query] = self[query][node] = lca