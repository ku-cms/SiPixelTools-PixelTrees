# remove.py
import argparse
import time
import os
import re

# Remove root files in directory according to requirements
# WARNING: removes files

def main():
    # options
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input_dir",  "-i", default="",       help="input directory containing root files to remove"     )
    parser.add_argument("--min_number", "-a", default=1e100,    help="remove all files with number larger than min_number" )
    parser.add_argument("--max_number", "-b", default=-1e100,   help="remove all files with number smaller than max_number" )
    parser.add_argument("--execute",    "-e", default = False,  action = "store_true", help="execute file removal"         )

    options    = parser.parse_args()
    input_dir  = options.input_dir
    min_number = int(options.min_number)
    max_number = int(options.max_number)
    execute    = options.execute

    if not os.path.exists(input_dir):
        print("ERROR: The input directory \"{0}\" does not exist.".format(input_dir))
        return

    t1 = time.time()
    
    n_files = 0

    file_list = os.listdir(input_dir)
    for f in file_list:
        # skip non root files:
        if not ".root" in f:
            continue
        nums = re.findall(r'\d+', f)
        if len(nums) != 1:
            print("WARNING: skipping file {0}, unique number not found: {1}".format(f, nums))
            continue
        n = int(nums[0])
        if n > min_number and n < max_number:
            n_files += 1
            path = "{0}/{1}".format(input_dir, f)
            print(f)
            #print(path)
            if execute:
                os.remove(path)
    
    t2 = time.time()
    
    run_time = t2 - t1
    
    if execute:
        print("Number of files removed: {0}".format(n_files))
        print("Run time: {0:.3f} seconds".format(run_time))
    else:
        print("Number of files that will be removed: {0}".format(n_files))
        print("Run again with -e flag to execute file removal.")

if __name__ == "__main__":
    main()

