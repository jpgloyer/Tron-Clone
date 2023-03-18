

class Map:
    def __init__(self, xSizeInPixels, ySizeInPixels):
        # self.xSize_inGridCells = int(xSize_inPixels/5)
        # self.ySize_inGridCells = int(ySize_inPixels/5)

        # self.map = [[0 for x in range(self.xSize_inGridCells)] for y in range(self.ySize_inGridCells)]
        # #Map represented as a 2D list of integers.

        self.xSizeInPixels = xSizeInPixels
        self.ySizeInPixels = ySizeInPixels
        self.map = [[(0,0,0,0) for x in range(self.xSizeInPixels)] for y in range(self.ySizeInPixels)]


    def get_pixel_value(self,row,col):
        if row >= 0 and row < len(self.map) and col >= 0 and col < len(self.map[0]):
            return self.map[row][col]
        else:
            return 0
    
    def set_pixel_value(self,row,col,value:tuple = (0,0,0,0)):
        if row >= 0 and row < len(self.map) and col >= 0 and col < len(self.map[0]):
            self.map[row][col] = value
        else:
            return 0
        pass
        
    def reset(self):
        self.map = [[(0,0,0,0) for x in range(self.xSizeInPixels)] for y in range(self.ySizeInPixels)]
        

