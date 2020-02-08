 NAME
 ====
 fastafromGenbank

 

 DEPENDENCIES
 ============

 python-biopython, python3-biopython

 DESCRIPTION
 ===========

 The files in this directory allow you to download multiple fasta files from Genbank. 
 You can also use the same files to download genbank records by subsitituting "rettype=fasta"
 with "rettype=gb" in the "*.py" files.




 SCRIPTS
 =======

 clipper.sh - use this script to extract the gi number from a header format
 
 acc2fa.py -  run this script using python2 on a list of gi or accession numbers or both. It will use the genbank eutils to download the set of fasta files for the given list of id's.

 acc2fa2.py - If the acc2fa.py script outputs "Error! Cannot fetch 'file-with-gi/acc-number' " for some of the ids
               then run this script using python3 and it will create a new file with the names of files still to download.

 

 INSTRUCTIONS FOR USE
 ====================

 1. Visually inspect file with list of id's using an editor (vi, vim, gedit, emacs, your favorite editor)

 2. The input file should be a list of different id formats. Don't worry about descriptions like "Acintobacteria_..". We'll deal with that shortly
    For now if there are full header lines in the list then use the "clipper.sh" script like so.

    $ bash clipper.sh inputfile
    ---------------------------


 3. This will create a new file called "clipped" with just gi numbers. You will then use this as the new input when running the python scripts like so

    $ cat clipped | python acc2fa.py > out.fasta
    --------------------------------------------

 
 4. For files that acc2fa.py cannot download an error message (Error! Cannot fetch:) will indicate what the id/description of this file is.
    To get a new list of all these names just run "acc2fa2.py" like so

    $ cat clipped | python3 acc2fa2.py > out.fasta
    ----------------------------------------------


 5. Visually inpect this new file called "test.txt". At this point the names of id's will most likely have the id numbers that genbbank requires as the first 8 or 9 digits
    in the string. In this case you can just use some simple cut commands followed by sed to replace "_" with empty space like so

    $ cat test.txt | cut -c 1-9 | sed -e 's/_/ /g' > retest.txt
    -----------------------------------------------------------

 
  6. Run the "acc2fa.py" on the new "retest.txt" file like so

     $ cat retest.txt | python acc2fa.py > out2.fasta
     ------------------------------------------------

    
  7. Now all the fasta are within files out.fasta and out2,fasta so we can conctenate them into one file like so
    
     $ cat out.fasta out2.fasta > all.fasta
     --------------------------------------

 
  8.  As a check to see if all the fasta files are there you can extract all the header and count them like so

      $ grep -e ">" allout.fasta | sort | uniq -c | wc -l
      ---------------------------------------------------
      
 
  9. Finally to split the multifasta file into separate fasta files according to each header use the following command

     $ seqretsplit allout.fasta 
     --------------------------
