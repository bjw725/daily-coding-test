class Solution(object):
    def sortPeople(self, names, heights):
        dict = {}
        val = []
        for i in range(len(names)):
            dict[heights[i]] = names[i]
        for i in sorted(dict):
            val.append(dict.get(i))
        return val[::-1]
        