def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        skill_list = list(skill)
        alpha_check = skill_list.pop(0)
        target = ""
        for s in i:
            if s in skill:
                target += s
        
        flag = True
        for alpha in target:
            try:
                if(alpha == alpha_check):
                    alpha_check = skill_list.pop(0)
                elif(alpha in skill_list):
                    flag = False
                    break
            except IndexError:
                break

        if(flag):
            answer += 1

        
    
    return answer


if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]	

    print(solution(skill,skill_trees))