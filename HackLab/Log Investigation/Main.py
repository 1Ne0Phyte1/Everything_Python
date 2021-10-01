import colorama
from colorama import Fore,Back, Style
import prettytable

colorama.init(autoreset=True)

table = prettytable.PrettyTable([Fore.RED+"Found in logs",Fore.BLUE+'Line Number',Fore.YELLOW+"Occurrences" , Fore.GREEN+"Reference Line", Fore.CYAN+" Initial vulnerable endpoint"])

file = "access.log"

# Add anything into the list to find in the logs
list  = ["Nmap", "Hydra", "sqlmap", "feroxbuster","dirbuster"]

for i in range(len(list)):
    # opening the log file
    with open(file, "r") as f:
        # enumrating the file for "line number" and message
        for number ,line in enumerate(f):
            if list[i] in line:

                # finding the text position
                text = line.find(list[i])
                Highlight = line[text:text+len(list[i])]

                # Finding the occurrence
                data = f.read()
                occurrences = data.count(list[i])

                #  finding vulnerable endpoint
                end_point = line.split(" ")


                table.add_row([Fore.RED+Highlight,Fore.BLUE + str(number), Fore.YELLOW+str(occurrences), Fore.GREEN + line, Fore.CYAN+end_point[6]])
                break
print(table)
