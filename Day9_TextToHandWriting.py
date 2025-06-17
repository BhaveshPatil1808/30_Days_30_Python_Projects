# Import library and give an alias name
import pywhatkit as pw

# Add your custom text
# Use triple quotes to add a whole paragraph
txt = """
Python is an interpreted high-level general-purpose 
programming language. 
Its design philosophy emphasizes code readability with its use of 
significant indentation.
"""

# Use the inbuilt function
# If no filename is given, it will save as 'pywhatkit.png' by default
# We can also give custom filename and color
pw.text_to_handwriting(txt, "python_handwriting.png", [0, 0, 255])  # Blue color in RGB

print("Code is running")
