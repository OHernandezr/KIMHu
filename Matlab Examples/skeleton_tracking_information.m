% Input: CSV with the skeleton tracking information
% Objective: read the information of the participant for each timestamp, 
% in each iteration the following information is obtained:
% 1. Position and orientation of 25 keypoints of the skeleton tracking.
% 2. Activities: EyeLeftClosed, EyeRightClosed, MouthOpen, MouthMoved, LookingAway
% 3. Expressions: happy, neutral
% 4. State of the hands: open, closed

%EXAMPLE: 
file= 'F:\KIMHu\EXT13 T1\EXT13_T1_skeleton_tracking.csv'; %File name
CSV = readtable(file,'delimiter',';'); 

for row = 1:height(CSV)
    jDataBody=string(CSV{row,10});
    jsonBody=jsondecode(jDataBody);
    joints=jsonBody.Joints;
    ShoulderRightPosX=joints.ShoulderRight.Position.X;
    ShoulderRightPosY=joints.ShoulderRight.Position.Y;
    ShoulderRightPosZ=joints.ShoulderRight.Position.Z;
end
