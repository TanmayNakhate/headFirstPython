import oslearn
from prettytable import PrettyTable
from oslearn import listdir
from oslearn.path import isfile,join


my_path = 'C:\\tmp\\excel\\'

class CsvHtmlConversion:
    def csv_operation(self,csv):
        global my_path
        csv_file = open(my_path+csv)
        csv_file = csv_file.readlines()
        final_list = []

        for i in csv_file:
            final_list.append(i.strip())

        row = final_list[0].split(',')
        return row;

    def table_operation(self,table,row):
        table.clear_rows()
        for a in range(0, len(row)):
            table.add_row([row[a],row[a + 1],"C:/Users/tanmayn/Desktop/htmlReports/index.html"])
            break;
        print(table)
        return table

    def html_conversion(self,table):

        html_code = table.get_html_string()
        html_file = open(my_path+'Result.html', 'a+')
        html_file = html_file.write(html_code)
        print("Report is successfully generated.,"
              "Open ",my_path,"Result.html file to view report")


make_report = CsvHtmlConversion()

onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]
table = PrettyTable(border=True, padding_width=10,
            field_names=['Test_Name', 'Status', 'Link'])
for i in range(0,len(onlyfiles)):
    row = make_report.csv_operation(onlyfiles[i]);
    table = make_report.table_operation(table,row)
    make_report.html_conversion(table)


