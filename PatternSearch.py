####    ####  ##############
####    ####  ##############
####    ####  ######
############  ####                   
####################################################################
#  ___  ____ ___ ___ ____ ____ _  _  ____ ____ ____ ____ ____ _  _ #
#  |__] |__|  |   |  |___ |__/ |\ |  [__  |___ |__| |__/ |    |__| #
#  |    |  |  |   |  |___ |  \ | \|  ___] |___ |  | |  \ |___ |  | #
####################################################################

'''START OF SCRIPT'''
### Imported the re module, the standard regex pattern-matching interface.
import re

### Paragraph for search and replace operation.
lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

### Created variable results, using the re.findall method to search through the lorem_ipsum string
### looking for any nonalphanumeric with the '\W' regular expression pattern and storing the results
### of that search in the variable "results".
results = re.findall(r'\W', lorem_ipsum)

### Output the length of the variable "results".
print(len(results))

### Created variable occurrance_sit_amet, using the re.findall method to search through the lorem_ipsum string
### looking for all matches of the variation sit[: or -]amet and saving them in the variable "occurrance_sit_amet".
occurrance_sit_amet = re.findall('sit[-:]amet', lorem_ipsum)

### Output the length of the variable "occurrance_sit_amet".
print(len(occurrance_sit_amet))

### Created variable replace_results, using the re.sub() method to substitute all instances of sit[: or -]amet with
### the string "sit amet" in the lorem_ipsum string.
replace_results = re.sub('sit[:-]amet', 'sit amet', lorem_ipsum)

### Created variable occurrance_sit_amet, using the re.findall method to find all instances of the string "sit amet" in
### the string variable "replace_results".
occurrance_sit_amet = re.findall('sit amet', replace_results)

### Output the length of the variable "occurrance_sit_amet".
print(len(occurrance_sit_amet))

'''END OF SCRIPT'''
