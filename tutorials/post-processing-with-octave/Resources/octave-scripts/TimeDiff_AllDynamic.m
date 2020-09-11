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


# Find all dynamic properties

Prop = riGetPropertyNames();
numProp = rows(Prop);
numDynamic = 1;

# Find dynamic properties
for i=1:numProp
  if strcmp(Prop(i).PropType,"DynamicNative");	# 1 when equal "DynamicNative" properties
    P_dynamic(numDynamic) = {Prop(i).PropName};
    numDynamic++;
  endif
endfor

# Calculate difference from time step 1
for P = P_dynamic		
  P1  = riGetActiveCellProperty(P);	# Load parameter

  DIFF_P = P1;
  for i=1:columns(P1) 
    DIFF_P(:,i) = P1(:,i) - P1(:,1);
  endfor

  P_Name = ["Diff_dt_",P{1}];
  riSetActiveCellProperty(DIFF_P,P_Name);
end
