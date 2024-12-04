#!/usr/bin/env python
# coding: utf-8

import os
import csv
import re



os.chdir('/Users/Ruschena/Anaconda Projects/Projects/TEPT/Review of Metaphysics/DD_RoM')

#we need to obtain textfile from pdf file. Here, pdftotext has been used as a command line: pdftotext -layout -f 2 DoctoralDissertations1963-1963.pdf in order to obtain a text file. -f 2 means starting from the second page, while -layout preserves indentation and other graphic features.
#to pdftotext all files in cwd on the command line: for i in `ls $PWD`; do pdftotext -layout -f 2 $i; done
#pdftotext's results seem to differ slightly if it runs as python library, so that this conversion relied on bash command line



#functions to discern among types of lines found in the text, after lines to ignore are filtered out while reading the file

def is_first_line(line): #recognise first lines of records
    if re.match(r'\s{0,1}\w', line): #criterion: zero to one spaces preceding text
        
        return True
    else:
        return False
    
def is_continuing_line(line): #recognise following lines of records
    if re.match(r'\s{3,10}(\(*\w|\d)', line):#criterion: three to ten spaces preceding text
        
        return True
    else:
        return False


def is_uni_line(line): #recognise lines that contains universities by exclusion
    if is_continuing_line(line) == False and is_first_line(line) ==False:
        if re.search(abchars, line) != None:
            return True
        else:
            return False

        
def match_lowercase_word(string): 
    # assess if line starts with a word that is not capitalised in titles: 
    #this serves to evaluate if a space is needed in joining a following line to a previous one. 
    #If it returns False, but str[0] is lower case, it means that the following line starts 
    #with the final chunk of a word that has been split by a new line, else a space is needed when joining.
    lowercase_words =['and', 'or', 'to', 'from', 'of', 'in', 'with', 'on', 'for','but', 'a', 'an', 'the', 'as']
    for word in lowercase_words:
        if re.match(word, string):
            return True
        
        
        
def split_line(complete_line): 
    # Parse line obtaining values to fill a temporary record dictionary, 
    #which stores values while proceeding in reading lines.
    fields = {'author': '', 'thesis_title': '', 'advisor': ''}
    working_line = re.sub("'", '-', complete_line)
    
    sep_aut = re.split(',|;|.\s"',working_line, maxsplit=1)
    fields['author']= sep_aut[0]
    advisors_match = re.search('dvis(o|e)rs*\s*\:*\s*', complete_line)
    
    if re.search(r'Title\sUnavailable', complete_line) != None or re.search(r'untitled\sdissertation', complete_line) != None:
        fields['thesis_title']='Title Unavailable'
    
    else:
        sep_title = sep_aut[1].split('"', 2)
        fields['thesis_title'] = sep_title[1]
    
    
    awarded = re.search(r'\(\s*(A|a)ward', complete_line) # check for mention of award in a different year in the complete record, usually in the form e.g. "(Awarded in 1965)"
    if awarded != None:
        if advisors_match != None:
            advisors_field = complete_line[advisors_match.span()[1]:awarded.span()[0]-2]
        else:
            advisors_field = ''
    else:
        if advisors_match != None:
            advisors_field= complete_line[advisors_match.span()[1]:-1]
        else:
            advisors_field = ''
        
    if re.search(r'(\sand\s|\w\,\s\w)', advisors_field) != None:
        fields['advisor']= re.split(r'(\sand\s|(?=\w)\,\s(?<=\w))',advisors_field)
    else:
        fields['advisor']= advisors_field
    
    return fields #return parsed portion of the record as fields to be included in the dataset


def get_txt_file_s_data(file): 
    #retrieve metadata for referencing individual records from the title of the txt file, 
    #which contains the year of publication. The function returns also a file name for a csv 
    #to be made out of a single document
    issue_year = file[-8:-4]
    csv_filename = f'DD_RoM_{issue_year}_clean.csv'
    txt_filename = file
    #args_for_funct = (txt_filename, csv_filename, issue_year)
    return txt_filename, csv_filename, issue_year



