import os
import shutil
import subprocess

import pytest

TEST_DATA_DIR = 'tests/data/'
TEST_FASTA_REFERENCE = TEST_DATA_DIR + 'test_ref.fa'

TEST_BAM = TEST_DATA_DIR + 'test.postprocessed.bam'
OUTPUT_VCF = TEST_DATA_DIR + 'output.vcf'

def test_haplotype_caller():
    tool_args = ['python', 'amphibolite/amphibolite.py',
            '--reference-fasta', TEST_FASTA_REFERENCE,
            '--output-vcf', OUTPUT_VCF,
            TEST_BAM]
    
    results = subprocess.check_output(tool_args).decode('utf-8')

    # just make sure we get here
    assert True

def test_call_with_variant_filter():
    tool_args = ['python', 'amphibolite/amphibolite.py',
            '--reference-fasta', TEST_FASTA_REFERENCE,
            '--output-vcf', OUTPUT_VCF,
            '--filter-variants',
            TEST_BAM]
    
    results = subprocess.check_output(tool_args).decode('utf-8')

    # just make sure we get here
    assert True
