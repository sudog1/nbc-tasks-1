import random


def updown(min_count, l, r):
    if min_count < r - l + 1:
        print(f"\n\n최고 시도 횟수: {min_count}")
    target = random.randint(l, r)
    count = 1
    while True:
        try:
            n = int(input("\n숫자를 입력해주세요: "))
        except ValueError:
            print("숫자만 입력 가능합니다.")
            continue
        if not l <= n <= r:
            print(f"{l} 부터 {r} 사이의 숫자를 입력해주세요.")
            continue
        if n < target:
            print("Up")
        elif n > target:
            print("Down")
        else:
            print(f"정답입니다! 시도한 횟수는 {count}번 입니다.")
            break
        count += 1
    return count


def play(l, r):
    min_count = r - l + 1
    while True:
        min_count = min(min_count, updown(min_count, l, r))
        print()
        res = input("한 번 더 하시겠습니까? (Y/n) ")
        if res == "n":
            break
    print("\n게임이 종료되었습니다.")


play(1, 100)
