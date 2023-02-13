#ライブラリインポート
from matplotlib import pyplot as plt

def get_debt(debt):
    monthly_interest = (1.66 / 12) / 100 #月利子を取得
    repayment_month = 360 #返済月数

    repayment_par_month = round((debt * monthly_interest * (1 + monthly_interest) ** repayment_month) / ((1 + monthly_interest) ** repayment_month - 1)) #月返済額を計算

    last_repayment = 0 #変数定義（最終月返済額）
    total_repayment = 0 #変数定義（合計返済額）

    x_list = [] #グラフのx軸データ配列（月）
    y_list = [] #グラフのy軸データ配列（借金残高）

    for month in range(repayment_month): #0~359　
        repayment = 0 #変数定義（月返済額 + 利子）
        debt *= 1 + monthly_interest #利子を上乗せ

        if month + 1 == repayment_month: #最終月は借金残高すべてを返済
            repayment = round(debt + (debt * monthly_interest))
            last_repayment = repayment
            debt = 0

        else: #最終月以外
            repayment = round(repayment_par_month + (debt * monthly_interest)) #月返済額 + 利子
            debt -= repayment_par_month #借金残高から返済額を減算

        total_repayment += repayment #合計返済額に加算

        x_list.append(month) #X軸データを追加
        y_list.append(debt) #Y軸データを追加

    #結果を表示
    print("月額返済額は " + "{:,}".format(repayment_par_month) + " 円 です。")
    print("最終月の返済額は " + "{:,}".format(last_repayment) + " 円 です。")
    print("合計支払い金額は " + "{:,}".format(total_repayment) + " 円 です。")
        
    #グラフをプロット
    plt.plot(x_list, y_list)
    plt.show()

    get_debt(int(input("借金額を入力：")))

if __name__ == '__main__':
    get_debt(6000000)



