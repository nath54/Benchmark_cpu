import threading,time,os,sys,platform
from multiprocessing.pool import ThreadPool
cac="\n"
cacc="#"
ccac="|"

from cpuinfo import get_cpu_info

#input
def inp(txt):
    vp=sys.version_info
    if vp[0]==2: return raw_input(txt)
    else: return input(txt)


#test1
def test1(tm): #Le plus d'incrementations possibles en 10sec
    t1=time.time()
    x=0
    while time.time()-t1<tm:
       x+=1
    return (time.time()-t1),x

#test2
def test2(tm): #Le plus de décrémentations possibles en 10sec
    t1=time.time()
    x=0
    while time.time()-t1<tm:
       x-=1
    return (time.time()-t1),x

#test3
def test3(nb): #Le plus de carre possibles en 2sec
    t1=time.time()
    for x in range(1,nb+1):
        x=x**2
    return x,(time.time()-t1)

#test4
def test4(tm,nbt):
    ts=[]
    ars=[]
    rts=[]
    rxs=[]
    for x in range(nbt):
        ts.append( ThreadPool(processes=1) )
    for t in ts:
        ars.append( t.apply_async(test1, (tm,) ) )
    for ar in ars:
        t,x=ar.get()
        rts.append(t)
        rxs.append(x)
    tt=max(rts)
    score=sum(rxs)
    return tt,score


#main
def main():
    vp=list(sys.version_info) #version de python
    for x in range(len(vp)): vp[x]=str(vp[x]) #version de python
    txt="Nom du processeur"+ccac+str( get_cpu_info()["brand"] )+cacc+"Architecture du cpu"+ccac+str( get_cpu_info()["arch"] )+cacc+"Nombre de coeurs"+ccac+str( get_cpu_info()["count"] )+cacc+"Frequence"+ccac+str( get_cpu_info()["hz_actual"] )+cacc+"Version de python utilisée"+ccac+".".join(vp)+cacc+"Platforme utilisée"+ccac+platform.system()         #la premiere partie du fichier contient les infos du benchmark
    print(txt)
    res=[] #la liste des résultats
    #test1
    if inp("Voulez vous faire le premier test ?\n(Le plus d'incrementations possibles en 10sec)\n(yes,y,oui)\n : ").lower() in ["y","yes","oui"]:
        t1,x1=test1(10)
        print("Test n°1 (incrémentations) : En "+str(t1)+" sec , le processeur a eu un score de "+str(x1)) 
        res.append( ["Test1",t1,x1] )
    #test2
    if inp("Voulez vous faire le second test ?\n(Le plus de décrémentations possibles en 10sec)\n(yes,y,oui)\n : ").lower() in ["y","yes","oui"]:
        t2,x2=test2(10)
        print("Test n°2 (décrémentations) : En "+str(t2)+" sec , le processeur a eu un score de "+str(-x2))
        res.append( ["Test2",t2,x2] )
    #test3
    if inp("Voulez vous faire le troisième test ?\n(Le temps de calcul des 10**8 premiers carrés sur nombre entiers)\n(yes,y,oui)\n : ").lower() in ["y","yes","oui"]:
        n3,t3=test3(10**8)
        print("Test n°3 (carrés) : Le processeur a calculé "+str(n3)+" carrés en "+str(t3)+" sec")
        res.append( ["Test3",n3,t3] )
    #test4
    if inp("Voulez vous faire le quatrième test ?\n(Le plus d'incrémentations possibles en 20sec avec 4 threads en multithreading )\n(yes,y,oui)\n : ").lower() in ["y","yes","oui"]:
        t4,x4=test4(20,4)
        print("Test n°4 (incrémentations en multithreading 4 threads) : En "+str(t4)+" sec ,le processeur a eu un score de "+str(x4))
        res.append( ["Test4",t4,x4] )
    #test5
    if inp("Voulez vous faire le cinquième test ?\n(Le plus d'incrémentations possibles en 20sec avec 8 threads en multithreading )\n(yes,y,oui)\n : ").lower() in ["y","yes","oui"]:
        t5,x5=test4(20,8)
        print("Test n°5 (incrémentations en multithreading 8 threads) : En "+str(t5)+" sec ,le processeur a eu un score de "+str(x5))
        res.append( ["Test5",t5,x5] )
    #on sauvegarde les données
    for r in res:
        txt+=str(r[0])+cacc+str(r[1])+cacc+str(r[2])+cac
    txt=txt[:-1]
    if not "results" in os.listdir("./"):
        os.mkdir("results")
    f=open("results/"+str(len(os.listdir("results"))+1)+".nath","w")
    f.write(txt)
    f.close()

main()

