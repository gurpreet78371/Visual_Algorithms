import pygame
from pygame.locals import *
from tkinter import *
import tkinter.messagebox
import webbrowser
import math
from Button import button, node

blue = (158, 198, 229)
dark_blue = (0, 0, 255)
maroon = (130, 0, 0)
navy_blue = (16, 24, 96)
node_color = (86, 161, 150)
node_color_hover = (255, 161, 0)
background_color = (240, 247, 249)
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
navy = (17, 53, 108)
weight = None
block_size = 10
display_width = 960
display_height = 500
button_ht = 3 * block_size
button_gap = 2 * block_size
red = (255, 0, 0)
mode = 'd'
edges = 5
start_node = 0

display = pygame.display.set_mode((display_width, display_height), 0, 0)
pygame.display.set_caption("graph algorithms")
font0 = pygame.font.SysFont('Century Gothic', 15)
font = pygame.font.SysFont('Century Gothic', 25)
font1 = pygame.font.SysFont('Century Gothic', 45)
font2 = pygame.font.SysFont('Century Gothic', 75)
clock = pygame.time.Clock()
running = True
redrawwindow_color = (77, 110, 129)


def onsubmit(window, startBox):
    global weight
    st = startBox.get()
    try:
        weight = int(st)
        window.quit()
        window.destroy()
    except:
        tkinter.messagebox.showinfo("Error", "weight can only be any numerical value !")


def selectNode(window, startBox, length):
    global start_node
    st = startBox.get()
    try:
        if int(st) >= length:
            error = int("hello")
        start_node = int(st)
        window.quit()
        window.destroy()
    except:
        tkinter.messagebox.showinfo("Error", "Starting node number is greater than expected !")


def message_to_screen(display, message, color, x, y, fontsize):
    if fontsize == "large":
        display_text = font.render(message, True, color)
    if fontsize == "small":
        display_text = font1.render(message, True, color)
    if fontsize == "extralarge":
        display_text = font2.render(message, True, color)
    display.blit(display_text, [x, y])


image = pygame.image.load('new.png')
blur = pygame.image.load('new.png')
back = pygame.image.load('download.png')
logo = pygame.image.load('logo.png')
intro_image = pygame.image.load('intro.jpg')
buttons = [button(blue, 5, 110, 300, 50, 60, 'Kruskal'),
           button(blue, 5, 170, 300, 50, 60, 'Prim'),
           button(blue, 5, 230, 300, 50, 60, 'BFS'),
           button(blue, 5, 290, 300, 50, 60, 'DFS'),
           button(blue, 5, 350, 300, 50, 60, 'Comparison')
           ]
button7 = button(redrawwindow_color, 335, 290, 300, 50, 60, 'Select')
button8 = button(redrawwindow_color, 335, 340, 300, 50, 60, 'Default Values')
button9 = button(red, 5, 5, 100, 50, 60, 'Back')
button10 = button(blue, 5, 410, 300, 50, 60, 'About Project')
button11 = button(redrawwindow_color, 335, 250, 300, 50, 60, 'Start')
button12 = button(redrawwindow_color, 335, 390, 300, 50, 60, 'Introduction')
button13 = button(redrawwindow_color, 5, display_height + 20, 250, 50, 30, "Prim's v/s Kruskal's")
button14 = button(redrawwindow_color, display_width - 270, display_height + 20, 250, 50, 30, 'BFS v/s DFS')

