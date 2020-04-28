import numpy as np
import pandas as pd


def close(A,B):
    if (A["Close"] - B["Close"])>std_close*2:
        return "L"
    elif (A["Close"] - B["Close"]) <std_close:
        return "S"
    else: return "M"

def volume(A,B):
    if (A["Volume"] - B["Volume"])>std_vol*2:
        return "L"
    elif (A["Volume"] - B["Volume"]) <std_vol:
        return "S"
    else: return "M"

def data2features(data,i):
    A=data.iloc[i]
    A_1=data.iloc[i-1]
    
    features = {
    "close":close(A,A_1),
    "volume": volume(A,A_1)
    }
    return features

def process(data):
	X_train = []
	global std_close
	global std_vol
	std_close = (data["Close"]-data["Close"].shift(1)).std()
	std_vol = (data["Volume"]-data["Volume"].shift(1)).std()

	for i in range(1,data.shape[0]):
	    X_train.append(data2features(data,i))
	X_train = [X_train]

	Y_train=[list(data["Target"].shift(-1))[:-1]]

	return X_train,Y_train


