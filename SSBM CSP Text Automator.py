from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, Button, filedialog

filePaths = None # Initialize the variable for storing image locations to prevent an error when simply trying to close the program

def openFile(): # Function that handles what to do when pressing the "Open image(s)" button
    global filePaths # Set the tuple containing path(s) to images to a global variable so it may be accessed outside of this function
    filePaths = filedialog.askopenfilenames(title = "Open image(s)", # Only accept PNG images, based on the M-EX Slippi Template Silhouette files
                                           filetypes = [("Image files", "*.png")])
    if (filePaths):
        mainWindow.destroy() # Close the window after selecting image(s) so the user can input into CMD

mainWindow = Tk() # Initialize the window variable
mainWindow.geometry("400x50") # Set the window size to a specific size
mainWindow.title("SSBM CSP Text Automator") # Give the window a title
openImagesButton = Button(text="Open image(s)", command=openFile) # Allow multiple files to be opened after clicking the button in the window
openImagesButton.pack()
mainWindow.mainloop()

if filePaths: # Proceed only if the user selected image(s)
    # Initialize a 2D array for if the user wants to batch import the output image(s) into M-EX, assuming they are using the M-EX Slippi Template Silhouette CSPs 
    cspNamesArr = (("csp_00", "csp_07", "csp_13", "csp_21", "csp_28", "csp_36", "csp_42", "csp_49", "csp_55", "csp_62", "csp_68", "csp_74", "csp_81", "csp_89", "csp_96", "csp_102", "csp_108", "csp_115", "csp_122", "csp_129", "csp_136", "csp_142", "csp_148", "csp_154", "csp_161"),
        ("PlMr", "PlFx", "PlCa", "PlDk", "PlKb", "PlKp", "PlLk", "PlNs", "PlPe", "PlPp", "PlPk", "PlSs", "PlYs", "PlPr", "PlMt", "PlLg", "PlMs", "PlZd", "PlCl", "PlDr", "PlFc", "PlPc", "PlGw", "PlGn", "PlFe"))

    while True:
        isForBatchImport = input("Should the output image(s) be formatted for batch importing in M-EX? Enter Y or N: ").upper() # Only accept the letters "Y" or "N" for Yes and No, lowercase letters get converted to uppcase
        if isForBatchImport in ("Y", "N"):
            break
        else:
            print("\nInvalid input. Enter Y or N: ") # Ask the user again for "Y" or "N" if they did not enter either of those letters

    for x in range(0, len(filePaths)):
        cspImage = Image.open(filePaths[x]) # Initialize the image variable that will be batch edited
        cspImageDraw = ImageDraw.Draw(cspImage) # Initialize the variable for drawing on the image for editing
        cspImageFont = ImageFont.truetype("impact", 12) # Initialize the variable for the font & size of the image text

        try:
            baseText = input("\nInput the text to show on each image, without the number suffix, where the base file is " + filePaths[x].rpartition('/')[-1] + ": ")
            
            if isForBatchImport == "Y":
                baseFileName = filePaths[x].rpartition('/')[-1].rsplit('.png')[0] # Set a variable to only having the "csp_###" part of the original file name where "##" are numbers
                if baseFileName in cspNamesArr[0]: # Check if the original file name matches up with what's in the first row of the cspNamesArr array
                    cspColumnIndex = cspNamesArr[0].index(baseFileName) # Get the column index of the M-EX Slippi Silhouette file name from the cspNamesArr array
                    mEXBatchName = cspNamesArr[1][cspColumnIndex] # Set the base file names of the output image(s) to the M-EX Batch Import format from the corresponding column
                else: 
                    print("\n---" + filePaths[x].rpartition('/')[-1] + " is not a recognized M-EX Slippi Template Silhouette file name---") # Skip the input image file if it doesn't match with the template CSP Silhouette files
                    mEXBatchName = input("\nYou may manually enter the base file name that M-EX uses if known (ex. 'PlMr' for Mario): ")
                    if mEXBatchName not in cspNamesArr[1]:
                        print("---Invalid M-EX base file name entered, " + filePaths[x].rpartition('/')[-1] + " will be skipped---")
                        continue    
                print("---The output image(s) will have " + mEXBatchName + " in the file names---") # Tell the user what the M-EX batch import format file name will be without the expansion slot number(s)

            if not baseText or not baseText.isalpha(): # Skip an image file if the baseText variable is invalid, must not be empty and must have letters
                print("---Invalid text entered, " + filePaths[x].rpartition('/')[-1] + " will be skipped---")
                continue
            startNum = input("Input starting expansion slot number: ") # Initialize the variable for the starting range of the expansion slot numbers
            endNum = input("Input ending expansion slot number: ") # Initialize the variable for the ending range of the expansion slot numbers
        except ValueError: # Skip the input image file if the baseText variable is invalid
            continue

        for y in range(int(startNum), int(endNum) + 1):
            cspImage = Image.open(filePaths[x])  # Reload the image to prevent drawing extra pixels
            cspImageDraw = ImageDraw.Draw(cspImage)
            fullImageText = baseText + str(y) # Text to draw on image(s), a combination of the expansion slot base color & each expansion slot number
            cspImageDraw.text((cspImage.size[0]/2, cspImage.size[1]/2), fullImageText, font=cspImageFont, fill='white', stroke_width=2, stroke_fill='black') # Draw text with a black outline on image(s) in the center of each image 
            
            if isForBatchImport == "N":
                cspImage.save(filePaths[x].rpartition('/')[-1].rsplit('.png')[0] + '_' + fullImageText + '.png') # Save image(s) to a file name similar to the original but with an underscore & text from the image
            elif isForBatchImport == "Y":
                cspImage.save(mEXBatchName + baseText + str(y) + ".png") # Save image(s) in a format ready for M-EX's Batch Import feature

        print("\n---Saved edited CSP image(s) based on " + filePaths[x].rpartition('/')[-1] + "---")