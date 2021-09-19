#author : theparri@protonmail.com
#date 18/9/2021
import csv
import time
import colorama as cr
import datetime
import os
class Timers:
    def __init__(self,timerdict):
        self.fieldnames = ["name","s","m","h","date"]
        self.timerdict = timerdict
        self.timerlist = list(timerdict.keys())
        self.runtimer = {}
        self.second = lambda s:round(s,3)
        self.minit = lambda s:round(s/60,3)
        self.hour = lambda s:round(s/3600,3)
    def ExistTimer(self,name):
        if name == "all":
            return self.timerdict.keys()
        else:
            if self.timerdict.get(name) == None: return False
            else : return True
    def NewTimer(self,name):
        row = {"name": name, "s": 0, "m": 0, "h": 0, "date": datetime.datetime.now().strftime("%d/%m/%Y")}
        with open("data.csv","a") as csvwriter:
            csvwriter = csv.DictWriter(csvwriter ,fieldnames=self.fieldnames)
            csvwriter.writerow(row)
        if self.timerlist.count(name) == 0:
            self.timerlist.append(name)
        self.timerdict.update({name:row})
    def OnTimer(self,name):
        self.runtimer.update({name:time.time()})
    def GetTimer(self,name,get_total = False):
        if self.runtimer.get(name) == None:
            this_time = 0
        else:
            this_time = time.time()-self.runtimer[name]
        total_time = this_time+float(self.timerdict[name]["s"])
        if get_total == False:
            return(self.second(this_time),self.minit(this_time),self.hour(this_time))
        if get_total == True:

            return (self.second(total_time),self.minit(total_time),self.hour(total_time))
    def SaveTimer(self,name):
        if name == "all":
            timerdict = []
            for timer in list(self.runtimer.keys()):
                times = self.GetTimer(timer, get_total=True)
                self.OnTimer(timer)
                self.timerdict.update({timer: {"name": timer, "s": times[0], "m": times[1], "h": times[2],"date": self.timerdict[timer]["date"]}})
                timerdict.append(self.timerdict[timer])

            with open("data.csv","w") as csvwriter:
                csvwriter = csv.DictWriter(csvwriter,fieldnames=self.fieldnames)
                csvwriter.writeheader()
                csvwriter.writerows(timerdict)
        else:
            times = self.GetTimer(name, get_total=True)
            self.OnTimer(name)
            with open("data.csv","w") as csvwriter:
                csvwriter = csv.DictWriter(csvwriter,fieldnames=self.fieldnames)
                csvwriter.writeheader()
                self.timerdict[name] = {"name": name, "s": times[0], "m": times[1], "h": times[2], "date": self.timerdict[name]["date"]}
                for i in self.timerdict: csvwriter.writerow(self.timerdict[i])
    def OffTimer(self,name):
        if name == "all":
            self.SaveTimer("all")
            self.runtimer.clear()
        else:
            self.SaveTimer(name)
            self.runtimer.pop(name)

    def ResetTimer(self,name):
        if name == "all":
            self.timerdict.clear()
            for timer in self.timerlist:
                self.NewTimer(timer)
        else:
            self.timerdict.pop(name)
            self.NewTimer(name)
        with open("data.csv","w") as csvwriter:
            csvwriter = csv.DictWriter(csvwriter,fieldnames=self.fieldnames)
            csvwriter.writeheader()
            for i in self.timerdict: csvwriter.writerow(self.timerdict[i])
    def DeleteTimer(self,name):
        if name == "all":
            self.timerdict.clear()
            self.timerlist.clear()
            with open("data.csv","w") as csvwriter:
                csvwriter = csv.DictWriter(csvwriter,fieldnames=self.fieldnames)
                csvwriter.writeheader()
        else:
            self.timerlist.remove(name)
            self.timerdict.pop(name)
            with open("data.csv","w") as csvwriter:
                csvwriter = csv.DictWriter(csvwriter,fieldnames=self.fieldnames)
                csvwriter.writeheader()
                for i in self.timerdict: csvwriter.writerow(self.timerdict[i])
