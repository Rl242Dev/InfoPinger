from dotenv import load_dotenv
import os

print('''

 ______           ______                _______  __                                     
/      |         /      \              /       \/  |                                    
$$$$$$/ _______ /$$$$$$  ______        $$$$$$$  $$/ _______   ______   ______   ______  
  $$ | /       \$$ |_ $$/      \       $$ |__$$ /  /       \ /      \ /      \ /      \ 
  $$ | $$$$$$$  $$   | /$$$$$$  |      $$    $$/$$ $$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$  |
  $$ | $$ |  $$ $$$$/  $$ |  $$ |      $$$$$$$/ $$ $$ |  $$ $$ |  $$ $$    $$ $$ |  $$/ 
 _$$ |_$$ |  $$ $$ |   $$ \__$$ |      $$ |     $$ $$ |  $$ $$ \__$$ $$$$$$$$/$$ |      
/ $$   $$ |  $$ $$ |   $$    $$/       $$ |     $$ $$ |  $$ $$    $$ $$       $$ |      
$$$$$$/$$/   $$/$$/     $$$$$$/        $$/      $$/$$/   $$/ $$$$$$$ |$$$$$$$/$$/       
                                                            /  \__$$ |                  
                                                            $$    $$/                   
                                                             $$$$$$/                    

[1] : Tools
[2] : Exit
''')
Choice = str(input('Choose : '))

if Choice in ('1', '2'):
    if Choice == '1':
        print('''
        
[1]: InstagramInfo
[2]: IpTracer
[3]: MetaData Extractor
[4]: Url Extender
[5]: Url Shortener
        ''')
        Choice = str(input('Choose : '))
        if Choice in ('1', '2', '3', '4', '5'):
            if Choice == '1':
                exec(open("Tools/igInfo.py").read())
            if Choice == '2':
                exec(open("Tools/ipTracer.py").read())
            if Choice == '3':
                exec(open("Tools/metaData.py").read())
            if Choice == '4':
                exec(open("Tools/urlExtend.py").read())
            if Choice == '5':
                exec(open('Tools/urlShort.py').read())
        else:
            print('Error Invalid Input')
            quit()
    if Choice == '2':
        quit()
else:
    print('Error Invalid Input')
    quit()