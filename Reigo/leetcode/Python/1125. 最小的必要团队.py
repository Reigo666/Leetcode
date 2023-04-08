class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_index={}
        #将技能转换为数字编号
        for i in range(len(req_skills)):
            skill_index[req_skills[i]]=i
        
        n=len(req_skills)
        max_skill=2**n
        dp=[inf]*(max_skill)
        pre_person=[None]*(max_skill)
        prev_skill=[None]*(max_skill)
        dp[0]=0
        
        people_skill=[]
            

        for i in range(len(people)):
            skill=0
            for j in range(len(people[i])):
                skill|=2**skill_index[people[i][j]]
            people_skill.append(skill)
            for pre_skill in range(max_skill):
                if dp[pre_skill]!=inf:
                    new_skill = pre_skill | skill
                    if dp[pre_skill]+1<dp[new_skill]:
                        dp[new_skill]=dp[pre_skill]+1
                        pre_person[new_skill]=i
                        prev_skill[new_skill]=pre_skill
            #print(dp)
        anslist=[]
        cur_skill=max_skill-1
        for i in range(dp[max_skill-1]):
            anslist.append(pre_person[cur_skill])
            cur_skill=prev_skill[cur_skill]
        return anslist

                
            
        