class ConsoleBuffer:
    def __init__(self,dictcsv):
        os.system("printf \"\033c\"")
        self.row = {"name":"","seconds":"","minit":"","hour":"","date":""}
        self.mensage = "commands = [exist,new,init,stop,delete,quit,help]"
        self.mensage1 = "| En uso -> "
        self.mytimer = Timers(dictcsv)
        self.Timer1 = " "
        self.Title = ""
    def title(self):
        os.system("printf \"\033c\"")
        self.Title = cr.Fore.RED + cr.Style.NORMAL + f"""
____________________________________________       
 ╭━━━┳━━━┳━━━┳━━━┳━━╮╱╱╭━━━━┳━━┳━╮╭━┳━━━┳━━━╮     {self.row["name"]}
 ┃╭━╮┃╭━╮┃╭━╮┃╭━╮┣┫┣╯╱╱┃╭╮╭╮┣┫┣┫┃╰╯┃┃╭━━┫╭━╮┃     {self.row["seconds"]}
 ┃╰━╯┃┃╱┃┃╰━╯┃╰━╯┃┃┃╱╱╱╰╯┃┃╰╯┃┃┃╭╮╭╮┃╰━━┫╰━╯┃     {self.row["minit"]}
 ┃╭━━┫╰━╯┃╭╮╭┫╭╮╭╯┃┃╱╭━━╮┃┃╱╱┃┃┃┃┃┃┃┃╭━━┫╭╮╭╯     {self.row["hour"]}
 ┃┃╱╱┃╭━╮┃┃┃╰┫┃┃╰┳┫┣╮╰━━╯┃┃╱╭┫┣┫┃┃┃┃┃╰━━┫┃┃╰╮     {self.row["date"]}
 ╰╯╱╱╰╯╱╰┻╯╰━┻╯╰━┻━━╯╱╱╱╱╰╯╱╰━━┻╯╰╯╰┻━━━┻╯╰━╯        
_____________________________________________""" + cr.Fore.RESET + cr.Style.RESET_ALL+"   "+self.mensage1+"\n"+self.mensage
        print(self.Title)
    def ConsoleExistTimer(self,name):
        if name == "all":
            self.mensage = f"""
Temporizadores existentes
-------------------------
{self.mytimer.ExistTimer("all")}
        """
        else:
            self.mensage = str(self.mytimer.ExistTimer(name))
    def ConsoleNewTimer(self,name):
        if name == "all": ConsoleError("__ALL__")
        self.mytimer.NewTimer(name)
        self.mensage = "Nuevo temporizador creado , nombre : "+name
    def ConsoleInitTimer(self,name):
        if name == "all":
            for k in self.mytimer.timerdict.keys():
                self.mytimer.OnTimer(k)
                self.mensage1 += k + " | "
            self.mensage = " Se han iniciado todos los temporizadores"
        else:
            if self.mytimer.ExistTimer(name):
                self.mytimer.OnTimer(name)
                self.mensage = name+" se ha iniciado"
                self.mensage1 += name+" | "
            else: ConsoleError(name)
    def ConsoleGetTimer(self,name):
        if self.mytimer.timerdict.get(name) == None: ConsoleError(name)
        else:
            t = self.mytimer.GetTimer(name)
            t1 = self.mytimer.GetTimer(name,True)
            self.row["name"] = f"nombre: {name}"
            self.row["seconds"] = f"segundos: {t[0]} | {+t1[0]}"
            self.row["minit"] = f"minutos: {t[1]} | {t1[1]}"
            self.row["hour"] = f"horas:  {t[2]} | {t1[2]}"
            self.row["date"] =  "date: "+self.mytimer.timerdict[name]["date"]
    def ConsoleSaveTimer(self,name):
        self.mytimer.SaveTimer(name)
        self.mensage1 = "Se ha guardado el programa "+name
    def ConsoleOffTimer(self,name):
        if name == "all":
            for k in self.mytimer.timerdict.keys():
                self.mytimer.OffTimer(k)
                self.mensage1 = self.mensage1.replace(k + " |", "")
            self.mensage = "Se han parado todos los temporizadores"
        else:
            self.mytimer.OffTimer(name)
            self.mensage = name+" se ha parado"
            self.mensage1 = self.mensage1.replace(name+" |","")
    def ConsoleResetTimer(self,name):
        self.mytimer.ResetTimer(name)
        self.mensage = "RESETEADO"
    def ConsoleDeleteTimer(self,name):
        if name == "all":
            self.mytimer.OffTimer("all")
            self.mytimer.DeleteTimer("all")
            self.mensage = "Se han borrado todos los temporizadores"
            self.mensage1 = "| En uso ->"
        else:
            self.mytimer.OffTimer(name)
            self.mytimer.DeleteTimer(name)
            self.mensage = name + " se ha borrado"
            self.mensage1 = self.mensage1.replace(name+" |", "")
    def ConsoleHelp(self):
        self.mensage = """
______________________________________________________________________
comando : "exist [nombre,all]"   Muestra que contadores existen
comando : "new [nombre]"         Crea un nuevo temporizador y lo guarda 
comando : "init [nombre]"        Inicia un temporizador ya creado
comando : "save [nombre]"		 guarda el programa
comando : "stop [nombre]"        Para un temporizador ya iniciado
comando : "delete [nombre]"      Borra un temporizador para siempre
comando : "see [nombre]"         Muestra temporizador creado
comando : "help"                 Abre el menu de ayuda 
________________________________________________________________________
"""
def ConsoleError(timer_name):
    os.system("clear")
    if timer_name == None:
        print(cr.Fore.RED + f"No se ha introducido comando. Revisa -> " + cr.Style.BRIGHT + "help " + cr.Style.NORMAL + "para más información" + cr.Fore.RESET + cr.Style.RESET_ALL)
    if timer_name == "__ALL__":
        print("El nombre \"all\" está reservado, utilice otro")
    else:
        print(cr.Fore.RED + f"\nError no se reconoce el temporizador " +cr.Style.BRIGHT+str(timer_name)+ cr.Fore.RESET+cr.Style.RESET_ALL)
    input("--Presiona Enter--")
