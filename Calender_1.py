from tkinter import *
import calendar

root = Tk()
root.title("calender")

def show_calender():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())

        cal = calendar.TextCalendar(calendar.SUNDAY).formatmonth(year, month)

        output_text.delete(0.0, END)
        output_text.insert(END, cal)
    
    except ValueError:        
        output_text.delete(0.0, END)

year_label = Label(root, text="Enter the year (intger): ")  
year_label.grid(row=0, column=0)
year_entry = Entry(root)
year_entry.grid(row=0, column=1)

month_label = Label(root, text="Enter the month (1-12): ")  
month_label.grid(row=1, column=0)
month_entry = Entry(root)
month_entry.grid(row=1, column=1)


show_button = Button(root, text="show calender", command = show_calender)
show_button.grid(row=3, column=0)

output_text = Text(root, width=20, height=10)
output_text.grid(row=4, column=0, columnspan=3,sticky=EW)

root.mainloop()