import pandas as pd
import numpy as np
import json
from datetime import datetime

class LuckySixEngine:
    def __init__(self):
        self.target_nums = [2, 11, 23, 24, 38, 42]
        
    def get_prediction(self):
        # 模擬 268 期權重運算
        scores = {}
        for n in range(1, 50):
            base = np.random.uniform(60, 85)
            # 加入時間擾動因子
            time_factor = np.sin(datetime.now().hour / 24 * np.pi) * 5
            scores[n] = round(base + time_factor, 2)
        return scores

    def run(self):
        scores = self.get_prediction()
        
        # 1. 準備漂移數據 (Drift)
        drift_entry = {
            "time": datetime.now().strftime("%H:%M"),
            "values": {f"num_{n}": scores[n] for n in self.target_nums}
        }

        # 2. 模擬近 28 期命中 (Hit Trend)
        hit_trend = [np.random.randint(0, 5) for _ in range(28)]

        # 3. 整合輸出的 JSON
        output = {
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "recommendation": self.target_nums,
            "current_scores": scores,
            "drift_history": drift_entry, # 雲端版建議由前端累加或讀取舊檔
            "hit_trend": hit_trend
        }
        
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    LuckySixEngine().run()
