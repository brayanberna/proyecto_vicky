        #Estilos 
                # set the height of the row 
                #sheet.row_dimensions[1].height = 70
                  
                # set the width of the column 
                #sheet.column_dimensions['B'].width = 20
                
        #max_row=ws.max_row
        #max_column=ws.max_column

        #for i in range(2,max_row+1):
        #   for j in range(1,max_column+1):
        #          cell_obj=ws.cell(row=i,column=j)
        #          print(cell_obj.value,end=' | ')
        #    print('\n')
      
        #ws['A3'] = '=SUM(A1, A2)'
        #sheet.auto_filter.add_filter_column(1, ['brown', 'white'])
        #sheet.sheet_properties.tabColor = "0072BA"
      #ws1 = wb.create_sheet("Mysheet1") #Crea nuevas hojas de trabajo.
      #ws2 = wb.create_sheet("Mysheet2") #Crea nuevas hojas de trabajo.
      #ws2 = wb.create_sheet("Mysheet2", 0)
      #ws3 = wb.create_sheet("Mysheet3", -1)
      
      #ws.append(datos).font = Font(color="000000", size=16, bold=True)
      #ws['A1':'F1'].font = Font(color="000000", size=16, bold=True)
      #ws['A1']:['F1'].font = Font(color="000000", size=16, bold=True)
      #ws['A1:F1'].font = Font(color="000000", size=16, bold=True)  
      #ws.merge_cells('A1:F1').font = Font(color="000000", size=16, bold=True)  #X
      #ws.cell(row=1, column=1).font = Font(color="000000", size=16, bold=True)
      #ws.cell(row=5, column=6, value='fugafugaufga')
      #b2 = ws.cell(column=2, row=2).value

      #for rows in datos:
        #print(rows)
        #ws.append(rows).font = Font(color="000000", size=16, bold=True)
        #rows.font = Font(color="000000", size=16, bold=True)
        #ws.append(rows).font = Font(color="000000", size=16, bold=True)
        #for cell in rows:
        #ws.append(cell)
      
      
      #for table in ws.tables.values():
      #  print("tablita: ",table)
      #print("tablitas: ",ws)
      
      #def dimensions(self):
      #      return self.calculate_dimension()
      #print("tablitas 1: ",dimensions(ws))
      #print("tablitas: ",max(ws)) #❌
      #print("tablitas 2: ",max(dimensions(ws))) #❌
      #print("tablitas 22: ",max(ws.calculate_dimension())) #❌
      #print("tablitas: ",dimensions(ws).min_row) #❌
      #print("tablitas 3: ",ws.max_row)
      #print("tablitas 4: ",ws.max_column)
      #print("tablitas 5: ",ws._cells[row, col])#❌
      #print("tablitas 3: ",ws.max_cells) #❌
      #print("tablitas 3: ",ws.max_col) #❌
      #print("tablitas 5: ",ws._current_row)
      #print("tablitas 5: ",ws.row) #❌
      

      #final = max(ws.calculate_dimension()) + str(ws.max_row)
      #print("ahora ti",final)


      #ws['A1':'F1'].fill = PatternFill("solid", fgColor="4BACC6")
      #ws['A1':'F1'].alignment = Alignment(horizontal="center")
      #thick 
      #bd = Side(style='thin', color="000000")
      #ws['A1':'F1'].border = Border(left=bd, top=bd, right=bd, bottom=bd)


      #print(ws['C2'])
      #ws['C2'].font = Font(color="000000", size=16, bold=True)  #Color de texto
      #ws['C2'].fill = PatternFill("solid", fgColor="4BACC6")
      #ws['C2'].alignment = Alignment(horizontal="center")
      #thick 
      #bd = Side(style='thin', color="000000")
      #ws['C2'].border = Border(left=bd, top=bd, right=bd, bottom=bd)
      #ws['A2'] = 23
      #ws['A2'].fill = PatternFill("solid", fgColor="4BACC6")
      #ws.fill = PatternFill("solid", fgColor="4BACC6")

      #s = 'I HAVE 6'
      #s.rsplit(maxsplit=1)  # or (' ', 1)
      #['I HAVE', '6']

      #print("tablitas 1: ",ws.calculate_dimension()) #❌
      #print("tablitas 2: ",max(ws.calculate_dimension())) #❌
      #print("tablitas 3: ",ws.max_row)
      #print("tablitas 4: ",ws.max_column)
      #print("tablitas 5: ",ws._current_row)

      #for i in range(2,max_row+1):
        # iterate over all columns
      #  for j in range(1,max_column+1):
              # get particular cell value    
      #        cell_obj=ws.cell(row=i,column=j)
              # print cell value     
      #        print(cell_obj.value,end=' | ')
        # print new line
      #  print('\n')