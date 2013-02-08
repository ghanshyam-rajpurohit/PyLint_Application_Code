'''
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break
        
         #################################################3  
        read lines no wise
        
        #line = open("file.txt", "r").readlines()[7]   
        fp = open("file")
for i, line in enumerate(fp):
    if i == 25:
        # 26th line
    elif i == 29:
        # 30th line
    elif i > 29:
        break
fp.close()

Note that i == n-1 for the nth line.
>>> import linecache
>>> linecache.getline('/etc/passwd', 4)
'sys:x:3:3:sys:/dev:/bin/sh\n'
####################################################################
'''
import re, linecache

def Make_it_standerd_code(OUT,filetoimplement):
    operator_with_spaces = re.compile("Operator not preceded by a space.*$")
    operator_with_comma_space = re.compile("Comma not followed by a space.*$")
    bad_indentation = re.compile("W: (?P<linenocolno>\d+,\d+): Bad indentation.+Found (?P<found>\d+) spaces, expected (?P<expeted>\d+)")
    invalid_name_to_variable = re.compile("C: (?P<lineno_occuer>\d+,\d+):(?P<modulename>.+): Invalid name \"(?P<valreabename>.+)\" for type variable \(should match (?P<pattern>.+)\)")
    wholetextoffile = filetoimplement.read()
    wholespltedtext = OUT.split('\n')
    badindentaion_list = bad_indentation.findall(OUT)
    invalid_variablelist = invalid_name_to_variable.findall(OUT)
    for invalid_variable_name in invalid_variablelist:
        line_no = invalid_variable_name[0][:2]
        needed_indent_line = linecache.getline(filetoimplement.name, 
                                               int(line_no))
        name_of_variable = invalid_variable_name[2]
        if invalid_variable_name[3].strip() == "[a-z_][a-z0-9_]{2,30}$":
            get_name = name_of_variable.lower()
        else:
            get_name = name_of_variable#raw_input("Present name in the code is %s it is not matching to pattern %s **be cautious while typing name**\n  :"%(name_of_variable, invalid_variable_name[3])) 
        if wholetextoffile.find(name_of_variable) != -1:
            #new_line_to_replace = needed_indent_line.replace(name_of_variable,
            #                                                 get_name)
            wholetextoffile = wholetextoffile.replace(name_of_variable, 
                                                      get_name)
    #items=re.findall("[.+]Operator not preceded by a spce.*$",OUT,re.MULTILINE)
    
    for value_implement in badindentaion_list:
        line_no = value_implement[0][:2]
        
        needed_indent_line = linecache.getline(filetoimplement.name, 
                                               int(line_no))
        #found_indent = value_implement[1]
        expected_indent = value_implement[2]
        new_line_to_replace = needed_indent_line.lstrip()
        spaces_value_string = ""
        for spacecreation in range(int(expected_indent)):
            spaces_value_string += " "
        new_line_to_replace = spaces_value_string+new_line_to_replace
        
        if wholetextoffile.find(needed_indent_line) != -1:
            wholetextoffile = wholetextoffile.replace(needed_indent_line, 
                                                      new_line_to_replace)  
    for line in wholespltedtext:
        
        alltext = operator_with_spaces.findall(line)
        commatext = operator_with_comma_space.findall(line)
        if alltext:
            if wholespltedtext[wholespltedtext.index(line)+1].find("==") == -1:
                if wholespltedtext[wholespltedtext.index(line)+1].find("=") != \
                -1 and wholespltedtext[\
                wholespltedtext.index(line)+1].find(" = ") == -1:
                    if wholetextoffile.find(wholespltedtext[\
                                        wholespltedtext.index(line)+1]) != -1:
                        linetoreplace = wholespltedtext[\
                            wholespltedtext.index(line)+1].replace("=", " = ")
                        wholetextoffile = wholetextoffile.replace(\
                wholespltedtext[wholespltedtext.index(line)+1], linetoreplace)
        if commatext:
            if wholespltedtext[wholespltedtext.index(line)+1].find(",")\
     != -1 and wholespltedtext[wholespltedtext.index(line)+1].find(", ") == -1:
                if wholetextoffile.find(wholespltedtext\
                                     [wholespltedtext.index(line)+1]) != -1:
                    linetoreplace = wholespltedtext[\
                            wholespltedtext.index(line)+1].replace(",", ", ")
                    wholetextoffile = wholetextoffile.replace(wholespltedtext\
                               [wholespltedtext.index(line)+1], linetoreplace)            
                  
   
    #print wholetextoffile
    writefile = open(filetoimplement.name[:-3]+"_Created"+".py", "w")
    writefile.write(wholetextoffile.replace("\t", "    "))
    writefile.close()    
if __name__ == '__main__':

    import subprocess
    PIPE_CONSTANT = subprocess.Popen(['pylint', 'ComperiotoZUF.py'],
                                           stdout=subprocess.PIPE, 
                                           stderr=subprocess.PIPE)
    OUT, ERR = PIPE_CONSTANT.communicate()
    FILENAMEIMPLEMNT = open("ComperiotoZUF.py", "r")  
    Make_it_standerd_code(OUT, FILENAMEIMPLEMNT)



