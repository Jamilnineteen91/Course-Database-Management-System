from tkinter import *

# Window set-up
window=Tk()
window.title('Course Database System')


# <--- Student Form --->

# Labels
cell_1=Label(window, text="Student ID")
cell_1.grid(row=0,column=0)

cell_2=Label(window, text="First name")
cell_2.grid(row=1,column=0)

cell_3=Label(window, text="Last name")
cell_3.grid(row=2,column=0)

cell_4=Label(window, text="Gender")
cell_4.grid(row=3,column=0)

cell_5=Label(window, text="Address")
cell_5.grid(row=4,column=0)

cell_6=Label(window, text="City")
cell_6.grid(row=5,column=0)

cell_7=Label(window, text="Region")
cell_7.grid(row=6,column=0)

cell_8=Label(window, text="Country")
cell_8.grid(row=7,column=0)

cell_9=Label(window, text="Zip")
cell_9.grid(row=8,column=0)

cell_10=Label(window, text="Phone number")
cell_10.grid(row=9,column=0)

# Entries
student_id=StringVar()
entry_1=Entry(window, textvariable=student_id)
entry_1.grid(row=0,column=1)

first_name=StringVar()
entry_2=Entry(window, textvariable=first_name)
entry_2.grid(row=1,column=1)

last_name=StringVar()
entry_3=Entry(window, textvariable=last_name)
entry_3.grid(row=2,column=1)

# Gender entry will be handled differently

Address=StringVar()
entry_5=Entry(window, textvariable=Address)
entry_5.grid(row=4,column=1)

City=StringVar()
entry_6=Entry(window, textvariable=City)
entry_6.grid(row=5,column=1)

Region=StringVar()
entry_7=Entry(window, textvariable=Region)
entry_7.grid(row=6,column=1)

Country=StringVar()
entry_8=Entry(window, textvariable=Country)
entry_8.grid(row=7,column=1)

Zip=StringVar()
entry_9=Entry(window, textvariable=Zip)
entry_9.grid(row=8,column=1)

Phone_number=StringVar()
entry_10=Entry(window, textvariable=Phone_number)
entry_10.grid(row=9,column=1)

# Buttons
button_1=Button(window, text="Add", width=12)
button_1.grid(row=2, column=3)

button_2=Button(window, text="Update", width=12)
button_2.grid(row=5, column=3)

button_3=Button(window, text="Delete", width=12)
button_3.grid(row=8, column=3)

# Display
display=Listbox(window, height=20, width=20)
display.grid(row=0,column=4, rowspan=10, columnspan=3)


window.mainloop()