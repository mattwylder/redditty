import curses
import praw

#Global Vars probably bad design
first = 2
between = 2    
limit = 10
width = 80
pad = 4
r = praw.Reddit(user_agent='redditty')
submissions_gen = r.get_subreddit('games').get_top(limit=limit)   
begin_y=0;begin_x=0
height=24;width=88
stdscr = curses.initscr() 
mainscr = curses.newwin(height,width,begin_y,begin_x)
begin_y=24;begin_x=0
height=2;width=88
smallscr = curses.newwin(height,width,begin_y,begin_x)
subs = []

def main():
    setup()
    populate_screen()
    loc = first
    change_highlight(loc)
    while(True):
	c = stdscr.getch()
	if c == ord('j') and loc <= limit*between -2:
	    prev = loc
	    loc=loc+between
	    change_highlight(loc, prev)
	if c == ord('k') and loc > first:
	    prev = loc
	    loc=loc-between
	    change_highlight(loc, prev)
    #curses.endwin()

def setup():
    curses.cbreak()
    curses.start_color()
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(1) 

#Pass submissions in?
def populate_screen():
    i=first
    for submission in submissions_gen:
	title = submission.title
	subs.append(submission)
	title = title[:width]
	mainscr.addstr(i,pad,title)
	i= i+between
    stdscr.refresh()
    smallscr.addstr(0,0,'hello')
    smallscr.refresh()

#Pass subs?   
def change_highlight(location, prev=-1):
    if prev != -1:
	title = subs[prev/2-1].title[:width]
	stdscr.addstr(prev, pad, title)
    title = subs[location/2 -1].title[:width]
    mainscr.addstr(location, pad, title, curses.A_UNDERLINE)
    mainscr.refresh()
    curses.flash()

main()
