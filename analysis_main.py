from fastqc import fastqc
from samfile import analysis
import argparse


def main(indir, outdir, samfile, nthreads, batch=False):
    _,_, out= fastqc.fastqc_runner(indir, outdir,batch=batch)
    totalSeq = fastqc.summaryCollector(outdir)
    print('received Total Sequences:',str(totalSeq))

    paironecount, pairtwocount, pairextracount = analysis.samanalysis(samfile)
    sumall = paironecount+pairtwocount+pairextracount
    print('Samfile sequences count: ',str(sumall))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="options for running fastqc")
    parser.add_argument('-o','--output_dir',dest='outdir',type=str,help='where to write fastqc output')
    parser.add_argument('-i','--fastq_dir',dest='indir',type=str,help='directory where fastq files are locate')
    parser.add_argument('-s','--samfile',dest='samfile',type=str,help="sam file location")
    parser.add_argument('-t','--threads',dest='nthreads',type=int,default=1,help="num files to process simultaneously")
    opts = parser.parse_args()
    main(opts.indir, opts.outdir, opts.samfile, opts.nthreads)
    
