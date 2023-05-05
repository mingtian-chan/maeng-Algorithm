# 문제

# 아인트호벤의 반 아베 근현대 미술관은, 언제나 관객에게 예술가를 가장 흥미로운 방식으로 소개합니다. 가끔 직접 일을 꾸미기도 합니다.

# 오늘은 (C.1에 주어진 것처럼) 완벽한 정사각형 형태의 액자에 전기가 흐르도록 필라멘트를 넣을 수 있는지 검토하는 중입니다. 필라멘트의 목적은 - 예를 들어, 경매 도중 등 - 적절하고 유쾌한 타이밍에 이미지가 자체적으로 발광하도록 하는 것입니다. 

# 당신은 작품의 둘레 전체를 둘러쌀 필라멘트를 사야 합니다. 몇 cm가 필요하겠습니까?

# 입력

#  입력은 이하의 내용을 포함합니다.

# - 이미지의 넓이를 제곱cm 기준으로 나타낸 하나의 정수 a (1 <= a <= 10 ^ 18)가 한 줄에 주어집니다.

# 출력

# cm 기준으로, 액자에 필요한 필라멘트의 총 길이를 출력합니다. 답안은 최대 10 ^ (-6)의 절대 또는 상대 오차를 지닐 수 있습니다.

i = float(input())
# 한 변의 길이 : 넓이^(1/2),
# 네 변의 길이 : 한 변의 길이 * 4
print(i**0.5*4)