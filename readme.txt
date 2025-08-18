cd "D:\Guvi Projects\cricsheet_project\New folder\scripts"
sqlite3 cricsheet.db
SQLite version 3.xx.x ...
Enter ".help" for usage hints.
sqlite>
SQLite will execute all queries in order.

Results of SELECT queries will be displayed in the console.

If you want a nicer output, you can set the mode before reading:

.mode column
.headers on
.read queries.sql