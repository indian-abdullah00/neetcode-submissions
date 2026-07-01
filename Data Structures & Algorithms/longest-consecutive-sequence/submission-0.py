class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_seq = []
        skip = []

        for num in nums:
            found = False
            # print("number :", num)
            number_skip = False
            for i in range(len(hash_seq)):
                if i in skip:
                    continue

                keys = hash_seq[i]
                # print("sequnce check at: ",keys )

                if num >keys[0] and num <keys [1]:
                    # print("already included ")
                    number_skip = True
                    break

                if not found:
                    if num == keys[0]:
                        keys[0] = keys[0]-1
                        merge_at = i
                        found = True
                        # print("found merge point at :", keys)

                    if num == keys[1]:
                        keys[1] = keys[1]+1
                        merge_at = i
                        found = True
                        # print("found merge point at :", keys)

                    continue
                if found:
                    if num == keys[0]:
                        hash_seq[merge_at][1] = keys[1]
                        skip.append(i)
                        # print("new range after merge: ",hash_seq[merge_at])
                    if num == keys[1]:
                        hash_seq[merge_at][0] = keys[0]
                        skip.append(i)
                        # print("new range after merge: ",hash_seq[merge_at])
                

                    
            if found:
                # print("array after one number", hash_seq,skip)

                continue
            if not number_skip:
                hash_seq.append([num-1,num+1])

            # print("array after one number", hash_seq)

        max = 0
        for ranges in hash_seq:
            length = ranges[1]-ranges[0] - 1
            if length > max :
                max = length
        
        return max

            