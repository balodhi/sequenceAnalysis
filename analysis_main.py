from fastqc import fastqc
from samfile import analysis
import argparse
import os


def main(indir, outdir, samfile, nthreads, batch=False):
    #_,_, out= fastqc.fastqc_runner(indir, outdir,batch=batch)
    pairEnd = True
    totalSeq = fastqc.summaryCollector(os.path.join(outdir,'QC'))
    print('received Total Sequences:',str(totalSeq))
    paironecount, pairtwocount, pairextracount = analysis.samanalysis(samfile)
    sumall = paironecount+pairtwocount+pairextracount
    totalSeq = float(totalSeq)
    if pairEnd:
       #print('asdfadsfad'+str(float(pairtwocount)/float(totalSeq)))
       print('Uniquelty mapped '+ str(round(float((pairtwocount)/(totalSeq))*100.0,3)))
       print('Broken '+ str(round(float((paironecount)/totalSeq)*100.0,3)))
       print('Multimapped '+ str(round(float(pairextracount/totalSeq)*100.0,3)))
    
    print('Samfile sequences count: ',str(sumall))
    #print('paired end borken count',str(paironecount))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="options for running fastqc")
    parser.add_argument('-o','--output_dir',dest='outdir',type=str,help='where to write fastqc output')
    parser.add_argument('-i','--fastq_dir',dest='indir',type=str,help='directory where fastq files are locate')
    parser.add_argument('-s','--samfile',dest='samfile',type=str,help="sam file location")
    parser.add_argument('-t','--threads',dest='nthreads',type=int,default=1,help="num files to process simultaneously")
    opts = parser.parse_args()
    main(opts.indir, opts.outdir, opts.samfile, opts.nthreads)
    
