# turtle_ver_02

from pyamaze import maze,COLOR,agent

m = maze(10,10)
m.CreateMaze(theme=COLOR.light)
a=agent(m, shape = 'arrow', footprints = True)
a.position = (5,4)
a.position = (5,3)
a.position = (5,2)
m.run()