def app():
    with open("data.csv","r") as csvfile:
        dictfile = csv.DictReader(csvfile)
        dictcsv = {}
        for row in dictfile:
            dictcsv.update({row["name"]:row})
    console = ConsoleBuffer(dictcsv)
    while True:
        console.title()
        command = input(cr.Fore.BLUE+"-> "+cr.Fore.RESET)
        #We open the csv file and it is transform in a dict list
        #COMMANDS
        if command == None : ConsoleError(None)
        command = command.split()
        try: timer_name = command[1]
        except: pass
        try: subcommand = command[2:]
        except: pass
        command = command[0]
        if command == "init" or command == "on":
            try:
               # print("inicialize "+dictcsv[timer_name]["name"])
                console.ConsoleInitTimer(timer_name)
            except: ConsoleError(timer_name)
        elif command == "see":
            try:
                console.ConsoleGetTimer(timer_name)
                try: console.ConsoleGetTimer(timer_name,bool(subcommand))
                except: pass
            except: ConsoleError(timer_name)
        elif command == "exist":
            try : console.ConsoleExistTimer(timer_name)
            except : console.ConsoleExistTimer("all")
        elif command == "new":
            try: console.ConsoleNewTimer(timer_name)
            except: ConsoleError(timer_name)
        elif command == "save":
            try: console.ConsoleSaveTimer(timer_name)
            except: ConsoleError(timer_name)
        elif command == "stop" or command == "off":
            try : console.ConsoleOffTimer(timer_name)
            except : ConsoleError(timer_name)
        elif command ==  "reset":
            try: console.ConsoleResetTimer(timer_name)
            except : ConsoleError(timer_name)
        elif command == "delete" or command == "remove":
            try: console.ConsoleDeleteTimer(timer_name)
            except: ConsoleError(timer_name)
        elif command == "help":
            console.ConsoleHelp()
        elif command == "quit" or command == "exit":
            quit()
        else:
            os.system("clear")
            print(cr.Fore.RED+f"ERROR no se reconoce el comando \"{command}\". Revisa -> "+cr.Style.BRIGHT+"help "+cr.Style.NORMAL+"para más información"+cr.Fore.RESET+cr.Style.RESET_ALL)
            input("--Presiona Enter--")
if __name__ == '__main__':
    app()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
