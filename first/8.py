'''my_list = [1,2,3,4]
for i in range(len(my_list)):
    print(i)

iterator= iter(my_list)
print(next(iterator))
print("what do we have")
print("Cakes")
print(next(iterator))
print("Il have some from my stash")
print(next(iterator))'''

'''def counter():
    yield 1
    yield 2
    yield 3'''

'''gen = counter()
print(next(gen))
print(next(gen))
print(next(gen))'''

'''def counter(starts=5,stops=1):
    while True:
        yield starts
        starts += stops
gen= counter()
for i in range(5)
    print(next gen)'''

'''def counter(starts=0):
    count=starts
    def next_number(step=1)
        nonlocal count
        count+=step
        return count
    return next_number()
counter=counter
print(counter(5))'''

import tkinter as tk
def counter(starts=5):
    while starts >=0:
        yield starts
        starts-=1
start_time = 60
counter = counter(start_time)

def update():
    try:
        time_left = next(counter)
        label.config(text=f'Time left: {time_left}')
        root.after(1000, update)
    except StopIteration:
        label.config(text=f'Time has run out')


root=tk.Tk()
root.title("Timer")
label = tk.Label(root, font=('Helvetica', 24), fg='blue')
label.pack(padx=20,pady=20)

update()
root.mainloop()
