import json
import os
import datetime
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE,'r',encoding = 'utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError,ValueError):
            return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE,'w',encoding = 'utf-8') as f:
        json.dump(tasks,f,ensure_ascii = False,indent = 4)

def mark_done(tasks):
    try:
        num = int(input("请输入要完成的任务编号： "))
        if 1 <= num <=len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print("标记成功")
        else:
            print("请输入有效编号")
    except ValueError:
        print("请输入有效数字")

def clear(tasks):
    if not tasks:
        print("已经空空如也啦")
    else:
        for i in range(len(tasks)-1,-1,-1):
           if tasks[i]["done"]:
               tasks.pop(i)
            
    print("所有已完成任务已经删除啦")
           
tasks = load_tasks()


while True:
    print("\n--- 待办事项管理器 ---")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 标记完成")
    print("5. 清空已完成任务")
    print("6. 退出")
  
    choice = input("请选择操作 (1/2/3/4/5/6): ")

    if choice == '1':                       #查看任务
        print("\n当前任务清单：")
        if not tasks:
            print("[空空如也]")
        for index, task  in enumerate(tasks):
            icon = "[✅]" if task["done"] else "[❌]"
            name = task["content"]
            time = task["create_time"]
            print(f"{index + 1}.{icon} {name}  （创建于: {time})")
    
    elif choice == '2':                     #添加任务
        content = input("请输入新任务内容: ")
        new_task = {"content": content,"done": False,"create_time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
        tasks.append(new_task)
        save_tasks(tasks)
        print("添加成功！")
    
    elif choice == '3':                     #删除任务

        print("\n当前任务清单: ")
        if not tasks: 
            print("清单是空的，没什么要删除的")
            continue
        try:
            
            for index,task in enumerate(tasks):
                print(f"{index+1}. {task}")
            delete_task_index = int(input("请输入删除的任务序号： ")) - 1
            if 0 <= delete_task_index < len(tasks):
                
                remove_task = tasks.pop(delete_task_index)
                save_tasks(tasks)
                print(f"成功删除任务： {remove_task}")
            else:
                print("编号不存在，请输入列表中的数字哦")
        except ValueError:
            print("请输入有效的数字")
    elif choice == '4':
        print("\n当前任务清单： ")
        for i,t in enumerate(tasks):
            print(f"{i+1}. {t}")
        mark_done(tasks)
    elif choice == '5':
        warning= input("你确定要清空已完成任务吗？(Y/N): ").upper()
        if warning == 'Y':
            clear(tasks)
        continue

    elif choice == '6':                     #退出
        print("程序已退出。")
        break
    
    else:
        print("输入有误，请重新选择。")
