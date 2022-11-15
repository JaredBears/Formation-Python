from typing import List
'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
Example:
Input:
image = [[1,1,1],
        [1,1,0],
        [1,0,1]]
imag2 = [[1,0,1],
        [1,1,0],
        [1,0,1]]
sr = 1, sc = 1, color = 2
Output:
image = [[2,2,2],
        [2,2,0],
        [2,0,1]]
imag2 = [[2,0,1],
        [2,2,0],
        [2,0,1]]

From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg


solution 1

start at input point
    recursively fill the 4 directional points if they are the same color as the input
    up
    down
    left
    right

image = [[1,1,1],
        [1,1,0],
        [1,0,1]]

[[1,1,1],
[1,2,0],
[1,0,1]]

[[1,2,1],
[1,2,0],
[1,0,1]]

[[2,2,1],
[1,2,0],
[1,0,1]]

[[2,2,2],
[1,2,0],
[1,0,1]]

[[2,2,2],
[2,2,0],
[1,0,1]]

[[2,2,2],
[2,2,0],
[2,0,1]]


'''

def floodFill(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor: return image
    count = 0
    def dfs(r, c, dir):
        nonlocal count
        count += 1
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1 and dir != 1: dfs(r-1, c, 0)
            if r+1 < R and dir != 0: dfs(r+1, c, 1)
            if c >= 1 and dir != 3: dfs(r, c-1, 2)
            if c+1 < C and dir != 2: dfs(r, c+1, 3)
    dfs(sr, sc, None)
    print(count)
    return image


testMatrixOne = [[1,1,1],[1,1,0],[1,0,1]]
testMatrixTwo = [[0,0,0],[0,0,0]]
testMatrixThree = [[1,1,1],[1,0,1],[1,1,1]]
testMatrixFour = [[1,1,1],[1,0,1],[1,1,1]]
testMatrixFive = [[1,0,1],[1,1,0],[1,0,1]]

resultMatrixOne = [[2,2,2], [2,2,0], [2,0,1]]
resultMatrixTwo = [[1,1,1],[1,1,1]]
resultMatrixThree = [[1,1,1],[1,2,1],[1,1,1]]
resultMatrixFour = [[2,2,2],[2,0,2],[2,2,2]]
resultMatrixFive = [[2,0,1],[2,2,0],[2,0,1]]

print(floodFill(testMatrixOne, 1, 1, 2) == resultMatrixOne)
print(floodFill(testMatrixTwo, 0, 0, 1) == resultMatrixTwo)
print(floodFill(testMatrixThree, 1, 1, 2) == resultMatrixThree)
print(floodFill(testMatrixFour, 0, 0, 2) == resultMatrixFour)
