#include <QCoreApplication>

#include <bits/stdc++.h>
#include <unordered_map>
#include <vector>
#include <queue>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>

//2d DP table initialization
//vector<vector<int>> DP(row_size, vector<int>(column_size, 0));

//Print a vector as string seperated by space
//std::copy(distance.begin(), distance.end(), std::ostream_iterator<int>(result, " "));

using namespace std;


struct edge
{
    int u;
    int v;
    int w;
};

struct {
    bool operator () (edge one, edge two)
    {
        if(one.w < two.w)
            return true;
        else
        {
            if(one.w > two.w)
                return false;
            else
            {
                if((one.w + one.u + one.v) < (two.w + two.u + two.v))
                    return true;
                else
                    return false;
            }
        }
    }
} compare;

int union_find(int u, vector<int> & set)
{
    if(set[u] < 0)
        return u;
    else
        return set[u] = union_find(set[u], set);
}

void union_set(int u, int v, vector<int> & set)
{
    int find_u = union_find(u, set);
    int find_v = union_find(v, set);

    int newSize = set[find_u] + set[find_v];
    if(set[find_u] < set[find_v]) {
        set[find_v] = find_u;
        set[find_u] = newSize;
    } else {
        set[find_u] = find_v;
        set[find_v] = newSize;
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    int u, v, w;
    vector<edge> arr;
    for(int i = 0; i < m; i++)
    {
        edge cur;
        cin >> cur.u >> cur.v >> cur.w;
        arr.push_back(cur);
    }
    sort(arr.begin(), arr.end(), compare);

    vector<int> dset;
    for(int i = 0; i <= n; i++)
    {
        dset.push_back(-1);
    }

    int ans = 0;
    for(edge cur : arr)
    {
        if(union_find(cur.u, dset) != union_find(cur.v, dset))
        {
            ans += cur.w;
            union_set(cur.u, cur.v, dset);
        }
    }

    cout << ans;
    return 0;
}
