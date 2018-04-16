import numpy as np

#计算两个向量的欧几里距离
def distEclud(rangA,rangB):
    a_b = np.sum(rangA * rangB)
    ab = np.sqrt(np.sum(rangA ** 2)) * np.sqrt(np.sum(rangA ** 2))
    try:
        result=a_b/ab
    except:
        return 1
    return result

#聚类中心
def rand_cent(data,k):
    cent_points = np.random.choice(100, k)
    cents = data[cent_points, :]
    return np.array(cents)

#k-means
def k_means(data,cents,k):
    for i in range(data.shape[0]):
        distance=[]
        for j in range(cents.shape[0]):
            distance.append(distEclud(data[i,:-1],cents[j,:-1]))
        idex=list.index(distance,max(distance))
        data[i,-1]=idex
    new_cents=[]
    for i in range(k):
        mean_k=np.mean(data[data[:,-1]==i],axis=0)
        new_cents.append(mean_k)
    return data,np.array(new_cents)

if __name__ == '__main__':
    data = np.genfromtxt("weight_range.txt")
    data.shape=100,-1
    label=np.zeros((100,1))
    data=np.hstack((data,label))
    k=3
    cents=rand_cent(data,k)#聚类中心的数组
    while(1):
        new_data,new_cents=k_means(data,cents,k)
        if np.sum((new_cents-cents)[:,:-1])==0:
            break
        cents=new_cents
    for i in range(k):
        print(new_data[new_data[:,-1]==i].shape[0])
