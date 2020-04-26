import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import requests
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
 
covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()
country_list=[]
for c in covid_data:
    country_list.append(c)

class Main_Class(object):
    """use a ttk.TreeView as a multicolumn ListBox"""
    def __init__(self):
        self.tree = None
        self._setup_widgets()

    def _setup_widgets(self):
        frame_1 = ttk.Frame(root)
        frame_1.pack(fill='both', expand=False)

        ttk.Label(frame_1, text="Country").grid(row=0,column=0,padx=2,pady=2, sticky="W")
        self.comboCountries = ttk.Combobox(frame_1, values=country_list)
        self.comboCountries.grid(row=0,column=1,padx=5,pady=5, sticky="W")
        self.comboCountries.set('--Select Country--')
        self.comboCountries.bind("<<ComboboxSelected>>", self._selected_covid)

        ttk.Label(frame_1, text="From").grid(row=0,column=2,padx=2,pady=2, sticky="W")
        today = date.today()
        d = int(today.strftime("%d"))
        m = int(today.strftime("%m"))
        y =int(today.strftime("%Y"))
        self.dateStart = DateEntry(frame_1, date_pattern='yyyy-MM-dd', width=12, background='darkblue',foreground='white', borderwidth=2)
        self.dateStart.set_date(f'{y}-{m}-{d-2}')
        self.dateStart.grid(row=0,column=3,padx=5,pady=5, sticky="W")
        self.dateStart.bind('<<DateEntrySelected>>',self._selected_covid)

        ttk.Label(frame_1, text="To").grid(row=0,column=4,padx=2,pady=2, sticky="W")
        self.dateEnd = DateEntry(frame_1, date_pattern='yyyy-MM-dd', width=12, background='darkblue',foreground='white', borderwidth=2)
        self.dateEnd.grid(row=0,column=5,padx=5,pady=5, sticky="W")
        self.dateEnd.bind('<<DateEntrySelected>>',self._selected_covid)

        frame_2 = ttk.Frame(root)
        frame_2.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        gridview_header = ['Date', 'Confirmed', 'Deaths', 'Recovered']
        self.tree = ttk.Treeview(columns=gridview_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=frame_2)
        vsb.grid(column=1, row=0, sticky='ns', in_=frame_2)
        hsb.grid(column=0, row=1, sticky='ew', in_=frame_2)
        frame_2.grid_columnconfigure(0, weight=1)
        frame_2.grid_rowconfigure(0, weight=1)

    def _build_tree(self,header,_List):
        self.tree.delete(*self.tree.get_children())
        for col in header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        for item in _List:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(header[ix],width=None)<col_w:
                    self.tree.column(header[ix], width=col_w)    

    def _selected_covid(self,*args):
        if self.comboCountries.get() != '--Select Country--': 
            header = ['Date', 'Confirmed', 'Deaths', 'Recovered']
            list_of_data = covid_data[self.comboCountries.get()]
            list_of_tuple = []
            dStart=datetime.strptime(self.dateStart.get(), '%Y-%m-%d').date()
            dEnd=datetime.strptime(self.dateEnd.get(), '%Y-%m-%d').date()
            for i in list_of_data:
                if datetime.strptime(i['date'], '%Y-%m-%d').date()>=dStart and datetime.strptime(i['date'], '%Y-%m-%d').date()<=dEnd:
                    list_of_tuple.append(tuple(i.values()))
            self._build_tree(header,list_of_tuple)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

root = tk.Tk()
root.wm_title("Covid-19")
mc_listbox = Main_Class()
root.mainloop()