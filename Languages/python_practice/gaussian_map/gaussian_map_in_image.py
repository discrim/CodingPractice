import numpy as np
import matplotlib.pyplot as plt

def rectangular_gaussian_map(x1, x2, y1, y2):
    # x좌표, y좌표 초기화.
    # -1부터 1까지를 (x2 - x1 + 1)개, -1부터 1까지를 (y2 - y1 + 1)개로 나눔.
    assert x1 < x2, "x1 < x2 must be true but it is not."
    assert y1 < y2, "y1 < y2 must be true but it is not."
    x, y = np.meshgrid(
        np.linspace(-2, 2, x2 - x1 + 1),
        np.linspace(-2, 2, y2 - y1 + 1))
    dist = np.sqrt(x * x + y * y)
    
    gauss = np.exp(-0.5 * dist ** 2)
    
    print(gauss)
    plt.imshow(gauss)
    plt.show()
    
    return gauss

def main():
    # 2차원 1채널 검정 가우스 맵 생성.
    gmap = np.zeros((480, 800))
    
    # 주어진 직사각형 영역의 가우스분포 구함.
    x1, x2, y1, y2 = 351, 380, 207, 234
    gauss = rectangular_gaussian_map(x1, x2, y1, y2)
    
    # 초기화한 가우스 맵에 구한 가우스 맵을 대입.
    gmap[y1:y2 + 1, x1:x2 + 1] = gauss

    plt.imshow(gmap)
    plt.show()

if __name__ == "__main__":
    main()