free_cell = [1,2,3,4,5,6,7,8,9]
choice = [(1,'-'),(2,'-'),(3,'-'),(4,'-'),(5,'-'),(6,'-'),(7,'-'),(8,'-'),(9,'-')]
t = 'X' # assisgnig the first user 
while len(free_cell) > 0:
    cell_inp = input ('Please, select cell for {}\n'.format(t))
    try:
        sel_cell = int(cell_inp)
    except:
        print('Please, select number of wanted free cell in range 1-9')
        continue
    if sel_cell > 9 or sel_cell < 1 or sel_cell not in free_cell:
        print('Your number is out of range 1-9 or was choosen before')
        continue
    free_cell.remove(sel_cell) # to have the list of available positions
    x = choice.pop(sel_cell-1)
    x = (sel_cell,t)
    choice.append(x) # updating list with selected cell value and value 'X' or 'O'
    choice.sort()
    f = list()
    for num, val in choice: # creating new list to fill-in cells with 'X' or 'O', if selected. Or num of cell - if not
        if val == '-':
            f.append(num)
        else:
            f.append(val)
    print ("-------------")
    for i in range(3):
        print( "|", f[0+i*3], "|", f[1+i*3], "|", f[2+i*3], "|")
        print('-------------')
    if len(free_cell) < 5 : # win is possible when at least 5 moves are done
        if (f[0] == f[1] == f[2] or f[3] == f[4] == f[5] or f[6] == f[7] == f[8] or  
            f[0] == f[3] == f[6] or f[1] == f[4] == f[7] or f[2] == f[5] == f[8] or
            f[0] == f[4] == f[8] or f[2] == f[4] == f[6]):  # checking the win
            print('Victory!!! Player "{}" WON'.format(t))
            exit()
        elif len(free_cell) < 1:
            print('And we have a DRAW!!!')
            exit()
    if t == 'X': # changing the turn of move
        t = 'O'
    else:
        t = 'X'
