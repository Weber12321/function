#!/usr/bin/env python
# coding: utf-8

# In[124]:


# detect [12,31] and [abc,bcd]
# 假設 12,31 為器官  abc,bcd為症狀
test = ['8412bcd','8731bcd','bcd1267','1264abc','9876abc31','31abc1451','65412abc','bbcd1287','einabc1','powabcz4831']
print(*test, sep = "\n")


# In[125]:


# 分類詞 1
li = ['12','31']
# 分類詞 2
li_2 = ['abc','bcd']

# 寫自訂分類函數，先將資料按照分類詞 1 分為 N 組，再從 N 組裏頭按照分類詞 2 分類，最後計算每一類的個數
def classifier_text(text, list1, list2):
    
    # 暫存list 與 空dictionary value
    out_list = []
    out_list_2 = []
    value = [] 
    
    # 先處理分類詞 1
    for w in range(len(list1)):
        match = [s for s in text if list1[w] in s] # 回傳有符合分類詞 1之字串之文章list
        out_list.append(match) # 貼到暫存list

    for w in range(len(out_list)):
        value.append(len(out_list[w])) # 將分類詞 1結果個數，貼到空dictionary value

    # 已經處理好分類詞 1，再處理分類詞 2
    for z in range(len(out_list)):
        for w in range(len(list2)):
            match = [s for s in out_list[z] if list2[w] in s]# 回傳有符合分類詞 2之字串之文章list
            out_list_2.append(match) # 貼到暫存list

    for z in range(len(out_list_2)):
        value.append(len(out_list_2[z])) # 將分類詞 2結果個數，貼到dictionary value

    # 創造分類詞 key值的list 
    key = list1
    for i in range(len(list1)):
        for j in range(len(list2)):
            key.append(list1[i]+' & '+list2[j])

    # 建立 dictionary
    d = dict(zip(key, value))

    return d


# In[126]:


dicts = classifier_text(test,li,li_2)
print("結果為(有包含分類詞文章 : 數量) :",dicts)

