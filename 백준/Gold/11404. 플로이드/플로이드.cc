#include <iostream>
using namespace std;

#define INF 1000000000

int N, M;
int cost[101][101];

void input();
void floyd();
void output();

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    input();
    floyd();
    output();

    return 0;
}

void input()
{
    cin >> N;
    cin >> M;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cost[i][j] = INF;
        }
    }

    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        cost[a][b] = c < cost[a][b] ? c : cost[a][b];
    }
}

void floyd()
{
    for (int k = 1; k <= N; k++)
    {
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                if (i == j)
                    continue;
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]);
            }
        }
    }
}

void output()
{
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cout << ((cost[i][j] == INF) ? 0 : cost[i][j]) << ' ';
        }
        cout << '\n';
    }
}