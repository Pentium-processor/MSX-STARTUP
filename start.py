import curses

#setting up the screen

screen = curses.initscr()
curses.cbreak()
curses.noecho()
curses.curs_set(0)
curses.start_color()
curses.use_default_colors()


def exit_funct(msg = ""):

  curses.endwin()
  quit(msg)


if curses.COLORS == 8:

   screen.refresh()
   exit_funct("\33[31mCannot execute following program due to your machine not supporting 256 colors\33[30m")

#color pair values for background


color_pairs = [
    [0,0],
    [234, 234],
    [235, 235],
    [236, 236],
    [237, 237],
    [238, 238],
    [239, 239],
    [240, 240],
    [241, 241],
    [242, 242],
    [243, 243],
    [244, 244],
    [245, 245],
    [231, 231],
    [27, 27]
]

# text color pair values

curses.init_pair(16,16,231)
curses.init_pair(17,15,27)


def detect_exit_key():

   detect_key = screen.getch()
   if detect_key == ord("q"):
      exit_funct("Program terminated due to the q exit key being pressed")
   else:
      pass



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


if curses.LINES >= 49 and curses.COLS >=167:


  screen.nodelay(True)


  for n in range(0,15,1):

     detect_exit_key()
     curses.init_pair(n,color_pairs[n][0],color_pairs[n][1])
     screen.bkgd(" ",curses.color_pair(n))
     curses.napms(100)


     screen.refresh()


  color_pairs.clear()

  detect_exit_key()
  curses.napms(1000)
  y_pos,x_pos = screen.getmaxyx()[0]//2 , screen.getmaxyx()[1]//2


  for pos,line in enumerate(MSX_LOGO.splitlines()[::-1],start=y_pos):

    detect_exit_key()
    x_pos-=1
    screen.refresh()
    screen.addstr(y_pos,x_pos,line,curses.color_pair(16))
    screen.refresh()


    curses.napms(100)
    x_pos=screen.getmaxyx()[1]//2 - 50
    y_pos-=1


  screen.refresh()
  screen.addstr(screen.getmaxyx()[0]//2,screen.getmaxyx()[1]//2 - 11,"VRAM: 128 Kbytes",curses.color_pair(17))
  screen.refresh()

  curses.napms(2000)

  exit_funct()

else:

   exit_funct("\33[31mScreen resolution of {columns}x{lines} is not large enough\33[30m".format(columns = curses.COLS, lines = curses.LINES))
