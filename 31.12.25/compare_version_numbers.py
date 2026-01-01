class Solution(object):
    def compareVersion(self, version1, version2):

        v1=version1.split(".")
        # print(v1)
        v2=version2.split(".")

        lv1=len(v1)
        lv2=len(v2)
        if lv1>lv2:
            for i in range(lv1-lv2):
                v2.append("0")
        elif (lv2>lv1):
            for i in range(lv2-lv1):
                v1.append("0")   
        
        for i in range(len(v1)):
            a=int(v1[i])
            b=int(v2[i])

            if a>b:
                # print(a)
                return 1
            elif b>a:
                # print(b)
                return -1
        return 0

            

