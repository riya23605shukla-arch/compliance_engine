
# import regular expressions(re) for cleaning the text  
# re helps to find and replace patterns in the text
# re.sub(pattern, replacement, text) 

import re

# creates a cleaning function
def clean_text(text):

    # Remove extra spaces 
    #  sub is substitute or replace , \s whitespace character , + means more times 
    # examples of white spaces " " , "  ", "\t" ,"\n"."    "

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    # Remove repeated line breaks
    text = re.sub(
        r'\n+',
        '\n',
        text
    )
  # remove the spaces from the beginning and the end
    return text.strip()