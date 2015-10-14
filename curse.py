import curses
import praw

#Global Vars probably bad design
first = 2
between = 2    
limit = 10
width = 80
r = praw.Reddit(user_agent='redditty')
submissions_gen = r.get_subreddit('games').get_top(limit=limit)   
stdscr = curses.initscr()
subs = []

def main():
    curses.cbreak()
    curses.start_color()
    curses.noecho()
    stdscr.keypad(1)
    populate_screen()
    loc = first
    change_highlight(loc, -1)
    while(True):
	c = stdscr.getch()
	if c == ord('j') and loc <= limit*between -2:
	    prev = loc
	    loc=loc+between
	    change_highlight(loc, prev)
	if c == ord('k') and loc >= first:
	    prev = loc
	    loc=loc-between
	    change_highlight(loc, prev)
    #curses.endwin()

#Pass submissions in?
def populate_screen():
    i=first
    for submission in submissions_gen:
	title = submission.title
	subs.append(submission)
	title = title[:width]
	stdscr.addstr(i,4,title)
	i= i+between
    stdscr.refresh()

#Pass subs?   
def change_highlight(location, prev):
    if prev != -1:
	title = subs[prev/2-1].title[:width]
	stdscr.addstr(prev, 4, title)
    title = subs[location/2 -1].title[:width]
    stdscr.addstr(location, 4, title, curses.A_UNDERLINE)
    stdscr.refresh()
    curses.flash()

main()
