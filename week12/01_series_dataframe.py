#!/usr/bin/env python3
# 12주차 1교시 - slide 6
# pandas Series / DataFrame 기본 자료구조
import pandas as pd

# Series (1차원): 인덱스 + 값
s = pd.Series([2847, 1523, 3891], index=["a", "b", "c"])
print(s["b"])  # 1523

# DataFrame (2차원): 행 × 열 (교재 패턴)
data = {
    "sensor_type": ["CDS", "CDS", "TEMP"],
    "raw_value":   [2847, 1523, 2048],
    "lux":         [695.2, 371.9, 25.3],
}
df = pd.DataFrame(data)
print(df)
#   sensor_type  raw_value    lux
# 0         CDS       2847  695.2
# 1         CDS       1523  371.9
# 2        TEMP       2048   25.3
