import matplotlib.pyplot as plt
import math
import pandas as pd
festes = [15,17,16,19,15,16,21,18,22,26,25,23]
ferfi = [2,2,5,6,7,3,8,2,3,0,5,2]
gyerek = [0,1,2,3,2,4,3,3,2,3,2,4]

noi = [8,13,9,8,11,10,15,8,13,6,13,13]
idk = [2,1,1,1,0,1,1,0,1,0,0,1]
alkalmi = [0,1,1,0,0,1,0,0,0,0,0,0]
lista = [festes,ferfi,gyerek,noi,idk,alkalmi]
Honapok = ["Jan","Feb","Mar","Apr","Maj","Jun","Jul","Aug","Szept","Okt","Nov","Dec"]
profit = [6000,11000,71600,62000,99300,15600,97060,106700,187900,132000,187700,209100,
              202800,226100,176400,228700,138300,299000,183900,260500,283000]
profit_2025 = profit[9:21]
honapok = pd.date_range(start="2024-04-01", end="2025-12-01", freq="MS")
bevetel = [332200,343700,420100,445800,436100,386400,461700,356300,554500,444900,530500,545000]
kifizetes = [140000 for i in range(0,11)]
kifizetes.append(150000)
anyagi_bevetel = [60000,56000,71000,103000,70000,70000,93000,78000,115500,121000,130000,112000]
oraber = [2360,2979,3319,3120,3768,3095,3573,2426,3833,3014,3775,3930]
ledolgozott_orak = [56,63,63,65,60,57,64,57,78,61,69,72]
ledolgozott_orak = [56,63,63,65,60,57,64,57,78,61,69,72]
lst = [["festés",festes],["férfi",ferfi],["gyerek",gyerek],["női",noi],["idk",idk],
           ["alkalmi",alkalmi],["fizetés",profit_2025],["Órabér",oraber],
           ["Anyagi kiadások",anyagi_bevetel],["Ledolgozott órák", ledolgozott_orak]]
l=[]
maxl=[]
def cov(l,k):
  cov=[]
  for i in range(len(l)):
   
        cov.append((l[i]-sum(l)/len(l))*((k[i]-sum(k)/len(k))))
     
  return sum(cov)/len(cov)
for i in range(len(lista)):
  for k in range(len(lista)):
    if i!=k:
      r=((cov(lista[i],lista[k]))//((math.sqrt(cov(lista[i],lista[i])))*math.sqrt(cov(lista[k],lista[k]))))
      l.extend([[lista[i],lista[k]]])
      maxl.append(r)
    else:
      continue
def corr(l,k):
  r=cov(l,k)/((math.sqrt(cov(l,l)))*(math.sqrt(cov(k,k))))
  return r


#print(l[element_func(maxl,max(maxl))])
#print(l[element_func(maxl,min(maxl))])
#print(max(maxl),min(maxl))
plt.figure(figsize=(14, 5))
plt.subplot(121)
plt.plot(Honapok,ferfi, label="Férfi hajvágás", marker="o")
plt.plot(Honapok,noi,label="Női hajvágás", marker="s")
plt.title("Leginkább: Férfi és női hajvágás korrelációja")
plt.legend(fontsize=10)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.subplot(122)
plt.plot(Honapok,festes, label="Festések", marker="o")
plt.plot(Honapok,alkalmi, label="Alkalmi", marker="s")
plt.title("Legkevésbé: Alkalmi és hajfestés korrelációja")
plt.legend(fontsize=10)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.suptitle("Leginkább, és legkevésbé korrelált szolgáltatáspárok")

plt.show()

plt.figure(figsize=(15,8))
plt.plot(honapok,profit)
plt.title("A fizetés alakulása 2024 Áprilisától")
plt.show()

plt.pie([sum(anyagi_bevetel),sum(kifizetes),sum(profit_2025)],labels=["Anyagi kiadás", "Kifizetés","Fizetés"],autopct='%1.1f%%',startangle=90)
plt.title("A bevételek, és a kötelezettségek megoszlása")
plt.show()

plt.figure(figsize=(15,8))
plt.plot(Honapok,oraber)
plt.title("Az órabér alakulása 2025-ben")
plt.show()


print("Átlagfizetés:", sum(profit_2025)/len(profit_2025))
print("fizetések szórása:", math.sqrt(cov(profit_2025,profit_2025)))
def median_func(l):
  l.sort()
  if len(l)%2==1:
    med=(len(l)//2)+0.5
    return l[med]

  else:
    median=(l[(len(l)//2)-1]+l[((len(l)//2))])/2
    return(median)
print("Medián bér:", median_func(profit_2025))
print("Átlagos Órabér", sum(oraber)/len(oraber))
print("Órabér szórása:",math.sqrt(cov(oraber,oraber)))
print("Összbevétel 2025-ben:", sum(bevetel))
print("Leginkább korrelált adatok:")
def corr_valogatot(l):
  for i in range(len(l)):
    for k in range(len(l)):
      if i<k:
        r=corr(l[i][1],l[k][1])
        if r>=0.7 or r<-0.7:
          print(l[i][0],"és",l[k][0], "korrelációja:", r)
        else:
          continue
      else:
        continue
corr_valogatot(lst)



plt.figure(figsize=(12,3))
plt.plot(Honapok,profit_2025, label="Fizetés", marker="o")
plt.plot(Honapok,[festes[i]*10000 for i  in range(len(festes))],label="Festések", marker ="s")
plt.title("Festések, és a fizetés")
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
