'''Geeks for Geeks Problem:N meetings in one room
Difficulty: EasyAccuracy: 45.3%Submissions: 395K+Points: 2Average Time: 20m
You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 
Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
Examples :
Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)
Input: start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meetings can be held with given start and end timings.
Input: start[] = [1, 2], end[] = [100, 99]
Output: 1
Constraints:
1 ≤ n ≤ 105
0 ≤ start[i] < end[i] ≤ 106'''
#Time Complexity=O(n),Space Complexity=O(n)

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
     def maximumMeetings(self,start,end):
        # code here
        meet = [[start[i],end[i]] for i in range(len(start))]
        result=[meet[0]]
        meet.sort(key = lambda x : (x[1],x[0]))
        last_end = meet[0][1]
        count = 1
        for i in range(1,len(start)):
            if meet[i][0] > last_end:
                count +=1
                result.append(meet[i])
                last_end = meet[i][1]
    
        return count,result

start = [1, 3, 0, 5, 8, 5] 
end =  [2, 4, 6, 7, 9, 9]
print(f'Max Possible meetings:{Solution().maximumMeetings(start,end)[0]}, Meetings info:{Solution().maximumMeetings(start,end)[1]}')
                