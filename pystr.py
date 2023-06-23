import re

st = re.compile(r' -?\d+')
f_in = open('IR.csv','r')
f_out = open('IR_out.csv','w')
myStr = ''
for line in f_in: 
    data_matches = st.findall(line)
    # numbers = [str(num) for num in data_matches]
    if len(data_matches) != 0: 
        # myStr += ', '.join(data_matches) 
        myStr += ' '.join(data_matches) 
    f_out.write(myStr+'\n') 
    myStr = ''
f_out.close()
