#coding:UTF-8
import os
import argparse
import subprocess
from main import html_report,pdf_report
'''
this is main 
'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = '---create mRNA analysis report---')
    parser.add_argument('mRNA_report_path',help='a dir where include your analysis results')
    parser.add_argument('--pdf',action='store_true',help='print out pdf report')
    parser.add_argument('--html',action='store_true',help='print out html report')
    args = parser.parse_args()

    if args.html:
        subprocess.call('cp -r {html_files} {report_path}'.format(html_files = 'html_files/*',
                                                                  report_path = os.path.join(args.mRNA_report_path,'analysis_report')),shell=True)
        html_report.enrichment_analysis(args.mRNA_report_path)
        html_report.fastqc_analysis(args.mRNA_report_path)
        html_report.mapping_analysis(args.mRNA_report_path)
        html_report.quantification_analysis(args.mRNA_report_path)
        html_report.rseqc_analysis(args.mRNA_report_path)
    if args.pdf:
        pdf_report.create_pdf_report(args.mRNA_report_path)
