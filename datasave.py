#just for simpler coding datasaves
class load:

    def load_int(filepath):         #returns an int from a file
        file=open(filepath,'r+')
        file_data=file.read()
        file.close()
        return int(file_data)


    def load_str(filepath):         #returns a str from a file
        file=open(filepath,'r+')
        file_data=file.read()
        file.close()
        return str(file_data)
    def load_list(filepath):         #returns a list from a file
        file=open(filepath,'r+')
        file_data=file.read()
        file.close()
        
        i=0
        newList=[]
        newString=''
        
        while i<len(file_data):
            if file_data[i]!='~':
                newString+=str((file_data[i]))
            else:
                newList.append(newString)
                newString=''
            i+=1

        
        return newList
class save:

    def save_str(filepath,var):         #saves an str to a file
        file=open(filepath,'w')
        file.write(str(var))
        file.close()

    def save_list(filepath,var):         #saves a list to a file
        file=open(filepath,'w')
        for i in var:
            file.write(str(i))
            file.write('~')
        file.close()





