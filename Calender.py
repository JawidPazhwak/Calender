from tkinter import *
import calendar

root = Tk()
root.title("calender")
root.configure(background="#0D0D0D")

def show_calender():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())

        cal = calendar.TextCalendar(calendar.SUNDAY).formatmonth(year, month)

        output_text.delete(0.0, END)
        output_text.insert(END, cal)
    
    except ValueError:        
        output_text.delete(0.0, END)

year_label = Label(root, text="Enter the year (intger): ", cursor="heart", bg="#0D0D0D", fg="white", 
font="matrix 8 bold", foreground="#00FFFF")  
year_label.grid(row=0, column=0)
year_entry = Entry(root, background="#0D0D0D", foreground="#00FFFF", font="matrix 8 bold", insertbackground="#00FFFF",
highlightcolor="#00FFFF", highlightthickness=1, selectbackground="red")
year_entry.grid(row=0, column=1)

month_label = Label(root, text="Enter the month (1-12): ", cursor="heart", bg="#0D0D0D", fg="white", 
font="matrix 8 bold", foreground="#00FFFF")  
month_label.grid(row=1, column=0)
month_entry = Entry(root, background="#0D0D0D", foreground="#00FFFF", font="matrix 8 bold", insertbackground="#00FFFF",
highlightcolor="#00FFFF", highlightthickness=1, selectbackground="red")
month_entry.grid(row=1, column=1)


show_button = Button(root, text="show calender", command = show_calender, background="#0D0D0D", foreground="#00FFFF",
 font="matrix 8 bold", activebackground="#00CC00")
show_button.grid(row=3, column=0, sticky=EW)

output_text = Text(root, width=20, height=10, background="#0D0D0D", foreground="#00FFFF",
 font="matrix 8 bold")
output_text.grid(row=4, column=0, columnspan=3, sticky=EW)

root.mainloop()