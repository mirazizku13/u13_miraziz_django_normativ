# dict_ = {"Ali": {"Matematika": 5, "Ingliz tili": 4}}
# ortacha ={}
# # ortacha["Ali"](["Matematika"]+["Ingliz tili"])/len(dict_)
# # print(ortacha)

# a =(dict_["Ali"]["Matematika"]+dict_["Ali"]["Ingliz tili"]/len(dict_["Ali"]))
# ortacha["Ali"] = a
# print(ortacha)

dict_ = {
    "Ali": {"Matematika": 5, "Ingliz tili": 4},
    "Vali": {"Matematika": 4, "Ingliz tili": 3},
    "Zuhra": {"Matematika": 5, "Ingliz tili": 5},
    "Olim": {"Matematika": 3, "Ingliz tili": 4}
}
ortacha = {}
for k,v in dict_.items():
#     a = (dict_[k]["Matematika"] + dict_[k]["Ingliz tili"]) / len(dict_[k])
#     ortacha[k] = a
# print(ortacha)
    ortacha[k] = sum(v.values())/len(v)
print(ortacha)







# a =((dict_["Ali"]["Matematika"] + dict_["Ali"]["Ingliz tili"])/2)
# b =((dict_["Olim"]["Matematika"] + dict_["Olim"]["Ingliz tili"])/2)
# d = ((dict_["Vali"]["Matematika"] + dict_["Vali"]["Ingliz tili"])/2)
# c = ((dict_["Zuhra"]["Matematika"] + dict_["Zuhra"]["Ingliz tili"])/2)
# ortacha["Ali"] = a
# print(a,b,d,c)















# # dict_ = {
# #     "Ali": {"Matematika": 5, "Ingliz tili": 4},
# #     "Vali": {"Matematika": 4, "Ingliz tili": 3},
# #     "Zuhra": {"Matematika": 5, "Ingliz tili": 5},
# #     "Olim": {"Matematika": 3, "Ingliz tili": 4}
# # }

# # for k,v in dict_.items():
# #     a = (v['Matematika'] + v['Ingliz tili'])/2
# #     print(f'{k}-ning ortacha bali {a}')
