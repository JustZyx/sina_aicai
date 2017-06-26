# 新浪爱彩必发交易数据

## data structure follows as below:
```
{ "_id" : ObjectId("5950b9b2ee478021ea0c8ab6"), "bifa_win" : 29.46, "zhu_scores" : 0, "screenings" : 1, "bifa_fail" : 46.19, "bifa_result" : 0, "real_result" : 1, "zhu_team" : "布里斯本狮吼", "date" : "20170203", "ke_scores" : 0, "bifa_balance" : 24.35, "ke_team" : "悉尼FC" }
```
* _id: MongoDB primary key
* bifa_win: 必发主胜成交量
* bifa_balance: 必发平局成交量
* bifa_fail: 必发主负成交量
* zhu_scores: 主队进球数
* ke_scores: 客队进球数
* screenings: 当日场次
* zhu_team: 主队名称
* ke_team: 客队名称
* date: 比赛日期
* bifa_result: 必发预测
* real_result: 实际赛果，2主胜，1平，0主负

## And so on
* 欧赔
* 亚盘