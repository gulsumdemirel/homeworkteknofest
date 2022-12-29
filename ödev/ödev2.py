import numpy as np
import cv2
def imagematrix(matrixf):
    matrixf=np.random.randint(0,256,size=(16,16))
    return matrixf

def filtering(matrixf, kernel, a=0, b=1):
    kernel = np.flipud(np.fliplr(kernel))

    x_kernel = kernel.shape[0]
    y_kernel = kernel.shape[1]
    x_matrixf = matrixf.shape[0]
    y_matrixf = matrixf.shape[1]

    x_matrixg = int(((x_matrixf - x_kernel + 2 * a) / b) + 1)
    y_matrixg = int(((y_matrixf - y_kernel + 2 * a) / b) + 1)
    output = np.zeros((x_matrixg, y_matrixg))

    if a!=0:
        matrixfa= np.zeros((matrixf.shape[0] + a*2, matrixf.shape[1] + a*2))
        matrixfa[int(a):int(-1 * a), int(a):int(-1 * a)] = matrixf
        print(matrixfa)
    else:
        matrixfa= matrixf
    
    for y in range(matrixf.shape[1]):
        if y > matrixf.shape[1] - y_kernel:
            break
        if y%b== 0:
            for x in range(matrixf.shape[0]):
                if x > matrixf.shape[0] - x_kernel:
                    break
                try:
                    if x%b== 0:
                        output[x, y] = (kernel * matrixfa[x: x + x_kernel, y: y + y_kernel]).sum()
                except:
                    break

    return output

if __name__ == '__main__':
    
    matrixf= imagematrix("matrixf.jpeg")

    satirlar=int(input("satir sayisi:"))
    sutunlar=int(input("sutun sayisi:"))
    print("lutfen eklemek istediginiz sayilari yaziniz:")
    elemanlar=list(map(int,input().split()))
    matrixV=np.array(elemanlar).reshape(satirlar,sutunlar)
    kernel=matrixV

    output = filtering(matrixf, kernel, a=2)
    cv2.imwrite("filtering.jpg", output) 

matrixf=np.random.randint(0,256,size=(16,16))

matrixf_edge1 = filtering(matrixf,kernel=matrixV)
cv2.imwrite("edge1.jpg", matrixf_edge1)

matrixf_edge2 = filtering(matrixf,kernel=matrixV)
cv2.imwrite("edge2.jpg", matrixf_edge2)















