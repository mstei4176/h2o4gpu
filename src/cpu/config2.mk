$(warning Using only CPU)

USEICC=0

ifdef MKLROOT
USEMKL=1
else
USEMKL=0
endif

#local settings
USEDEBUG=0
USENVTX=0
USENCCL=0

