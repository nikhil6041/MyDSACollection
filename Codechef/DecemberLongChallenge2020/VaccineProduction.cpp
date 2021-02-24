/* #include<bits/stdc++.h>
using namespace std;

int main(){
    map <string,int> m ;
    m["hi"] = 10;
    cout << m["i"] << "\n";
    return 0;
} */
/* #pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2,fma")

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef tree<long long,null_type,less<long long>,rb_tree_tag,tree_order_statistics_node_update> indexed_set;
typedef tree<long long,null_type,less_equal<long long>,rb_tree_tag,tree_order_statistics_node_update> indexed_multiset;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef priority_queue<int> pqmaxi;
typedef priority_queue<ll> pqmaxl;
typedef priority_queue<int, vi, greater<int>> pqmini;
typedef priority_queue<ll, vl, greater<ll>> pqminl;
 
template <typename T,typename U> using umap=unordered_map<T,U>;
template <typename T>            using uset=unordered_set<T>;

#define F first;
#define S second;
#define fo(i, a, b) for (long long i = a; i < b; ++i)
#define fm(i, a, b) for (long long i = a; i > b; --i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)x.size()
#define test     \
    ll test;     \
    cin >> test; \
    while (test--)
#define pb(i) push_back(i)
#define eb(i) emplace_back(i)
#define mp(i, j) make_pair(i, j)
#define fast                     \
    ios::sync_with_stdio(false); \
    cin.tie(NULL);
const ll mod=1000000007;

// --------- IMP FUNCTIONS----------------------------------------------------------------------------------------------------------------

// Binary Exponentiation under mod p
ll power(ll x,ull y,ll p){ 
    ll r=1;  x%=p;
    if(!x) return 0;  
    while(y){    
        if(y&1) r=(r*x)%p;    
        y>>=1;   
        x=(x*x)%p;  
    }  
    return r;  
}

// String multiplication
string operator*(string lhs, const int rhs){
	string res="";
	for(int i=0;i<rhs;++i) res+=lhs;
	return res;
}


//-----MAIN-----------------------------------------------------------------------------------------------------------------------
int main(){
    auto time_req= clock();
    fast;
    // code goes here
    
    ll n; cin >> n;
    vl a(n); fo(i,0,n) cin >> a[i];

    ll preCalc[n][n]; // min(i,j) i,j <=n
    memset(preCalc,-1 ,sizeof(preCalc)); // -1 initialization
    ll maxlen= 1 << (ll)log2(n); // 2**(log2(n))
    // n =8 , maxlen = 8 

    // 1 , 2 , 4 , 8
    ll length=1;
    while(length<=maxlen){
        ll startindex=0,endindex=length-1; 
        while(endindex<n){
            //base case
            if(startindex==endindex) preCalc[startindex][endindex]=a[startindex];
            else preCalc[startindex][endindex]=max( preCalc[startindex][startindex+ length/2  -1],preCalc[startindex+length/2][endindex] );
            startindex++;
            endindex++;
        }
        length <<= 1; //length*=2;
    }

    cout << "Precalculation\n";
    fo(i,0,n){
        fo(j,0,n){
            cout << preCalc[i][j] << " ";
        }
        cout << "\n";
    }

    cout << "Full table\n";
    fo(i,0,n){
        fo(j,0,n){
            if(preCalc[i][j]!=-1) cout << preCalc[i][j] << " ";
            else{
                ll length = j-i+1;
                ll k = 1 << (ll)log2(length);
                cout << max(preCalc[i][i+k-1] , preCalc[j-k+1][j]) << " ";
            }
        }
        cout << "\n";
    }

    cerr << "\nSolved, time = " << (float)(clock()-time_req)/CLOCKS_PER_SEC << "s\n";
    return 0;
} */
/* #include<iostream>
using namespace std;

int main(){
    int t,n,k,i,j,count=0;
    cin>>t;
    for(i=0;i<t;i++){
        cin>>n>>k;
        for(j=1;j<=n-k;j++){
            cout<<-j<<" ";
        }
        for(j=n-k+1;j<=n;j++){
            cout<<j<<" ";
        }
        cout << "\n";
    }
    return 0;

} */
/* 
vishal kumar
12 hours ago
@TopEdge 

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        long long int n, x;
        cin >> n >> x;

        long long int a[1000000];

        for(long long int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        long long int i = 0;

        for(long long int k = x; k > 0 && i < n-1; k--)
        {
            bool flag = 0;
            long long int p = log(a[i])/log(2);
            long long int r = 1 << p;
            a[i] = a[i] ^ r;

            for(long long int j = i + 1; j < n; j++)
            {
                if((a[j] ^ r) < a[j])
                {
                    a[j] = a[j] ^ r;
                    flag = 1;
                    break;
                }
            }

            if(flag == 0)
            {
                a[n - 1] = a[n - 1] ^ r;
            }

            while(a[i] <= 0)
            {
                i++;
            }

            long long int z = k + 1;

            if(z > 0)
            {
                if((n < 3) && (z % 2 == 0) && z > 0) 
                {
                    a[n - 1] = a[n - 1] ^ 1;
                    a[n - 2] = a[n - 2] ^ 1;
                }
            }


        }

        for(int i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }

        cout << endl;
    }
}

 */
#include<iostream>
using namespace std;
#include<vector>

int main(){
    int t,n,k,i,j,sum=0;
    vector<int> a;
    cin>>t;
    for(i=0;i<t;i++){
        cin>>n>>k;
        sum=0;
        for(j=1;j<=n;j++){
            a.push_back(-j);
        }
        int b=n-k;
        for(j=0;j<n;j++){
            if(j%2==0 && b>0){
                cout<<a[j]<<" ";
                b--;
            }
            else{
                cout<<-1*a[j]<<" ";
            }
        }
        cout << "\n";
    }
    return 0;

}