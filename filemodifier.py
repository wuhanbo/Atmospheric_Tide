import os
import shutil

def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step



#os.chdir("finitetest")
#list1 = frange(5,25,5)
list2 = frange(18.0,28.1,0.1)


#for x in list1:
for y in list2:

    #myfile = open("tmp.sh","ab")
    #myfile.write("cd runtest"+str(18+float(x)/10)+"h; ./most_plasim_run &"+"\n")
    #myfile.close()
    filename = "earth_"+str(y)+"h"
        #shutil.copy("most_plasim_run",filename)
    #os.mkdir(filename)
    
    #shutil.copy("./earth_sample/newplanet_from_archive.def",filename)
    #os.chdir("./..")
    #shutil.rmtree(filename)

    #Copy all files from a backup diretory to each spin rate directories
    '''
    src_files = os.listdir("t21_l10_backup")
    for file_name in src_files:
        full_file_name = os.path.join("t21_l10_backup", file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, filename)
             
        #path = "runtest"+str(x)
        #shutil.copy('burn7.x',path)

    #os.chdir(filename)
        #os.chdir('output')
        #shutil.rmtree('test_sunnyvale3')
        #os.chdir("./../..")
    '''
    #os.remove("plasim_restart")
    #shutil.copy("burn_namelist",path)
    
     
   #Change content from certain files
    
    os.chdir(filename)	
    filedata = None
    #filedata2 = None
    #f = open('newplanet_from_archive.def','r')
    #f = open('run.def','r')
    f = open('num_run','r')
    #f = open('burn_namelist','r')
    #f = open('most_plasim_run','r')
    #f = open('plasim_namelist','r')
    #f = open('radmod_namelist','r')
    #f = open('planet_namelist','r')
    filedata = f.read()
    f.close()
    #newdata = filedata.replace("7.27221e-5",str(7.27221e-5*24.0/y))
    #newdata = filedata.replace("ecritphy=5","ecritphy=4800")
    #newdata = filedata.replace("ecritphy=4800","ecritphy=5")
    #newdata = filedata.replace("nday=10","nday=300")
    newdata = filedata.replace("2","4")
    #newdata = filedata.replace("nday=300","nday=10")
    #newdata = filedata.replace("rm -f plasim_restart","#rm -f plasim_restart")
    #newdata = filedata.replace("#rm -f plasim_restart","rm -f plasim_restart")
    #newdata = filedata.replace("cp *output $test"," ")
    #newdata = filedata.replace("N_RUN_YEARS =     20","N_RUN_YEARS =     1")
    #newdata = filedata.replace("N_RUN_YEARS =     1","N_RUN_YEARS =     20")
    #newdata = filedata.replace("NWPD        =     "+str(int(round(y))),"NWPD        =     1")
    #newdata = filedata.replace("NWPD        =     1","NWPD        =     "+str(int(round(y))))
    #newdata = filedata.replace("MPSTEP      =     10","MPSTEP      =     30")
    #newdata = filedata.replace("NO3            =       0","NO3            =       1")
    #newdata = filedata.replace("PLARAD      =   7326903.0","PLARAD      =   6371000.0")
    #newdata = filedata.replace("10*0.1","10*0.05")
    #f = open('newplanet_from_archive.def','w')
    #f = open('run.def','w')
    f = open('num_run','w')
    #f = open('most_plasim_run','w')
    #f = open('fluxmod_namelist','w')
    #f = open('plasim_namelist','w')
    #f = open('radmod_namelist','w')
    #f = open('planet_namelist','w')
    f.write(newdata)

    f.close()
    
    #f2 = open('planet_namelist','r')
    #filedata2 = f2.read()
    #f2.close()
    #newdata2= filedata2.replace("SIDEREAL_DAY= 68572.25","SIDEREAL_DAY= "+str(86164.09/24*y))    
    #f = open('burn','w')
    #f = open('most_plasim_run','w')
    #f = open('plasim_namelist','w')
    #f2 = open('planet_namelist','w')
    
    #f2.write(newdata2)
    #f2.close()
    os.chdir("./..")


   
'''
for y in list2:
    filename = "l"+str(10)+"_"+str(y)+"h"
    os.chdir(filename)
    os.remove("planet_namelist")
    os.chdir("./..")
    shutil.copy("planet_namelist",filename)
    os.chdir("./..")
'''
#os.mkdir("newdir")


#shutil.copy('./test*','./newdir/')
