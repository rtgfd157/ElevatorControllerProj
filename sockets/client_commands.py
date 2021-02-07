import subprocess



# p1 = subprocess.Popen(['python3','client_skeleton.py' ,'el_button_press','5','4'],
#  shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout)


#p2.terminate()
#p2.kill()
#p2.stdout.close()
 
# print(f'error {err}')
# print(f'out {out}')

def call_script(cl):
    p2 = subprocess.Popen(cl, shell=False, stdin=None)
    out, err = p2.communicate()

c_list =[['python3', 'client_skeleton.py' ,'floor_up','4'],
        ['python3', 'client_skeleton.py' ,'el_button_press','4','1' ],
                   # ['python3', 'client_skcd soeleton.py' ,'s' ],
                    ]

for cl in c_list:
    call_script(cl)
    