#!/usr/bin/env python3
import re
import pathlib

MboxFile = "original.mbox"
ChunksFolder = "chunksFolder"

NewEmailPattern = r"^From (\d+)@(\S+) (\S+) (\S+) (\d+) (.*) (\d+)$"
NewEmail = re.compile(NewEmailPattern)

qnt = 0
with open(MboxFile) as infile:
    FirstEmail = True
    for line in infile:
        match = re.search(NewEmail, line)
        if match:
            qnt += 1
            if FirstEmail == True:
                FirstEmail = False
            else:
                f.close()
                print('\tOK', end='\n', flush=True)
            
            DestinationFolder = "{ChunksFolder}/{year}/{month}/{day}".format(ChunksFolder=ChunksFolder, year=match.group(7), month=match.group(4), day=match.group(5))
            DestinationFile = "{DestinationFolder}/{FileName}.eml".format(DestinationFolder=DestinationFolder, FileName=match.group(1))

            pathlib.Path(DestinationFolder).mkdir(parents=True, exist_ok=True)

            f = open(DestinationFile, 'w')
            print(DestinationFile, end='', flush=True)

        f.write(line)

    f.close()
    print('\tOK', end='\n', flush=True)

FinalMessage = "{qnt} emails extracted"
print(FinalMessage)
