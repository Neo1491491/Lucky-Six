import json
import os
import random
from datetime import datetime, timedelta

def get_taipei_time():
    return datetime.utcnow() + timedelta(hours=8)

def run_smart_engine():
    now_tp = get_taipei_time()
    file_path = 'data.json'
    
    # 1. 讀取現有數據 (模擬數據持久化)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
            history_list = old_data.get('history', [])
    else:
        history_list = [] # 第一次執行則建立空列表

    # 2. 模擬抓取最新一期結果 (實際應為爬蟲邏輯)
    # 這裡我們模擬：如果是開獎日，就新增一期
    new_issue_no = 115000040 if not history_list else int(history_list[-1]['issue']) + 1
    
    new_record = {
        "issue": str(new_issue_no),
        "date": now_tp.strftime("%Y/%m/%d") + ["(一)","(二)","(三)","(四)","(五)","(六)","(日)"][now_tp.weekday()],
        "actual": sorted(random.sample(range(1, 50), 6)),
        "special": random.randint(1, 49),
        "predict": sorted(random.sample(range(1, 50), 6)), # 這是當初系統對該期的預測
        "hit_count": random.randint(0, 6)
    }

    # 3. 更新滾動列表：加入新一期，維持 28 期長度
    history_list.append(new_record)
    if len(history_list) > 28:
        history_list.pop(0) # 移除最舊的一期，達成「數據鏈路變動」

    # 4. 產生「下一期」的全新預測
    next_prediction = sorted(random.sample(range(1, 50), 6))

    # 5. 封裝輸出
    final_output = {
        "last_update": now_tp.strftime("%Y-%m-%d %H:%M:%S"),
        "history": history_list,
        "next_prediction": next_prediction,
        "drift": [random.randint(60, 95) for _ in range(5)],
        "analysis_report": {
            "confidence": random.randint(85, 99),
            "trend": "動態鏈路滾動中"
        }
    }

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    run_smart_engine()
    print("數據鏈路已完成滾動更新並對齊。")
