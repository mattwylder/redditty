import curses
import praw

#Global Vars probably bad design
first = 2
between = 2    
limit = 10;
r = praw.Reddit(user_agent='redditty')
submissions_gen = r.get_subreddit('games').get_top(limit=limit)   
stdscr = curses.initscr()
subs = []

def main():
    curses.cbreak()
    curses.start_color()
    curses.noecho()
    stdscr.keypad(1)
    i = first
    populate_screen()
    loc = first
    change_highlight(loc)
    while(True):
	c = stdscr.getch()
	if c == ord('j') and loc <= limit*between -2:
	    loc=loc+between
	    chhilite(loc)
	if c == ord('k') and loc >= first:
	    loc=loc-between
	    change_highlight(loc)
    #curses.endwin()

#Pass submissions in?
def populate_screen():
    i=first
    for submission in submissions_gen:
	title = submission.title
	subs.append(submission)
	title = title[:80]
	stdscr.addstr(i,4,title)
	i= i+between
    stdscr.refresh()

#Pass subs?   
def change_highlight(location):
    #title = submissions[location]
    stdscr.addstr(location, 4, subs[location/2 - 1].title, curses.A_UNDERLINE)
    stdscr.refresh()
    curses.flash()

main()
