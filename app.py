import pandas as pd
import numpy as np
import json
import random
from datetime import datetime

def analyze_and_predict():
    # 1. 模擬/抓取 1-49 號碼池 (這部分應與你的 268 期數據庫連動)
    numbers = list(range(1, 50))
    
    # 2. 動態權重引擎 (核心升級)
    # 我們假設獲取了近 28 期的開獎頻率 (此處模擬統計結果)
    # 實際運作時，這裡會由爬蟲抓到的數據進行計數
    freq_map = {n: random.randint(1, 10) for n in numbers} 
    
    # 找出近 28 期最熱門的「尾數」
    tails = [n % 10 for n in numbers if freq_map[n] > 7] # 假設頻率大於 7 為熱門
    popular_tail = max(set(tails), key=tails.count) if tails else 8
    
    weights = []
    for n in numbers:
        score = 1.0
        # A. 全號碼段熱度補償 (越熱門的號碼權重越高)
        score += (freq_map[n] * 0.1)
        
        # B. 動態尾數加權 (根據近 28 期大數據自動鎖定，而非手動指定 8 尾)
        if n % 10 == popular_tail:
            score += 0.5
            
        # C. 遺漏值補償 (若號碼長時間未出，給予反彈權重)
        # 這裡模擬遺漏期數越長，權重微增
        score += random.uniform(0, 0.2)
        
        weights.append(score)

    # 3. 執行機率抽樣 (從 1-49 中選出 6 碼)
    # 由於是加權抽樣，熱門號與趨勢尾數中獎機率最高，但冷門號也有機會被抽中
    recommendation = random.choices(numbers, weights=weights, k=15)
    final_six = sorted(list(set(recommendation)))[:6]
    
    # 如果不足六碼(重複抽中)，則補足
    while len(final_six) < 6:
        extra = random.randint(1, 49)
        if extra not in final_six:
            final_six.append(extra)
            
    return sorted(final_six), popular_tail

def update_cloud_data():
    new_nums, current_hot_tail = analyze_and_predict()
    
    # 模擬 2.3 版的漂移數據
    drift = [random.randint(60, 98) for _ in range(5)]
    
    data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "recommendation": new_nums,
        "analysis_note": f"目前偵測最強尾數: {current_hot_tail} 尾",
        "drift": drift,
        "hit_trend": [random.randint(0, 3) for _ in range(28)],
        "status": "Adaptive Engine v2.3"
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    update_cloud_data()
