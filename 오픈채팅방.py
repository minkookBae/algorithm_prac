def solution(record):
    answer = []
    intent_dict = dict()
    
    for sentence in record:
        msg = sentence.split()

        if(msg[0] == "Enter"):
            if(msg[1] not in intent_dict):
                intent_dict[msg[1]] = msg[2]
            else:
                intent_dict[msg[1]] = msg[2]

        elif(msg[0] == "Change"):
            if(msg[1] in intent_dict):
                intent_dict[msg[1]] = msg[2]
    
    for sentence in record:
        msg = sentence.split()

        if(msg[0] == "Enter"):
            answer.append(intent_dict[msg[1]]+"님이 들어왔습니다.")
        elif(msg[0] == "Leave"):
            answer.append(intent_dict[msg[1]]+"님이 나갔습니다.")

    print(answer)
    return answer


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	

    solution(record)