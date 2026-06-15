# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 김도형 20603
# 프로젝트 주제: 

import random

while True:
    user = input("가위, 바위, 보 중 하나를 입력하세요 (종료: 끝): ")

    if user == "끝":
        print("게임을 종료합니다.")
        break

    computer = random.choice(["가위", "바위", "보"])

    print("컴퓨터:", computer)

    if user == computer:
        print("무승부!")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        print("승리!")
    elif user in ["가위", "바위", "보"]:
        print("패배!")
    else:
        print("잘못 입력했습니다.")

    print()