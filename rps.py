import random


def play():
    rps_map = {"rock": 0, "paper": 1, "scissors": 2}
    arr = ["바위", "보", "가위"]
    win = 0
    lose = 0
    draw = 0
    while True:
        try:
            a = rps_map[input("\n가위 바위 보! (Rock, Paper, Scissors): ").lower()]
        except KeyError:
            print("(Rock, Paper, Scissors) 중 하나를 입력해주세요.")
            continue
        b = random.randint(0, 2)
        res = (3 + b - a) % 3
        print(f"당신 - {arr[a]} | 컴퓨터 - {arr[b]}")
        if res == 1:
            lose += 1
            print("패배했습니다!")
        elif res == 2:
            win += 1
            print(f"승리했습니다!")
        else:
            draw += 1
            print("비겼습니다!")
        if input("\n재도전 하시겠습니까? (Y/n) ") == "n":
            break
    print(f"\n승리: {win} | 패배: {lose} | 무승부: {draw}")


play()
