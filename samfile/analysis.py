from __future__ import division
from tqdm import tqdm
def samanalysis(pathToSam):

    pairEnd = True

    mate_pairs = {}
    with open(pathToSam, 'r') as samFile:
        for line in tqdm(samFile):
            id = line.split('\t')[0]
            if id[0] == '@':
            	continue
            
            try:
            	if mate_pairs[id]:
            		mate_pairs[id] = mate_pairs[id] + 1
            except Exception as e:
            	mate_pairs[id] = 1
            
    paironecount = 0
    pairtwocount = 0
    pairextracount = 0
    for key in tqdm(mate_pairs.keys()):
        if pairEnd:
        	if mate_pairs[key] == 1:
        		paironecount +=1
        	elif mate_pairs[key] == 2:
        		pairtwocount += 1
        	elif mate_pairs[key] > 2:
        		pairextracount += 1
        else:
            if mate_pairs[key] == 1:
                paironecount +=1
            elif mate_pairs[key] > 1:
                pairextracount += 1
    return paironecount, pairtwocount, pairextracount

if __name__ == "__main__":

    paironecount, pairtwocount, pairextracount = samanalysis(samFile)

    sumall = paironecount+pairtwocount+pairextracount

    print('#'*50)
    print('Total reads: ',str(sumall),'\n')
    if pairEnd:
        print("PairEnd",'\n')
        print('Uniquely mapped reads: ',str(pairtwocount), ' ', str(round(float(pairtwocount/sumall)*100.0,3)),'%%','\n')
        print('unmapped/broken reads: ', str(paironecount),' ' , str(round(float(paironecount/sumall)*100.0,3)),'%%','\n')
    else:
        print("SingleEnd",'\n')
        print('Uniquely mapped reads: ',str(paironecount), ' ', str(round(float(paironecount/sumall)*100.0,3)),'%%','\n')

    print('Multiple mapped reads: ',str(pairextracount), ' ' , str(round(float(pairextracount/sumall)*100.0,3)),'%%','\n')
    print('#'*50)