def get_one_big_csv_file_from_rom_txt(name_of_csv_file_to_make):
    with open(name_of_csv_file_to_make, 'w') as out_file:
        fieldnames = ['author', 'thesis_title', 'advisor', 'university', 'year', 'original_line', 'provenance']
        csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for file in os.listdir(wd):
            if file[0]!= '.' and file[-4:] == '.txt':
        
        

                with open(file, 'r') as in_file:
                        lines= in_file.readlines()
                        clean_line=[]
                        uni= {"university": ''}
                        provenance = file

                        for line in lines[:-1]:
                            year_of_grad = get_txt_file_s_data(file)[2]
                            checker = True
                            subsequent_line=lines[lines.index(line)+1]

                            for patt in patterns:
                                if re.search(patt, str(line)) != None:
                                    checker = False #checher is False for every line matching stuff that needs to be excluded from retrieval such as headers and publisher's stamps
                                    print(f'This line will not be included in the retrieval:{line}')
                            print(checker)        
                            if (checker == True):

                                if is_uni_line(line)==True:
                                    uni["university"] = re.sub(r'(\s{2,}|\n)', '', line)

                                if is_first_line(line) == True:
                                    clean_line=[re.sub(r'\n', '', line)]
                                    

                                elif is_continuing_line(line) == True:
                                    cleaning = re.sub(r'\A\s+', '', line) # get rid of multiple white spaces at the beginning of continuing lines
                                    clean_line.append(re.sub(r'\n', '', cleaning))# get rid of new lines chars 


                                if (is_first_line(line) == True or is_continuing_line(line) == True) and is_continuing_line(subsequent_line) == False:
                                    print('last_line')
                                    definitive_line=''
                                    for element in clean_line: # clean_line is a list, each element of which is an original line in the text

                                        if element[0].isupper() == True or match_lowercase_word(element) == True: 
                                            # This takes care of discern with new lines needing a space before joining or not
                                            #(e.g. new line A: 'Pure Reason' needs a space vs new line B :'viser: Ernst Nagel' does not need a space char)
                                            definitive_line = definitive_line + ' ' + element
                                        else:
                                            definitive_line=definitive_line + element


                                    year_guess = re.search(r'(19\d\d|20\d\d)(?=\s*\.\s*\))', definitive_line) 
                                    #check for indications of year in the record different from the standard year indicated 
                                    #by the title of the survey and by the name of the text file
                                    if year_guess != None:
                                        year = definitive_line[year_guess.span()[0]:year_guess.span()[1]]
                                    else:
                                        year= year_of_grad
                                        
                                        
                                    author=split_line(definitive_line)['author']
                                    title = split_line(definitive_line)['thesis_title']
                                    advisor = split_line(definitive_line)['advisor']

                                    csv_writer.writerow({'original_line': definitive_line, 'author': author, 'thesis_title': title, 'advisor': advisor, 'university': uni["university"], 'year': year, 'provenance': provenance})

                                    


abchars = r'[A-Za-z]'
patterns = ['DOCTORAL DISSERTATIONS', 'This content downloaded from', 'All use subject to', "The three figures below each institution", 'graduate students enro','ed in its philosophy department', '(2) the number ', 'to (1) the numb', '(3) the number', 'of faculty members', 'residence graduate students', 'his information is included also for', 'dash indicates that the inform', 'required has not been provid', 'faculty members teaching in the grad', 'The Review of Metaphysics', 'full time students as that term','students as that term', 'present list may not be complete', 'some of the institutions which confer doctoral', 'in part because some of the institutions', 'our requests for information may have conferred', 'basis of written dissertaions. We hope', 'when we plan to publish the', 'dissertations in philosophy in the two', r'\A\s*Metaphysics\s*\.*\n', 'Review of Metaphysics', 'SURVEY OF GRADUATE PROGRAMS', 'North America. We wish to thank', r'represented for their cooperation.\n', r'\d\d\d\.\d\d\.\d\d\d\.\d\d\d', r'\d\d:\d\d:\d\d\s\+', 'fifteen members teach courses in their', r'\Aments.\s*\n', r'\A\s*\*\s*\w', 'Holyoke Colleges, and this last', 'faculty members in the', 'ere information was not supplied', 'Review invites and encourages', 'recently begun a Doctoral Program or', 'one in the near future', 'the graduate program', r'\A\sprogram\.*', 'program\.\n' 'graduate students as the term', ' Mount Holyoke and Smith', '\D\d\d\d\n', 'SUR VEY OF GRADUA TE PROGRAMS', 'graduate students as the term is understood by the institution', 'students as the term is understood', 'graduate program', ' and (3) the', 'received too late to be included','various dissertation committees to name']
#patterns results from the enumeration of recurring elements of lines that need to be ignored, e.g. headers,footnotes, editors' stamps, page numbers and so on.




#This makes one big csv file containing all the info
get_one_big_csv_file_from_rom_txt('ToPNA_RoM_pre_cleaning.csv')

