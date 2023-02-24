# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:31:08 2021

@author: zhou1281
"""

import numpy as np
import scipy.stats as st
import argparse
from sklearn.metrics import f1_score
import pandas as pd

def gold_test_index(lines,var):
    gold = []
    test = []
    token = []
    for i in range(len(lines)):
        k = lines[i].split('\t')
        k = [m.strip() for m in k]

        if k[1] == var:
            whole_start = i 
            #whole_test = k[2]
            for j in range(i+1,len(lines)):
                if lines[j] != '\n':
                    aa = lines[j].split('\t')
                    aa = [n.strip() for n in aa]
                    ss = aa[1]
                    if ss =='I'+var[1:]:
                        pass
                    else:
                        whole_end = j-1
                        break
                else:
                    break
            gold.append([whole_start,whole_end])
            token.append([whole_start,whole_end])
        if k[2] == var:
            whole_start_test = i 
            #whole_test = k[2]
            for m in range(i+1,len(lines)):
                if lines[m] != '\n':
                    aa = lines[m].split('\t')
                    aa = [n.strip() for n in aa]
                    ss = aa[2]
                    if ss =='I'+var[1:]:
                        pass
                    else:
                        whole_end_test = m-1
                        break
                else:
                    break            
            test.append([whole_start_test,whole_end_test])
    return gold,test


def p_r_f_strict(gold,test):
    g_num = len(gold)
    true_num = 0
    test_num = len(test)
    for i in range(len(gold)):
        if gold[i] in test:
            true_num+= 1
    if g_num == 0:
        recall = 0
    else:
        recall = true_num/g_num
    if test_num>0:
        precision = true_num/test_num
    else:
        precision = 0
    if recall == 0 and precision == 0:
        f1= 0
    else:
        f1 = 2*precision*recall/(precision+recall)
    return precision, recall, f1
    
def p_r_f_lenient(gold,test):
    g_num = len(gold)
    true_num = 0
    test_num = len(test)
    for i in range(len(gold)):
        for t in test:
            if (gold[i][0]<= t[0] and t[0] <= gold[i][1]) or (gold[i][0]<= t[1] and t[1] <= gold[i][1]) or (t[0] <= gold[i][0] and gold[i][1]<= t[1]):
                true_num += 1
                break
    recall = true_num/g_num
    if test_num>0:
        precision = true_num/test_num
    else:
        precision = 0
    if recall == 0 and precision == 0:
        f1= 0
    else:
        f1 = 2*precision*recall/(precision+recall)
    return precision, recall, f1

def calculate_performance(file_names):
    
    df = pd.DataFrame(columns = ['vars','F1','fci_0.05','fci_0.1','gold_num','micro','microci_0.05','microci_0.1','macro','macroci_0.05','macroci_0.1'])
    dic = {i:[] for i in uniqb}
    dicnum = {i:[] for i in uniqb}
    lens = len(file_names)
    for fi in file_names:
        with open(fi,'r') as f:
            lines = f.readlines()
        for var in uniqb:
            g,t = gold_test_index(lines,var)
            dicnum[var].append(len(g))
            p,r,f = p_r_f_strict(g,t)
            dic[var].append(f)
    f1micro = [0]*lens
    f1macro = [0]*lens

    for k,v in dic.items():
        for n in range(lens):
            f1macro[n] += v[n]
            f1micro[n] += dicnum[k][n]*v[n]
    f1macro = [i/len(dic) for i in f1macro]
    nums = [0]*lens

    for k,v in dicnum.items():
        for m in range(lens):
            nums[m] += v[m]
    for k in range(lens):
        f1micro[k] = f1micro[k]/nums[k]
        
    
    varlist = []
    f1 = []
    fci005 = []
    fci01 = []
    total_num = []

    for k,v in dic.items():
        varlist.append(k)
        f1.append(np.mean(v))
        fci005.append(st.t.interval(0.95,len(v)-1,loc = np.mean(v),scale = st.sem(v)))
        fci01.append(st.t.interval(0.90,len(v)-1,loc = np.mean(v),scale = st.sem(v)))
        total_num.append(sum(dicnum[k]))
    df['vars'] = varlist
    df['F1'] = f1
    df['fci_0.05'] = fci005
    df['fci_0.1'] = fci01
    df['gold_num'] = total_num
    df['micro'] = sum(f1micro)/len(f1micro)
    df['microci_0.05'] = [st.t.interval(0.95,len(f1micro)-1,loc = np.mean(f1micro),scale = st.sem(f1micro))]*len(varlist)
    df['microci_0.1'] = [st.t.interval(0.90,len(f1micro)-1,loc = np.mean(f1micro),scale = st.sem(f1micro))]*len(varlist)
    df['macro'] = sum(f1macro)/len(f1macro)
    df['macroci_0.05'] = [st.t.interval(0.95,len(f1macro)-1,loc = np.mean(f1macro),scale = st.sem(f1macro))]*len(varlist)
    df['macroci_0.1'] = [st.t.interval(0.90,len(f1macro)-1,loc = np.mean(f1macro),scale = st.sem(f1macro))]*len(varlist)
    return df
    
def calculate_performance_lenient(file_names):
    df = pd.DataFrame(columns = ['vars','F1','fci_0.05','fci_0.1','gold_num','micro','microci_0.05','microci_0.1','macro','macroci_0.05','macroci_0.1'])
    dic = {i:[] for i in uniqb}
    dicnum = {i:[] for i in uniqb}
    lens = len(file_names)
    for fi in file_names:
        with open(fi,'r') as f:
            lines = f.readlines()
        for var in uniqb:
            g,t = gold_test_index(lines,var)
            dicnum[var].append(len(g))
            p,r,f = p_r_f_lenient(g,t)
            dic[var].append(f)
    f1micro =[0]*lens
    f1macro =[0]*lens

    for k,v in dic.items():
        for n in range(lens):
            f1macro[n] += v[n]
            f1micro[n] += dicnum[k][n]*v[n]
    f1macro = [i/len(dic) for i in f1macro]
    nums = [0]*lens

    for k,v in dicnum.items():
        for m in range(lens):
            nums[m] += v[m]
    for k in range(lens):
        f1micro[k] = f1micro[k]/nums[k]
        
    varlist = []
    f1 = []
    fci005 = []
    fci01 = []
    total_num = []
    print(f1micro,f1macro)
    for k,v in dic.items():
        varlist.append(k)
        f1.append(np.mean(v))
        fci005.append(st.t.interval(0.95,len(v)-1,loc = np.mean(v),scale = st.sem(v)))
        fci01.append(st.t.interval(0.90,len(v)-1,loc = np.mean(v),scale = st.sem(v)))
        total_num.append(sum(dicnum[k]))
    df['vars'] = varlist
    df['F1'] = f1
    df['fci_0.05'] = fci005
    df['fci_0.1'] = fci01
    df['gold_num'] = total_num
    df['micro'] = sum(f1micro)/len(f1micro)
    df['microci_0.05'] = [st.t.interval(0.95,len(f1micro)-1,loc = np.mean(f1micro),scale = st.sem(f1micro))]*len(varlist)
    df['microci_0.1'] = [st.t.interval(0.90,len(f1micro)-1,loc = np.mean(f1micro),scale = st.sem(f1micro))]*len(varlist)
    df['macro'] = sum(f1macro)/len(f1macro)
    df['macroci_0.05'] = [st.t.interval(0.95,len(f1macro)-1,loc = np.mean(f1macro),scale = st.sem(f1macro))]*len(varlist)
    df['macroci_0.1'] = [st.t.interval(0.90,len(f1macro)-1,loc = np.mean(f1macro),scale = st.sem(f1macro))]*len(varlist)
    return df

uniqb = ['B-stage-value',
 'B-grade-value',
 'B-receptor',
 'B-htype-value',
 'B-size-value',
 'B-laterality-value',
 'B-receptor-status',
 'B-site-value']

file_names = ['label_test2.txt']
df = calculate_performance_lenient(file_names)
dfs = calculate_performance(file_names)
df.to_csv('cancer_bert_mayo_lenient.csv',index = False)
dfs.to_csv('cancer_bert_mayo_strict.csv',index = False)
