class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            den = (coordinates[1][0]-coordinates[0][0])
            if den == 0:
                slope=9999
            else:
                slope = (coordinates[1][1]-coordinates[0][1])/den
            
            for i in range(2, len(coordinates)):
                den = (coordinates[i][0]-coordinates[i-1][0])
                if den == 0:
                    if slope == 9999:
                        pass
                    else:
                        return False
                else:
                    if slope == (coordinates[i][1]-coordinates[i-1][1])/den:
                        pass
                    else:
                        return False
            return True
