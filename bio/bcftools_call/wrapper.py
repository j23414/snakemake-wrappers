__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "(samtools mpileup {snakemake.params.mpileup} "
    "--region {snakemake.wildcards.region} {snakemake.input.bams} "
    "--fasta-ref {snakemake.input.fasta} --BCF --uncompressed | "
    "bcftools call -m {snakemake.params.call} -o {snakemake.output.bcf} -v -) 2> {snakemake.log}")
