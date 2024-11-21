import os
import glob
import argparse

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Rename files with a specified suffix.')
    parser.add_argument('-s','--suffix', type=str,nargs='+', help='The suffix of the files to rename',default=['.icc','.icm'])
    parser.add_argument('-f','--directory',default='./', type=str, help='The directory of files')
    parser.add_argument('-l','--layers', type=int,nargs='+', default=[0,1,2],help='The number of layers under directory')
    parser.add_argument('-r','--restore', action='store_true', help='Restore the original filenames')
    parser.add_argument('-d','--duplicate', action='store_true', help='Duplicate the files')
    # Parse the arguments
    args = parser.parse_args()
    suffixes = args.suffix
    directory = args.directory
    print(f'Suffix: {suffixes}')
    print(f'Directory: {directory}')
    # Get the current working directory
    
    for i in args.layers:
        print(i)
        layers=''
        for j in range(i):
            
            layers+='*/'
            for suffix in suffixes:
                # Use glob to find all files with the specified suffix in the current directory
                print(f'Looking for files with suffix {suffix} in {directory}{layers}/*{suffix}')
                files_with_suffix = glob.glob(f'{directory}{layers}/*{suffix}')
                #print(files_with_suffix)
                if args.restore:
                    restore(files_with_suffix,suffix)
                elif args.duplicate:
                    duplicate(files_with_suffix,suffix)


def restore(files_with_suffix,suffix):
    for i in files_with_suffix:
        # Get the filename without the extension
        directory = os.path.dirname(i)
        filename = os.path.basename(i).split('.')[0]
        newname =  filename + suffix
        os.rename(i, directory+'/'+newname)
        print(f'restored {i} to {newname}')

def duplicate(files_with_suffix,suffix):
    for i in files_with_suffix:
        # Get the filename without the extension
        directory = os.path.dirname(i)
        filename = os.path.basename(i).split('.')[0]
        newname = filename + '.' + filename + suffix
        os.rename(i, directory+'/'+newname)
        print(f'duplicated name {i} to {newname}')

if __name__ == "__main__":
    main()