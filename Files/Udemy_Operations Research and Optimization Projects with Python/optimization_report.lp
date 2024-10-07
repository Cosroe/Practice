\ Model facility_capacity_optimization
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  10 x[0] + 9 x[1] + 11 x[2] + 10.5 x[3] + 9.5 x[4] + 500 y[0] + 600 y[1]
   + 700 y[2] + 450 y[3] + 550 y[4]
Subject To
 demand: x[0] + x[1] + x[2] + x[3] + x[4] = 500
 capacity[0]: x[0] - 100 y[0] <= 0
 capacity[1]: x[1] - 150 y[1] <= 0
 capacity[2]: x[2] - 200 y[2] <= 0
 capacity[3]: x[3] - 120 y[3] <= 0
 capacity[4]: x[4] - 180 y[4] <= 0
Bounds
Binaries
 y[0] y[1] y[2] y[3] y[4]
End
