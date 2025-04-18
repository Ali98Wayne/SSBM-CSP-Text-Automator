# SSBM CSP Text Automator

A simple Python script intended for use with David V. Kimball's "m-ex Slippi Template Pack" for Super Smash Bros. Melee (SSBM), specifically the silhouette CSP (Character Select Portrait) image files. The script accepts those images as input and can batch ouptut multiple files based on each image that will write text over them to denote the game color & expansion slot number of an added costume to the game. There is an option to format the output file name(s) in a way that [mexTool](https://github.com/akaneia/mexTool) will recognize for batch importing CSP image files. Overall it's easier to correlate the file name of an added costume to an edited CSP in-game, do note that replacing too many CSPs will prevent access to the CSS (Character Select Screen) due to RAM overload. The limit of replaced CSPs and the "MnSlChr.usd" file that handles them haven't been tested.

![image](https://github.com/user-attachments/assets/b844baa8-27ed-4594-8b31-1cc85fda91e0)

Here's an example of what the program can output, these image files correspond to any added costumes based on Mario's default (or normal) costume that can be batch imported into mexTool:

![image](https://github.com/user-attachments/assets/ee969520-bbee-4d40-820f-99ff2357dfa3)

# Dependencies:
* This was made with Python 3.13 & Pillow 11.1 in mind
* The "Silhouettes" folder from [David V. Kimball's m-ex Slippi Template Pack](https://ssbmtextures.com/other-mod-types/assets-non-character-specific/m-ex-slippi-template-pack/)

# How to use?
* Step 1: Run the "SSBM CSP Text Automator.py" script.
* Step 2: Click "Open image(s)".
* Step 3: Select the silhouette image(s) for characters with expansion costumes.
* Step 4: The UI Window will close and user input will be accepted from the CMD (Command Prompt) or Terminal.
* Step 5: Answer this prompt depending on how the output image files should be named:
  * ![image](https://github.com/user-attachments/assets/f66887f5-279d-457b-b6c4-861868f040f7)
  * Entering "Y" will use the naming convention m-ex does for CSPs, for example: "PlMrNr2" for Mario's first normal costume color expansion slot
  * Entering "N" will name the output file(s) similar to the original but with the costume color and expansion slot appended to it, for example: "csp_00_Nr2" for Mario's first normal costume color expansion slot
* Step 6: This prompt will depend on the image file loaded, "csp_00.png" for Mario was used as the first file here and the answer depends on the costume color of an added costume for a character:
  * ![image](https://github.com/user-attachments/assets/ae1eece1-983e-4e0c-a043-274286890d6a)
  * For example: if a mod file is called "PlMrNr2.dat", then the base text that should be on each output image would be "Nr" corresponding to Mario's normal costume expansion slot.
  * If "Y" was entered in Step 5, the program will automatically map the silhouette file name to the equivilent m-ex base CSP file name, for example going from "csp_00" to "PlMr.
* Step 7: The program will ask for the starting range for expansion slots based on the costume color entered in Step 6, typically this value will be "2"
* Step 8: The program will ask for the ending range for expansion slots based on the costume color entered in Step 6, this depends on what the last instance of an expansion slot would be with respect to costume color.
  * For example: if an expansion normal costume setup for Mario doesn't go beyond "PlMrNr14", where there exists similarly named added costumes from 2-13 as well, then the value that should be entered in the prompt is "14"
  * After entering a value, the program should successfully generate multiple images in the same directory as the Python script.
* Repeat steps 6-8 if there are more input image files

# Notes:
There are validation checks to make sure the user inputs are valid, such as: 
* File input(s) are restricted to .png file(s).
* Only allowing the letters "Y" or "N" (lowercase also accepted) in Step 5.
* If the user entered "Y" in Step 5 and the silhouette file isn't named how it was in the original download, the user may manually enter the base file name of a character as long as m-ex can recognize it, otherwise skip the image.
* Accepting numeric inputs for Step 7 & Step 8.
