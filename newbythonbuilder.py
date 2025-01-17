
import os
import time
from rich import console,live,style
from rich.progress import Progress
from lang import language
languages = language("en_US")
live = live.Live(console=console, refresh_per_second=4)
import getpass
Style = style.Style()
title = \
"""
┌────────────────────────────────────────────────┐
| [#0eeae3]https://gitee.com/mono163/bython-builder       [/#0eeae3]|
└────────────────────────────────────────────────┘
[yellow]FastBuilder 11.45.14 (unknow)[/yellow]
[red]%s[/red]
%s""" % (languages.message_1, languages.Special_Startup)
console = console.Console()
console.print(title,end="")
console.print(languages.Notice_CheckUpdate)
bytoken=""
if os.path.exists("bytoken"):
    with open("bytoken","r",encoding="utf-8") as f:
        bytoken=f.read()
while True:
    if len(bytoken)==0:
        name=input(languages.Enter_FBUC_Username)
        bytoken=getpass.getpass(languages.EnterPasswordForFBUC)
        if len(name) == 0 or len(bytoken)==0:
            continue
        else:
            with open("bytoken","w",encoding="utf-8") as f:
                f.write(bytoken)
    else:
        break
while True:
    server_code=input(languages.Enter_Rental_Server_Code)
    if len(server_code)==0:
        continue
    else:
        break
server_password=input(languages.Enter_Rental_Server_Password)
console.print(languages.ServerCodeTrans+server_code,style="yellow")
time.sleep(2)
console.print(languages.ConnectionEstablished,style="yellow")

tasks =[]
while True:
    msg=input()
    if msg.strip().split().__len__()==0:
        continue
    message=msg.strip().split()[1:]
    match msg.split()[0]:
        case "set":
            if message.__len__()==3:
                console.print(languages.PositionSet+" "+message[0]+" "+message[1]+" "+message[2])
        case "bdump":
            if message.__len__()==1:
                console.print(languages.Sch_FailedToResolve+f"- {message[0]}")
            elif message.__len__()==2 and message[1]=="-mono":
                tasks.append({"type":"bdump","file":message[0],"schedule":0})
                console.print(languages.TaskCreated)
                # 创建一个Progress对象
                with Progress() as progress:
                    # 创建一个任务，总进度为100
                    task = progress.add_task("[cyan]正在加载...", total=100)

                    # 模拟一些工作
                    while not progress.finished:
                        progress.update(task, advance=1)  # 每次更新进度1
                        time.sleep(0.02)  # 模拟工作时间
                        if progress.tasks[task].completed >= 100:
                            progress.update(task,description=message[0]+"已完成", completed=100)

