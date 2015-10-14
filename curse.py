import curses
import praw

def main():
    first = 2
    between = 2    
    curses.cbreak()
    curses.start_color()
    curses.noecho()
    stdscr.keypad(1)
    i = first
    for submission in submissions:
	title = submission.title
	title = title[:80]
	stdscr.addstr(i,4,title)
	i= i+between
    stdscr.refresh()
    loc = first
    chhilite(loc)
    while(True):
	c = stdscr.getch()
	if c == ord('j') and loc <= limit*between -2:
	    loc=loc+between
	    chhilite(loc)
	if c == ord('k') and loc >= first:
	    loc=loc-between
	    chhilite(loc)
    #curses.endwin()
   
def chhilite(location):
    #title = submissions[location]
    stdscr.addstr(location, 4, 'here i am ', curses.A_UNDERLINE)
    stdscr.refresh()
    curses.flash()

limit = 10;
r = praw.Reddit(user_agent='reddpyxx')
submissions = r.get_subreddit('games').get_top(limit=limit)
    
stdscr = curses.initscr()

main()
