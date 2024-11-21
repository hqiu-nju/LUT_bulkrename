# LUT_bulkrename
A script to bulk rename rename LUT files for CaptureOne


### USAGE
"python BulkRename_CaptureOne.py -d" to duplicate the file name before the suffix for all files under the current directory and subdirectories (up to 3 levels)

"python BulkRename_CaptureOne.py -r" to restore the file names

you can adjust the suffix with -s, default is .icc and .icm 

number of layers of subdirectories can also be adjusted ("-l 0 1 2 3" or "--layers 0 1 2 3"), default is 0-3


