# 改成1维数组。
import numpy as np

def NLmeansfilter(input, t, f, h):
    # input: arrary to be filtered
    # t: radio of search window
    # f: radio of similarity window
    # h: degree of filtering
    n = input.shape[0]
    m = input.shape[1]
    output = np.zeros([n, m])
    input2 = np.pad(input, ((0, 0),(f, f)), 'symmetric')

    kernel = make_kernel(n, f)  # 改成一维
    kernel = kernel / np.sum(kernel, axis=1).reshape([-1,1])
    h = h * h
    for i in range(0, m):
        i1 = i + f
        W1 = input2[:, i1 - f:i1 + f + 1]

        wmax = np.zeros([n])
        average = np.zeros([n])
        sweight = np.zeros([n])

        rmin = max(i1 - t, f + 1)
        rmax = min(i1 + t, m + f)

        for r in range(rmin - 1, rmax):
            if r - 1 == i1:
                continue
            W2 = input2[:, r - f:r + f + 1]
            d = np.sum(kernel * (W1 - W2) * (W1 - W2), axis=1)
            w = np.exp(-1 * d / h)
            #解决方案1：c = a-b，判断c是否大于0
            #解决方案2：比较后能否直接取大值？可以使用np.maximum
            wmax = np.maximum(w,wmax)
            sweight = sweight + w
            average = average + w * input2[:,r]
        average = average + wmax * input2[:,i1]
        sweight = sweight + wmax
        output[:,i] = np.float32(sweight>0)*(average/sweight)+np.float32(sweight<=0)*(input[:,i])
    return output


def make_kernel(n, f):
    kernel = np.zeros([n, 2 * f + 1])
    for d in range(1, f + 1):
        value = 1 / (2 * d + 1) ** 2
        for i in range(-d, d + 1):
            for j in range(-d, d + 1):
                kernel[:, f - i] = kernel[:, f - i] + value
    return kernel / f