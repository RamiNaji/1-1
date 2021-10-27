import turtle as trtl
t = trtl.Turtle()
graph = str(input("What is your graph(If y=mx-b please do y=mx+-b): "))
graph = graph.split("+")
print(graph)
print(graph[1])