import json
import random
from datetime import datetime, timedelta

def get_taipei_time():
    """將伺服器時間轉換為台北時間 (UTC+8)"""
    return datetime.utcnow() + timedelta(hours=8)

def is_update_required():
    """
    判斷今日是否需要執行更新：
    1. 週二、週五 (例行開獎日)
    2. 位於指定的加碼活動區間內
    """
    now_tp = get_taipei_time()
    today_str = now_tp.strftime("%Y-%m-%d")
    weekday = now_tp.weekday()  # 0=Mon, 1=Tue, ..., 4=Fri, 6=Sun

    # --- 💡 在此輸入台彩公告的加碼活動日期 ---
    # 格式：("開始日期", "結束日期")
    EVENT_PERIODS = [
        ("2026-04-01", "2026-04-07"), # 範例：清明連假加碼
        ("2026-06-15", "2026-06-25")  # 範例：端午端午加碼
    ]
    
    # A. 檢查例行開獎日 (週二=1, 週五=4)
    if weekday in [1, 4]:
        return True, f"例行開獎日 ({today_str})"

    # B. 檢查是否在加碼活動區間
    for start, end in EVENT_PERIODS:
        if start <= today_str <= end:
            return True, f"加碼活動期間 ({today_str})"

    return False, f"非更新日 ({today_str})"

def generate_smart_prediction():
    """
    核心運算引擎 2.7：
    模擬 268 期歷史長線 + 28 期短線能量共振
    """
    # 1-49 號碼池
    numbers = list(range(1, 50))
    
    # 模擬權重計算 (此處為核心邏輯，可依需求擴充真實爬蟲數據)
    weights = []
    for n in numbers:
        # 基礎分 1.0
        score = 1.0
        # 隨機模擬長短線共振 (實際應帶入統計數值)
        score += random.uniform(0.1, 0.5) 
        weights.append(score)

    # 根據權重取出 6 個不重複號碼
    recommendation = sorted(random.choices(numbers, weights=weights, k=15))
    final_six = sorted(list(set(recommendation))[:6])
    
    # 確保補足六碼
    while len(final_six) < 6:
        extra = random.randint(1, 49)
        if extra not in final_six:
            final_six.append(extra)
            final_six.sort()
            
    return final_six

def main():
    # 1. 智慧調度檢查
    required, reason = is_update_required()
    print(f"DEBUG: 系統檢查結果 -> {reason}")
    
    if not required:
        print("INFO: 今日不符合更新條件，腳本安全結束。")
        return

    # 2. 執行預測運算
    new_numbers = generate_smart_prediction()
    
    # 3. 模擬數據漂移與趨勢
    drift_data = [random.randint(45, 98) for _ in range(5)]
    hit_trend = [random.randint(0, 4) for _ in range(28)]
    
    # 4. 封裝 JSON 數據
    output_data = {
        "last_update": get_taipei_time().strftime("%Y-%m-%d %H:%M:%S"),
        "recommendation": new_numbers,
        "drift": drift_data,
        "hit_trend": hit_trend,
        "analysis_report": {
            "confidence": random.randint(78, 96),
            "trend": "加碼活動偵測中" if "加碼" in reason else "規律遞進",
            "update_reason": reason
        }
    }

    # 5. 寫入檔案
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)
        print(f"SUCCESS: 數據更新完成，推薦號碼：{new_numbers}")
    except Exception as e:
        print(f"ERROR: 寫入檔案失敗: {e}")

if __name__ == "__main__":
    main()
