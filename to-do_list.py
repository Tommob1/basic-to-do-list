#Import modules
from tkinter import *

#Initialize GUI window
root = Tk()
root.title('To-Do List')
root.geometry('300x400')
root.resizable(0, 0)
root.config(bg='White')

#Heading label
Label(root, text='List', bg='Grey', font=("Calibre", 15), wraplength=300).place(x=35, y=0)

#Listbox all tasks with scrollbar
tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=50, height=232)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=35, y=50)

# Adding and Deleting items functions
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open(r'C:\Users\Pc\Desktop\Coding Files\Python Files\To Do List Project\list.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')

def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open(r'C:\Users\Pc\Desktop\Coding Files\Python Files\To Do List Project\list.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)

        tasks_list_file.close()

#Adding items to Listbox
with open(r'C:\Users\Pc\Desktop\Coding Files\Python Files\To Do List Project\list.txt', 'r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

#Create entry widget where user can enter new items
new_item_entry = Entry(root, width=37)
new_item_entry.place(x=35, y=310)

#Create buttons .
add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12), 
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=45, y=350)

delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12), 
                 command=lambda: delete_item(tasks))
delete_btn.place(x=150, y=350)

#Finalizing the window
root.update()
root.mainloop()