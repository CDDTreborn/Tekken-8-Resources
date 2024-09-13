README - T8 Modding Assistant v3

Please feel free to DM on Discord or Twitter with any questions or concerns
not addressed in this document.

Addon Installation

0. Download T8 Modding Assistant v3 Package and unzip.
1. Inside the zip will be this document, an image of how to install in 
Blender and "Addon_T8Modding_Assistant_v3.zip".
2. Open Blender
3. Go to Edit > Preferences > Addons > Install
4. Navigate to where you downloaded "Addon_T8Modding_Assistant_v3.zip".
5. Select it and hit OK
6. Search for "T8" if you don't see it in the list of addons.
7. Once located make sure the box next to it is checked.
8. This will be located on your N-Panel as "T8 Mod Assist v3"

Function Instructions and Information
(Instructions also available on the addon if you click the "?")

Quick Weight Transfer

1. Select two mesh
2. Default settings are Nearest Face Interpolated and Replace.
After hitting button a black box will appear at bottom of 
screen to allow changing settings.
NOTE: Weights transfer to last mesh selected

Switch Blend Mode

1. Select all meshes you want affected
2. Hit button and choose blend from dropdown
NOTE: All mats on selected objects will be changed

Export FBX

Setup and Information:
1. Create a collection called 'RIGS'. Place in it all armatures
that you want the mesh exported on
2. This works on all mesh in all collection(s) that end with 
the suffix '_exp'.
Changing the suffix will remove it from export list
3. The blend file must be saved in order for this to work
4. Mesh must be visible to be exported. Rigs do not.

Instructions:
1. Hit the Button
2. All mesh in a collection are parented as a group to each 
Armature and exported.
3. Exports are saved in a generated folder called 'UE_Ready'
NOTE: Exports with same name will override previously exported mesh

Consolidate UVs

1. Select all mesh you want to share the same UV
2. Hit button and give new UV a name
NOTE: Mesh do not need joined. 
UVs to be consolidated don't need to have the same name.
The Active Render UV (white camera) will be the one
used in the consolidation.

Match Rigs
        
1. Select two Armatures
2. If you want a mesh to be resized then make sure it is
weighted and parented to the 1st armature selected
3. Make sure both armatures are centered in the world
or have the same origin point.
4. Hit button
5. This sets a new pose which can be saved or cleared.
NOTE: Process could take a few seconds depending on
the amount of bones in the armatures.
This relies on match bone names in the two rigs so if using
rigs with different bone names you will need to manually
rename the ones you want to match