import os
import sys
import argparse
def parseargs():
    parser = argparse.ArgumentParser(
        description="replace all instances of a word within a directory"
    )
    parser.add_argument('-p','--path',type=str, required = True, help = 'Path of directory or file/dir to be changed')
    parser.add_argument('-ra','--relativeabsolute',type=str, required = True, help = 'Indicate whether path is absolute or relative using "-ra absolute" or "-ra relative"')
    parser.add_argument('-w','--word',type=str, required = True, help = 'Indicate word which you are trying to change')
    parser.add_argument('-t','--target',type=str,required =True, help = 'Indicate what word you are trying to change the words to')
    args = parser.parse_args()
    if args.relativeabsolute == "absolute":
        return args.path,args.word,args.target
    else:
        return os.path.abspath(args.path), args.word, args.target

def main():
    
    path, word, target = parseargs()

    if(os.path.isdir(path)):

        roots = []
        dirss = []
        filess = []
        for (root,dirs,files) in os.walk(path, topdown=True): 
            roots.append(root) 
            dirss.append(dirs) 
            filess.append(files) 

        # for i in range(len(roots)):

        for i in range(len(roots)):
            for j in range(len(filess[i])):
                filepath = str(roots[i])+"/"+str(filess[i][j])
                if filepath == "./replacewords.py":
                    pass
                else:
                    try:
                        f = open(filepath,"r")
                        contents = f.read()
                        edited = contents.replace(word,target)
                        f.close()

                        f = open(filepath,"w")
                        f.write(edited)
                        f.close()
                        print("file changed: " + filepath)
                    except Exception:
                        print("file failed to read: "+filepath)
    else:
        filepath = path
        try:
            f = open(filepath,"r")
            contents = f.read()
            edited = contents.replace(word,target)
            f.close()
            f = open(filepath,"w")
            f.write(edited)
            f.close()
            print("file changed: " + filepath)
        except Exception:
            print("file failed to read: "+filepath)
main()