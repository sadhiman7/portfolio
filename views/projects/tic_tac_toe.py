import streamlit as st

st.title('Tic Tac Toe')

cols = st.columns(3)

if 'board' not in st.session_state:
    st.session_state['board'] = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

def print_board(b):
    for idx, i in enumerate(b):
        print(' | '.join(i))
        if idx<2:
            print('---------')

def button_click(i, j):
    # global session_state
    print('ij', i, j)
    print_board(st.session_state['board'])
    st.session_state['board'][i][j] = 'X'
    display_board(st.session_state['board'])
    print('DONEE')

def display_board(b):
    print_board(b)
    for i, m in enumerate(b):
        for j, n in enumerate(m):
            if n==' ':
                with cols[j]:
                    st.button('  ', key=f'{i}{j}', on_click=button_click, args=[i, j])
            else:
                with cols[j]:
                    st.button(n, key=f'{i}{j}')
    

# if st.button('START'):
    # display_board(st.session_state['board'])
st.error('Coming soon!')





































# board = [[' ']*3]*3
import copy

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(b):
    for idx, i in enumerate(b):
        print(' | '.join(i))
        if idx<2:
            print('---------')

def is_win(b, c):
    #straight
    if c*3 in [''.join(i) for i in b] + [''.join(i) for i in list(map(list, zip(*b)))]:
        return True
    #diagonal
    if c*3 in [''.join([b[0][0], b[1][1], b[2][2]])] or c*3 in [''.join([b[0][2], b[1][1], b[2][0]])]:
        return True
    return False

def get_best_move(b):
    nb = copy.deepcopy(b)
    #check win
    for i, m in enumerate(nb):
        for j, n in enumerate(m):
            if n==' ':
                nb[i][j] = 'O'
                if is_win(nb, 'O'):
                    return i, j
                nb[i][j] = ' '
    #check opponent win
    for i, m in enumerate(nb):
        for j, n in enumerate(m):
            if n==' ':
                nb[i][j] = 'X'
                if is_win(nb, 'X'):
                    return i, j
                nb[i][j] = ' '
    #setup
    for i1, m1 in enumerate(nb):
        for j1, n1 in enumerate(m1):
            if n1==' ':
                nb[i1][j1] = 'O'
                for i2, m2 in enumerate(nb):
                    for j2, n2 in enumerate(m2):
                        if n2 == ' ':
                            nb[i2][j2] = 'O'
                            if is_win(nb, 'O'):
                                return i1, j1
                            nb[i2][j2] = ' '
                b[i1][j1] = ' '
    #play random
    for i, m in enumerate(nb):
        for j, n in enumerate(m):
            if n==' ':
                return i, j
    return False

game_over = False

def check_game_over(b):
    if is_win(b, 'X') or is_win(b, 'O'):
        return True
    for i in b:
        if ' ' in i:
            return False
    return True

# while not game_over:
#     user_inp = input()
#     i, j = [int(x) for x in user_inp.split()]
#     if board[i][j]!= ' ':
#         print('Invalid Input')
#         continue
#     board[i][j] = 'X'
#     print_board(board)

#     x, y = get_best_move(board)

#     board[x][y] = 'O'

#     print_board(board)

#     game_over = check_game_over(board)

#     # break
