for i in range(int(input())):

    dp=[0]*100001;
    dp[0]=0;
    dp[1]=1;

    n=int(input());

    for i in range(2,n+1):
        dp[i]=max(dp[int(i/2)]+dp[int(i/3)]+dp[int(i/4)],i);

    print(dp[n]);
    