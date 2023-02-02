import easygui

path = easygui.fileopenbox()
easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No'))
easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
print(path)