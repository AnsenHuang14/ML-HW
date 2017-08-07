import pandas as pd

def processed_train():
	df = pd.read_csv('./data/train.csv',encoding='Big5')
	df = df.drop(df.columns[1],1)
	Measurements = df.loc[0:17,df.columns[1]]
	new_colname = list()
	new_colname.append('date')
	for n in Measurements:
		for i in xrange(0,24):
			new_colname.append(n+'@'+str(i))
	
	df_new = pd.DataFrame(columns = new_colname)

	for i in xrange(len(df)):
		if df.loc[i,df.columns[1]]=='AMB_TEMP':
			temp_df = df.loc[i,df.columns]
			temp_df = temp_df.drop(df.columns[1],0)
			# print temp_df
		elif df.loc[i,df.columns[1]]=='WS_HR':
			temp_df= pd.concat([temp_df, df.loc[i,df.columns[2:]] ], axis=0)
			temp_df.index = new_colname
			df_new=df_new.append(temp_df,ignore_index = True)
		else :
			temp_df= pd.concat([temp_df, df.loc[i,df.columns[2:]] ], axis=0)
		print i
	print df_new.shape
	df_new.to_csv('./data/processed_train.csv',index=False)

def processed_test():
	df = pd.read_csv('./data/test_X.csv',encoding='Big5',header=None)
	print df.head()
	Measurements = df.loc[0:17,df.columns[1]]
	new_colname = list()
	new_colname.append('date')
	for n in Measurements:
		for i in xrange(0,9):
			new_colname.append(n+'@'+str(i))
	
	df_new = pd.DataFrame(columns = new_colname)

	for i in xrange(len(df)):
		if df.loc[i,df.columns[1]]=='AMB_TEMP':
			temp_df = df.loc[i,df.columns]
			temp_df = temp_df.drop(df.columns[1],0)
			# print temp_df
		elif df.loc[i,df.columns[1]]=='WS_HR':
			temp_df= pd.concat([temp_df, df.loc[i,df.columns[2:]] ], axis=0)
			temp_df.index = new_colname
			df_new=df_new.append(temp_df,ignore_index = True)
		else :
			temp_df= pd.concat([temp_df, df.loc[i,df.columns[2:]] ], axis=0)
		print i
	print df_new.shape
	df_new.to_csv('./data/processed_test.csv',index=False)
	

if __name__ == '__main__':
	processed_test()