def determine_pitcher_result(innings_pitched, earned_runs, total_runs, is_winning_team):
    result = ""
    if(innings_pitched < 5): 
        result = "中繼"
    elif(is_winning_team):
        result = "勝投"
    else:
        result = "敗投"

    return result

# 測試你的函式
print(determine_pitcher_result(6.0, 2, 5, True))   # 預期輸出: 勝投
print(determine_pitcher_result(7.0, 1, 3, False))  # 預期輸出: 敗投
print(determine_pitcher_result(4.2, 0, 2, True))   # 預期輸出: 中繼
print(determine_pitcher_result(3.0, 3, 1, False))  # 預期輸出: 中繼
