from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from results import getAllStats



wb = load_workbook('3rd_Q_Statistics.xlsx')
ws = wb.active

row = ws.max_row + 1

for col in range(1, 24):
    char = get_column_letter(col)
    ws[char + str(row)] = getAllStats()[col - 1]

wb.save('3rd_Q_Statistics.xlsx')