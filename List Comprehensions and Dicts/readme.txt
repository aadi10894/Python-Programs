
# This is how I tested my answer:

# make a temp file containing your answers followed by my driver
cat program.py driver3.py > temp.py

# run the temp file
python3 temp.py > out.txt

# compare against sample output
diff output3.py out.txt

# Note that your answers (in a file containing ONLY your answers, NOT
# my driver) should precede my driver, so that the functions will be
# defined before they are called.

# writing a script for this is also recommended so you don't have to key in
# all of the commands every time.



