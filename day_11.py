# There are three types of ways to apply CSS in html files
# 1. Inline CSS:- In this case we have to write CSS code in those specific
# HTML tags.
# Examples:-
# <!-- This is Inline CSS --> <h1 style="background-color: greenyellow;">This is
# Gulam</h1>
# 2. Internal Stylesheet:-In this case we have to write CSS code inside the
# style tag.
# Examples:-
# <style>
# p{
# background-color: yellow;
# }
# </style>
# ___________
# 3. External Stylesheet:-In this case we have to create a separate CSS
# file. Write CSS code inside and link this CSS file any HTML files
# Examples:-
# <head>
# <title>Document</title>
# <!-- <link rel="stylesheet" href="./test.css"> -->
# </head>
# ___________
# Flexbox:-
# ➢ Flexbox(Flexible Box layout) is a CSS layout system used to arrange HTML Element
# easily in row or columns
# ➢ Horizontal → Row
# ➢ Vertical→ Column
# ➢ displaye: flex:- it decides content alignment.
# Notes:- whenever we apply display flex direction row wise. ___________
# Basic Syntax:-
# .container {
# display: flex;
# }
# Display: flex is applied to a parent element,its direct children flex items
# ___________
# Flex Container and flex Items:-
# ➢ Flex container:- the parent element on which display:flex is applied is
# called a flex container
# ➢ Flex items:- the direct child element inside the flex container are called
# flex items.
# <div class="container">
# <p>Box1</p>
# <p>Box2</p>
# <p>Box3</p>
# </div>
# /* CSS */
# .container {
# display: flex;
# }
# Here:
# ● .container → Flex Container ● Box 1, Box 2, Box 3 → Flex Items
# ___________
# flex-direction :-
# ➢ It defines the direction in which flex items are placed.
# row
# Default value.
# flex-direction: row;
# Output
# Box 1 → Box 2 → Box 3
# ___________
# row-reverse
# flex-direction: row-reverse;
# Output
# Box 3 → Box 2 → Box 1
# ___________
# column
# flex-direction: column;
# Output
# Box 1
# Box 2
# Box 3
# ___________
# column-reverse
# flex-direction: column-reverse; Output
# Box 3
# Box 2
# Box 1
# ___________
# justify-content:-
# ➢ justify content work X axis wise
# ➢ it will work when flex direction = row
# flex-start
# justify-content:flex-start;
# Items are placed at the beginning.
# flex-end
# justify-content:flex-end;
# Items are placed at the end.
# center
# justify-content:center;
# Items are placed in the center.
# space-between
# justify-content:space-between;
# Equal space is placed between the items.
# space-around justify-content:space-around;
# Space is placed around each item.
# space-evenly
# justify-content:space-evenly;
# Equal space is placed between items and at the edges.
# ___________
# align-items
# ➢ Align item works Y axis wise
# ➢ it will works when flex direction = column