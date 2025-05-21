# [2020 카카오 인턴] 키패드 누르기

def solution(numbers, hand):
    keypad = {3:[1,2,3,4],6:[2,1,2,3],9:[3,2,1,2],1:[1,2,3,4],4:[2,1,2,3],7:[3,2,1,2], 0:[3,2,1,0],"*":[4,3,2,1],"#":[4,3,2,1],
              5:[1,0,1,2],2:[0,1,2,3],8:[2,1,0,1]}
    a = {2:0,5:1,8:2,0:3}
    result = ""
    left,right = "*","#"
    print(keypad[right])
    for number in numbers:
        if number in [1,4,7]:
            result += "L"
            left = number
        elif number in [3,6,9]:
            result += "R"
            right = number
        else:
            if keypad[left][a[number]] > keypad[right][a[number]]:
                result += "R"
                right = number
            elif keypad[left][a[number]] < keypad[right][a[number]]:

                result += "L"
                left = number
            else:
                if hand == "right":
                    result += "R"
                    right = number
                else:
                    result += "L"
                    left = number
    return result


print(solution(	[3,0], "left"))