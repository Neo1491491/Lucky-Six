import json
import random
from datetime import datetime, timedelta

def get_taipei_time():
    return datetime.utcnow() + timedelta(hours=8)

def is_update_required():
    now_tp = get_taipei_time()
    today_str = now_tp.strftime("%Y-%m-%d")
    weekday = now_tp.weekday()
    
    # 活動期間設定 (可自行增加)
    EVENT_PERIODS = [("2026-04-01", "2026-04-07")]
    
    if weekday in [1, 4]: return True, f"例行開獎日 ({today_str})"
    for start, end in EVENT_PERIODS:
        if start <= today_str <= end: return True, f"加碼活動期間 ({today_str})"
    return False, f"非更新日 ({today_str})"

def main():
    required, reason = is_update_required()
    print(f"DEBUG: {reason}")
    
    if not required: return

    # --- 核心數據模擬 (未來可在此加入爬蟲抓取台彩官網) ---
    current_issue = "115000025"  # 假設當前剛開完的是 25 期
    last_actual_numbers = [07, 12, 24, 33, 41, 48] # 上一期真實獎號
    last_predicted_numbers = [05, 12, 23, 33, 40, 48] # 系統當時的預測
    
    # 產生下一期 (26期) 的預測
    next_prediction = sorted(random.sample(range(1, 50), 6))

    output_data = {
        "last_update": get_taipei_time().strftime("%Y-%m-%d %H:%M:%S"),
        "current_issue": current_issue,
        "last_actual": last_actual_numbers,
        "last_predicted": last_predicted_numbers,
        "recommendation": next_prediction,
        "drift": [random.randint(50, 95) for _ in range(5)],
        "hit_trend": [random.randint(0, 4) for _ in range(28)],
        "analysis_report": {
            "confidence": random.randint(80, 98),
            "trend": "穩定遞增",
            "update_reason": reason
        }
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"SUCCESS: {current_issue} 期數據已存檔。")

if __name__ == "__main__":
    main()
