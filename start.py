import curses


#setting up the screen

screen = curses.initscr()
curses.cbreak()
curses.noecho()
curses.curs_set(0)
curses.start_color()
curses.use_default_colors()

#color pair values for background

curses.init_pair(1,234,234)
curses.init_pair(2,235,235)
curses.init_pair(3,236,236)
curses.init_pair(4,237,237)
curses.init_pair(5,238,238)
curses.init_pair(6,239,239)
curses.init_pair(7,240,240)
curses.init_pair(8,241,241)
curses.init_pair(9,242,242)
curses.init_pair(10,243,243)
curses.init_pair(11,244,244)
curses.init_pair(12,245,245)
curses.init_pair(13,231,231)
curses.init_pair(14,27,27)

# text color pair values

curses.init_pair(15,16,231)
curses.init_pair(16,15,27)

def detect_exit_key():

   detect_key = screen.getch()
   if detect_key == ord("q"):
      curses.endwin()
      quit("")

MSX_LOGO = '''
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████▒░░░░░▒██████▓░░░░░░▓█████████▒░░░░░░░░░░░░░░░░░░░░░░░░░▓█████████▒░░░░░░░░▓████████
███████████████▒░░░░░░░██████▒░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██████▓░░░░░░░░▒██████████
███████████████▒░░░░░░░▒████▓░░░░░░░░█████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒████▒░░░░░░░░▓███████████
██████████████▓░░░░░░░░░▓███▒░░░░░░░░▒██▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒░░░░░░░░█████████████
██████████████▒░░░░░░░░░░██▓░░░░░░░░░░▓█▓▒░░░░░░▓███████████████████▒░░░░░░░░░░░░░░░░▒██████████████
█████████████▒░░░░░░░░░░░▓█▒░░░░░░░░░░▒█▓▒░░░░░░▒▓███████████████████▓░░░░░░░░░░░░░░████████████████
█████████████▒░░░░░░░░░░░▒▓░░░░░░░░░░░░██▒░░░░░░░░░░░░░░░░░▒███████████▒░░░░░░░░░░▒█████████████████
████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▒░░░░░░░░░░░░░░░░░░░██████████▒░░░░░░░░▒██████████████████
████████████▒░░░░░░▒▒░░░░░░░░░░░▒▒░░░░░░████▒░░░░░░░░░░░░░░░░░░▓██████▓░░░░░░░░░░░░█████████████████
███████████▓▒░░░░░▒█▒▒░░░░░░░░░░█▓▒░░░░░▓██████▓▒▒▒▒▒▒▒▒░░░░░░░▒█████▒░░░░░░░░░░░░░░▒███████████████
███████████▒░░░░░░▓██▒░░░░░░░░░▓██▒░░░░░░████████████████▒░░░░░░███▓▒░░░░░░░░░░░░░░░░▒██████████████
██████████▓░░░░░░▒███▓░░░░░░░░░████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▓░░░░░░░░▒██▓░░░░░░░░▒████████████
██████████▒░░░░░░▓████▒░░░░░░░▒████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▒░░░░░░░░▓█████▒░░░░░░░░███████████
█████████▓▒░░░░░▒█████▒░░░░░░▒█████▓▒░░░░░░░░░░░░░░░░░░░░░░░░▒█▓▒░░░░░░░▒████████▒░░░░░░░░▓█████████
█████████▒░░░░░░▓██████▒░░░░░▓██████▒░░░░░░░░░░░░░░░░░░░░░░▓██▒░░░░░░░▒▓███████████▒░░░░░░░▒████████
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████

'''
try:

 if curses.LINES >= 49 and curses.COLS >= 167:

  screen.nodelay(True)

  for n in range(1,15,1):
     detect_exit_key()
     screen.bkgd(" ",curses.color_pair(n))
     curses.napms(100)
     screen.refresh()


  detect_exit_key()
  curses.napms(1000)
  y_pos,x_pos = screen.getmaxyx()[0]//2 + 5 , screen.getmaxyx()[1]//2

  for pos,line in enumerate(MSX_LOGO.splitlines()[::-1],start=y_pos):

    detect_exit_key()
    x_pos-=1
    screen.refresh()
    screen.addstr(y_pos,x_pos,line,curses.color_pair(15))

    curses.napms(100)
    x_pos=screen.getmaxyx()[1]//2 - 50
    y_pos-=1



  detect_exit_key()
  screen.refresh()
  screen.addstr(screen.getmaxyx()[0]//2+5,screen.getmaxyx()[1]//2-11,"VRAM: 128 Kbytes",curses.color_pair(16))
  screen.refresh()

  curses.napms(2000)
  curses.endwin()
  quit("")

 else:

   curses.endwin()
   quit("Screen resolution of {columns}x{lines} is not large enough".format(columns = curses.COLS, lines = curses.LINES))

except curses.error:

    curses.endwin()
    quit("AN error occurred")
