# გვაქვს 1,5,10,20 და 50 თეთრიანი მონეტები. დაწერეთ ფუნქცია, რომელსაც გადაეცემა
# თანხა (თეთრებში) და აბრუნებს მონეტების მინიმალურ რაოდენობას, რომლითაც
# შეგვიძლია ეს თანხა დავახურდაოთ.

def min_coins_required(amount: int) -> int:
    coins = [1, 5, 10, 20, 50]
    coin_count = 0

    while(amount > 0):
        i = len(coins) - 1
        # ვიპოვოთ ყველაზე დიდი მონეტა რომელიც დაეტევა amount-ში
        while(i >= 0):
            # ეს მონეტა გამოვაკლოთ amount-ს და გავიმეოროთ იგივე ახალ
            # amount-ზე სანამ იგი არ გახდება 0
            if coins[i] <= amount:
                coin_count += 1
                amount -= coins[i]
                break
            i -= 1

    return coin_count

testcases = [70, 100, 3, 500, 1000, 2048, 5000, 82321, 10**6, 1273489]
for testcase in testcases:
    print(testcase, min_coins_required(testcase))