msg_k = ""
msg_p = ""
msg2 = ""
def Kruskal(screen, choice, node_list, edgelist):
    screen.fill(background_color)
    edgelist.sort(key=lambda edge: edge.weight)
    no = 0
    parent = [-1] * len(node_list)
    mst_list = list()
    mst_node = list()
    stage = False
    global msg2
    msg2 = ""
    while True:
        screen.fill(background_color)
        msg = "Press space to continue and backspace for previous step"
        message = font0.render(msg, True, red)
        screen.blit(message, ((display_width // 2 - message.get_width() / 2), display_height + 36))
        for event in pygame.event.get():
            global cycle_flag
            pos1 = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if button9.isOver(pos1):
                    button9.change((155, 0, 0))
                else:
                    button9.change(redrawwindow_color)
            if event.type == MOUSEBUTTONDOWN:
                if button9.isOver(pos1):
                    return
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if len([i for i in mst_list if i[1] == 0]) == len(node_list) - 1:
                        msg2 = "COMPLETED"
                        break
                    if stage:
                        stage = False
                        x = edgelist[no].nodes_no[0]
                        while parent[x] >= 0:
                            x = parent[x]
                        y = edgelist[no].nodes_no[1]
                        while parent[y] >= 0:
                            y = parent[y]
                        if x == y:
                            mst_list.append((edgelist[no], 1))
                            mst_node.append(node_list[edgelist[no].nodes_no[0]])
                            mst_node.append(node_list[edgelist[no].nodes_no[1]])
                            msg2 = "CYCLE"
                        else:
                            parent[x] = y
                            edgelist[no].color = dark_blue
                            mst_node.append(node_list[edgelist[no].nodes_no[0]])
                            mst_node.append(node_list[edgelist[no].nodes_no[1]])
                            node_list[edgelist[no].nodes_no[0]].change_color(red)
                            node_list[edgelist[no].nodes_no[1]].change_color(red)
                            mst_list.append((edgelist[no], 0))
                            msg2 = ""
                        no = no + 1
                        for i in edgelist:
                            if i not in mst_list:
                                i.color = maroon
                    else:
                        stage = True
                        for i in edgelist:
                            if i not in (j[0] for j in mst_list):
                                i.color = (77, 255, 77)
                        msg2 = ''
                if event.key == K_BACKSPACE:
                    if len(mst_list) <= 0:
                        stage = False
                        for i in edgelist:
                            if i not in (j[0] for j in mst_list):
                                i.color = maroon
                        msg2 = "EMPTY"
                        break
                    if not stage:
                        stage = True
                        no = no - 1
                        edgelist[no].color = maroon
                        mst_node.remove(node_list[edgelist[no].nodes_no[0]])
                        mst_node.remove(node_list[edgelist[no].nodes_no[1]])
                        if mst_node.count(node_list[edgelist[no].nodes_no[0]]) <= 0:
                            node_list[edgelist[no].nodes_no[0]].change_color(node_color)
                        if mst_node.count(node_list[edgelist[no].nodes_no[1]]) <= 0:
                            node_list[edgelist[no].nodes_no[1]].change_color(node_color)
                        y = edgelist[no].nodes_no[1]
                        if mst_list.pop()[1] == 0:
                            while parent[y] >= 0:
                                print("reverse")
                                y = parent[y]
                            x = edgelist[no].nodes_no[0]
                            while parent[x] != y:
                                x = parent[x]
                            parent[x] = -1
                        else:
                            print("cycle reverse")
                        for i in edgelist:
                            if i not in (j[0] for j in mst_list):
                                i.color = (77, 255, 77)
                        msg2 = ""
                    else:
                        stage = False
                        for i in edgelist:
                            if i not in (j[0] for j in mst_list):
                                i.color = maroon
                        msg2 = ""
        for i in edgelist:
            i.width = 3
            for j in mst_list:
                if j[1] == 0:
                    j[0].color = navy
                    j[0].width = 7
            i.draw_edge(screen)
        button9.draw(screen)
        wht = "WEIGHT: " + str(sum(i[0].weight for i in mst_list if i[1] == 0))
        wht = font0.render(wht, True, red)
        screen.blit(wht, (5, display_height - wht.get_height() - 5))
        message2 = font0.render(msg2, True, red)
        screen.blit(message2, ((display_width - message2.get_width() - 5), display_height - wht.get_height() - 5))
        for i in node_list:
            i.draw(screen)
        pygame.display.update()


def Prim(screen, choice, node_list, edgelist):
    no_of_nodes = len(node_list)
    adjancency_list = dict((i, []) for i in range(len(nodelist)))
    for i in edge_list:
        adjancency_list[i.nodes_no[0]].append(i)
        adjancency_list[i.nodes_no[1]].append(i)
    screen.fill(background_color)
    node_list[0].color = red
    mst_nodes = [node_list[0], ]
    mst_edges = list()
    flag = True
    global msg2
    msg2 = ""
    while True:
        complete_flag = False
        screen.fill(background_color)
        msg = "press space to continue and backspace for previous step"
        message = font0.render(msg, True, red)
        screen.blit(message, ((display_width // 2 - message.get_width() / 2), display_height + 36))
        for event in pygame.event.get():
            pos1 = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEMOTION:
                if button9.isOver(pos1):
                    button9.change((155, 0, 0))
                else:
                    button9.change(redrawwindow_color)
            if event.type == MOUSEBUTTONDOWN:
                if button9.isOver(pos1):
                    return
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if len(mst_nodes) == no_of_nodes:
                        flag = True
                        mst_edges[-1][0].color = navy
                        mst_edges[-1][0].width = 7
                        for j in mst_nodes:
                             j.change_color(red)
                        for i in edgelist:
                            if i not in (k[0] for k in mst_edges):
                                i.color = maroon
                        msg2 = "Completed"
                        break
                    min_edge_weight = sys.maxsize
                    min_edge = edge(0, 0, 0, 0)
                    if flag:
                        flag = False
                        for i in mst_nodes:
                            for j in adjancency_list[i.num]:
                                if j not in (k[0] for k in mst_edges):
                                    j.width = 3
                                    j.color = (77, 255, 77)
                                    if j.weight < min_edge_weight:
                                        min_edge_weight = j.weight
                                        min_edge = j
                        cylcle1 = False
                        cylcle2 = False
                        for i in mst_nodes:
                            if i.num == min_edge.nodes_no[0]:
                                cylcle1 = True
                            if i.num == min_edge.nodes_no[1]:
                                cylcle2 = True
                        if cylcle1 and cylcle2:
                            mst_edges.append((min_edge, 1))
                            msg2 = "CYCLE FOUND"
                        elif cylcle1:
                            mst_nodes.append(node_list[min_edge.nodes_no[1]])
                            mst_edges.append((min_edge, 0))
                            msg2 = ""
                        else:
                            mst_nodes.append(node_list[min_edge.nodes_no[0]])
                            mst_edges.append((min_edge, 0))
                            msg2 = ""
                    else:
                        flag = True
                        if mst_edges[-1][1] == 0:
                            mst_edges[-1][0].color = navy
                            mst_edges[-1][0].width = 7
                        else:
                            mst_edges[-1][0].width = 3
                            mst_edges[-1][0].color = maroon
                        for i in node_list:
                            if i in mst_nodes:
                                i.change_color(red)
                            else:
                                i.change_color(node_color)
                        for i in edgelist:
                            if i not in (k[0] for k in mst_edges):
                                i.color = maroon
                        msg2 = ""
                if event.key == K_BACKSPACE:
                    if len(mst_edges) <= 0:
                        flag = True
                        msg2 = "EMPTY"
                        break
                    if not flag:
                        flag = True
                        temp_edge = mst_edges.pop()
                        temp_edge[0].width = 3
                        temp_edge[0].color = maroon
                        if temp_edge[1] == 1:
                            print("cycle")
                        else:
                            mst_nodes[-1].change_color(node_color)
                            mst_nodes.pop()
                        for i in edgelist:
                            if i not in (k[0] for k in mst_edges):
                                i.color = maroon
                        msg2 = ""
                    else:
                        flag = False
                        temp = mst_edges.pop()
                        temp2 = mst_nodes.pop()
                        temp2.change_color(node_color)
                        for i in mst_nodes:
                            for j in adjancency_list[i.num]:
                                if j not in (k[0] for k in mst_edges):
                                    j.width = 3
                                    j.color = (77, 255, 77)
                        mst_edges.append(temp)
                        mst_nodes.append(temp2)
                        mst_nodes[-1].change_color(red)
                        msg2 = ""
        for i in edgelist:
            i.draw_edge(screen)
        for i in node_list:
            i.draw(screen)
        button9.draw(screen)
        wht = "WEIGHT: " + str(sum(i[0].weight for i in mst_edges if i[1] == 0))
        wht = font0.render(wht, True, red)
        screen.blit(wht, (5, display_height - wht.get_height() - 5))
        message2 = font0.render(msg2, True, red)
        screen.blit(message2, ((display_width - message2.get_width() - 5), display_height - wht.get_height() - 5))
        if complete_flag:
            break
        pygame.display.update()


def BFS(screen, choice, node_list, edgelist):
    global start_node
    adjancency_list = dict((i, []) for i in range(len(node_list)))
    for i in edgelist:
        adjancency_list[i.nodes_no[0]].append(node_list[i.nodes_no[1]])
        adjancency_list[i.nodes_no[1]].append(node_list[i.nodes_no[0]])
    screen.fill(background_color)
    button9.draw(screen)
    node_list.sort(key=lambda node: node.num)
    queue = list()
    visited = list()
    window = Tk()
    label = Label(window, text='Start Node ')
    startBox = Entry(window)
    submit = Button(window, text='Submit', command=lambda: selectNode(window, startBox, len(node_list)))
    submit.grid(columnspan=2, row=3)
    startBox.grid(row=0, column=1, pady=3)
    label.grid(row=0, pady=3)
    window.attributes("-topmost", True)
    startBox.focus()
    mainloop()
    for node in node_list:
        if node.num == start_node:
            queue.append(node)
    next_nodes = list()
    while len(visited) != len(node_list):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        current_node = queue[0]
        visited.append(current_node)
        for edge in edgelist:
            if current_node.x == edge.start[0] and current_node.y == edge.start[1]:
                for node in node_list:
                    if node not in visited:
                        if node.x == edge.end[0] and node.y == edge.end[1] and node not in next_nodes:
                            next_nodes.append(node)
            elif current_node.x == edge.end[0] and current_node.y == edge.end[1]:
                for node in node_list:
                    if node not in visited:
                        if node.x == edge.start[0] and node.y == edge.start[1] and node not in next_nodes:
                            next_nodes.append(node)
        next_nodes.sort(key=lambda node: node.num)
        for node in next_nodes:
            if node not in queue:
                queue.append(node)
        next_nodes = list()
        queue.remove(current_node)
    for node in queue:
        if node not in visited:
            visited.append(node)
    added = list()
    flag = False
    running = True
    while running:
        screen.fill(background_color)
        button9.draw(screen)
        msg = "press space to continue and backspace for previous step"
        message = font0.render(msg, True, red)
        screen.blit(message, ((display_width // 2 - message.get_width() / 2), display_height + 36))
        for i in edgelist:
            i.draw_edge(screen)
        for i in node_list:
            i.color = node_color
            i.draw(screen, node_color)
        i = display_width // 2 - 30
        for node in added:
            node.color = red
            node.draw(screen)
            n = str(node.num)
            message_to_screen(screen, n, navy_blue, i, display_height + 10, "large")
            i += 20
        pygame.display.update()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if len(added) == len(node_list):
                        running = False
                        message_to_screen(screen, "COMPLETED", red, 5, display_height, "large")
                        break
                    if visited[0] not in added:
                        added.append(visited[0])
                        if max == visited[0].num:
                            min1 = min(next_nodes[0].num)
                        next_nodes = list()
                    del visited[0]
            if event.type == MOUSEBUTTONDOWN:
                if button9.isOver(pos):
                    return
            if event.type == MOUSEMOTION:
                if button9.isOver(pos):
                    button9.color = (155,0,0)
                else:
                    button9.color = redrawwindow_color
        pygame.display.update()


def DFS(screen, choice, node_list, edgelist):
    global start_node
    screen.fill(background_color)
    adjancency_list = dict((i, []) for i in range(len(node_list)))
    for i in edgelist:
        adjancency_list[i.nodes_no[0]].append(node_list[i.nodes_no[1]])
        adjancency_list[i.nodes_no[1]].append(node_list[i.nodes_no[0]])
    node_list.sort(key=lambda node: node.num)
    queue = list()
    visited = list()
    window = Tk()
    label = Label(window, text='Start Node ')
    startBox = Entry(window)
    submit = Button(window, text='Submit', command=lambda: selectNode(window, startBox, len(node_list)))
    submit.grid(columnspan=2, row=3)
    startBox.grid(row=0, column=1, pady=3)
    label.grid(row=0, pady=3)
    window.attributes("-topmost", True)
    startBox.focus()
    mainloop()
    screen.fill(background_color)
    node_list.sort(key=lambda node: node.num)
    queue = list()
    visited = list()
    current_node = node_list[start_node]
    next_nodes = list()
    while len(visited) != len(node_list):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        visited.append(current_node)
        while len(visited) != len(node_list):
            min_node = len(node_list) + 1
            for i in adjancency_list[current_node.num]:
                if i not in visited:
                    if (min_node > i.num):
                        min_node = i.num
            if min_node == len(node_list) + 1:
                j = visited.index(current_node) - 1
                current_node = visited[j]
            else:
                visited.append(node_list[min_node])
                current_node = node_list[min_node]
    added = list()
    flag = 0
    next_nodes = list()
    running = True
    while running:
        screen.fill(background_color)
        button9.draw(screen)
        msg = "press space to continue and backspace for previous step"
        message = font0.render(msg, True, red)
        screen.blit(message, ((display_width // 2 - message.get_width() / 2), display_height + 36))
        for i in edgelist:
            i.draw_edge(screen)
        for i in node_list:
            i.color = node_color
            i.draw(screen, node_color)
        i = display_width // 2 - 30
        for node in added:
            node.color = red
            node.draw(screen)
            n = str(node.num)
            message_to_screen(screen, n, navy_blue, i, display_height + 10, "large")
            i += 20
        for node in next_nodes:
            node.color = (77, 255, 77)
            node.draw(screen)
        pygame.display.update()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if len(added) == len(node_list):
                        running = False
                        message_to_screen(screen, "COMPLETED", red, 5, display_height, "large")
                        break
                    if flag == 0:
                        if visited[0] not in added:
                            added.append(visited[0])
                            next_nodes = list()
                        del visited[0]
                    if flag == 1 and len(added) != 0:
                        for edge in edgelist:
                            if added[-1].x == edge.start[0] and added[-1].y == edge.start[1]:
                                for node in node_list:
                                    if node.x == edge.end[0] and node.y == edge.end[
                                        1] and node not in next_nodes and node not in added:
                                        next_nodes.append(node)
                            elif added[-1].x == edge.end[0] and added[-1].y == edge.end[1]:
                                for node in node_list:
                                    if node.x == edge.start[0] and node.y == edge.start[
                                        1] and node not in next_nodes and node not in added:
                                        next_nodes.append(node)
                    flag ^= 1
                if event.key == K_BACKSPACE:
                    if (len(added) != 0):
                        visited.insert(0, added.pop())
            if event.type == MOUSEBUTTONDOWN:
                if button9.isOver(pos):
                    return
            if event.type == MOUSEMOTION:
                if button9.isOver(pos):
                    button9.color = (155,0,0)
                else:
                    button9.color = redrawwindow_color
        pygame.display.update()




def Comparison(ch1, ch2):
    no = edges
    global running
    running = True
    node_size = 20
    width = 1200
    height = 600
    screen = pygame.display.set_mode((width, height), 0, 0)
    screen.fill(white)
    msg = "press space to continue and backspace for previous step"
    message = font0.render(msg, True, red)
    screen.blit(message, ((width // 2 - message.get_width() / 2), height - 22))
    pygame.draw.line(display, maroon, (int(width / 2), 2), (int(width / 2), height - 22), 3)
    message_to_screen(screen, ch1, navy_blue, 15, 7, "large")
    message_to_screen(screen, ch2, navy_blue, 700, 7, "large")

    global nodelist1, nodelist2, edge_list1, edge_list2
    nodelist1 = list()
    nodelist2 = list()

    edge_list1 = list()
    edge_list2 = list()

    global edge_list
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        for j in range(2):
            radius = min(int(width / 4.17), int(height / 1.90)) - node_size - 10
            theta = 0
            for i in range(no):
                if j == 0:
                    x = int(radius * (math.cos(theta)) + width / 4.17)
                    y = int(height / 1.90 + radius * (math.sin(theta)))

                    nodelist1.append(node(node_color, i, x, y, node_size, str(i)))
                    nodelist1[-1].draw(screen, node_color)


                elif j == 1:
                    x = int(radius * (math.cos(theta)) + width / 4) + width // 2
                    y = int(height / 1.90 + radius * (math.sin(theta)))

                    nodelist2.append(node(node_color, i, x, y, node_size, str(i)))
                    nodelist2[-1].draw(screen, node_color)
                theta += (2 * 3.14) / (no)

        for j in range(2):
            for i in range(len(edge_list)):
                if j == 0:
                    s = edge_list[i].nodes_no[0]
                    e = edge_list[i].nodes_no[1]

                    edge_list1.append(edge((nodelist1[s].x, nodelist1[s].y), (nodelist1[e].x, nodelist1[e].y),
                                           edge_list[i].weight, edge_list[i].nodes_no))

                    edge_list1[-1].draw_edge(screen)
                elif j == 1:
                    s = edge_list[i].nodes_no[0]
                    e = edge_list[i].nodes_no[1]

                    edge_list2.append(edge((nodelist2[s].x, nodelist2[s].y), (nodelist2[e].x, nodelist2[e].y),
                                           edge_list[i].weight, edge_list[i].nodes_no))

                    edge_list2[-1].draw_edge(screen)

        for j in range(2):
            for i in range(no):
                if j == 0:
                    nodelist1[i].draw(screen, node_color)
                elif j == 1:
                    nodelist2[i].draw(screen, node_color)
        if ch1 == "Prim's":
            comp_prims()
            screen.fill(background_color)
            pygame.display.set_mode((display_width, display_height), 0, 0)
            return
        else:
            comp_fs()
            screen.fill(background_color)
            pygame.display.set_mode((display_width, display_height), 0, 0)
            return
        pygame.display.update()


def comp_prims():
    node_size = 20
    width = 1200
    height = 600
    screen = pygame.display.set_mode((width, height), 0, 0)
    screen.fill(background_color)
    msg = "Press SPACE to continue and BACKSPACE for previous step"
    message = font0.render(msg, True, red)
    screen.blit(message, ((width // 2 - message.get_width() / 2), height - 22))
    pygame.draw.line(display, maroon, (int(width / 2), 2), (int(width / 2), height - 22), 3)
    message_to_screen(screen, "KRUSKAL'S", navy_blue, 7, 58, "large")
    message_to_screen(screen, "PRIM'S", navy_blue, 610, 58, "large")

    # kruskals
    global edge_list1, nodelist1
    edge_list1.sort(key=lambda edge: edge.weight)
    no1 = 0
    parent1 = [-1] * len(nodelist1)
    mst_list1 = list()
    mst_node1 = list()
    stage1 = False
    global msg_k
    msg_k = ""

    # prims
    global edge_list2, nodelist2
    no_of_nodes2 = len(nodelist2)
    adjancency_list2 = dict((i, []) for i in range(len(nodelist2)))
    for i in edge_list2:
        adjancency_list2[i.nodes_no[0]].append(i)
        adjancency_list2[i.nodes_no[1]].append(i)
    # screen.fill(background_color)
    nodelist2[0].color = red
    mst_nodes2 = [nodelist2[0], ]
    mst_edges2 = list()
    flag2 = True
    global msg_p
    msg_p = ""

    while True:
        screen.fill(background_color)
        msg = "Press SPACE to continue and BACKSPACE for previous step"
        message = font0.render(msg, True, red)
        screen.blit(message, ((width // 2 - message.get_width() / 2), height - 22))
        pygame.draw.line(display, maroon, (int(width / 2), 2), (int(width / 2), height - 22), 3)
        message_to_screen(screen, "KRUSKAL'S", navy_blue, 7, 58, "large")
        message_to_screen(screen, "PRIM'S", navy_blue, 610, 58, "large")
        for event in pygame.event.get():
            pos1 = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if button9.isOver(pos1):
                    button9.change((155, 0, 0))
                else:
                    button9.change(redrawwindow_color)
            if event.type == MOUSEBUTTONDOWN:
                if button9.isOver(pos1):
                    return

            if event.type == KEYDOWN:
                # kruskals
                if event.key == K_SPACE:
                    if len([i for i in mst_list1 if i[1] == 0]) == len(nodelist1) - 1:
                        msg_k = "COMPLETED"
                    elif stage1:
                        stage1 = False
                        x = edge_list1[no1].nodes_no[0]
                        while parent1[x] >= 0:
                            x = parent1[x]
                        y = edge_list1[no1].nodes_no[1]
                        while parent1[y] >= 0:
                            y = parent1[y]
                        if x == y:
                            mst_list1.append((edge_list1[no1], 1))
                            mst_node1.append(nodelist1[edge_list1[no1].nodes_no[0]])
                            mst_node1.append(nodelist1[edge_list1[no1].nodes_no[1]])
                            msg_k = "CYCLE"
                        else:
                            parent1[x] = y
                            edge_list1[no1].color = navy
                            edge_list1[no1].width = 7
                            mst_node1.append(nodelist1[edge_list1[no1].nodes_no[0]])
                            mst_node1.append(nodelist1[edge_list1[no1].nodes_no[1]])
                            nodelist1[edge_list1[no1].nodes_no[0]].change_color(red)
                            nodelist1[edge_list1[no1].nodes_no[1]].change_color(red)
                            mst_list1.append((edge_list1[no1], 0))
                            msg_k = ""
                        no1 = no1 + 1
                        for i in edge_list1:
                            if i not in mst_list1:
                                i.color = maroon
                    else:
                        stage1 = True
                        for i in edge_list1:
                            if i not in (j[0] for j in mst_list1):
                                i.color = (77, 255, 77)
                        msg_k = ''

                    # prims
                    if len(mst_nodes2) == no_of_nodes2:
                        flag2 = True
                        mst_edges2[-1][0].color = navy

                        # mst_nodes2[-1].change_color(navy)
                        # for i in edge_list2:
                        #     if i not in (k[0] for k in mst_edges2):
                        #         i.color = blue
                        mst_edges2[-1][0].width = 7
                        for j in mst_nodes2:
                             j.change_color(red)
                        for i in edge_list2:
                            if i not in (k[0] for k in mst_edges2):
                                i.color = maroon
                        msg_p = "COMPLETED"
                        break
                    min_edge_weight = sys.maxsize
                    min_edge = edge(0, 0, 0, 0)
                    if flag2:
                        flag2 = False
                        for i in mst_nodes2:
                            for j in adjancency_list2[i.num]:
                                if j not in (k[0] for k in mst_edges2):
                                    j.width = 3
                                    j.color = (77, 255, 77)
                                    if j.weight < min_edge_weight:
                                        min_edge_weight = j.weight
                                        min_edge = j
                        cycle1 = False
                        cycle2 = False
                        for i in mst_nodes2:
                            if i.num == min_edge.nodes_no[0]:
                                cycle1 = True
                            if i.num == min_edge.nodes_no[1]:
                                cycle2 = True
                        if cycle1 and cycle2:
                            mst_edges2.append((min_edge, 1))
                            msg_p = "CYCLE FOUND"
                        elif cycle1:
                            mst_nodes2.append(nodelist2[min_edge.nodes_no[1]])
                            mst_edges2.append((min_edge, 0))
                            msg_p = ""
                        else:
                            mst_nodes2.append(nodelist2[min_edge.nodes_no[0]])
                            mst_edges2.append((min_edge, 0))
                            msg_p = ""
                    else:
                        flag2 = True
                        if mst_edges2[-1][1] == 0:
                            mst_edges2[-1][0].color = navy
                            mst_edges2[-1][0].width = 7
                        else:
                            mst_edges2[-1][0].width = 3
                            mst_edges2[-1][0].color = maroon
                        for i in nodelist2:
                            if i in mst_nodes2:
                                i.change_color(red)
                            else:
                                i.change_color(node_color)
                        for i in edge_list2:
                            if i not in (k[0] for k in mst_edges2):
                                i.color = maroon
                        msg_p = ""

                if event.key == K_BACKSPACE:
                    if len(mst_list1) <= 0:
                        msg_k = "EMPTY"
                        stage1 = False
                        for i in edge_list1:
                            if i not in (j[0] for j in mst_list1):
                                i.color = maroon
                    elif not stage1:
                        stage1 = True
                        no1 = no1 - 1
                        edge_list1[no1].color = maroon
                        mst_node1.remove(nodelist1[edge_list1[no1].nodes_no[0]])
                        mst_node1.remove(nodelist1[edge_list1[no1].nodes_no[1]])
                        if mst_node1.count(nodelist1[edge_list1[no1].nodes_no[0]]) <= 0:
                            nodelist1[edge_list1[no1].nodes_no[0]].change_color(node_color)
                        if mst_node1.count(nodelist1[edge_list1[no1].nodes_no[1]]) <= 0:
                            nodelist1[edge_list1[no1].nodes_no[1]].change_color(node_color)
                        y = edge_list1[no1].nodes_no[1]
                        if mst_list1.pop()[1] == 0:
                            while parent1[y] >= 0:
                                print("reverse")
                                y = parent1[y]
                            x = edge_list1[no1].nodes_no[0]
                            while parent1[x] != y:
                                x = parent1[x]
                            parent1[x] = -1
                        else:
                            print("cycle reverse")
                        for i in edge_list1:
                            if i not in (j[0] for j in mst_list1):
                                i.color = (77, 255, 77)
                        msg_k = ""
                    else:
                        stage1 = False
                        for i in edge_list1:
                            if i not in (j[0] for j in mst_list1):
                                i.color = maroon
                        msg_k = ""

                    # prims
                    if len(mst_edges2) <= 0:
                        flag2 = True
                        msg_p = "EMPTY"
                        break
                    elif not flag2:
                        flag2 = True
                        temp_edge = mst_edges2.pop()
                        temp_edge[0].width = 3
                        temp_edge[0].color = maroon
                        if temp_edge[1] == 1:
                            print("cycle")
                        else:
                            mst_nodes2[-1].change_color(node_color)
                            mst_nodes2.pop()
                        for i in edge_list2:
                            if i not in (k[0] for k in mst_edges2):
                                i.color = maroon
                        msg_p = ""
                    else:
                        flag2 = False
                        temp = mst_edges2.pop()
                        temp2 = mst_nodes2.pop()
                        temp2.change_color(node_color)
                        for i in mst_nodes2:
                            for j in adjancency_list2[i.num]:
                                if j not in (k[0] for k in mst_edges2):
                                    j.width = 3
                                    j.color = (77, 255, 77)
                        mst_edges2.append(temp)
                        mst_nodes2.append(temp2)
                        mst_nodes2[-1].change_color(red)
                        msg_p = ""

        # printing
        for i in edge_list1:
            i.width = 3
            for j in mst_list1:
                if j[1] == 0:
                    j[0].color = navy
                    j[0].width = 7
            i.draw_edge(screen)
        button9.draw(screen)
        pygame.draw.rect(screen,background_color,(5,height-41,100,20))
        wht1 = "WEIGHT: " + str(sum(i[0].weight for i in mst_list1 if i[1] == 0))
        wht1 = font0.render(wht1, True, red)
        #screen.blit(r,(width // 2 - message_k.get_width() - 5, height - wht1.get_height() - 25))
        screen.blit(wht1, (5, height - wht1.get_height() - 25))
        pygame.draw.rect(screen, background_color, (width // 2-102, height - 41, 100, 20))
        message_k = font0.render(msg_k, True, red)
        screen.blit(message_k, ((width // 2 - message_k.get_width() - 5), height - wht1.get_height() - 25))
        for i in nodelist1:
            i.draw(screen)

        # prims
        for i in edge_list2:
            i.draw_edge(screen)
        for i in nodelist2:
            i.draw(screen)
        button9.draw(screen)
        pygame.draw.rect(screen, background_color, (width // 2 + 5, height - 41, 100, 20))
        wht2 = "WEIGHT: " + str(sum(i[0].weight for i in mst_edges2 if i[1] == 0))
        wht2 = font0.render(wht2, True, red)
        #pygame.draw.rect(screen, navy_blue, (width - message_p.get_width() - 5, height - wht2.get_height() - 25, 70, 17))
        screen.blit(wht2, (width // 2 + 5, height - wht2.get_height() - 25))
        pygame.draw.rect(screen, background_color, (width - 100, height - 41, 100, 20))
        message_p = font0.render(msg_p, True, red)
        screen.blit(message_p, ((width - message_p.get_width() - 5), height - wht2.get_height() - 25))
        pygame.display.update()

def comp_fs():
    global nodelist1, nodelist2, edge_list1, edge_list2, start_node
    adjancency_list = dict((i, []) for i in range(len(nodelist2)))
    for i in edge_list2:
        adjancency_list[i.nodes_no[0]].append(nodelist2[i.nodes_no[1]])
        adjancency_list[i.nodes_no[1]].append(nodelist2[i.nodes_no[0]])
    node_size = 20
    width = 1200
    height = 650
    screen = pygame.display.set_mode((width, height), 0, 0)
    screen.fill(background_color)
    button9.draw(screen)
    msg = "Press space to continue and backspace for previous step"
    message = font0.render(msg, True, red)
    screen.blit(message, ((width // 2 - message.get_width() / 2), height - 22))
    pygame.draw.line(display, maroon, (int(width / 2), 2), (int(width / 2), height - 22), 3)
    message_to_screen(screen, "BFS", navy_blue, 7, 58, "large")
    message_to_screen(screen, "DFS", navy_blue, 670, 58, "large")
    nodelist1.sort(key=lambda node: node.num)
    queue1 = list()
    visited1 = list()
    next_nodes1 = list()
    for i in edge_list1:
        i.draw_edge(screen)
    for i in edge_list2:
        i.draw_edge(screen)

    for i in nodelist1:
        i.color = node_color
        i.draw(screen, node_color)
    for i in nodelist2:
        i.color = node_color
        i.draw(screen, node_color)

    pygame.display.update()
    window = Tk()
    label = Label(window, text='Start Node ')
    startBox = Entry(window)
    submit = Button(window, text='Submit', command=lambda: selectNode(window, startBox, len(nodelist1)))
    submit.grid(columnspan=2, row=3)
    startBox.grid(row=0, column=1, pady=3)
    label.grid(row=0, pady=3)
    window.attributes("-topmost", True)
    startBox.focus()
    mainloop()
    queue1.append(nodelist1[start_node])
    while len(visited1) != len(nodelist1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        current_node = queue1[0]
        visited1.append(current_node)
        for edge in edge_list1:
            if current_node.x == edge.start[0] and current_node.y == edge.start[1]:
                for node in nodelist1:
                    if node not in visited1:
                        if node.x == edge.end[0] and node.y == edge.end[1] and node not in next_nodes1:
                            next_nodes1.append(node)
            elif current_node.x == edge.end[0] and current_node.y == edge.end[1]:
                for node in nodelist1:
                    if node not in visited1:
                        if node.x == edge.start[0] and node.y == edge.start[1] and node not in next_nodes1:
                            next_nodes1.append(node)
        next_nodes1.sort(key=lambda node: node.num)
        for node in next_nodes1:
            if node not in queue1:
                queue1.append(node)
        next_nodes1 = list()
        queue1.remove(current_node)

    nodelist2.sort(key=lambda node: node.num)
    queue2 = list()
    visited2 = list()
    current_node = nodelist2[start_node]
    visited2.append(current_node)
    while len(visited2) != len(nodelist2):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            min_node = len(nodelist2) + 1
            for i in adjancency_list[current_node.num]:
                if i not in visited2:
                    if (min_node > i.num):
                        min_node = i.num
            if min_node == len(nodelist2) + 1:
                j = visited2.index(current_node) - 1
                current_node = visited2[j]
            else:
                visited2.append(nodelist2[min_node])
                current_node = nodelist2[min_node]
    added1 = list()
    added2 = list()
    while True:
        screen.fill(background_color)
        button9.draw(screen)
        msg = "Press space to continue and backspace for previous step"
        message = font0.render(msg, True, red)
        screen.blit(message, ((width // 2 - message.get_width() / 2), height - 22))
        pygame.draw.line(display, maroon, (int(width / 2), 2), (int(width / 2), height - 45), 3)
        message_to_screen(screen, "BFS", navy_blue, 7, 58, "large")
        message_to_screen(screen, "DFS", navy_blue, 670, 58, "large")
        button9.draw(screen)
        for i in edge_list1:
            i.draw_edge(screen)
        for i in edge_list2:
            i.draw_edge(screen)

        for i in nodelist1:
            i.color = node_color
            i.draw(screen, node_color)
        for i in nodelist2:
            i.color = node_color
            i.draw(screen, node_color)

        i = 15
        for node in added1:
            node.color = red
            node.draw(screen)
            n = str(node.num)
            message_to_screen(screen, n, navy_blue, i, 600, "large")
            i += 20
        i = 700
        for node in added2:
            node.color = red
            node.draw(screen)
            n = str(node.num)
            message_to_screen(screen, n, navy_blue, i, 600, "large")
            i += 20
        pygame.display.update()

        for event in pygame.event.get():
            pos1 = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if button9.isOver(pos1):
                    button9.change((155, 0, 0))
                else:
                    button9.change(redrawwindow_color)
            if event.type == MOUSEBUTTONDOWN:
                if button9.isOver(pos1):
                    return
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if len(added1) == len(nodelist1) and len(added2) == len(nodelist2):
                        print("complete")
                        break
                    if (visited1[0] not in added1) and (visited2[0] not in added2):
                        added1.append(visited1[0])
                        added2.append(visited2[0])
                    del visited1[0]
                    del visited2[0]
                if event.key == K_BACKSPACE:
                    if (len(added1) != 0) and (len(added2) != 0):
                        visited1.insert(0, added1.pop())
                        visited2.insert(0, added2.pop())
        button9.draw(screen)


class edge:
    def __init__(self, start, end, weight, nodes_no, color=maroon, width=3):
        self.start = start
        self.end = end
        self.weight = weight
        self.nodes_no = nodes_no
        self.color = color
        self.width = width

    def draw_edge(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(str(self.weight), 1, black)
        x = 4
        p = self.end
        q = self.start
        if abs(self.nodes_no[0] - self.nodes_no[1]) == 1:
            x = 2
        if (self.start[0] > self.end[0]):
            p = self.start
            q = self.end
        if self.weight != None:
            x_cord = p[0] + (q[0] - p[0]) / x
            y_cord = p[1] + (q[1] - p[1]) / x
            pygame.draw.circle(screen, background_color, (int(x_cord), int(y_cord)), 13, 0)
            screen.blit(text, (int(x_cord - text.get_width() / 2), int(y_cord - text.get_width() / 2)))



def intro():
    display = pygame.display.set_mode((display_width, display_height), 0, 0)
    display.blit(intro_image, (0, 0))
    display.blit(back, (5,5))
    b = button(blue, 5, 5,60,30,1)
    b.draw(display)
    display.blit(back,(5,5))
    display.blit(logo,(display_width - 170,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if b.isOver(pos):
                    first()

def second(choice):
    global running, edges, mode
    running = True
    display1 = pygame.display.set_mode((display_width, display_height), 0, 0)
    display1.blit(blur, (0, 0))
    msg = "Enter number of nodes"
    message = font.render(msg, True, navy_blue)
    name = ""
    error_flag = False
    while running:
        for event in pygame.event.get():
            pos1 = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.type == K_RETURN:
                    name = ""
                elif event.key == K_1:
                    name += '1'
                elif event.key == K_2:
                    name += '2'
                elif event.key == K_3:
                    name += '3'
                elif event.key == K_4:
                    name += '4'
                elif event.key == K_5:
                    name += '5'
                elif event.key == K_6:
                    name += '6'
                elif event.key == K_7:
                    name += '7'
                elif event.key == K_8:
                    name += '8'
                elif event.key == K_9:
                    name += '9'
                elif event.key == K_0:
                    name += '0'
            if event.type == MOUSEBUTTONDOWN:
                if button7.isOver(pos1):
                    mode = 'n'
                    try:
                        edges = int(name)
                        third(choice)
                    except:
                        msg2 = "Error, Please enter number of nodes"
                        message2 = font0.render(msg2, True, red)
                        error_flag = True
                if button8.isOver(pos1):
                    mode = 'd'
                    edges = 5
                    third(choice, mode)
                if button9.isOver(pos1):
                    first()
                if button12.isOver(pos1):
                    if choice == 'Kruskal':
                        webbrowser.open(
                            'https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/')
                    if choice == 'Prim':
                        webbrowser.open('https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/')
                    if choice == 'BFS':
                        webbrowser.open('https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/')
                    if choice == 'DFS':
                        webbrowser.open('https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/')

            if event.type == MOUSEMOTION:
                if button7.isOver(pos1):
                    button7.change((155, 0, 0))
                else:
                    button7.change(redrawwindow_color)
                if button8.isOver(pos1):
                    button8.change((155, 0, 0))
                else:
                    button8.change(redrawwindow_color)
                if button9.isOver(pos1):
                    button9.change((155, 0, 0))
                else:
                    button9.change(redrawwindow_color)
                if choice != "Comparison":
                    if button12.isOver(pos1):
                        button12.change((155, 0, 0))
                    else:
                        button12.change(redrawwindow_color)
        block = font1.render(name, True, redrawwindow_color)
        rect = block.get_rect()
        rect.center = display1.get_rect().center
        display1.blit(blur, (0, 0))
        display1.blit(block, rect)
        display1.blit(message, ((display_width // 2 - message.get_width() / 2), 72))
        if error_flag:
            display1.blit(message2, ((display_width // 2 - message2.get_width() / 2), 108))
        button7.draw(display)
        button8.draw(display)
        button9.draw(display)
        if choice != "Comparison":
            button12.draw(display)
        pygame.display.update()

def dfs_check(v, adj, vis):
    if vis[v] is True:
        return
    vis[v] = True
    for u in adj[v]:
        if vis[u] is False:
            dfs_check(u, adj, vis)

def third(choice,mode='n'):
    global edges,running, weight,edge_list,nodelist
    edge_list = list()
    nodelist = list()
    width = 960
    height = 500
    no = edges
    selected = list()
    edge_list = list()
    FLAG = 0
    running = True
    screen = pygame.display.set_mode((width, height + 60), 0, 0)
    screen.fill(background_color)
    if choice != 'Comparison':
        run = button(redrawwindow_color, width - 110, 5, 100, 50, 60, 'Run')
        run.draw(screen)
    else:
        button13.draw(screen)
        button14.draw(screen)
    pygame.display.set_caption("graph algorithms  ----> " + choice)
    button9.draw(screen)
    pygame.display.update()
    Flag = True
    while running:
        for event in pygame.event.get():
            pos1 = pygame.mouse.get_pos()
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if button9.isOver(pos1):
                    second(choice)
                if choice != 'Comparison':
                    if run.isOver(pos1):
                        visited = [False for _ in range(len(nodelist))]
                        adjancency_list = dict((i, []) for i in range(len(nodelist)))
                        for i in edge_list:
                            adjancency_list[i.nodes_no[0]].append(i.nodes_no[1])
                            adjancency_list[i.nodes_no[1]].append(i.nodes_no[0])
                        dfs_check(0, adjancency_list, visited)
                        if False in visited:
                            msg = "GRAPH IS NOT CONNECTED"
                            message = font0.render(msg, True, red)
                            screen.blit(message, ((display_width // 2 - message.get_width() / 2), display_height + 36))
                            continue
                        elif choice == 'Kruskal':
                            Kruskal(screen, choice, nodelist, edge_list)
                        elif choice == 'Prim':
                            Prim(screen, choice, nodelist, edge_list)
                        elif choice == 'BFS':
                            BFS(screen, choice, nodelist, edge_list)
                        elif choice == 'DFS':
                            DFS(screen, choice, nodelist, edge_list)
                        for i in edge_list:
                            i.width = 3
                            i.color = maroon
                            i.draw_edge(screen)
                if choice == 'Comparison':
                    choice1 = "Prim's"
                    choice2 = "Kruskal's"
                    if button13.isOver(pos1):
                        choice1 = "Prim's"
                        choice2 = "Kruskal's"
                        Comparison(choice1, choice2)
                        pygame.display.set_mode((width, height + 60), 0, 0)
                        screen.fill(background_color)
                        button9.change(redrawwindow_color)
                        button9.draw(screen)
                        button13.draw(screen)
                        button14.draw(screen)
                        pygame.display.set_caption("graph algorithms  ----> " + choice)
                        button9.draw(screen)
                        pygame.display.update()
                        for i in edge_list:
                            i.color = maroon
                            i.draw_edge(screen)
                    if button14.isOver(pos1):
                        choice1 = "BFS"
                        choice2 = "DFS"
                        Comparison(choice1, choice2)
                        pygame.display.set_mode((width, height + 60), 0, 0)
                        screen.fill(background_color)
                        button9.change(redrawwindow_color)
                        button9.draw(screen)
                        button13.draw(screen)
                        button14.draw(screen)
                        pygame.display.set_caption("graph algorithms  ----> " + choice)
                        button9.draw(screen)
                        pygame.display.update()
                        for i in edge_list:
                            i.color = maroon
                            i.draw_edge(screen)
            if event.type == MOUSEMOTION:
                if choice == 'Comparison':
                    if button13.isOver(pos1):
                        button13.color = red
                        button13.draw(screen)
                    else:
                        button13.color = redrawwindow_color
                        button13.draw(screen)
                    if button14.isOver(pos1):
                        button14.color = red
                        button14.draw(screen)
                    else:
                        button14.color = redrawwindow_color
                        button14.draw(screen)
                else:
                    if button9.isOver(pos1):
                        button9.change((155, 0, 0))
                        button9.draw(display)
                    else:
                        button9.change(redrawwindow_color)
                        button9.draw(display)
                    if run.isOver(pos1):
                        run.color = red
                        run.draw(screen)
                    else:
                        run.color = redrawwindow_color
                        run.draw(screen)
        pygame.display.update()
        mouse_pos = pygame.mouse.get_pos()
        node_size = 35
        radius = min(int(width / 2), int(height / 2)) - node_size - 10
        theta = 0
        nodelist = list()
        for i in range(no):
            x = int(radius * (math.cos(theta)) + width / 2)
            y = int(height / 2 + radius * (math.sin(theta)))
            if i in selected:
                nodelist.append(node(red, i, x, y, node_size, str(i)))
                nodelist[-1].draw(screen, black)
            else:
                nodelist.append(node(node_color, i, x, y, node_size, str(i)))
                nodelist[-1].draw(screen, node_color)
            theta += (2 * 3.14) / (no)
        if mode == 'd' and Flag == True:
            weight = -20
            if choice == 'BFS' or choice == 'DFS':
                weight = None
            edge_list.append(edge((nodelist[0].x, nodelist[0].y), (nodelist[2].x, nodelist[2].y), weight, (0, 2)))
            if weight != None:
                weight += 5
            edge_list.append(edge((nodelist[1].x, nodelist[1].y), (nodelist[2].x, nodelist[2].y), weight, (1, 2)))
            if weight != None:
                weight += 5
            edge_list.append(edge((nodelist[3].x, nodelist[3].y), (nodelist[4].x, nodelist[4].y), weight, (3, 4)))
            if weight != None:
                weight += 5
            edge_list.append(edge((nodelist[4].x, nodelist[4].y), (nodelist[2].x, nodelist[2].y), weight, (4, 2)))
            if weight != None:
                weight += 5
            edge_list.append(edge((nodelist[1].x, nodelist[1].y), (nodelist[4].x, nodelist[4].y), weight, (1, 4)))
            if weight != None:
                weight += 5
            edge_list.append(edge((nodelist[0].x, nodelist[0].y), (nodelist[3].x, nodelist[3].y), weight, (0, 3)))
            if weight != None:
                weight += 5
            edge_list.append(edge((nodelist[0].x, nodelist[0].y), (nodelist[1].x, nodelist[1].y), weight, (0, 1)))
            if weight != None:
                weight += 5
            edge_list.append(edge((nodelist[1].x, nodelist[1].y), (nodelist[3].x, nodelist[3].y), weight, (1, 3)))
            for e in edge_list:
                e.draw_edge(screen)
            pygame.display.update()
            Flag = False
        elif mode != 'd':
            for i in enumerate(nodelist):
                if i[1].isOver(mouse_pos):
                    if event.type == MOUSEBUTTONDOWN and not FLAG:
                        FLAG = 1
                        nodelist[i[0]].change_color(red)
                        nodelist[i[0]].draw(screen)
                        pygame.display.update()
                        if (len(selected) >= 1 and nodelist[i[0]].num != selected[0]):
                            if choice == 'DFS' or choice == 'BFS':
                                weight = None
                            else:
                                FLAG = 0
                                window = Tk()
                                label = Label(window, text='Weight: ')
                                startBox = Entry(window)
                                submit = Button(window, text='Submit', command=lambda: onsubmit(window, startBox))
                                submit.grid(columnspan=2, row=3)
                                startBox.grid(row=0, column=1, pady=3)
                                label.grid(row=0, pady=3)
                                window.attributes("-topmost", True)
                                startBox.focus()
                                mainloop()
                            selected.append(i[0])
                            edge_list.append(
                                edge((i[1].x, i[1].y), (nodelist[selected[0]].x, nodelist[selected[0]].y), weight,
                                     selected))
                            edge_list[-1].draw_edge(screen)
                            selected = list()
                        else:
                            selected.append(i[0])
                    if event.type == MOUSEBUTTONUP:
                        FLAG = 0
                    nodelist[i[0]].change_color(node_color_hover)
                    nodelist[i[0]].draw(screen)
                pygame.display.update()


def first():
    global running, mode, edges
    display = pygame.display.set_mode((display_width, display_height), 0, 0)
    pygame.display.set_caption("graph algorithms")
    while running:
        display.blit(image, (0, 0))
        message_to_screen(display, "Select Algorithm :  ", blue, 30, 10, "extralarge")

        for button in buttons:
            button.draw(display)
        button10.draw(display)

        for event in pygame.event.get():
            pos1 = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                for i in buttons:
                    if i.isOver(pos1):
                        choice = i.text
                        second(choice)
                        third(choice)
                if button10.isOver(pos1):
                    intro()

            if event.type == MOUSEMOTION:
                for i in buttons:
                    if i.isOver(pos1):
                        i.change((155, 0, 0))
                    else:
                        i.change(blue)
                if button10.isOver(pos1):
                    button10.change((155, 0, 0))
                else:
                    button10.change(blue)
        pygame.display.update()


first()
pygame.quit()
