#include <bits/stdc++.h>
#include <unordered_map>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

//Print a vector as string seperated by space
//std::copy(distance.begin(), distance.end(), std::ostream_iterator<int>(result, " "));

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<VB> VVB;
typedef list<string> LS;
typedef pair<int,int> PII;
typedef pair<int,char> PIC;
typedef vector<PII> VPII;
typedef unordered_map<string, int> UMSI;
typedef set<int> SI;
typedef unordered_set<int> USI;
typedef tuple<int,int,int> TIII;
#define _F first
#define _S second
#define _PB push_back
#define _MP make_pair
#define _SZ size()
#define _B begin()
#define _E end()
#define _RB rbegin()
#define _RE rend()
typedef stringstream SS;
typedef istringstream ISS;
typedef ostringstream OSS;

//Print a vector as string seperated by space
//std::copy(distance.begin(), distance.end(), std::ostream_iterator<int>(result, " "));


#include<iostream>
#include<thread>
#include<pthread.h>
#include <chrono>
using namespace std;

//
//Print series 010203040506. Using multi-threading 1st thread will print only 0 2nd thread will print only even numbers and 3rd thread print only odd numbers.
//


pthread_mutex_t lock1;
int turn = 0;
string ans;

void trythis(int id)
{
    static int count = 0;
    bool flag = true;
    while(flag)
    {
        pthread_mutex_lock(&lock1);

        if(turn == 0)
        {
            if(id == 1)
            {
                ans += "0";
                cout<<" thread id: " << id << " ans: " << ans << endl;

                count++;

                if(count%2)
                    turn = 1;
                else
                    turn = 2;
            }
        }
        else if (turn == 1)
        {
            if(id == 2)
            {
                ans += to_string(count);
                cout<<" thread id: " << id << " ans: " << ans << endl;
                turn = 0;
            }
        }
        else if (turn == 2)
        {
            if(id == 3)
            {
                ans += to_string(count);
                cout<<" thread id: " << id << " ans: " << ans << endl;
                turn = 0;
            }
        }
        if (count >= 6)
            flag = false;

        pthread_mutex_unlock(&lock1);

    }
    return;
}

int main(void)
{
    int i = 0;
    int rc;
    int error;
    thread t1(trythis, 1);
    thread t2(trythis, 2);
    thread t3(trythis, 3);
    t1.join();
    t2.join();
    t3.join();
    cout << ans << endl;
    return 0;
}
