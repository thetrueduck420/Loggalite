# Loggalite
Are YOU looking for a program that allows you to keep logs, like a diary?
A program so simple that its not quite a text editor, but also not quite a blank terminal?
Well look NO MORE!

Loggalite is a tiny dependency-free, AI free, Human-made personal journal written in Python3!
It stores all your entries in a database file inside your home directory (~/.loggalite/logs.db), so that you dont need a whole cluttered up directory of individual text files!

Now, you may notice that loggalite has only 2 options: Entry, and Reading;
At first, this may seem too simple, too tiny and stupid, but this design is intended!
The lack of other options makes loggalite so simple, that even your great great grandma could write her cookie recipie in it!
___
## Installation guide
To install Loggalite, you must first clone the repository using the following command:
```git clone https://github.com/thetrueduck420/Loggalite.git```
Then, change into the Loggalite directory
```cd Loggalite```
Now, for the actual installation!
To install Loggalite, simply run the "install.sh" script like this:
```sudo ./install.sh```
Done! you have now successfully installed Loggalite, you may run it by running the following command:
```loggalite```
___
## User guide
Loggalite has 2 main modes, "entry", and "reading"
in this guide, I will explain how to use them!

### Entry mode:
To enter this mode, open up loggalite (reffer to the installation guide in order to install, and run loggalite)
Then, simply type "entry" into the interface!

You will now be prompted to give your entry a title, this can be anything you want, like this:
```OPTION[: entry
TITLE[: Loggalite tutorial!```

You can now start writing your entry, its that simple!
To save and close your entry, simply type "__END__" into the interface.
Please note that typing "__END__" ANYWHERE in the entry, will save and close it!

### Reading mode:
To enter this mode, open up loggalite again, and type "reading" into the interface
A menu simmilar to this should pop up:
```OPTION[: reading
('2026-09-29_15:02:21', 'test')
('2026-09-29_15:25:16', 'Success!')
('2026-09-29_15:32:17', 'Success 2!')
LOG-DATE[: 
```

You can now simply type in one of the dates (dates are shown on the left), and loggalite will automatically read it out in your terminal!

___
That wasnt so hard, was it?
This is my first "useful" program that ive ever released on github; i hope yall like it
I made this to keep developement logs of my other projects, i didnt need a text editor for something that small, so i built this little thing in a few hours!
I hope it can be as useful to you as it is to me!
- Andrew :3
