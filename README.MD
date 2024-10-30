The GADM GPKG dataset has problems in the dataset that make it difficult to use for GeoDjango. One is that what should be `NULL`, `None`, in Python, is represented by the string `NA`.  Another is that the layers are presented out of order.

What this set of scripts does is 

1. Fetch the dataset
2. Create a JSON that shows layer names and known columns
3. Correct the known columns and write it out
4. Create a JSON that shows layer names and known columns for the corrected file

At some point, I should make my utilities functions available as a library. 

There is a Makefile that shows the instructions in order and how to execute them.

1. make ensure_paths
2. make download_and_unzip_gadm
3. generate_layer_names_and_columns
4. replace_null_values_in_selected_columns
5. corrected_file_generate_layer_names_and_columns