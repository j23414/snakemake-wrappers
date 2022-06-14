__author__ = "Jane Doe"
__copyright__ = "Copyright 2022, Jane Doe"
__email__ = "janedoe@email.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

filter_params = snakemake.params.get("filter_params", "")

# augur filter takes additional threads through its option -@
# One thread for samtools merge
# Other threads are *additional* threads passed to the '-@' argument
threads = "" if snakemake.threads <= 1 else " -@ {} ".format(snakemake.threads - 1)

shell(
    " augur filter "
    " --sequences {snakemake.input.sequences_fasta} "
    " --metadata {snakemake.input.metadata_tsv} "
    " --exclude {snakemake.input.exclude_txt} "
    " --output {snakemake.output.filtered_fasta} "
    " {filter_params} " 
)