#!/usr/bin/env python
from Clict import Clict
import os
def main():
	pass


if __name__ == '__main__':
	main()
#!/usr/bin/env bash

##     System Variables

####      Graphics Card

#WINE_D3D_CONFIG="renderer=vulkan;VideoPciVendorID=0xc0de"
W=Clict()
W.VK_ICD_FILENAMES="/usr/share/vulkan/icd.d/nvidia_icd.json"
W.WINE_D3D_CONFIG="renderer=vulkan"


####     Audio Device

# default : AUDIODEV="/dev/dsp"
#                       MIXERDEV="/dev/mixer"
#                       MIDIDEV="/dev/sequencer"


####     Wine Staging Server:
####          Wine Server Process Priority: (1(lowest)-19(highest))

W.STAGING_RT_PRIORITY_SERVER=19
W.STAGING_RT_PRIORITY_BASE=19
W.STAGING_WRITECOPY=1
W.STAGING_SHARED_MEMORY=1

####     Wine Environment

W.WINEDEBUG="-all"
W.WINEARCH="win64"
W.WINEPREFIX="${CELLAR}/${CELL}/pfx"
W.WINELOADER="${CELLAR}/${CELL}/bin/wine/bin/wine"
W.WINESERVER="${CELLAR}/${CELL}/bin/wine/bin/wineserver"
W.WINEDLLOVERRIDES="winemenubuilder.exe=d"


####     Needed for Winetricks

W.WINE="${CELLAR}/${CELL}/bin/wine/bin/wine"


####     Wine Font's FIX
####         if your linux system has many fonts installed this can significantly prolong startuptime for
####         wine programs in order to avoid this create a seperate fontconfig  and use:

W.FONTCONFIG_PATH="${CELLAR}/${CELL}/lib/fonts/"
W.FONTCONFIG_FILE="${CELLAR}/${CELL}/lib/fonts/fonts.conf"

ENV=os.environ
for var in W:
	ENV[var]=W[var]
