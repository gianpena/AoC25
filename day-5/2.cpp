#include <bits/stdc++.h>
using namespace std;
using ll = long long;
set<pair<ll,ll>> intervals;

pair<ll,ll> unite(ll x1, ll y1, ll x2, ll y2) {
    bool not_intersecting = y1 < x2 || y2 < x1;
    if(not_intersecting) return {-1,-1};

    if(x1 <= x2 && x2 <= y1 && y1 <= y2)
        return {x1,y2};
    if(x2 <= x1 && x1 <= y2 && y2 <= y1)
        return {x2,y1};
    if(x1 <= x2 && x2 <= y2 && y2 <= y1)
        return {x1,y1};
    if(x2 <= x1 && x1 <= y1 && y1 <= y2)
        return {x2,y2};

    return {-1,-1};
}
void addInterval(ll a, ll b) {
    auto it = intervals.begin();
    pair<ll,ll> current_interval = {a,b};
    while(it != intervals.end()) {
        auto [x1,y1] = *it;
        auto [x2,y2] = current_interval;
        auto [xu,yu] = unite(x1,y1,x2,y2);
        if(xu == -1 && yu == -1) {
            it++;
            continue;
        }

        current_interval = {xu,yu};
        auto next = it;
        ++next;

        intervals.erase(it);
        it = next;
    }
    intervals.insert(current_interval);

}


int main() {
    string line;
    while (getline(cin, line)) {
        if (line.empty()) break;

        stringstream ss(line);
        ll a, b;
        char dash;

        ss >> a >> dash >> b;

        addInterval(a, b);
    }


    ll ans = 0;
    for(auto it = intervals.begin(); it != intervals.end(); ++it) {
        ans += (it->second - it->first + 1);
    }

    cout<<ans<<'\n';
    return 0;
}