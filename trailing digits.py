#Column 'C' in dataset df1 has the following text vlaues:
#Sample df1['C']
"""16th Street  115                               
Bryant Street  200                             
Potrero Avenue  100"""      

#I want to get rid of only the trailing digits without disturbing the digits that appear in the text otherwise. The following code does it all!
df1['C'].str.replace("\d+$", '') #Here '\d' - regex pattern - which represents digits and the '+' sign is to comprise the digits that appear once or more. The '$' in the pattern is to focus only on the trailing digits.

#And the desired output appears as:
"""16th Street                                    
Bryant Street                                  
Potrero Avenue""" 