import pandas as pd
import numpy as np
import boto
import boto3
import nltk
from nltk.tag import StanfordNERTagger
import time
from multiprocessing import Pool

st = StanfordNERTagger('/home/ec2-user/GKGPreprocessing/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
                       '/home/ec2-user/GKGPreprocessing/stanford-ner-2018-10-16/stanford-ner-3.9.2.jar',
                       encoding='utf-8')

def getDecision(input_list):
    for item in input_list:
        if item[1] == 'ORGANIZATION':
            return "Yes"
            break   
    return "No"

def ner_result(input_str):
    new_str = [w.capitalize() for w in input_str.split(' ')]
    classified_text = st.tag(new_str)
    return getDecision(classified_text)

def main(start_num,end_num,file_num):
	file_path = 's3://gkgpreprocessing/'
	file_name = 'df_{}.csv'.format(file_num)
	output_file = 'df_{}_{}_{}.csv'.format(file_num,start_num,end_num)
	new_df = pd.read_csv(file_path + file_name ,index_col='Unnamed: 0')

	parsed_df = new_df.loc[start_num:end_num].copy()
	cleaned_name = list(parsed_df['cleaned_name'])

	s = time.time()
	p = Pool()
	result = p.map(ner_result,cleaned_name)
	p.close()
	p.join()
	print(time.time() - s)

	parsed_df['decision'] = pd.Series(result)
	output_df = parsed_df[parsed_df.decision == 'Yes']
	output_df = output_df[['original_name','cleaned_name']]
	output_df.to_csv(output_file,header = False,index = False)

	# for i in range(len(result)):
	# 	temp_decision = result[i]
	# 	if temp_result == 'Yes':
	# 		with open (output_file,'a') as f:
	# 			f.write('{},{}\n'.format(original_name[i],cleaned_name[i]))
	# 			f.close()
	# 	else:
	# 		pass
	# for i in tqdm(range(start_num,end_num)):
	# 	original_name = new_df.iloc[i]['original_name']
	# 	cleaned_name = new_df.iloc[i]['cleaned_name']
	# 	result = ner_result(cleaned_name)
	# 	if result == 'Yes':
	# 		with open (output_file,'a') as f:
	# 			f.write('{},{}\n'.format(original_name,cleaned_name))
	# 			f.close()
	# 	else:
	# 		pass

if __name__ == '__main__':
	while True:
		file_num = int(input('enter file you want to open: '))
		start_num = int(input('enter your start number: '))
		end_num = int(input('enter your end number: '))
		result_str = 'df_{} start from {} and end at {}, right? [y/n] '.format(str(file_num),str(start_num),str(end_num))
		if input(result_str) == 'y':
			break
		else:
			pass

	main(start_num,end_num,file_num)


