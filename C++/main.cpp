#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <math.h>

using namespace std;


void generatePoweSet(string& S, vector<string>& ans)
{
    /*set_size of power set of a set with set_size
     n is (2**n -1)*/
    unsigned int pow_set_size = pow(2, S.size());
    int counter, j;

    /*Run from counter 000..0 to 111..1*/
    for(counter = 0; counter < pow_set_size; counter++)
    {
        string a;
        for(j = 0; j < S.size(); j++)
        {
            /* Check if jth bit in the counter is set
             If set then add jth element from S */
            if(counter & (1<<j))
                a += S[j];
        }
        ans.push_back(a);
    }
}


struct Word
{
    string word;
    int val;
};

int main()
{
    int N;
    cin >> N; cin.ignore();
    unordered_map<string, Word> D;
    vector<string> IP;

    unordered_map<char, int> V {{'a', 1}, {'e', 1}, {'i', 1}, { 'o',1},  {'n', 1}, { 'r',1}, { 't',1}, { 'l', 1}, {'s', 1}, {'u', 1} ,
        {'d', 2}, {'g' , 2} ,
        {'b', 3}, { 'c', 3}, { 'm', 3}, {'p', 3},
        {'f', 4}, { 'h', 4}, { 'v', 4}, { 'w', 4}, {'y', 4},
        {'k', 5},
        {'j', 8}, {'x', 8},
        {'q', 10}, {'z',10}
    };

    for (int i = 0; i < N; i++) {
        string W;
        Word w;
        getline(cin, W);
        IP.push_back(W);

        w.word = W;
        sort(W.begin(), W.end());

        int val = 0;
        for(char c: W)
            val += V[c];

        w.val = val;
        D[W] = w;
    }

    string L;
    getline(cin, L);

    sort(L.begin(), L.end());

    int ans = -1;
    string ansStr;
    vector<string> PS;

    generatePoweSet(L, PS);

    for(string& t: PS)
        {
            if(D.find(t) != D.end())
            {
                if(D[t].val > ans)
                {
                    ans = D[t].val;
                    ansStr = D[t].word;
                }
                else if(D[t].val == ans)
                {
                    auto it1 = find(IP.begin(), IP.end(), D[t].word);
                    auto it2 = find(IP.begin(), IP.end(), ansStr);
                    if( distance(it1, it2) > 0)
                        ans = D[t].val, ansStr = D[t].word;
                }
            }
        }

    if(ans == -1)
        cout << "invalid word" << endl;
    else
        cout << ansStr << endl;
}
