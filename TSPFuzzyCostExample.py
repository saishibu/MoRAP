import TSPFuzzyCost as fuzzy
#Install SKFUZZY --> pip3 install scikit-fuzzy

flame=0.3
pir=1
distance=50
temp=30

cost=fuzzy.getCost(flame,pir,distance,temp)
print("Weight for TSP:")
print(cost)
