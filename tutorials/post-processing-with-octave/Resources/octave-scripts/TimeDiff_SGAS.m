# Created by hhgs July 2014
#-----------------------------------------------------------------------------------
# For working in a standalone Octave session with ResInsight data, 
#  -> set "addpath" active to the riOctave-functions (and to script folder if needed)
#
# For resinsight:
#addpath("/project/res/x86_64_RH_6/share/Resinsight/jenkins_master");
#
# For resinsightdaily:
#addpath("/project/res/x86_64_RH_6/share/Resinsight/jenkins_daily_install");
#-----------------------------------------------------------------------------------


SGAS = riGetActiveCellProperty("SGAS");

SGASDIFF = SGAS;

# Calculate the change in gas saturation with time compared to timestep 1
for i=1:columns(SGAS) 
	SGASDIFF(:,i) = SGAS(:,i) - SGAS(:,1);
endfor

riSetActiveCellProperty(SGASDIFF, "SGAS_dt_DIFF");

