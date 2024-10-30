The GADM GPKG dataset has problems in the dataset that make it difficult to use for GeoDjango. One is that what should be `NULL`, `None`, in Python, is represented by the string `NA`.  Another is that the layers are presented out of order.

What this script does is 

1. Fetch the dataset
2. Create a JSON that shows layer names and known columns
3. Correct the known columns and write it out
4. Create a JSON that shows layer names and known columns for the corrected file
5. Compares the JSON represenations of both.

At some point, I should make my utilities functions available as a library. 

There is a Makefile that shows the instructions in order and how to execute them.
